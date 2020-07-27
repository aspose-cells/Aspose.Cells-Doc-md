+++
title = "Saving File to Response Object" 
description = "" 
weight = 12064 
+++

Aspose.Cells for .NET : Saving File to Response Object  

# Aspose.Cells for .NET : Saving File to Response Object



Aspose.Cells makes it possible to manipulate files. This article explains the various ways in which files can be saved to a response object.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Saving File to Response Object](#SavingFiletoResponseObject-SavingFiletoResponseObject)
    *   1.1 [XLS Files](#SavingFiletoResponseObject-XLSFiles)
    *   1.2 [XLSX Files](#SavingFiletoResponseObject-XLSXFiles)
    *   1.3 [PDF Files](#SavingFiletoResponseObject-PDFFiles)
{{< /panel >}}
 

## Saving File to Response Object

It is also possible to generate a file dynamically and send it directly to a client browser. In order to do so, use a special overloaded version of the [Save](https://apireference.aspose.com/net/cells/aspose.cells.workbook/save/methods/5) method that accepts the following parameters:

*   ASP.NET [HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8) object.
*   File name.
*   [ContentDisposition](https://apireference.aspose.com/net/cells/aspose.cells/contentdisposition), the content-disposition type of the output file.
*   [SaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/saveoptions), the file format type

The [ContentDisposition](https://apireference.aspose.com/net/cells/aspose.cells/contentdisposition) enumeration determines whether the file being sent to the browser provides the option to open by itself directly in the browser or in an application associated with .xls/.xlsx or another extension.

The enumeration contains the following pre-defined save types:

{{< table style="table-striped" >}}
|Type|Description|
|:----|:----|
|Attachment|Sends the spreadsheet to the browser and opens in an application as an attachment associated with .xls/.xlsx or other extensions|
|Inline|Sends the document to the browser and presents an option to save the spreadsheet to disk or open inside the browser|
{{< /table >}}

### XLS Files

### XLSX Files

### PDF Files

  
  

