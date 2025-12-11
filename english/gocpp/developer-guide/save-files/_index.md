---
title: Different Ways to Save Files with Golang via C++
linktitle: Save Files
type: docs
weight: 40
url: /go-cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ can save files to different formats. Save Files to PDF. Save Files to HTML. Save Files to DOCX. Save Files to PPTX. Save Files to JSON. Save Files to MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C++, Save or Convert Workbook to PDF HTML JSON TXT SQL in C++.
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to create and save files. This article explains the various ways in which files can be saved.

{{% /alert %}}

## **Different Ways to Save Files**

Aspose.Cells provides the [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) which represents a Microsoft Excel file and provides the properties and methods necessary to work with Excel files. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class provides the [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) method used to save Excel files. The [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) method has many overloads that are used to save files in different ways.

The file format that the file is saved to is decided by the [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration

|**File Format Types**|**Description**|
| :- | :- |
|CSV|Represents a CSV file|
|Excel97To2003|Represents an Excel 97-2003 file|
|Xlsx|Represents an Excel 2007 XLSX file|
|Xlsm|Represents an Excel 2007 XLSM file|
|Xltx|Represents an Excel 2007 template XLTX file|
|Xltm|Represents an Excel 2007 macro‑enabled XLTM file|
|Xlsb|Represents an Excel 2007 binary XLSB file|
|SpreadsheetML|Represents a Spreadsheet XML file|
|TSV|Represents a Tab‑separated values file|
|TabDelimited|Represents a Tab‑Delimited text file|
|ODS|Represents an ODS file|
|Html|Represents HTML file(s)|
|MHtml|Represents an MHTML file(s)|
|Pdf|Represents a PDF file|
|XPS|Represents an XPS document|
|TIFF|Represents Tagged Image File Format (TIFF)|

## **How to Save File to Different Formats**

To save files to a storage location, specify the file name (complete with storage path) and the desired file format (from the [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration) when calling the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object's [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles.go" >}}
## **How to Save Workbook to PDF**
Portable Document Format (PDF) is a type of document created by Adobe back in the 1990s. The purpose of this file format was to introduce a standard for representation of documents and other reference material in a format that is independent of application software, hardware, as well as operating systems. The PDF file format has full capability to contain information such as text, images, hyperlinks, form fields, rich media, digital signatures, attachments, metadata, geospatial features, and 3D objects that can become part of the source document.

The following code shows how to save a workbook as a PDF file with Aspose.Cells:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-1.go" >}}
## **How to Save Workbook to Text or CSV Format**

Sometimes, you want to convert or save a workbook with multiple worksheets into a text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into a text format. Load the source workbook, which could be any Microsoft Excel or OpenOffice spreadsheet file (e.g., XLS, XLSX, XLSM, XLSB, ODS, and so on) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.

You can modify the same example to save your file to CSV. By default, `TxtSaveOptions.GetSeparator()` is a comma, so do not specify a separator if saving to CSV format. Please note: If you are using the evaluation version and even if the `TxtSaveOptions.GetExportAllSheets()` property is set to true, the program will still export only one worksheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-2.go" >}}
## **How to Save File to Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain‑text file that can have customized delimiters between its data.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-3.go" >}}
## **How to Save File to a Stream**

To save files to a stream, create a *MemoryStream* or *FileStream* object and save the file to that stream object by calling the [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) object's [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) method. Specify the desired file format using the [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration when calling the **Save** method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-4.go" >}}
## **How to Save Excel File to HTML and MHT Files**
Aspose.Cells can simply save an Excel file, JSON, CSV, or other files that can be loaded by Aspose.Cells as .html and .mht files.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-5.go" >}} 

## **How to Save Excel File to OpenOffice (ODS, SXC, FODS, OTS)**
We can save the files as OpenOffice formats: ODS, SXC, FODS, OTS, etc.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-6.go" >}}
## **How to Save Excel File to JSON or XML**

JSON (JavaScript Object Notation) is an open standard file format for sharing data that uses human‑readable text to store and transmit data. JSON files are stored with the `.json` extension. JSON requires less formatting and is a good alternative to XML. JSON is derived from JavaScript but is a language‑independent data format. The generation and parsing of JSON is supported by many modern programming languages. `application/json` is the media type used for JSON.

Aspose.Cells supports saving files to JSON or XML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-7.go" >}}

## **Advanced topics**
- [Adjust workbook compression level](/cells/cpp/adjust-workbook-compression-level/)
- [Save Workbook to Strict Open XML Spreadsheet Format](/cells/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Saving File to Response Object](/cells/cpp/saving-file-to-response-object/)