---
title : "Saving Excel files to CSV PDF and other formats" 
description : "" 
weight : 12066 
toc : false
type: docs
url: /java/developerguide/ld-sv-cvt-mng/saving+excel+files+to+csv+pdf+and+other+formats/
---

# Aspose.Cells for Java : Saving Excel files to CSV, PDF and other formats


**Aspose.Cells** allows developers to create Excel files from scratch using its flexible API. Once you create Excel files, you would also need to save your workbook (file). Aspose.Cells provides a variety of ways to save these files. In this topic, we will discuss all those possible ways that can be adopted by developers to save their files.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Different Ways to Save Your Files](#different-ways-to-save-your-files)
*   2 [Saving File to Some Location](#saving-file-to-some-location)
*   3 [Saving Workbook to Text or CSV Format](#saving-workbook-to-text-or-csv-format)
*   4 [Saving Text Files with Custom Separator](#saving-text-files-with-custom-separator)
*   5 [Saving File to a Stream](#saving-file-to-a-stream)
*   6 [Saving File to Other Format](#saving-file-to-other-format)
    *   6.1 [XLS Files](#xls-files)
    *   6.2 [XLSX Files](#xlsx-files)
    *   6.3 [PDF Files](#pdf-files)
        *   6.3.1 [Set ContentCopyForAccessibility option](#set-contentcopyforaccessibility-option)
        *   6.3.2 [Export Custom properties to PDF](#export-custom-properties-to-pdf)
*   7 [Convert Excel Workbook to Markdown](#convert-excel-workbook-to-markdown)
{{< /panel >}}
 

## Different Ways to Save Your Files

Aspose.Cells API provides a class named [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) that represents an Excel file and provides all necessary properties and methods that developers may need to work with their Excel files. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) class provides a [save](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method that is used to save Excel files. The [save](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method has many overloads that are used to save Excel files in different ways.

Developers can also specify the file format in which their files should be saved. The files can be saved in several formats such as XLS, SpreadsheetML, CSV, Tab Delimited, Tab-separated values TSV, XPS and many more. These file formats are specified using the [SaveFormat](https://apireference.aspose.com/java/cells/com.aspose.cells/SaveFormat) enumeration.

[SaveFormat](https://apireference.aspose.com/java/cells/com.aspose.cells/SaveFormat) enumeration contains many pre-defined file formats (that can be chosen by you) as follows:

{{< table style="table-striped" >}}
|File Format Types|Description|
|:----|:----|
|[AUTO](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#AUTO)|API tries to detect the appropriate format from the file extension specified in the first parameter to the `save` method|
|[CSV](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#CSV)|Represents a CSV file|
|[XLSX](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#XLSX)|Represents an Office Open XML SpreadsheetML file|
|`[XLSM](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#XLSM)`|Represents XML-based XLSM file|
|[XLTX](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#XLTX)|Represents an Excel template file|
|[XLTM](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#XLTM)|Represents an Excel Macro-enabled template file|
|[XLAM](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#XLAM)|Represents an Excel XLAM file|
|[TSV](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#TSV)|Represents a Tab-separated values file|
|[TAB\_DELIMITED](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#TAB_DELIMITED)|Represents a Tab Delimited text file|
|[HTML](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#HTML)|Represents an HTML file(s)|
|[M\_HTML](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#M_HTML)|Represents an MHTML file(s)|
|[ODS](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#ODS)|Represents an OpenDocument Spreadsheet file|
|[EXCEL\_97\_TO\_2003](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Represents an XLS file that is the default format for Excel 1997 to 2003 revisions|
|[SPREADSHEET\_ML](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#SPREADSHEET_ML)|Represents a SpreadSheetML file|
|[XLSB](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#XLSB)|Represents an Excel 2007 binary XLSB file|
|[UNKNOWN](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#UNKNOWN)|Represents unrecognized format, cannot be saved.|
|[PDF](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#PDF)|Represents a PDF Document|
|[XPS](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#XPS)|Represents an XML Paper Specification (XPS) file|
|[TIFF](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#TIFF)|Represents a Tagged Image File Format (TIFF) file|
|[SVG](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#SVG)|Represents an XML-based Scalable Vector Graphics (SVG) file|
|[DIF](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#DIF)|Represents Data Interchange Format.|
|[NUMBERS](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#NUMBERS)|Represents a numbers file.|
|[MARKDOWN](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#MARKDOWN)|Represents a markdown document.|
{{< /table >}}

**Normally, there are two ways to save Excel files as follows:**

1.  **Saving the file to some location**
2.  **Saving the file to a stream**

## Saving File to Some Location

If developers need to save their files to some storage location then they can simply specify the file name (with its complete storage path) and desired file format (using the [SaveFormat](https://apireference.aspose.com/java/cells/com.aspose.cells/SaveFormat) enumeration) while calling the [save](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method of [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) object.

**Example:**


## Saving Workbook to Text or CSV Format

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into text format. Load the source workbook which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS and so on) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to TXT format.

You can modify the same example to save your file to CSV. By default, [TxtSaveOptions.Separator](https://apireference.aspose.com/java/cells/com.aspose.cells/txtsaveoptions#Separator) is a comma, so do not specify a separator if saving to CSV format.

**Example:**

## Saving Text Files with Custom Separator

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.

## Saving File to a Stream

If developers need to save their files to a **Stream** then they should create a **FileOutputStream** object and then save the file to that **Stream** object by calling the [save](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method of [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) object. Developers can also specify the desired file format (using the [SaveFormat](https://apireference.aspose.com/java/cells/com.aspose.cells/SaveFormat) enumeration) while calling the **save** method.

**Example:**

## Saving File to Other Format

### XLS Files

### XLSX Files

### PDF Files

#### Set ContentCopyForAccessibility option

With the [PdfSaveOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/PdfSaveOptions) class, you can get or set the PDF [AccessibilityExtractContent](https://apireference.aspose.com/java/cells/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) option to control the content access in the converted PDF. It means it allows screen reader software to utilize the text within the PDF file for reading the PDF file.  You can disable it by applying a change permissions password and deselecting the two items in the screenshot [here](https://docs2.aspose.com/cells/java/attachments/5276010/71630877.png).

#### Export Custom properties to PDF

With the [PdfSaveOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/PdfSaveOptions) class, you can export the custom properties in source workbook to the PDF. [PdfCustomPropertiesExport](https://apireference.aspose.com/java/cells/com.aspose.cells/PdfCustomPropertiesExport) enumerator is provided for specifying the way by which properties are exported. These properties can be observed in Adobe Acrobat Reader by clicking on File and then properties option as shown in the following image. Template file "sourceWithCustProps.xlsx"  can be downloaded [here](https://docs.aspose.com/download/attachments/5013526/sourceWithCustProps.xlsx?version=1&modificationDate=1537199854325&api=v2) for testing and output PDF file "outSourceWithCustProps" is available [here](https://docs.aspose.com/download/attachments/5013526/outSourceWithCustProps.pdf?version=1&modificationDate=1537199854325&api=v2) for analysis.

![](https://docs2.aspose.com/cells/java/attachments/5276010/72417294.png)

## Convert Excel Workbook to Markdown

The Aspose.Cells API provides support for exporting spreadsheets to Markdown format. To export the active worksheet to Markdown, pass [SaveFormat.Markdown](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#MARKDOWN) as the second parameter of [Workbook.Save](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#save(java.lang.String,%20int)) method. You may also use [MarkdownSaveOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/MarkdownSaveOptions) class to specify additional settings for exporting worksheet to Markdown.

The following code example demonstrates exporting active worksheet to Markdown by using [SaveFormat.Markdown](https://apireference.aspose.com/java/cells/com.aspose.cells/saveformat#MARKDOWN) enumeration member. Please see the [output Markdown file](https://docs.aspose.com/download/attachments/5013525/Book1.md?version=1&modificationDate=1557893527266&api=v2) generated by the code for reference.

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Screen+Shot+2015-05-21+at+8.50.49+AM.png](https://docs2.aspose.com/cells/java/attachments/5276010/71630877.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [image2018-9-19 20:7:4.png](https://docs2.aspose.com/cells/java/attachments/5276010/72417293.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [CustomProperties.PNG](https://docs2.aspose.com/cells/java/attachments/5276010/72417294.png) (image/png)  

