---
title: Copia delle forme tra fogli di lavoro in Aspose.Cells
type: docs
weight: 30
url: /it/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

A volte è necessario copiare elementi in un foglio di lavoro, ad esempio immagini, grafici e altri oggetti disegnati, tra fogli di lavoro. Aspose.Cells supporta questa funzionalità. Grafici, immagini e altri oggetti possono essere copiati con il massimo grado di precisione.

Questo articolo fornisce una comprensione dettagliata su come copiare forme tra fogli di lavoro. Per illustrare, crea un'applicazione console in Visual Studio.Net, copia immagini, grafici e altri oggetti disegnati tra fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}} 

Di seguito è riportato il codice per copiare un grafico da un foglio di lavoro a un altro

**C#**

{{< highlight csharp >}}

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

**Nota:** Per ulteriori dettagli su come copiare più forme è necessario visitare [qui](/cells/it/net/copy-shapes-between-worksheets/)
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Scarica Esempio in Esecuzione**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
