---
title: Imposta il colore della scheda del foglio di lavoro in Aspose.Cells
type: docs
weight: 90
url: /it/java/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Imposta il colore della scheda del foglio di lavoro**
Aspose.Cells consente di cambiare il colore delle singole schede del foglio di lavoro per renderle evidenti rispetto alle altre. Ad esempio, è possibile rendere Rosso le Spese, Verde le Vendite, Blu i Beni, ecc.
#### **Impostare il Colore della Scheda del Foglio di Lavoro con Microsoft Excel**
1. Fare clic con il pulsante destro del mouse su una scheda nell'insieme di schede nella parte inferiore della scheda corrente.
1. Seleziona il **colore della scheda**.
1. Seleziona un colore dalla tavolozza.
1. Fai clic su **OK**.

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataPath + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Imposta il colore della scheda del foglio di lavoro](/java/set-worksheet-tab-color).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
