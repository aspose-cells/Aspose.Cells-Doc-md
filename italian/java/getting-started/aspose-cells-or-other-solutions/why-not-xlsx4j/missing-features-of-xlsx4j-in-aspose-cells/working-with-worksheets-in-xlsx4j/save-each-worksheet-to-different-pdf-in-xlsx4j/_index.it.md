---
title: Salva ciascun foglio di calcolo in file PDF separati in xlsx4j
type: docs
weight: 50
url: /it/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---

## **Aspose.Cells - Salva ciascun foglio di lavoro in un PDF diverso**
Aspose.Cells supporta la conversione dei file XLS (che contengono immagini, grafici, ecc.) in documenti PDF. Aspose.Cells for Java può lavorare in modo indipendente per convertire un foglio di calcolo in un documento Pdf e non è più necessario utilizzare Aspose.Pdf for Java per la conversione. La conversione non richiede di creare/utilizzare file temporanei in quanto l'intero processo può essere eseguito in memoria.

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Salva ogni foglio di lavoro in un file PDF separato](/cells/it/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
