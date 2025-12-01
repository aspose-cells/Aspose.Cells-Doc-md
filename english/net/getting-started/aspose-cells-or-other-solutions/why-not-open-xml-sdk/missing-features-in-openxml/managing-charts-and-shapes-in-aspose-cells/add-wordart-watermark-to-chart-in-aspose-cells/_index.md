---
title: Add WordArt Watermark to Chart in Aspose.Cells
type: docs
weight: 10
url: /net/add-wordart-watermark-to-chart-in-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

You can use WordArt to add special text effects to spreadsheets. For example, stretch a title, decorate text, make text fit a preset shape, or apply the affected text to a chart’s plot area as a watermark. The WordArt becomes an object that you can move or position in your spreadsheets to add decoration.

{{% /alert %}} 

The following example shows how to add a WordArt shape as a watermark for an existing chart’s plot area. The example uses a template Excel file that already contains the chart.

**The input file** 

![todo:image_alt_text](picture1.png)

**The output file**

![todo:image_alt_text](picture2.png)

**C#**

{{< highlight csharp >}}

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

## **Download Sample Code**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Download Running Example**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
