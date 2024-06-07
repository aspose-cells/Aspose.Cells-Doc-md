---
title: 保存文件的不同方式
linktitle: 保存文件
type: docs
weight: 40
url: /zh/net/different-ways-to-save-files/
description: Aspose.Cells for .NET可以保存文件到不同的格式。保存文件为PDF。保存文件为HTML。保存文件为DOCX。保存文件为PPTX。保存文件为JSON。保存文件为MHTML。
keywords: Aspose.Cells可将Excel保存为PDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTML等格式，使用C#，在C#中保存或转换工作簿为PDF、HTML、JSON、TXT、SQL。
---

{{% alert color="primary" %}}

Aspose.Cells使得创建和保存文件成为可能。本文介绍了可以保存文件的各种方式。

{{% /alert %}}

## **保存文件的不同方式**

Aspose.Cells提供代表Microsoft Excel文件的Workbook类，并提供处理Excel文件所需的属性和方法。Workbook类提供用于保存Excel文件的Save方法。Save方法有许多重载，用于以不同方式保存文件。

所保存的文件格式由SaveFormat枚举决定

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|表示CSV文件|
|Excel97To2003|代表一个 Excel 97 - 2003 文件|
|Xlsx|表示Excel 2007 XLSX文件|
|Xlsm|表示Excel 2007 XLSM文件|
|Xltx|表示Excel 2007模板XLTX文件|
|Xltm|表示Excel 2007启用宏的XLTM文件|
|Xlsb|表示Excel 2007二进制XLSB文件|
|SpreadsheetML|表示电子表格XML文件|
|TSV|表示制表符分隔值文件|
|TabDelimited|表示一个Tab分隔文本文件|
|ODS|表示ODS文件|
|Html|表示HTML文件|
|MHtml|表示MHTML文件
|Pdf|表示PDF文件|
|XPS|表示XPS文档|
|TIFF|表示带标签的图像文件格式（TIFF）|

## **如何将文件保存为不同格式**

要将文件保存到存储位置，请在调用Workbook对象的Save方法时，指定文件名（完整的存储路径）和所需的文件格式（来自SaveFormat枚举）。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **如何将工作簿保存为Pdf**
便携文档格式（PDF）是由Adobe在上世纪90年代创建的一种文档类型。这种文件格式的目的是引入一种标准，以在与应用软件、硬件以及操作系统无关的格式中表示文档和其他参考资料。PDF文件格式可以包含文本、图像、超链接、表单字段、富媒体、数字签名、附件、元数据、地理空间特征和3D对象等信息，这些信息可以成为源文档的一部分。

以下代码显示如何使用Aspose.Cells将工作簿保存为pdf文件:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **如何将工作簿保存为文本或CSV格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何包含任意工作表数量的Microsoft Excel或OpenOffice电子表格文件（如XLS、XLSX、XLSM、XLSB、ODS等）。

当代码执行时，它将工作簿中所有工作表的数据转换为TXT格式。

您可以修改相同示例以将文件保存为CSV。默认情况下，**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)** 为逗号，因此如果保存为CSV格式，则不要指定分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **如何使用自定义分隔符将文件保存为文本文件**

文本文件包含没有格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **如何将文件保存到流**

要将文件保存到流，创建一个 *MemoryStream* 或 *FileStream* 对象，并通过调用 **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** 对象的 **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** 方法将文件保存到该流对象。在调用 **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** 方法时，使用 **[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** 枚举指定所需的文件格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **如何将 Excel 文件保存为 Html 和 Mht 文件**
Aspose.Cells 可以简单地将 Excel 文件、JSON、CSV 或其他文件保存为 .html 和 .mht 文件。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}


## **如何将 Excel 文件保存为 OpenOffice（ODS、SXC、FODS、OTS）**
我们可以将文件保存为 OpenOffice 格式：ODS、SXC、FODS、OTS 等。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **如何将 Excel 文件保存为 JSON 或 XML**

JSON（JavaScript 对象表示）是一种用于共享数据的开放标准文件格式，它使用人类可读的文本来存储和传输数据。JSON 文件存储为 .json 扩展名。JSON 需要较少的格式化，是 XML 的良好替代品。JSON 源自 JavaScript，但是是一种与语言无关的数据格式。许多现代编程语言都支持 JSON 的生成和解析。application/json 是用于 JSON 的媒体类型。

Aspose.Cells 支持将文件保存为 JSON 或 XML。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **高级主题**
- [调整工作簿压缩级别](/cells/zh/net/adjust-workbook-compression-level/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [将文件保存到响应对象](/cells/zh/net/saving-file-to-response-object/)
