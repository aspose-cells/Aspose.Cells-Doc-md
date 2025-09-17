##Different Ways to Save Files
Aspose.Cells for .NET can save files to different formats. Save Files to PDF. Save Files to HTML. Save Files to DOCX. Save Files to PPTX. Save Files to JSON. Save Files to MHTML.
Aspose.Cells makes it possible to create and save files. This article explains the various ways in which files can be saved.
## **Different Ways to Save Files**
Aspose.Cells provides the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) which represents a Microsoft Excel file and provides the properties and methods necessary to work with Excel files. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class provides the [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method used to save Excel files. The [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method has many overloads that are used to save files in different ways.
The file format that the file is saved to is decided by the [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) enumeration
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
## **How to Save File to Different Formats**
To save files to a storage location, specify the file name (complete with storage path) and the desired file format (from the [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) enumeration) when calling the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) object's [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method.
## **How to Save Workbook to Pdf**
Portable Document Format (PDF) is a type of document created by Adobe back in 1990s. The purpose of this file format was to introduce a standard for representation of documents and other reference material in a format that is independent of application software, hardware as well as Operating System. The PDF file format has full capability to contain information like text, images, hyperlinks, form-fields, rich media, digital signatures, attachments, metadata, Geospatial features and 3D objects in it that can become as part of source document.
The following codes shows how to save workboook as pdf file With Aspose.Cells:
## **How to Save Workbook to Text or CSV Format**
Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.
The following code example explains how to save an entire workbook into text format. Load the source workbook which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS and so on) with any number of worksheets.
When the code is executed, it converts the data of all sheets in the workbook to the TXT format.
You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) is comma, so do not specify a separator if saving to CSV format. Please note: If you are using the evaluation version and even if the [**TxtSaveOptions.ExportAllSheets**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/exportallsheets/) property is set to true, the program will still only export one worksheet.
## **How to Save File to Text Files with Custom Separator**
Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.
## **How to Save File to a Stream**
To save files to a stream, create a *MemoryStream* or *FileStream* object and save the file to that stream object by calling the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) object's [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method. Specify the desired file format using the [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) enumeration when calling the [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) method.
## **How to Save Excel File to Html and Mht files**
Aspose.Cells can simply save an Excel file ,JSON, CSV or other files which could be loaded by Aspose.Cells as .html and .mht files.
## **How to Save Excel File to OpenOffice (ODS, SXC, FODS, OTS)**
We can saving the files as open offce format : ODS, SXC, FODS, OTS etc.
## **How to Save Excel File to JSON or XML**
JSON (JavaScript Object Notation) is an open standard file format for sharing data that uses human-readable text to store and transmit data. JSON files are stored with the .json extension. JSON requires less formatting and is a good alternative for XML. JSON is derived from JavaScript but is a language-independent data format. The generation and parsing of JSON is supported by many modern programming languages. application/json is the media type used for JSON.
Aspose.Cells supports saving files to JSON or XML.
## **Advance topics**
- [Adjust workbook compression level](https://docs.aspose.com/cells/net/adjust-workbook-compression-level/)
- [Save Workbook to Strict Open XML Spreadsheet Format](https://docs.aspose.com/cells/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Saving File to Response Object](https://docs.aspose.com/cells/net/saving-file-to-response-object/)
