---
title: 如何检测文件格式并检查文件是否已加密
type: docs
weight: 2700
url: /zh/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

有时，在打开文件之前需要检测文件的格式，因为文件扩展名不能保证文件内容的正确性。文件可能已被加密（密码保护），因此不能直接读取，或者我们不应读取它。Aspose.Cells for Python via .NET 提供了[**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format)静态方法及相关API，可用于处理文档。

{{% /alert %}}

以下示例代码说明如何通过文件路径检测文件格式并检查其扩展名。您还可以确定该文件是否已加密。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

