---
title: 通过C++使用Golang保存文件的不同方法
linktitle: 保存文件
type: docs
weight: 40
url: /zh/go-cpp/different-ways-to-save-files/
description: Aspose.Cells for C++可以将文件保存为不同格式。保存为PDF。保存为HTML。保存为DOCX。保存为PPTX。保存为JSON。保存为MHTML。
keywords: Aspose.Cells使用C++将Excel保存为PDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTML等格式，或将工作簿保存或转换为PDF、HTML、JSON、TXT、SQL。
---

{{% alert color="primary" %}}

Aspose.Cells 可以创建和保存文件。本文介绍了可保存文件的各种方式。

{{% /alert %}}

## **不同的文件保存方式**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)，代表Microsoft Excel文件，并提供必要的属性和方法来处理Excel文件。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)类提供了用于保存Excel文件的[**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法。[**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法有许多重载，用于以不同的方式保存文件。

保存文件的文件格式由[**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/)枚举决定

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

要将文件保存到存储位置，请在调用[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象的[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法时指定文件名（包括存储路径）和所需的文件格式（从[**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/)枚举中）。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles.go" >}}
## **如何将工作簿保存为PDF**
便携式文档格式（PDF）是Adobe于1990年代创建的一种文档类型。该文件格式的目的是引入一种标准，以在与应用软件、硬件和操作系统无关的格式中表示文档和其他参考材料。PDF文件格式具有完整的能力，可以包含文本、图像、超链接、表单字段、富媒体、数字签名、附件、元数据、地理空间特征和3D对象等信息，这些信息可以成为源文档的一部分。

以下代码显示了如何使用Aspose.Cells将工作簿保存为PDF文件：
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-1.go" >}}
## **如何将工作簿保存为文本或CSV格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells都仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何Microsoft Excel或OpenOffice电子表格文件（例如XLS、XLSX、XLSM、XLSB、ODS等），并且可以具有任意数量的工作表。

执行代码后，将会将工作簿中所有工作表的数据转换为TXT格式。

你可以修改相同的示例将文件保存为CSV格式。默认情况下，[**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) 是逗号，因此在保存为CSV格式时无需指定分隔符。请注意：如果您使用的是评估版，即使将 [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) 属性设置为 true，程序仍将只导出一个工作表。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-2.go" >}}
## **如何使用自定义分隔符将文件保存为文本文件**

文本文件包含无格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-3.go" >}}
## **如何将文件保存到流中**

要将文件保存到流，请创建*MemoryStream*或*FileStream*对象，并通过调用[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)对象的[**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法将文件保存到该流对象。在调用[**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法时，使用[**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举指定所需的文件格式。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-4.go" >}}
## **如何将Excel文件保存为Html和Mht文件**
Aspose.Cells可以简单地保存一个Excel文件、JSON、CSV或其他可以被Aspose.Cells加载的文件为.html和.mht文件。
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-5.go" >}} 

## **如何将Excel文件保存为OpenOffice（ODS，SXC，FODS，OTS）**
我们可以将文件保存为开放办公格式：ODS、SXC、FODS、OTS等。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-6.go" >}}
## **如何将Excel文件保存为JSON或XML**

JSON（JavaScript对象表示）是一种用于存储和传输数据的开放标准文件格式，它使用人类可读的文本。JSON文件存储为.json扩展名。JSON需要更少的格式化，是XML的一个很好的替代品。JSON源自JavaScript，但是是一种与语言无关的数据格式。许多现代编程语言都支持JSON的生成和解析。application/json是用于JSON的媒体类型。

Aspose.Cells支持将文件保存为JSON或XML。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-7.go" >}}

## **高级主题**
- [调整工作簿压缩级别](/cells/zh/cpp/adjust-workbook-compression-level/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [将文件保存到响应对象](/cells/zh/cpp/saving-file-to-response-object/)
