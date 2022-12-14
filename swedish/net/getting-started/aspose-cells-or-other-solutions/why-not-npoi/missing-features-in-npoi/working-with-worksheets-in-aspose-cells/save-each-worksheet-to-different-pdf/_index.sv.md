---
title: Spara varje arbetsblad till olika PDF-filer
type: docs
weight: 10
url: /sv/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - Spara varje kalkylblad till en annan PDF**
Aspose.Cells stöder konvertering av XLS-filer (som innehåller bilder, diagram etc.) till PDF-dokument. Aspose.Cells för .NET kan arbeta oberoende för att konvertera ett kalkylblad till Pdf-dokument och du behöver inte längre använda Aspose.Pdf för .NET för konverteringen. Konverteringen kräver inte att man skapar/använder någon temporär fil(er) också eftersom hela processen kan göras i minnet.

**C#**

{{< highlight "cs" >}}

 //Instantiera en ny arbetsbok och öppna Excel

//Fil från sin plats

Arbetsbok arbetsbok = ny arbetsbok("../../data/test.xlsx");

//Hämta antalet arbetsblad i arbetsboken

int sheetCount = arbetsbok.Worksheets.Count;

//Gör alla ark osynliga utom det första kalkylbladet

 för (int i = 1; i< workbook.Worksheets.Count; i++)

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
## **Ladda ner Running Code**
 Ladda ner**Spara varje arbetsblad till olika PDF-filer** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Spara varje kalkylblad till en annan PDF-fil](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
