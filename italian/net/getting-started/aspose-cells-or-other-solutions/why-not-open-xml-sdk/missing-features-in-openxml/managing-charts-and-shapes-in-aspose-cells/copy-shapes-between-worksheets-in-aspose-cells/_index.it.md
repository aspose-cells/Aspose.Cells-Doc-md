---
title: Copia forme tra fogli di lavoro in Aspose.Cells
type: docs
weight: 30
url: /it/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

A volte, è necessario copiare elementi su un foglio di lavoro, ad esempio immagini, grafici e altri oggetti di disegno, tra fogli di lavoro. Aspose.Cells supporta questa funzione. Grafici, immagini e altri oggetti possono essere copiati con la massima precisione.

Questo articolo fornisce informazioni dettagliate su come copiare le forme tra i fogli di lavoro. Per illustrare, crea un'applicazione console in Visual Studio.Net, copia immagini, grafici e altri oggetti di disegno tra fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}} 

Di seguito è riportato il codice per copiare un grafico da un foglio di lavoro a un altro

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**Nota:** Per maggiori dettagli sulla copia di più forme è necessario visitare[qui](/cells/it/net/copy-shapes-between-worksheets/)
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Scarica l'esempio di esecuzione**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
