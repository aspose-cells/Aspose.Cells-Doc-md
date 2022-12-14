---
title: Salva ogni foglio di lavoro in un PDF diverso in xlsx4j
type: docs
weight: 50
url: /it/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---
## **Aspose.Cells - Salva ogni foglio di lavoro in un PDF diverso**
Aspose.Cells supporta la conversione di file XLS (che contengono immagini, grafici ecc.) in documenti PDF. Aspose.Cells for Java può funzionare in modo indipendente per convertire un foglio di calcolo in un documento Pdf e non è più necessario utilizzare Aspose.Pdf for Java per la conversione. La conversione non richiede di creare/utilizzare alcun file temporaneo, poiché l'intero processo può essere eseguito nella memoria.

**Java**

{{< highlight "java" >}}

//Ottieni il percorso del file Excel

String filePath = dataDir + "workbook.xlsx";

// Crea un'istanza di una nuova cartella di lavoro e apri Excel

//File dalla sua posizione

Cartella di lavoro cartella di lavoro = nuova cartella di lavoro(filePath);

//Ottieni il conteggio dei fogli di lavoro nella cartella di lavoro

int sheetCount = workbook.getWorksheets().getCount();

//Rendi tutti i fogli invisibili tranne il primo foglio di lavoro

 per (int i = 1; i< workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Salva ogni foglio di lavoro in un file PDF diverso](/cells/it/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
