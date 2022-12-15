---
title: Imposta il colore della scheda del foglio di lavoro in xlsx4j
type: docs
weight: 60
url: /it/java/set-worksheet-tab-color-in-xlsx4j/
---
## **Aspose.Cells - Imposta il colore della scheda del foglio di lavoro**
Aspose.Cells ti consente di cambiare il colore delle singole schede del foglio di lavoro per renderle prominenti rispetto al resto. Ad esempio, puoi impostare Spese in rosso, Vendite in verde, Attività in blu, ecc.
### **Impostazione del colore della scheda del foglio di lavoro con Microsoft Excel**
1. Fare clic con il pulsante destro del mouse su una scheda nella scheda nella parte inferiore del foglio di lavoro corrente.
1. Selezionare**Colore scheda**.
1. Seleziona un colore dalla tavolozza.
1. Clic**OK**.

**Giava**

{{< highlight "java" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Imposta il colore della scheda del foglio di lavoro](/java/set-worksheet-tab-color).

{{% /alert %}}
