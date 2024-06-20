---
title: Salva ciascun foglio di lavoro in un PDF diverso
type: docs
weight: 10
url: /it/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - Salva ciascun foglio di lavoro in un PDF diverso**
Aspose.Cells supporta la conversione di file XLS (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for .NET può lavorare autonomamente per convertire un foglio di calcolo in un documento Pdf e non è più necessario utilizzare Aspose.Pdf for .NET per la conversione. La conversione non richiede di creare/utilizzare alcun file temporaneo in quanto l'intero processo può essere eseguito in memoria.

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
## **Scarica il codice in esecuzione**
Scarica **Salva ciascun foglio di lavoro in un PDF diverso** da uno dei siti di codice sociale qui sotto:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Salva ogni foglio di lavoro in un file PDF diverso](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
