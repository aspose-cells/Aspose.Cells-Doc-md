---
title: Mostra o nascondi schede in Aspose.Cells
type: docs
weight: 80
url: /it/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

Se osservi attentamente la parte inferiore di un file Excel Microsoft, vedrai una serie di controlli. Questi includono:

- Schede dei fogli.
- Pulsanti di scorrimento delle schede.

Le schede dei fogli rappresentano i fogli di lavoro nel file Excel. Fare clic su qualsiasi scheda per passare a quel foglio di lavoro. Maggiore è il numero di fogli di lavoro nella cartella di lavoro, maggiore sarà il numero di schede dei fogli. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Quindi, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere le schede del foglio.

**Schede dei fogli e pulsanti di scorrimento delle schede** 

![cose da fare:immagine_alt_testo](display-or-hide-tabs-in-aspose-cells_1.png)

Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità delle schede dei fogli e dei pulsanti di scorrimento delle schede nei file Excel.

{{% /alert %}} 

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), ne nasconde le schede e salva il file modificato come output.xls.

Puoi vedere che il file Book1.xls contiene schede nella figura seguente. Dopo che il codice di esempio è stato eseguito, le schede sono nascoste, come puoi vedere dallo screenshot del file output.xls qui sotto.

**book1.xls: file Excel prima di qualsiasi modifica** 

![cose da fare:immagine_alt_testo](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: file Excel dopo la modifica** 

![cose da fare:immagine_alt_testo](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Controllo della larghezza della barra delle linguette**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
