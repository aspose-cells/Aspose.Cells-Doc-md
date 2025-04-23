---
title: 保存文件的不同方式
linktitle: 保存文件
type: docs
weight: 40
url: /zh/python-net/different-ways-to-save-files/
description: Aspose.Cells for Python via .NET 支持多种格式保存文件，包括 PDF、HTML、DOCX、PPTX、JSON、MHTML。
keywords: Aspose.Cells for Python via .NET 支持将 Excel 文件保存为 PDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTML 等格式。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 让文件创建与保存变得简单，本文介绍多种保存方式。

{{% /alert %}}

## **不同的文件保存方式**

Aspose.Cells for Python via .NET 提供 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) ，它代表一个 Microsoft Excel 文件，并提供操作 Excel 文件所需的属性和方法。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含 [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) 方法，用于保存 Excel 文件。[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) 方法有多个重载，支持不同的保存方式。

保存文件的文件格式由[**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)枚举决定

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|表示 CSV 文件|
|Excel97To2003|表示Excel 97-2003文件
|Xlsx|表示Excel 2007 XLSX文件|
|Xlsm|表示Excel 2007 XLSM文件|
|Xltx|表示Excel 2007模板XLTX文件|
|Xltm|表示Excel 2007启用宏的XLTM文件|
|Xlsb|表示Excel 2007二进制XLSB文件|
|SpreadsheetML|表示一种Spreadsheet XML文件|
|TSV|表示制表符分隔数值文件|
|TabDelimited|代表分隔符文本文件|
|ODS|表示 ODS 文件|
|Html|表示HTML文件|
|MHtml|表示一个MHTML文件|
|Pdf|表示一个PDF文件|
|XPS|表示一个XPS文档|
|TIFF|表示Tagged Image File Format (TIFF)|

## **如何将文件保存为不同的格式**

要将文件保存到存储位置，请在调用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)对象的[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)方法时指定文件名（包括存储路径）和所需的文件格式（从[**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)枚举中）。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SavingFiletoSomeLocation-1.py" >}}

## **如何将工作簿保存为PDF**
便携式文档格式（PDF）是Adobe于1990年代创建的一种文档类型。该文件格式的目的是引入一种标准，以在与应用软件、硬件和操作系统无关的格式中表示文档和其他参考材料。PDF文件格式具有完整的能力，可以包含文本、图像、超链接、表单字段、富媒体、数字签名、附件、元数据、地理空间特征和3D对象等信息，这些信息可以成为源文档的一部分。

以下代码展示如何使用 Aspose.Cells for Python via .NET 将工作簿保存为 PDF 文件：
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Save-As-Pdf.py" >}}

## **如何将工作簿保存为文本或CSV格式**

有时，您希望将具有多个工作表的工作簿保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和 Aspose.Cells for Python via .NET 仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何Microsoft Excel或OpenOffice电子表格文件（例如XLS、XLSX、XLSM、XLSB、ODS等），并且可以具有任意数量的工作表。

执行代码后，将会将工作簿中所有工作表的数据转换为TXT格式。

你可以修改相同的示例将文件保存为CSV格式。默认情况下，[**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator) 是逗号，因此在保存为CSV格式时无需指定分隔符。请注意：如果您使用的是评估版，即使将 [**TxtSaveOptions.export_all_sheets**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/export_all_sheets/) 属性设置为 true，程序仍将只导出一个工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToTextCSVFormat-1.py" >}}

## **如何使用自定义分隔符将文件保存为文本文件**

文本文件包含无格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-OpeningTextFilewithCustomSeparator-1.py" >}}


## **如何将Excel文件保存为Html和Mht文件**
Aspose.Cells for Python via .NET 可以轻松保存Excel文件、JSON、CSV或其他文件，这些文件可以被Aspose.Cells for Python via .NET加载为.html和.mht文件。
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-MHTML.py" >}}


## **如何将Excel文件保存为OpenOffice（ODS，SXC，FODS，OTS）**
我们可以将文件保存为开放办公格式：ODS、SXC、FODS、OTS等。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-ODS.py" >}}

## **如何将Excel文件保存为JSON或XML**

JSON（JavaScript对象表示）是一种用于存储和传输数据的开放标准文件格式，它使用人类可读的文本。JSON文件存储为.json扩展名。JSON需要更少的格式化，是XML的一个很好的替代品。JSON源自JavaScript，但是是一种与语言无关的数据格式。许多现代编程语言都支持JSON的生成和解析。application/json是用于JSON的媒体类型。

Aspose.Cells for Python via .NET支持将文件保存为JSON或XML。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-JSON.py" >}}


## **高级主题**
- [调整工作簿压缩级别](/cells/zh/python-net/adjust-workbook-compression-level/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/)

