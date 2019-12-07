# yuliao_pyqt

自制语料分析小工具，使用 PyQt5 制作 UI

## 使用方法

- Requirements
    - Python>=3.6
    - pyqt5>=5.12
    - pandas
    
- 将所需语料以 txt 格式存储，编码须为 GB2312。
- 有两种方式标识对话
    - 在文件开头标识，如
    ```
    1-法国
    2-中国
    
    1你好，我叫亚当。
    2你好，我叫张明。
    ```  
    - 在每段对话行首标识，如
    ```
    1（法国）你好，我叫亚当。
    2（中国）你好，我叫张明。
    ```
    - 在国别后可加上姓名，便于统计，如`1-法国-亚当`
- 命令行启动 `python main.py`

## Change log

- 20191207
    - fix bug: 搜索得到结果后，再次搜索为空时，出错
    - add fun: 增加统计功能
    - add fun: plot bar
    - add fun: delete shortcut