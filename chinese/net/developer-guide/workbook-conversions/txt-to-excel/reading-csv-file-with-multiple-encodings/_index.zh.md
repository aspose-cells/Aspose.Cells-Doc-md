---
title: 使用多种编码方式读取CSV文件
type: docs
weight: 200
url: /zh/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

有时，您的CSV文件包含多种编码（Unicode、ANSI、UTF8、UTF7等）。Aspose.Cells允许您加载此类CSV文件，并将其转换为其他格式，例如PDF或XLSX。

{{% /alert %}}

Aspose.Cells提供了[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)属性，您需要将其设置为**true**以正确加载包含多种编码的CSV文件。

以下截图显示了一个包含两行的示例CSV文件。第一行是**ANSI**编码，第二行是**Unicode**编码

|**输入文件**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下截图显示了未将[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)属性设置为**true**的情况下从上述CSV文件转换的XLSX文件。如您所见，Unicode文本未正确转换。

|**输出文件1：未对多种编码进行处理**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

以下截图显示了将[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)属性设置为**true**后从上述CSV文件转换的XSLX文件。如您所见，现在Unicode文本已经正确转换。

|**输出文件2：IsMultiEncoded设置为true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下是将上述 CSV 文件正确转换为 XLSX 格式的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## 相关文章

- [打开 CSV 文件](/cells/zh/net/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="csharp" >}}
