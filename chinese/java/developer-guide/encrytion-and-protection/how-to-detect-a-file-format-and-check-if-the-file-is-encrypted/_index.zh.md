---
title: 如何检测文件格式并检查文件是否已加密
type: docs
weight: 2000
url: /zh/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

有时您需要在打开文件之前检测文件的格式，因为文件扩展名不能保证文件内容是否合适。文件可能已加密（受密码保护）因此无法直接读取，或者我们不应该读取它。Aspose.Cells 提供了 [**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)）静态方法和一些相关的 API，可以用于处理文档。

{{% /alert %}}

## **Java 代码以检测文件格式并检查文件是否已加密**

以下示例代码说明如何通过文件路径检测文件格式并检查其扩展名。您还可以确定该文件是否已加密。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
