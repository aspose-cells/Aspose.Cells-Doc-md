---
title: 将Excel文件保存为CSV、PDF等格式
linktitle: 保存文件
type: docs
weight: 20
url: /zh/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells**允许开发人员使用其灵活的 API 从头开始创建 Excel 文件。创建 Excel 文件后，您还需要保存工作簿（文件）。 Aspose.Cells 提供了多种保存这些文件的方法。在本主题中，我们将讨论开发人员可以采用的所有可能的文件保存方式。

{{% /alert %}}

## **保存文件的不同方法**

Aspose.Cells API 提供了一个名为[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)表示一个 Excel 文件并提供开发人员处理其 Excel 文件可能需要的所有必要属性和方法。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类提供了[**节省**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)方法，用于保存 Excel 文件。这[**节省**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)方法有许多重载，用于以不同方式保存 Excel 文件。

开发人员还可以指定保存文件的文件格式。这些文件可以保存为多种格式，例如 XLS、SpreadsheetML、CSV、制表符分隔、制表符分隔值 TSV、XPS 等等。这些文件格式使用[**保存格式**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)枚举。

[**保存格式**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)枚举包含许多预定义的文件格式（可以由您选择），如下所示：

|**文件格式类型**|**描述**|
|:- |:- |
|[**汽车**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API 尝试检测从第一个参数中指定的文件扩展名到保存方法的适当格式|
|[**CSV文件**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|表示 CSV 文件|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|表示 Office Open XML SpreadsheetML 文件|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|表示基于 XML 的 XLSM 文件|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|代表一个Excel模板文件|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|表示启用 Excel 宏的模板文件|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|表示 Excel XLAM 文件|
|[**硅通孔**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|表示制表符分隔值文件|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|表示制表符分隔的文本文件|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|代表一个 HTML 文件|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|表示一个 MHTML 文件|
|[**消耗臭氧层物质**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|表示 OpenDocument 电子表格文件|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|代表一个 XLS 文件，它是 Excel 1997 到 2003 修订版的默认格式|
|[**电子表格_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|表示一个 SpreadSheetML 文件|
|[**超低频**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|表示 Excel 2007 二进制 XLSB 文件|
|[**未知**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|表示无法识别的格式，无法保存。|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|代表一个PDF文件|
|[**聚苯乙烯**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|表示 XML 纸张规范 (XPS) 文件|
|[**国际电影节**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|表示标记图像文件格式 (TIFF) 文件|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|表示基于 XML 的可缩放矢量图形 (SVG) 文件|
|[**差值**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|表示数据交换格式。|
|[**数字**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|代表数字文件。|
|[**降价促销**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|代表降价文件。|
**通常情况下，保存Excel文件的方法有以下两种：**

1. **将文件保存到某个位置**
1. **将文件保存到流**

## **将文件保存到某个位置**

如果开发人员需要将他们的文件保存到某个存储位置，那么他们可以简单地指定文件名（及其完整的存储路径）和所需的文件格式（使用[**保存格式**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)枚举），同时调用[**节省**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)） 的方法[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)目的。

**例子：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **将工作簿保存为文本或 CSV 格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如 TXT、TabDelim、CSV 等），默认情况下 Microsoft Excel 和 Aspose.Cells 都只保存活动工作表的内容。

下面的代码示例说明了如何将整个工作簿保存为文本格式。加载源工作簿，它可以是任何 Microsoft Excel 或 OpenOffice 电子表格文件（如 XLS、XLSX、XLSM、XLSB、ODS 等）和任意数量的工作表。

代码执行时，将工作簿中所有工作表的数据转换为TXT格式。

您可以修改同一示例以将文件保存为 CSV。默认，[**TxtSaveOptions.分隔符**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator)是逗号，所以如果保存为 CSV 格式，请不要指定分隔符。

**例子：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **使用自定义分隔符保存文本文件**

文本文件包含未格式化的电子表格数据。该文件是一种纯文本文件，其数据之间可以有一些自定义的分隔符。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **将文件保存到流**

如果开发人员需要将他们的文件保存到**溪流**那么他们应该创建一个**文件输出流**对象，然后将文件保存到那个**溪流**通过调用对象[**节省**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)） 的方法[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)目的。开发人员还可以指定所需的文件格式（使用[**保存格式**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)枚举），同时调用[**节省**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)） 方法。

**例子：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **将文件保存为其他格式**

### **XLS 文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX 文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF文件**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **设置 ContentCopyForAccessibility 选项**

随着[**Pdf保存选项**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)类，您可以获取或设置 PDF[**辅助功能提取内容**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent)选项来控制转换后的 PDF 中的内容访问。这意味着它允许屏幕阅读器软件利用 PDF 文件中的文本来阅读 PDF 文件。您可以通过应用更改权限密码并取消选择屏幕截图中的两项来禁用它[这里](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **将自定义属性导出为 PDF**

随着[**Pdf保存选项**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)类，您可以将源工作簿中的自定义属性导出到 PDF。[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)枚举器用于指定导出属性的方式。可以在 Adobe Acrobat Reader 中通过单击“文件”然后单击“属性”选项来观察这些属性，如下图所示。可以下载模板文件“sourceWithCustProps.xlsx”[这里](sourceWithCustProps.xlsx)用于测试和输出 PDF 文件“outSourceWithCustProps”可用[这里](outSourceWithCustProps.pdf)进行分析。

![待办事项：图像_替代_文本](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **将 Excel 工作簿转换为 Markdown**

Aspose.Cells API 提供了将电子表格导出为Markdown格式的支持。要将活动工作表导出到 Markdown，请通过[**保存格式.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)作为第二个参数[**工作簿.保存**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)） 方法。您也可以使用[**Markdown 保存选项**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)类以指定将工作表导出到 Markdown 的其他设置。

下面的代码示例演示了通过使用将活动工作表导出到 Markdown[**保存格式.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)枚举成员。请参阅[输出 Markdown 文件](Book1.txt)生成的代码供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **推进主题**
- [调整工作簿压缩级别](/cells/zh/java/adjust-workbook-compression-level/)
- [将工作簿转换为不同格式](/cells/zh/java/converting-workbook-to-different-formats/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [跟踪 Excel 到 TIFF 的转换进度](/cells/zh/java/track-conversion-progress-of-excel-to-tiff/)
- [跟踪文档转换进度](/cells/zh/java/track-document-conversion-progress/)
