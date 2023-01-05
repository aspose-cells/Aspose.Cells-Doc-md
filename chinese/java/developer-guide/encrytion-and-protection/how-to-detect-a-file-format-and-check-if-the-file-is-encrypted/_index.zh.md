---
title: 如何检测文件格式并检查文件是否加密
type: docs
weight: 2000
url: /zh/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

有时您需要在打开文件之前检测文件的格式，因为文件扩展名并不能保证文件内容是合适的。该文件可能已加密（受密码保护的文件），因此无法直接读取它，或者我们不应该读取它。 Aspose.Cells 提供了[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)静态方法和一些可用于处理文档的相关 API。

{{% /alert %}}

## **Java 检测文件格式并检查文件是否加密的代码**

以下示例代码说明了如何检测文件格式（使用文件路径）并检查其扩展名。您还可以确定文件是否已加密。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
