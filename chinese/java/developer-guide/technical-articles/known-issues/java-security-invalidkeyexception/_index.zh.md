---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /zh/java/java-security-invalidkeyexception/
---

## **摘要**
默认情况下，AES支持128位密钥，如果您计划使用192位或256位密钥，Java编译器将抛出非法密钥大小异常。这不是Aspose.Cells API的错误，而是由于JDK/JRE本身的功能受限。JDK/JRE的默认策略文件由于某些国家的进口限制而受到了限制。用户必须获取"无限制的强度"策略文件并将它们安装在他们的JRE中，以便用于高级加密功能进行加密/解密。
## **症状**
加载受保护的电子表格时可能会遇到java.security.InvalidKeyException: 非法密钥大小或默认参数或java.security.InvalidKeyException: 非法密钥大小。 
## **解决方案**
解决方案非常简单，如下所述。

1. 下载Java加密扩展（JCE）无限强度司法管辖区政策文件。
1. 从下载的存档中提取JAR文件并将它们放置在${java.home}/jre/lib/security/目录中。
1. 重新运行该程序。
## **下载链接**
请使用与您的JDK/JRE版本相对应的下载链接。

- [Java加密扩展（JCE）无限强度司法管辖区政策文件 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java加密扩展（JCE）无限强度司法管辖区政策文件 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java加密扩展（JCE）无限强度司法管辖区政策文件 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
