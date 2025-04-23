---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /zh/java/java-security-invalidkeyexception/
---

## **摘要**
默认情况下，AES 支持 128 位密钥，如果您打算使用 192 位或 256 位密钥，Java 编译器将抛出非法密钥大小异常。这不是 Aspose.Cells API 的错误，而是由于 JDK/JRE 本身的有限特性。JDK/JRE 的默认策略文件由于某些国家的进口限制而被限制。用户必须获取“无限制强度”策略文件并将其安装在其 JRE 中，以便使用高级加密功能进行加密/解密。
## **症状**
在加载受保护的电子表格时，您可能会遇到 java.security.InvalidKeyException: 非法密钥大小或默认参数，或者 java.security.InvalidKeyException: 非法密钥大小。 
## **解决方案**
解决方案实际上非常简单，如下所述。

1. 下载 Java 加密扩展（JCE）无限制强度管辖区策略文件。
2. 从下载的存档中提取 JAR 文件，并将其放置在 ${java.home}/jre/lib/security/ 目录中。
3. 重新运行程序。
## **下载链接**
请使用与您的 JDK/JRE 版本相对应的下载链接。

- [Java 加密扩展（JCE）无限制强度管辖区策略文件 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java 加密扩展（JCE）无限制强度管辖区策略文件 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java 加密扩展（JCE）无限制强度管辖区策略文件 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
{{< app/cells/assistant language="java" >}}
