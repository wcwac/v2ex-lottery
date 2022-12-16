# v2ex 抽奖小工具

- 对回帖用户进行了去重，并且去除了楼主的回帖
- 使用了xmr实时区块高度作为随机数种子，保证了每次抽奖的公平性

## Requirements

- python3
- requests

## Example

```bash
$ python3 main.py
请输入帖子ID: 666666
请输入抽奖人数: 5
符合条件的用户共有 33 人
当前时间: 2022-12-16 09:13:49  
当前区块高度: 2778411
抽奖结果: 
leesheen
duskpark
Gladoos
EdwardYoung
maemual
```
