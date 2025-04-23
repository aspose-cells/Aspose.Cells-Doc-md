---
title: Imposta il colore della scheda del foglio di lavoro in Aspose.Cells
type: docs
weight: 20
url: /it/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Imposta il colore della scheda del foglio di lavoro**
Aspose.Cells consente di cambiare il colore delle singole schede del foglio di lavoro per renderle evidenti rispetto alle altre. Ad esempio, è possibile rendere Rosso le Spese, Verde le Vendite, Blu i Beni, ecc.
### **Impostare il Colore della Scheda del Foglio di Lavoro con Microsoft Excel**
1. Fare clic con il pulsante destro del mouse su una scheda nell'insieme di schede nella parte inferiore della scheda corrente.
1. Seleziona il **colore della scheda**.
1. Seleziona un colore dalla tavolozza.
1. Fai clic su **OK**.

**C#**

{{< highlight cs >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Imposta il colore della scheda del foglio di lavoro** da uno dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Imposta il colore della scheda del foglio di lavoro](/cells/it/net/set-worksheet-tab-color/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
