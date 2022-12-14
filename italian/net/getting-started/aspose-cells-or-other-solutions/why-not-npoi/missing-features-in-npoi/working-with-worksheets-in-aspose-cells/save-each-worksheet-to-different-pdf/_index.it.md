---
title: Salva ogni foglio di lavoro in un PDF diverso
type: docs
weight: 10
url: /it/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - Salva ogni foglio di lavoro in un PDF diverso**
Aspose.Cells supporta la conversione di file XLS (che contengono immagini, grafici ecc.) in documenti PDF. Aspose.Cells for .NET può funzionare in modo indipendente per convertire un foglio di calcolo in un documento Pdf e non è più necessario utilizzare Aspose.Pdf for .NET per la conversione. La conversione non richiede di creare/utilizzare alcun file temporaneo, poiché l'intero processo può essere eseguito nella memoria.

**C#**

{{< highlight "cs" >}}

 // Crea un'istanza di una nuova cartella di lavoro e apri Excel

//File dalla sua posizione

Cartella di lavoro cartella di lavoro = nuova cartella di lavoro("../../data/test.xlsx");

//Ottieni il conteggio dei fogli di lavoro nella cartella di lavoro

int sheetCount = workbook.Worksheets.Count;

//Rendi tutti i fogli invisibili tranne il primo foglio di lavoro

 per (int i = 1; i< workbook.Worksheets.Count; i++)

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
 Scarica**Salva ogni foglio di lavoro in un PDF diverso** formare uno dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Salva ogni foglio di lavoro in un file PDF diverso](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
