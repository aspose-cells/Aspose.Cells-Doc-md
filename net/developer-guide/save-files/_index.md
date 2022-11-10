---
title: Different Ways to Save Files
linktitle: Save Files
type: docs
weight: 40
url: /net/different-ways-to-save-files/
aliases: [/net/convert-excel-to-xml/,/net/convert-excel-to-sxc/,/net/convert-excel-to-fods/,/net/convert-excel-to-dif/]
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to create and save files. This article explains the various ways in which files can be saved.

{{% /alert %}}

## **Different Ways to Save Files**

Aspose.Cells provides the **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** which represents a Microsoft Excel file and provides the properties and methods necessary to work with Excel files. The **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** class provides the **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** method used to save Excel files. The **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** method has many overloads that are used to save files in different ways.

The file format that the file is saved to is decided by the **[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumeration

|**File Format Types**|**Description**|
| :- | :- |
|CSV|Represents a CSV file|
|Excel97To2003|Represents an Excel 97 - 2003 file|
|Xlsx|Represents an Excel 2007 XLSX file|
|Xlsm|Represents an Excel 2007 XLSM file|
|Xltx|Represents an Excel 2007 template XLTX file|
|Xltm|Represents an Excel 2007 macro-enabled XLTM file|
|Xlsb|Represents an Excel 2007 binary XLSB file|
|SpreadsheetML|Represents a Spreadsheet XML file|
|TSV|Represents a Tab-separated values file|
|TabDelimited|Represents a Tab Delimited text file|
|ODS|Represents an ODS file|
|Html|Represents HTML file(s)|
|MHtml|Represents an MHTML file(s)|
|Pdf|Represents a PDF file|
|XPS|Represents an XPS document|
|TIFF|Represents Tagged Image File Format (TIFF)|

## **Saving File to Some Location**

To save files to a storage location, specify the file name (complete with storage path) and the desired file format (from the **[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumeration) when calling the **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** object's **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** method.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Saving Workbook to Text or CSV Format**

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into text format. Load the source workbook which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS and so on) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.

You can modify the same example to save your file to CSV. By default, **[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)** is comma, so do not specify a separator if saving to CSV format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Saving Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Saving File to a Stream**

To save files to a stream, create a *MemoryStream* or *FileStream* object and save the file to that stream object by calling the **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** object's **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** method. Specify the desired file format using the **[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumeration when calling the **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** method.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Saving as OpenOffice (ODS, SXC, FODS, OTS)**
We can saving the files as open offce format : ODS, SXC, FODS, OTS etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Saving Excel file as JSON or XML**

JSON (JavaScript Object Notation) is an open standard file format for sharing data that uses human-readable text to store and transmit data. JSON files are stored with the .json extension. JSON requires less formatting and is a good alternative for XML. JSON is derived from JavaScript but is a language-independent data format. The generation and parsing of JSON is supported by many modern programming languages. application/json is the media type used for JSON.

Aspose.Cells supports saving files to JSON or XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}