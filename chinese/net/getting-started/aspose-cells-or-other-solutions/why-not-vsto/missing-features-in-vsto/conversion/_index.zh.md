---
title: 转换
type: docs
weight: 30
url: /zh/net/conversion/
---

Aspose.Cells 提供的独特功能，可在不影响工作的情况下灵活进行版本转换。
SaveFormat 是一个枚举，可以将文档转换为下表中给出的扩展名。

|**成员名称** |**值** |**描述** |
| :- | :- | :- |
|CSV |1 |代表一个 CSV 文件。 |
|Xlsx |6 |代表一个 xlsx 文件。 |
|Xlsm |7 |代表一个启用宏的 xlsm 文件。 |
|Xltx |8 |代表一个 xltx 文件。 |
|Xltm |9 |代表一个启用宏的 xltm 文件。 |
|TabDelimited |11 |代表一个制表符分隔的文本文件。 |
|Html |12 |代表一个 html 文件。 |
|MHtml |17 |代表一个 mhtml 文件。 |
|ODS |14 |代表一个 ods 文件。 |
|Excel97To2003 |5 |代表一个 Excel97-2003 xls 文件。 |
|SpreadsheetML |15 |代表一个 Excel 2003 xml 文件。 |
|Xlsb |16 |代表一个 xlsb 文件。 |
|Auto |0 |如果将文件保存到磁盘，则文件格式应符合文件名的扩展名。 <br> 如果将文件保存到流中，文件格式为 xlsx。|
|Unknown |255 |表示无法识别的格式，无法保存。|
|Pdf |13 |表示 Pdf 文件。|
|XPS |20 |表示 XPS 文件。|
|TIFF |21 |表示 TIFF 文件。|
|SVG |22 |表示 SVG 文件。|
|Dif |30 |数据交换格式。|
下面是代码片段，显示了从 xls 转换为 xlsx 的过程，也可以反过来做。

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **下载示例代码**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
