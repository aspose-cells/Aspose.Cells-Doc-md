---
title: 如何检测文件格式并检查文件是否已加密
type: docs
weight: 2700
url: /zh/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

有时，在打开文件之前，您需要检测文件的格式，因为文件扩展名并不保证文件内容是适当的。文件可能被加密（密码保护文件），因此无法直接读取，或者不应该读取它。Aspose.Cells提供了 [**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) 的静态方法和一些相关API，可以用于处理文档。

{{% /alert %}}

以下示例代码说明如何通过文件路径检测文件格式并检查其扩展名。您还可以确定该文件是否已加密。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
