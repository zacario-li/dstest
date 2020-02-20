# 常用查找算法
## 顺序查找
即遍历所有数据，复杂度为O(N)
## 二分查找
mid = (low + high)//2, 复杂度为O(lgN)
## 插值查找
mid = low + (target - data[low])//(data[high]-data[low])*(high - low), 复杂度为O(loglogN)
## 跳跃查找
设定一个搜索步长，来快速确定目标范围，然后再进行顺序搜索
## 快速查找
TODO
## 哈希查找
建立hashtable，建立索引
