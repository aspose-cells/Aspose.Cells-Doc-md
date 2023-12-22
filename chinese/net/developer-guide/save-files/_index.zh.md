---
title: 保存文件的不同方法
linktitle: 保存文件
type: docs
weight: 40
url: /zh/net/different-ways-to-save-files/
description: Aspose.Cells for .NET 可以将文件保存为不同的格式。将文件保存到 PDF。 将文件保存到 HTML。 将文件保存到 DOCX。 将文件保存到 PPTX。 将文件保存到 JSON。 将文件保存到 MHTML。
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells 可以创建和保存文件。本文介绍了保存文件的各种方式。

{{% /alert %}}

##  **保存文件的不同方法**

 Aspose.Cells 提供**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**它代表 Microsoft Excel 文件，并提供使用 Excel 文件所需的属性和方法。这**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**类提供了**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**用于保存 Excel 文件的方法。这**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法有许多重载，用于以不同的方式保存文件。

文件保存的文件格式由**[保存格式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**枚举

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|代表CSV文件|
|Excel97To2003|代表 Excel 97 - 2003 文件|
|Xlsx|代表 Excel 2007 XLSX 文件|
|XLSM|代表 Excel 2007 XLSM 文件|
|Xlx|代表 Excel 2007 模板 XLTX 文件|
|西尔特|表示启用宏的 Excel 2007 XLTM 文件|
|Xlsb|表示 Excel 2007 二进制 XLSB 文件|
|SpreadsheetML|表示电子表格 XML 文件|
|TSV|表示制表符分隔值文件|
|TabDelimited|表示制表符分隔的文本文件|
|ODS|代表ODS文件|
|网页|代表 HTML 文件|
|MHtml|代表 MHTML 文件|
|pdf|代表PDF文件|
|XPS|代表一个XPS文档|
|TIFF|表示标记图像文件格式 (TIFF)|

##  **如何将文件保存为不同格式**

要将文件保存到存储位置，请指定文件名（包含存储路径）和所需的文件格式（来自**[保存格式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**枚举）调用时**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**对象的**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **如何将工作簿保存为 PDF**
便携式文档格式 (PDF) 是 Adobe 在 20 世纪 90 年代创建的一种文档类型。该文件格式的目的是引入一种以独立于应用程序软件、硬件以及操作系统的格式表示文档和其他参考材料的标准。 PDF 文件格式完全能够包含文本、图像、超链接、表单字段、富媒体、数字签名、附件、元数据、地理空间特征和 3D 对象等信息，这些信息可以成为源文档的一部分。

以下代码显示如何将工作簿另存为 pdf 文件，格式为 Aspose.Cells：
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **如何将工作簿保存为文本或 CSV 格式**

有时，您想要将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如 TXT、TabDelim、CSV 等），默认情况下 Microsoft Excel 和 Aspose.Cells 都仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何 Microsoft Excel 或 OpenOffice 电子表格文件（例如 XLS、XLSX、XLSM、XLSB、ODS 等）以及任意数量的工作表。

执行代码时，会将工作簿中所有工作表的数据转换为 TXT 格式。

您可以修改相同的示例以将文件保存到 CSV。默认情况下，**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**是逗号，因此如果保存为 CSV 格式，则无需指定分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **如何使用自定义分隔符将文件保存为文本文件**

文本文件包含未格式化的电子表格数据。该文件是一种纯文本文件，其数据之间可以有一些自定义的分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **如何将文件保存到流**

要将文件保存到流中，请创建一个*内存流*或者*文件流*对象并通过调用将文件保存到该流对象**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**对象的**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。使用指定所需的文件格式**[保存格式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**调用时的枚举**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **如何将 Excel 文件保存为 Html 和 Mht 文件**
Aspose.Cells可以简单地保存Excel文件，JSON，CSV或其他可以由Aspose.Cells加载的文件作为.html和.mht文件。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **如何将Excel文件保存到OpenOffice（ODS、SXC、FODS、OTS）**
我们可以将文件保存为open Office格式：ODS、SXC、FODS、OTS等。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **如何将 Excel 文件保存为 JSON 或 XML**

JSON（JavaScript 对象表示法）是一种用于共享数据的开放标准文件格式，它使用人类可读的文本来存储和传输数据。 JSON 文件以 .json 扩展名存储。 JSON 需要较少的格式，是 XML 的良好替代方案。 JSON 源自 JavaScript，但是一种独立于语言的数据格式。许多现代编程语言都支持JSON的生成和解析。 application/json 是 JSON 使用的媒体类型。

Aspose.Cells支持将文件保存为JSON或XML。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **高级主题**
- [调整工作簿压缩级别](/cells/zh/net/adjust-workbook-compression-level/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [将文件保存到响应对象](/cells/zh/net/saving-file-to-response-object/)
