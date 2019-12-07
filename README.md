# yuliao_pyqt

语料分析小工具，使用PyQt5制作UI

## 使用方法

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
- 其中

## Change log

- 20191207
    - fix bug: 搜索得到结果后，再次搜索为空时，出错
    - add fun: 增加统计功能