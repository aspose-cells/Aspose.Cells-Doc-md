---
title: Saving File to Response Object
type: docs
weight: 50
url: /net/saving-file-to-response-object/
---

{{% alert color="primary" %}} 

Aspose.Cells makes it possible to manipulate files. This article explains the various ways in which files can be saved to a response object.

{{% /alert %}} 
## **Saving File to Response Object**
It is also possible to generate a file dynamically and send it directly to a client browser. In order to do so, use a special overloaded version of the [Save](https://apireference.aspose.com/net/cells/aspose.cells.workbook/save/methods/5) method that accepts the following parameters:

- ASP.NET [HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8) object.
- File name.
- [ContentDisposition](https://apireference.aspose.com/net/cells/aspose.cells/contentdisposition), the content-disposition type of the output file.
- [SaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/saveoptions), the file format type

The [ContentDisposition](https://apireference.aspose.com/net/cells/aspose.cells/contentdisposition) enumeration determines whether the file being sent to the browser provides the option to open by itself directly in the browser or in an application associated with .xls/.xlsx or another extension.

The enumeration contains the following pre-defined save types:

|**Type**|**Description**|
| :- | :- |
|Attachment|Sends the spreadsheet to the browser and opens in an application as an attachment associated with .xls/.xlsx or other extensions|
|Inline|Sends the document to the browser and presents an option to save the spreadsheet to disk or open inside the browser|
### **XLS Files**


{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}
### **XLSX Files**


{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}
### **PDF Files**


{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}



