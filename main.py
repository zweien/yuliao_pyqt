__version__ = 1.2
__date__ = '20191207'
__author__ = 'zweien'

import sys, os, pickle
import yuliao_ui,  yuliao_stat  # UI from QtDesigner

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow,\
    QMessageBox,QFileDialog,QProgressDialog, \
    QTableWidgetItem,QHeaderView,QTextEdit, QLabel
from PyQt5.QtGui import QIcon

from yuliao import *

class StatWindow(QMainWindow, yuliao_stat.Ui_Dialog):
    def __init__(self, parent=None, dialogues=None):
        super().__init__(parent)
        self.setupUi(self)
        if dialogues is None or len(dialogues) == 0:
            return
        countries = pd.Series(count_countries(dialogues))
        des_df = describe_dialogues(dialogues)
        people_country = countries.value_counts()
        word_country = count_word_from_country(dialogues)

        for line, (country, num_people) in enumerate(people_country.iteritems()):
            num_word = word_country[country]
            self.tableWidget.insertRow(line)

            country_item = QTableWidgetItem(country)
            self.tableWidget.setItem(line, 0, country_item)

            people_item = QTableWidgetItem(str(num_people))
            self.tableWidget.setItem(line, 1, people_item)

            word_item = QTableWidgetItem(str(num_word))
            self.tableWidget.setItem(line, 2, word_item)

        total_word = sum(word_country.values())
        china_word = word_country['中国']
        foreign_word = total_word - china_word

        self.label_china.setText(str(china_word))
        self.label_foreign.setText(str(foreign_word))
        self.label_total.setText(str(total_word))



class myWindow(QMainWindow, yuliao_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(f'语料库 {__version__}')
        self.setWindowIcon(QIcon('./baby.ico'))

        self.dialogues = []
        self.results = None
        self.word = ''
        self.select_dia_index = None
        self.select_index = None
        self.select_row = None
        self.changed = False

        self.label_status_msg = QLabel(self)
        self.label_status_msg.setMinimumWidth(200)
        self.statusBar1.addWidget(self.label_status_msg)

        self.label_status_diaNum = QLabel(self)
        self.statusBar1.addWidget(self.label_status_diaNum)
        self.label_status_diaNum.setMinimumWidth(100)
        self.label_status_searchNum = QLabel(self)
        self.statusBar1.addWidget(self.label_status_searchNum)
        self.label_status_searchNum.setMinimumWidth(100)
        self.status_update()

        # self.pushButton.clicked.connect(self.fun)
        self.toolButton.clicked.connect(self.choose_dir)
        self.pushButton_read.clicked.connect(self.generate)
        self.pushButton_add.clicked.connect(self.add_dialogue)
        self.pushButton_search.clicked.connect(lambda: self.search(refresh=True))
        # self.tableWidget.cellPressed.connect(self.select)
        self.tableWidget.selectionModel().selectionChanged.connect(self.select)
        # self.tableWidget.verticalHeader().sectionClicked.connect(self.select)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_saveDialog.clicked.connect(self.save_dialogue)
        self.textEdit.textChanged.connect(self.text_changed)
        self.actionSave.triggered.connect(self.save_dialogues)
        self.actionLoad.triggered.connect(self.load_dialogues)
        self.actionQuit.triggered.connect(self.close)
        self.actionExcel.triggered.connect(self.save_to_excel)
        self.actionStat.triggered.connect(self.stat)


    def stat(self):

        stat_window = StatWindow(self, self.dialogues)
        stat_window.show()


    def save_to_excel(self):
        if self.results is not None:
            filename, _ = QFileDialog.getSaveFileName(self, '搜索结果导出', './', 'excel (*.xlsx);;所有文件 (*)')
            if filename:
                self.results.to_excel(filename, self.lineEdit_search.text())
                self.label_status_msg.setText('成功导出excel')
        else:
            self.label_status_msg.setText('搜索结果为空')

    def add_dialogue(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, '追加对话文件', './')

        if filenames:
            for filename in filenames:
                dialogue = Dialogue(filename)
                dialogue.handle()
                self.dialogues.append(dialogue)
            self.status_update()
            self.label_status_msg.setText('追加{}个对话'.format(len(filenames)))


    def save_dialogues(self):
        if self.dialogues:
            filename, _ = QFileDialog.getSaveFileName(self,'保存数据文件', './', 'dat数据 (*.dat);;所有文件 (*)')
            if filename:
                with open(filename, 'wb') as file:
                    pickle.dump(self.dialogues, file)
                    pickle.dump(self.lineEdit.text(), file)
                    pickle.dump(self.lineEdit_search.text(), file)
                    pickle.dump(self.lineEdit_include.text(), file)
                    pickle.dump(self.lineEdit_exclude.text(), file)


    def load_dialogues(self):
        filename,_ = QFileDialog.getOpenFileName(self, '打开数据文件', './', 'dat数据 (*.dat);;所有文件 (*)')

        if filename:
            with open(filename, 'rb') as file:
                self.dialogues = pickle.load(file)
                self.lineEdit.setText(pickle.load(file))
                self.lineEdit_search.setText(pickle.load(file))
                self.lineEdit_include.setText(pickle.load(file))
                self.lineEdit_exclude.setText(pickle.load(file))
            self.search()


    def text_changed(self):
        print('changed')
        self.changed = True

    def save_dialogue(self):
        if (self.select_row is not None) and (self.changed==True):
            res = QMessageBox.warning(self, "注意", "保存修改？",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if res == QMessageBox.Yes:
                content = self.textEdit.toPlainText()
                dialogue = self.dialogues[self.select_dia_index]
                dialogue.lines = content.split()
                dialogue.reset()
                dialogue.handle()
                self.search(refresh=False)
                self.changed = False
                self.label_save_dialog.setText(str(self.select_row+1))


            # self.results.iloc[self.select_row].content = dialogue
            # self.tableWidget


    def fun(self,selected):
        print('table',selected.indexes()[0].row())

    def choose_dir(self):
        fdir = QFileDialog.getExistingDirectory(self,'选择目录','./')
        self.lineEdit.setText(fdir)

    def generate(self):
        filepath_list = gen_filepaths(self.lineEdit.text())
        n = len(filepath_list)
        if n > 0:
            progress = QProgressDialog(self)
            progress.setWindowTitle("请稍等")
            progress.setLabelText("正在操作...")
            progress.setMinimumDuration(1000)
            progress.setWindowModality(Qt.WindowModal)

            progress.setRange(0,n)
            self.dialogues = []
            for i, fpath in enumerate(filepath_list):
                progress.setValue(i)
                if progress.wasCanceled():
                    QMessageBox.warning(self, "提示", "操作失败")
                    break
                dialogue = Dialogue(fpath)
                dialogue.handle()
                self.dialogues.append(dialogue)
            else:
                progress.setValue(n)
                QMessageBox.information(self, "提示", "成功读取对话{}个！".format(n))
                self.label_status_msg.setText('成功读取对话{}个！'.format(n))
                self.status_update()
        else:
            QMessageBox.warning(self, '提示', '未找到对话')
        # self.dialogues = gen_dialogues(filepath_list)
        # print(len(self.dialogues))

    def status_update(self):
        self.label_status_diaNum.setText('对话数：{}'.format(len(self.dialogues)))
        if self.results is None:
            resultsNum=0
        else:
            resultsNum = len(self.results)
        self.label_status_searchNum.setText('搜索结果数：{}'.format(resultsNum))

    def search(self, refresh=True):
        self.word = self.lineEdit_search.text()
        include = self.lineEdit_include.text().split()
        exclude = self.lineEdit_exclude.text().split()
        # print(word, include,exclude)

        if not include:
            include=None
        if not exclude:
            exclude=None
        self.results = None

        self.results = find_word(self.dialogues, self.word, include=include, exclude=exclude)


        if self.results is not None:
            self.status_update()
        else:
            QMessageBox.warning(self, "提示", "无匹配")
            self.label_status_msg.setText('无匹配!')

        self.show_table(self.results)

        if refresh:
            self.textEdit.clear()

    def remove_rows(self, rows):
        # print("删除行：", rows)
        indexes = self.results.iloc[rows]['index'].values
        dia_indexes = self.results.iloc[rows]['dia_index'].values
        # 删除dialogues 中相应行
        print(indexes, dia_indexes)
        for i,j in zip(dia_indexes, indexes):
            dialogue = self.dialogues[i].data
            # print(dialogue.index[j])
            dialogue.drop(j, inplace=True)
        rows.reverse()
        for r in rows:
            # 逆序逐行删除
            self.tableWidget.removeRow(r)
        self.results.drop(self.results.index[rows], inplace=True) #drop删行只能按index,所以index[rows]



        n = self.tableWidget.rowCount()
        self.status_update()

    def delete(self):
        res = QMessageBox.warning(self, "注意！", "删除可不能恢复了哦！",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.Yes:
            current_row = self.tableWidget.currentRow()
            selections = self.tableWidget.selectionModel()
            selected_list = selections.selectedRows()
            rows = []
            for r in selected_list:
                rows.append(r.row())
            if len(rows) == 0:
                rows.append(current_row)
            self.remove_rows(rows)
            self.textEdit.clear()
            self.select_row = None
            self.select_index = None
            self.select_dia_index = None

    def show_table(self, results):
        table_rows = self.tableWidget.rowCount()
        if table_rows > 0:
            # print('remove')
            for row in range(table_rows, -1, -1): #逆序删除！！
                self.tableWidget.removeRow(row)
        if results is None:
            return
        for i, line in results.iterrows():
            country = line.country
            name = line['name']
            # print(name)
            file = line.file
            content = line.content

            self.tableWidget.insertRow(i)

            country_item = QTableWidgetItem(country)
            self.tableWidget.setItem(i, 0, country_item)

            name_item = QTableWidgetItem(name)
            self.tableWidget.setItem(i, 1, name_item)

            file_item = QTableWidgetItem(os.path.basename(file))
            self.tableWidget.setItem(i, 2, file_item)

            # content_item = QTableWidgetItem(content)
            # self.tableWidget.setItem(i, 3, content_item)
            content_edit = QTextEdit()
            content = content.replace(self.word, '<font color="red">'+self.word+'</font>')
            content_html = '<font color="blue">'+content+'</font>'
            content_edit.setHtml(content_html)

            self.tableWidget.setCellWidget(i,3,content_edit)
            cursor = content_edit.document().find(self.word)
            cursor.setPosition(cursor.position())
            content_edit.setTextCursor(cursor)

        # 表格
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)


    def select(self, selected):
        if not selected.indexes():
            return
        row = selected.indexes()[0].row()

        self.select_row = row
        dia_index = self.results.iloc[row]['dia_index']
        index = self.results.iloc[row]['index']
        self.select_dia_index = dia_index
        self.select_index = index
        print('select',dia_index, index)
        dialogue = self.dialogues[dia_index].data.copy()
        sentence_p = dialogue.loc[index].content
        sentence = sentence_p.replace(self.word, '<font color="red">'+self.word+'</font>')
        dialogue.loc[index].content = '<font color="blue">'+sentence+'</font>'

        dia_text = '<br>'.join(dialogue.content.values)
        # print()
        self.textEdit.setHtml(dia_text)

        cursor = self.textEdit.document().find(sentence_p)
        # print(position)
        cursor.setPosition(cursor.position())
        self.textEdit.setTextCursor(cursor)
        self.changed = False


###################################################
# main loop
app = QApplication(sys.argv)
mainw = myWindow()
mainw.show()
sys.exit(app.exec_())