---
title: 转换
type: docs
weight: 30
url: /zh/net/conversion/
---

Aspose.Cells独特的功能，能够在不影响工作的情况下灵活进行版本转换。
SaveFormat是一个枚举，可以将文档转换为下表中给出的扩展名。

|**成员名称** |**值** |**描述** |
| :- | :- | :- |
|CSV |1 |表示CSV文件.|
|Xlsx |6 |表示xlsx文件.|
|Xlsm |7 |表示启用宏的xlsm文件.|
|Xltx |8 |表示xltx文件.|
|Xltm |9 |表示启用宏的xltm文件.|
|TabDelimited |11 |表示一个制表符分隔的文本文件.|
|Html |12 |表示一个HTML文件.|
|MHtml |17 |表示一个MHTML文件.|
|ODS |14 |表示一个ods文件.|
|Excel97To2003 |5 |表示一个Excel97-2003 xls文件.|
|SpreadsheetML |15 |表示一个Excel 2003 xml文件.|
|Xlsb |16 |表示一个xlsb文件.|
|Auto |0 |如果将文件保存到磁盘，则文件格式符合文件名的扩展名.<br>如果将文件保存到流中，则文件格式为xlsx.|
|Unknown |255 |表示无法识别的格式，无法保存.|
|Pdf |13 |表示一个Pdf文件.|
|XPS |20 |表示一个XPS文件.|
|TIFF |21 |表示一个TIFF文件.|
|SVG |22 |代表一个SVG文件。|
|Dif |30 |数据交换格式。|
以下是代码片段，显示从 xls 转换为 xlsx，同样也可以反过来。

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **下载示例代码**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
