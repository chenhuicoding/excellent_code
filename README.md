Some Questions
=================

Contents
============

 * [Question2](#question2)
 * [Question3](#question3)
 * [Question4](#question4)     
 * [Question6](#question6)   
 * [Question9](#question9)   
               
Question2
==============
   思路： 将ifconfig命令结果保存，通过管道,grep,sed命令将端口和IP地址输出


Question3
==============
   思路： 通过grep,sed命令进行匹配和替换              
 
Question4
==============
  思路： 将每天产生的日志文件，按照天去保存
  
             
Question6
==============

> 思路：保存CPU利用率，system time，user time， iowait time以及idle time. 用\t为分隔符保存在log文件中。每个log文件只记录100000条信息， 一旦超过100000条， 就保存到新的log文件中。

**代码使用了psutil python库**


**PS**: needs to install `psutil`

Linux

`sudo apt-get install psutil`

Question9
==============
 思路 Group类保存k叉树的根节点, 并提供add\get方法. Node类是节点类, 使用list来保存子节点, 并指向父节点. add方法即在相应的Node对象的list中添加元素. get即返回相应节点的list              

