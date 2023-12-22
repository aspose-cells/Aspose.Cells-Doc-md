---
title: 读取多种编码的CSV文件
type: docs
weight: 200
url: /zh/python-net/reading-csv-file-with-multiple-encodings/
description: 使用 Aspose.Cells for Python via .NET API 读取具有多种编码的 CSV 文件。
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

有时，您的 CSV 文件包含多种编码（Unicode、ANSI、UTF8、UTF7 等）。 Aspose.Cells 允许您加载此类 CSV 文件并将其转换为其他格式，例如 PDF 或 XLSX。

{{% /alert %}}

 Aspose.Cells 提供[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)属性，您需要将其设置为**真的**正确加载具有多种编码的 CSV 文件。

以下屏幕截图显示了包含两行的示例 CSV 文件。第一行是在**ANSI**编码，第二行是**统一码**编码

|**输入文件**|
| :- |
|![待办事项：图像_替代_文本](reading-csv-file-with-multiple-encodings_1.png)|

下面的截图是上面的CSV文件转换后的XLSX文件，没有设置[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)属性为 *true**。如您所见，Unicode 文本未正确转换。

|**输出文件 1：未对多重编码进行调整**|
| :- |
|![待办事项：图像_替代_文本](reading-csv-file-with-multiple-encodings_2.png)|

下图为上述CSV文件转换后的XSLX文件[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)属性为 *true**。如您所见，Unicode 文本现在已正确转换。

|**输出文件 2：IsMultiEncoded 设置为 true**|
| :- |
|![待办事项：图像_替代_文本](reading-csv-file-with-multiple-encodings_3.png)|

下面是将上面的CSV文件正确转换为XLSX格式的示例代码。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
