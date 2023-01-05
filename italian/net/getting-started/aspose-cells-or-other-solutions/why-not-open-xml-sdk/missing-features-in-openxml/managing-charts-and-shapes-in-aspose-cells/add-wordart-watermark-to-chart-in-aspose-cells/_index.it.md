---
title: Aggiungi filigrana WordArt al grafico in Aspose.Cells
type: docs
weight: 10
url: /it/net/add-wordart-watermark-to-chart-in-aspose-cells/
---
{{% alert color="primary" %}} 

Puoi utilizzare WordArt per aggiungere effetti di testo speciali ai fogli di calcolo. Ad esempio, allungare un titolo, decorare il testo, adattare il testo a una forma preimpostata o applicare il testo interessato all'area del tracciato di un grafico come filigrana. La WordArt diventa un oggetto che puoi spostare o posizionare nei tuoi fogli di calcolo per aggiungere decorazioni.

{{% /alert %}} 

Nell'esempio seguente viene illustrato come aggiungere una forma WordArt come filigrana per l'area del tracciato di un grafico esistente. L'esempio utilizza un file Excel modello che contiene già il grafico.

**Il file di input** 

![cose da fare:immagine_alt_testo](picture1.png)

**Il file di output**

![cose da fare:immagine_alt_testo](picture2.png)

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Chart.xlsx";

//Open the existing excel file.

Workbook workbook = new Workbook(FileName);

//Get the chart in the first worksheet.

Aspose.Cells.Charts.Chart chart = workbook.Worksheets[0].Charts[0];

//Add a WordArt watermark (shape) to the chart's plot area.

Aspose.Cells.Drawing.Shape wordart = chart.Shapes.AddTextEffectInChart(MsoPresetTextEffect.TextEffect2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

Aspose.Cells.Drawing.MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the transparency.

wordArtFormat.Transparency = 0.9;

//Get the line format and make it invisible.

Aspose.Cells.Drawing.MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the excel file.

workbook.Save(FileName);

{{< /highlight >}}

## **Scarica il codice di esempio**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Scarica l'esempio di esecuzione**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
