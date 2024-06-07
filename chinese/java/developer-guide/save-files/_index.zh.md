---
title: 将 Excel 文件保存为 CSV、PDF 和其他格式
linktitle: 保存文件
type: docs
weight: 20
url: /zh/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** 允许开发人员使用其灵活的 API 从头开始创建 Excel 文件。一旦创建了 Excel 文件，您还需要保存工作簿（文件）。Aspose.Cells 提供了各种保存这些文件的方式。在本课题中，我们将讨论开发人员可以采用的所有可能的保存文件方式。

{{% /alert %}}

## **保存文件的不同方式**

Aspose.Cells API 提供了一个名为 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 的类，表示一个 Excel 文件并提供开发人员可能需要处理其 Excel 文件所需的所有必要属性和方法。 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 类提供 [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)）方法，用于保存 Excel 文件。[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)）方法有很多重载，用于以不同的方式保存 Excel 文件。

开发人员还可以指定其文件应保存的文件格式。文件可以以多种格式保存，例如 XLS、SpreadsheetML、CSV、Tab Delimited、制表符分隔值 TSV、XPS 等等。这些文件格式是使用 [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) 枚举来指定的。

[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) 枚举包含许多预定义文件格式（可以由您选择）如下:

|**文件格式类型**|**描述**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API尝试从保存方法的第一个参数中指定的文件扩展名中检测适当的格式|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|代表CSV文件|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|代表Office Open XML SpreadsheetML文件|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|代表基于XML的XLSM文件|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|代表Excel模板文件|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|代表启用宏的Excel模板文件|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|代表Excel XLAM文件|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|代表以制表符分隔的值文件|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|代表一个制表符分隔的文本文件|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|代表HTML文件（s）|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|代表MHTML文件（s）|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|代表OpenDocument电子表格文件|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|代表XLS文件，这是Excel 1997至2003版本的默认格式|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|代表SpreadSheetML文件|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|代表Excel 2007二进制XLSB文件|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|代表无法识别的格式，无法保存。|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|代表PDF文档|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|代表XML Paper规范（XPS）文件|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|代表TIFF文件|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|代表基于XML的可伸缩矢量图形（SVG）文件|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|代表数据交换格式。|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|代表数字文件。|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|代表Markdown文档。|
**通常，保存 Excel 文件有两种方式如下:**

1. **将文件保存到某个位置**
1. **保存文件到流中**

## **将文件保存到某个位置**

如果开发人员需要将其文件保存到某个存储位置，则可以在调用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)对象的[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)方法时简单地指定文件名（及其完整存储路径）和所需的文件格式（使用[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)枚举）。

**示例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **将工作簿保存为文本或CSV格式**

有时，您希望将一个包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下Microsoft Excel和Aspose.Cells只保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何包含任意工作表数量的Microsoft Excel或OpenOffice电子表格文件（如XLS、XLSX、XLSM、XLSB、ODS等）。

当代码执行时，它将工作簿中所有工作表的数据转换为TXT格式。

您可以修改相同的示例以将文件保存为CSV格式。 默认情况下，[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator)是逗号，因此在保存为CSV格式时不要指定分隔符。

**示例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **以自定义分隔符保存文本文件**

文本文件包含没有格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **保存文件到流**

如果开发人员需要将其文件保存到**流**中，则应创建**FileOutputStream**对象，然后通过调用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)对象的[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)方法将文件保存到该**流**对象中。开发人员还可以在调用[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)方法时指定所需的文件格式（使用[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)枚举）。

**示例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **保存文件至其他格式**

### **XLS 文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX 文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF 文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **设置AccessibilityExtractContent选项**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)类，您可以获取或设置PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent)选项以控制转换后PDF中的内容访问。这意味着允许屏幕阅读器软件利用PDF文件中的文本来阅读PDF文件。您可以通过应用更改权限密码并取消选择截图中的两个项目来禁用它。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **导出自定义属性至PDF**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)类，您可以将源工作簿中的自定义属性导出为PDF文件。提供了[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)枚举值，用于指定导出属性的方式。这些属性可以在Adobe Acrobat Reader中通过单击“文件”，然后单击“属性”选项来查看。

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **将Excel工作簿转换为Markdown**

Aspose.Cells API支持将电子表格导出为Markdown格式。要将活动工作表导出为Markdown，请将[**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)方法的第二个参数传递为[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)。您还可以使用[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)类指定导出工作表至Markdown的其他设置。

以下代码示例演示了如何使用[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)枚举成员将活动工作表导出为Markdown。请参见代码生成的[Markdown文件输出](Book1.txt)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **高级主题**
- [调整工作簿压缩级别](/cells/zh/java/adjust-workbook-compression-level/)
- [将工作簿转换为不同格式](/cells/zh/java/converting-workbook-to-different-formats/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [跟踪Excel到TIFF的转换进度](/cells/zh/java/track-conversion-progress-of-excel-to-tiff/)
- [跟踪文档转换进度](/cells/zh/java/track-document-conversion-progress/)
