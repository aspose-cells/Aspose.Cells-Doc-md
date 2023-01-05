---
title: 读取具有多个编码的 CSV 文件
type: docs
weight: 200
url: /zh/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

有时，您的 CSV 文件包含多个编码（Unicode、ANSI、UTF8、UTF7 等）。 Aspose.Cells 允许您加载此类 CSV 文件并将其转换为其他格式，例如 PDF 或 XLSX。

{{% /alert %}}

Aspose.Cells 提供了[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)属性，您需要将其设置为**真的**正确加载具有多种编码的 CSV 文件。

以下屏幕截图显示了包含两行的示例 CSV 文件。第一行在**美标**编码，第二行是**统一码**编码

|**输入文件**|
|:- |
|![待办事项：图片_替代_文本](reading-csv-file-with-multiple-encodings_1.png)|

下面的截图是在没有设置[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)财产给**真的**.如您所见，Unicode 文本未正确转换。

|**输出文件 1：没有为多重编码做出调整**|
|:- |
|![待办事项：图片_替代_文本](reading-csv-file-with-multiple-encodings_2.png)|

下面的截图是上面CSV文件设置后转换的XSLX文件[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)财产给**真的**.如您所见，Unicode 文本现在已正确转换。

|**输出文件 2：IsMultiEncoded 设置为 true**|
|:- |
|![待办事项：图片_替代_文本](reading-csv-file-with-multiple-encodings_3.png)|

下面是将上述 CSV 文件正确转换为 XLSX 格式的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## 相关文章

- [打开 CSV 文件](/cells/zh/net/opening-files-with-different-formats/#opening-csv-files)
