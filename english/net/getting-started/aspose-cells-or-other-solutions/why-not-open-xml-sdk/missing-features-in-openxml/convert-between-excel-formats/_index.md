---
title: Convert between Excel formats
type: docs
weight: 20
url: /net/convert-between-excel-formats/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Converting Excel to PDF**

**PDF** files are widely used for exchanging documents between organizations, government sectors and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into **PDF** documents.
**Aspose.Cells** supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

Aspose.Cells for .NET supports conversion from spreadsheets to PDF independently of other software. Save an Excel file to PDF using the Workbook class' Save method. The Save method provides the SaveFormat.Pdf enum member that converts the native Excel files to PDF format.

**Converting** directly from spreadsheet to PDF, instead of using a third-party tool or external API, has several **advantages**:

1. Direct conversion does not require temporary files because the whole process can be done in memory.
1. No XML file is needed so large files can easily be converted.
1. The conversion speed is much faster.

**To convert files to PDF:**

1. Instantiate an object of the **Workbook** class by calling its empty constructor.
1. You may **open/load** an existing template file or skip this step if you are creating the workbook from scratch.
1. Do your desired work (input data, apply formatting, set formulas, insert pictures or other drawing objects, and so on) on the spreadsheet using Aspose.Cells' APIs.
1. When the spreadsheet code is complete, call the **Workbook class' Save method** to save the spreadsheet. The file format should be PDF so select Pdf (a pre-defined value) from the SaveFormat enumeration to generate the final PDF document.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Converting Excel to MHTML**

**MHTML** combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio and so on) into one file. They are used for emails with the .mht file extension.
Aspose.Cells supports reading and writing MHTML files.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Converting Excel to XPS**

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Download Sample Code**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
