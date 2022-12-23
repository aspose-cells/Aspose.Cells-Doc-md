---
title: Imposta il colore della scheda del foglio di lavoro in Aspose.Cells
type: docs
weight: 20
url: /it/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Imposta il colore della scheda del foglio di lavoro**
Aspose.Cells ti consente di cambiare il colore delle singole schede del foglio di lavoro per renderle prominenti rispetto al resto. Ad esempio, puoi impostare Spese in rosso, Vendite in verde, Attività in blu, ecc.
### **Impostazione del colore della scheda del foglio di lavoro con Microsoft Excel**
1. Fare clic con il pulsante destro del mouse su una scheda nella scheda nella parte inferiore del foglio di lavoro corrente.
1. Selezionare**Colore scheda**.
1. Seleziona un colore dalla tavolozza.
1. Clic**OK**.

**C#**

{{< highlight "cs" >}}

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
 Scaricamento**Imposta il colore della scheda del foglio di lavoro** formare uno dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Imposta il colore della scheda del foglio di lavoro](/cells/it/net/set-worksheet-tab-color/).

{{% /alert %}}
