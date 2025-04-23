---
title: Spara varje kalkylblad i olika PDF
type: docs
weight: 10
url: /sv/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - Spara varje kalkylblad i olika PDF**
Aspose.Cells stöder konvertering av XLS-filer (som innehåller bilder, diagram etc.) till PDF-dokument. Aspose.Cells for .NET kan arbeta självständigt för att konvertera en kalkylblad till Pdf-dokument och du behöver inte längre använda Aspose.Pdf för .NET för konverteringen. Konverteringen kräver inte heller att du skapar/använder några temporära filer eftersom hela processen kan göras i minnet.

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
## **Ladda ned körbar kod**
Ladda ner **Spara varje kalkylblad i olika PDF** från någon av nedanstående sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

För mer detaljer, besök [Spara varje kalkylblad som en annan PDF-fil](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
