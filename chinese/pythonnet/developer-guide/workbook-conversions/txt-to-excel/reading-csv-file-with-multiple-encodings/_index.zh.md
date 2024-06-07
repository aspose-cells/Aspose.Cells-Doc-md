---
title: 读取具有多种编码的CSV文件
type: docs
weight: 200
url: /zh/python-net/reading-csv-file-with-multiple-encodings/
description: 通过Aspose.Cells for Python通过.NET API读取具有多种编码的CSV文件。
keywords: Python通过.NET读取具有多种编码的CSV文件，将具有多种编码的CSV文件转换为Excel，在Python中通过NET加载具有多种编码的CSV文件。
---

{{% alert color="primary" %}}

有时，您的CSV文件包含多种编码（Unicode，ANSI，UTF8，UTF7等）。Aspose.Cells允许您加载这种CSV文件并将其转换为其他格式，例如PDF或XLSX。

{{% /alert %}}

Aspose.Cells提供了[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)属性，您需要将其设置为true以正确加载具有多种编码的CSV文件。

以下屏幕截图显示了一个包含两行的示例CSV文件。第一行采用**ANSI**编码，第二行采用**Unicode**编码

|**输入文件**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下屏幕截图显示了未将[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)属性设置为true时从上述CSV文件转换的XLSX文件。您可以看到Unicode文本没有被正确转换。

|**输出文件 1：未对多重编码做出调整**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

以下屏幕截图显示了设置[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)属性为true后从上述CSV文件转换的XSLX文件。您可以看到Unicode文本现在被正确转换。

|**输出文件 2：IsMultiEncoded设置为true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下是将上述CSV文件正确转换为XLSX格式的示例代码。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
