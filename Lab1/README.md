## notes
* 命名格式尽量统一一下，除了类名的首字母大写之外，其他的均采用下划线命名，而且有实际含义
* 方法尽量加上注释，注释的方式可以参考我的代码
* 为了处理未登录词，所有的单字都算词

## data文件夹
原始数据  
已转换为utf-8编码

## ref文件夹
参考文件  
实际上是和实验相关的，老师上课的课件

## result文件夹
内含词典文件和简化的文章  
考虑到实验的要求，词典文件同时包含1-gram和2-gram  
简化的文章用于计算F1之类的评测结果

## src文件夹
### [main.py](src/main.py)
入口函数，用于调用和测试
### [config.py](src/config.py)
整合了各种可以修改的参数，含义可以看相应的help  
方便同意设置参数
### [pre-treat.py](src/pre-treat.py)
用于生成词典文件和简化后的文章（去掉用不到的词性）  
分别存储在result下的dic.txt和simplified.txt  
词典的每一行格式为：  
该词组所含单词个数 词组出现的频率 单词1 单词2 ...
### [paragraph.py](src/paragraph.py)
内含一个处理文章的类  
有一个tokenize方法，用于对文章进行分词操作，需接收一个分词器（tokenizer）
### [vocabulary.py](src/vocabulary.py)
内含一个处理词组表的类  
实例化时需要接收一个组织存储结构的方式（storage）
### [phrase.py](src/phrase.py)
内含一个处理词组的类  
存储该词组及其出现的次数
### [utils.py](src/utils.py)
各种计算评测结果的函数  
我个人建议每个方法接收两个Paragraph作为参数
### [storage](src/storage)
词典结构组织器的文件夹  
每个组织器应当实现add(Phrase)和get(str) -> Phrase两个方法
### [tokenizer](src/tokenizer)
分词器的文件夹  
每个分词器应当实现__call__(List[List[str]]) -> List[List[str]]方法