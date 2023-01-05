---
title: 转换
type: docs
weight: 30
url: /zh/net/conversion/
---
Aspose.Cells 独特的功能，在不影响工作的情况下提供版本转换的灵活性。
SaveFormat 是枚举，可以在下表中给出的扩展名中转换文档。

|**成员名字** |**价值** |**描述** |
|:- |:- |:- |
|CSV |1 |表示一个 CSV 文件。|
| Xlsx|6 |表示一个 xlsx 文件。|
| Xlsm|7 |表示启用宏的 xlsm 文件。|
| Xlx|8 |表示一个 xltx 文件。|
| Xltm|9 |表示启用宏的 xltm 文件。|
|TabDelimited |11 |表示制表符分隔的文本文件。|
|HTML|12 |表示一个 html 文件。|
| HTML|17 |表示一个 mhtml 文件。|
|ODS |14 |代表一个ods文件。|
| Excel97To2003|5 |表示 Excel97-2003 xls 文件。|
|SpreadsheetML |15 |表示 Excel 2003 xml 文件。|
| XLSB|16 |表示一个 xlsb 文件。|
|汽车|0 |如果将文件保存到磁盘，文件格式格式根据文件名的扩展名。<br>如果将文件保存到流中，则文件格式为 xlsx。|
|未知|255 |表示无法识别的格式，无法保存。|
| PDF格式|13 |表示一个 Pdf 文件。|
|XPS |20 |表示一个 XPS 文件。|
|TIFF |21 |表示一个 TIFF 文件。|
|SVG |22 |表示一个 SVG 文件。|
|差异|30 |数据交换格式。|
下面是显示从 xls 到 xlsx 的转换的代码片段，反之亦然

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **下载示例代码**
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
