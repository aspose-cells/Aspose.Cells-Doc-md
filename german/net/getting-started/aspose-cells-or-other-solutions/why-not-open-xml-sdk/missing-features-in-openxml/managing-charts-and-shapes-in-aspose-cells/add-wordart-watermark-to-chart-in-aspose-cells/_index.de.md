---
title: WordArt Wasserzeichen zu Diagramm in Aspose.Cells hinzufügen
type: docs
weight: 10
url: /de/net/add-wordart-watermark-to-chart-in-aspose-cells/
---

{{% alert color="primary" %}} 

Sie können WordArt verwenden, um spezielle Texteffekte in Tabellenkalkulationen hinzuzufügen. Zum Beispiel, einen Titel strecken, Text dekorieren, Text an eine voreingestellte Form anpassen oder den betroffenen Text als Wasserzeichen auf den Diagrammbereich anwenden. Das WordArt wird zu einem Objekt, das Sie in Ihren Tabellenkalkulationen verschieben oder positionieren können, um Dekorationen hinzuzufügen.

{{% /alert %}} 

Das folgende Beispiel zeigt, wie Sie eine WordArt-Form als Wasserzeichen für den vorhandenen Diagrammbereich hinzufügen. Das Beispiel verwendet eine Vorlagen-Excel-Datei, die bereits das Diagramm enthält.

**Die Eingabedatei** 

![todo:image_alt_text](picture1.png)

**Die Ausgabedatei**

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

## **Beispielcode herunterladen**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Laufendes Beispiel herunterladen**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
