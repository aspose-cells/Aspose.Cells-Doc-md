---
title: Saving Excel files to CSV, PDF and other formats
type: docs
weight: 35
url: /java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** allows developers to create Excel files from scratch using its flexible API. Once you create Excel files, you would also need to save your workbook (file). Aspose.Cells provides a variety of ways to save these files. In this topic, we will discuss all those possible ways that can be adopted by developers to save their files.

{{% /alert %}}

## **Different Ways to Save Your Files**

Aspose.Cells API provides a class named [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) that represents an Excel file and provides all necessary properties and methods that developers may need to work with their Excel files. The [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) class provides a [**save**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method that is used to save Excel files. The [**save**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method has many overloads that are used to save Excel files in different ways.

Developers can also specify the file format in which their files should be saved. The files can be saved in several formats such as XLS, SpreadsheetML, CSV, Tab Delimited, Tab-separated values TSV, XPS and many more. These file formats are specified using the [**SaveFormat**](https://apireference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumeration.

[**SaveFormat**](https://apireference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumeration contains many pre-defined file formats (that can be chosen by you) as follows:

|**File Format Types**|**Description**|
| :- | :- |
|[**AUTO**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API tries to detect the appropriate format from the file extension specified in the first parameter to the save method|
|[**CSV**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Represents a CSV file|
|[**XLSX**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Represents an Office Open XML SpreadsheetML file|
|[**XLSM**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Represents XML-based XLSM file|
|[**XLTX**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Represents an Excel template file|
|[**XLTM**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Represents an Excel Macro-enabled template file|
|[**XLAM**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Represents an Excel XLAM file|
|[**TSV**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Represents a Tab-separated values file|
|[**TAB_DELIMITED**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Represents a Tab Delimited text file|
|[**HTML**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Represents an HTML file(s)|
|[**M_HTML**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Represents an MHTML file(s)|
|[**ODS**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Represents an OpenDocument Spreadsheet file|
|[**EXCEL_97_TO_2003**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Represents an XLS file that is the default format for Excel 1997 to 2003 revisions|
|[**SPREADSHEET_ML**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Represents a SpreadSheetML file|
|[**XLSB**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Represents an Excel 2007 binary XLSB file|
|[**UNKNOWN**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Represents unrecognized format, cannot be saved.|
|[**PDF**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Represents a PDF Document|
|[**XPS**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Represents an XML Paper Specification (XPS) file|
|[**TIFF**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Represents a Tagged Image File Format (TIFF) file|
|[**SVG**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Represents an XML-based Scalable Vector Graphics (SVG) file|
|[**DIF**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Represents Data Interchange Format.|
|[**NUMBERS**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Represents a numbers file.|
|[**MARKDOWN**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Represents a markdown document.|
**Normally, there are two ways to save Excel files as follows:**

1. **Saving the file to some location**
1. **Saving the file to a stream**

## **Saving File to Some Location**

If developers need to save their files to some storage location then they can simply specify the file name (with its complete storage path) and desired file format (using the [**SaveFormat**](https://apireference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumeration) while calling the [**save**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method of [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) object.

**Example:**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Saving Workbook to Text or CSV Format**

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into text format. Load the source workbook which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS and so on) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to TXT format.

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.Separator**](https://apireference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) is a comma, so do not specify a separator if saving to CSV format.

**Example:**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Saving Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Saving File to a Stream**

If developers need to save their files to a **Stream** then they should create a **FileOutputStream** object and then save the file to that **Stream** object by calling the [**save**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method of [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) object. Developers can also specify the desired file format (using the [**SaveFormat**](https://apireference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumeration) while calling the [**save**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method.

**Example:**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Saving File to Other Format**

### **XLS Files**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX Files**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF Files**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Set ContentCopyForAccessibility option**

With the [**PdfSaveOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) class, you can get or set the PDF [**AccessibilityExtractContent**](https://apireference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) option to control the content access in the converted PDF. It means it allows screen reader software to utilize the text within the PDF file for reading the PDF file.  You can disable it by applying a change permissions password and deselecting the two items in the screenshot [here](71630877.png).

{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Export Custom properties to PDF**

With the [**PdfSaveOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) class, you can export the custom properties in source workbook to the PDF. [**PdfCustomPropertiesExport**](https://apireference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) enumerator is provided for specifying the way by which properties are exported. These properties can be observed in Adobe Acrobat Reader by clicking on File and then properties option as shown in the following image. Template file "sourceWithCustProps.xlsx"  can be downloaded [here](sourceWithCustProps.xlsx) for testing and output PDF file "outSourceWithCustProps" is available [here](outSourceWithCustProps.pdf) for analysis.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Convert Excel Workbook to Markdown**

The Aspose.Cells API provides support for exporting spreadsheets to Markdown format. To export the active worksheet to Markdown, pass [**SaveFormat.Markdown**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) as the second parameter of [**Workbook.Save**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) method. You may also use [**MarkdownSaveOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions) class to specify additional settings for exporting worksheet to Markdown.

The following code example demonstrates exporting active worksheet to Markdown by using [**SaveFormat.Markdown**](https://apireference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) enumeration member. Please see the [output Markdown file](Book1.md) generated by the code for reference.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}
