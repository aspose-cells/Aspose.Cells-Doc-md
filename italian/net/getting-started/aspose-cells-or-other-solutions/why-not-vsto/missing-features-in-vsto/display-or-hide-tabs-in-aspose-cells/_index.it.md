---
title: Mostra o Nasconde Schede in Aspose.Cells
type: docs
weight: 80
url: /it/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

Se osservi attentamente in fondo a un file di Microsoft Excel, vedrai una serie di controlli. Questi includono:

- Schede del foglio.
- Pulsanti di scorrimento delle schede.

Le schede del foglio rappresentano i fogli di lavoro nel file di Excel. Fai clic su qualsiasi scheda per passare a quel foglio di lavoro. Più ci sono fogli di lavoro nel libro, più schede del foglio ci sono. Se il file Excel ha un buon numero di fogli di lavoro, hai bisogno di pulsanti per navigare attraverso di essi. Quindi, Microsoft Excel fornisce pulsanti di scorrimento delle schede per scorrere attraverso le schede dei fogli.

**Schede del foglio e pulsanti di scorrimento delle schede** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità delle schede del foglio e dei pulsanti di scorrimento delle schede nei file di Excel. 

{{% /alert %}} 

Di seguito è riportato un esempio completo che apre un file Excel (book1.xls), nasconde le sue schede e salva il file modificato come output.xls.

Puoi vedere che il file Book1.xls contiene delle schede nella figura sottostante. Dopo l'esecuzione del codice di esempio, le schede vengono nascoste, come puoi vedere dalla schermata del file output.xls sottostante.

**book1.xls: File Excel prima di qualsiasi modifica** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: File Excel dopo la modifica** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Controllare la larghezza della barra delle schede**
**C#**

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
