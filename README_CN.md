# CUE自动分割器
[ENGLISH](https://github.com/itoukou1/CueAutoSplit/blob/main/README.md "ENGLISH")	[中文](https://github.com/itoukou1/CueAutoSplit/blob/main/README_CN.md "中文")	[日本语](https://github.com/itoukou1/CueAutoSplit/blob/main/README_JA.md "日本语")

## 功能
快速将cue分开(多文件夹)在某些情况下可以自动查找cue定义错误源文件和分割并自动查找cue编码。标签和封面(如果存在)在分割后自动添加。这个库通常用于分割多个线索(如日本动漫系列歌曲)。

## 安装方式
https://sourceforge.net/projects/sox/files/sox/
下载sox安装并设置环境变量

将包含cue的文件夹放到代码目录下（cue无须从文件夹取出）
（如需添加封面请放入一个图片文件，程序将自动处理添加）

运行代码
```python
python process.py
```

## 感谢
Sox
[Deflacue](https://github.com/idlesign/deflacue/ "Deflacue")





