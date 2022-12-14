---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /zh/java/java-security-invalidkeyexception/
---
## **概括**
默认情况下，AES 支持 128 位密钥，如果您计划使用 192 位或 256 位密钥，java 编译器将抛出 Illegal key size 异常。这不是由于 Aspose.Cells API 的某些错误，而是由于 JDK/JRE 本身的有限功能。由于某些国家/地区的进口限制，JDK/JRE 的默认策略文件已损坏。用户必须获得“无限强度”策略文件并将它们安装在他们的 JRE 中才能使用高级加密功能进行加密/解密。
## **症状**
您可能会收到 java.security.InvalidKeyException: Illegal key size or default parameters 或 java.security.InvalidKeyException: Illegal key size 在加载受保护的电子表格时。
## **解决方案**
解决方法其实很简单，详见下文。

1. 下载 Java 加密扩展 (JCE) 无限强度管辖策略文件。
1. 从下载的存档中提取 JAR 文件并将它们放在 ${java.home}/jre/lib/security/ 目录中。
1. 重新运行程序。
## **下载链接**
请使用与您的 JDK/JRE 版本相对应的下载链接。

- [Java 加密扩展 (JCE) 无限强度管辖策略文件 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java 加密扩展 (JCE) 无限强度管辖策略文件 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java 加密扩展 (JCE) 无限强度管辖策略文件 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
