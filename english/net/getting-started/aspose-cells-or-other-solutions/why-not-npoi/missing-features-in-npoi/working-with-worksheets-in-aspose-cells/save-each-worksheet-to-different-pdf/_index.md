---
title: Save Each Worksheet to Different PDF
type: docs
weight: 10
url: /net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - Save Each Worksheet to Different PDF**
Aspose.Cells supports converting XLS files (that contain images, charts etc.) to PDF documents. Aspose.Cells for .NET can work independently to convert a spreadsheet to Pdf document and you do not need to use Aspose.Pdf for .NET for the conversion any longer. The conversion does not require to create / use any temporary file(s) too as the whole process can be done in the memory.

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **Download Running Code**
Download **Save Each Worksheet to Different PDF** form any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

For more details, visit [Save Each Worksheet to a Different PDF File](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}