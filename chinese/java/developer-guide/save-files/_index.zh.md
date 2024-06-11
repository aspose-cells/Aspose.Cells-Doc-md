---
title: 将 Excel 文件保存为 CSV、PDF 和其他格式
linktitle: 保存文件
type: docs
weight: 20
url: /zh/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** 允许开发人员使用其灵活的 API 从头开始创建 Excel 文件。创建 Excel 文件后，您还需要保存工作簿（文件）。Aspose.Cells 提供了多种保存这些文件的方式。在本主题中，我们将讨论开发人员可以采用的所有可能的保存方式。

{{% /alert %}}

## **保存文件的不同方式**

Aspose.Cells API 提供了一个名为 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 的类，代表 Excel 文件，并提供开发人员可能需要处理其 Excel 文件所需的所有必要属性和方法。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 类提供了一个 [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) 方法，用于保存 Excel 文件。[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) 方法有许多重载，用于以不同方式保存 Excel 文件。

开发人员还可以指定文件应保存的文件格式。文件可以以多种格式保存，如 XLS、SpreadsheetML、CSV、Tab Delimited、Tab-separated values TSV、XPS 等。这些文件格式使用 [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) 枚举进行指定。

[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) 枚举包含许多预定义的文件格式（可以由您选择），如下所示：

|**文件格式类型**|**描述**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API尝试从保存方法中指定的文件扩展名检测适当的格式
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|表示CSV文件
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|表示Office Open XML SpreadsheetML文件|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|表示基于XML的XLSM文件|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|表示Excel模板文件|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|表示启用宏的Excel模板文件|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|表示Excel XLAM文件|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|表示制表符分隔的值文件|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|表示制表符分隔的文本文件|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|表示HTML文件|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|表示MHTML文件|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|表示开放文档电子表格文件|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|表示XLS文件，是Excel 1997到2003版本的默认格式|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|表示SpreadSheetML文件|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|表示Excel 2007二进制XLSB文件|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|表示无法识别的格式，无法保存|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|表示PDF文档|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|表示XML Paper Specification (XPS)文件|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|表示Tagged Image File Format (TIFF)文件|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|表示基于XML的可伸缩矢量图形 (SVG) 文件|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|表示数据交换格式|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|表示一个数字文件|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|表示一个markdown文档。
**通常，有两种方法可以保存Excel文件如下:**

1. **将文件保存到某个位置**
1. **将文件保存到流中**

## **将文件保存到某个位置**

如果开发人员需要将文件保存到某个存储位置，他们可以在调用对象的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)方法时简单指定文件名（完整的存储路径）和所需的文件格式（使用[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)枚举）。

**示例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **将工作簿保存为文本或CSV格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何Microsoft Excel或OpenOffice电子表格文件（例如XLS、XLSX、XLSM、XLSB、ODS等），并且可以具有任意数量的工作表。

当代码执行时，将工作簿中所有工作表的数据转换为TXT格式。

您可以修改相同的示例以将文件保存为CSV。默认情况下，[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator)是一个逗号，因此在保存为CSV格式时不要指定分隔符。

**示例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **使用自定义分隔符保存文本文件**

文本文件包含无格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **将文件保存到流中**

如果开发人员需要将文件保存到**Stream**，则应创建一个**FileOutputStream**对象，然后通过调用对象的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)方法将文件保存到该**Stream**对象中。开发人员还可以在调用对象的[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)方法时指定所需的文件格式（使用[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)枚举）。

**示例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **将文件保存为其他格式**

### **XLS文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **设置ContentCopyForAccessibility选项**

通过[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)类，您可以获取或设置PDF[**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent)选项以控制转换后PDF中的内容访问。这意味着它允许屏幕阅读器软件利用PDF文件中的文本来阅读PDF文件。您可以通过应用更改权限密码并取消在截图中选择两个项目来禁用它。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **导出自定义属性到PDF**

通过[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)类，您可以将源工作簿中的自定义属性导出到PDF中。提供了[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)枚举用于指定导出属性的方式。您可以通过单击“文件”，然后单击属性选项在Adobe Acrobat Reader中查看这些属性。

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **将Excel工作簿转换为Markdown**

Aspose.Cells API支持将电子表格导出为Markdown格式。要导出活动工作表为Markdown，请将[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)作为[**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)方法的第二个参数传递。

以下代码示例演示了如何使用[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)枚举成员将活动工作表导出为Markdown。请参阅代码生成的[Markdown文件](Book1.txt)以供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **高级主题**
- [调整工作簿压缩级别](/cells/zh/java/adjust-workbook-compression-level/)
- [将工作簿转换为不同的格式](/cells/zh/java/converting-workbook-to-different-formats/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [跟踪Excel转换为TIFF的进度](/cells/zh/java/track-conversion-progress-of-excel-to-tiff/)
- [跟踪文档转换进度](/cells/zh/java/track-document-conversion-progress/)
