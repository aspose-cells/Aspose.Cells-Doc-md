---
title: Lägg till WordArt Watermark i diagrammet i Aspose.Cells
type: docs
weight: 10
url: /sv/net/add-wordart-watermark-to-chart-in-aspose-cells/
---
{{% alert color="primary" %}} 

Du kan använda WordArt för att lägga till speciella texteffekter i kalkylblad. Du kan till exempel sträcka ut en titel, dekorera text, få text att passa en förinställd form eller tillämpa den berörda texten på ett diagrams plotområde som en vattenstämpel. WordArt blir ett objekt som du kan flytta eller placera i dina kalkylblad för att lägga till dekoration.

{{% /alert %}} 

Följande exempel visar hur du lägger till en WordArt-form som en vattenstämpel för ett befintligt diagrams plotområde. I exemplet används en Excel-mall som redan innehåller diagrammet.

**Inmatningsfilen** 

![todo:image_alt_text](picture1.png)

**Utdatafilen**

![todo:image_alt_text](picture2.png)

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

## **Ladda ner exempelkod**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Ladda ner körningsexempel**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
