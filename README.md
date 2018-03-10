# textanalysis
A tool of analyzing the text in python

  这是我在分析内核代码的地址分布的时候，做的一个能自动分析内核代码的小工具。
  编译内核之后，会生成一个vmlinux，其为内核空间的镜像，包含内核代码以及地址分布，使用命令：
  objdump -S vmlinux > a 
  可以得到文件a，该文件清晰地呈现了地址、机器码、汇编指令等信息。
  现在我需要对文件a进行文本分析，得到我需要的信息，比如我需要知道所有call函数的地址。
  这里我们使用python即可利用各种包实现文本匹配功能。
