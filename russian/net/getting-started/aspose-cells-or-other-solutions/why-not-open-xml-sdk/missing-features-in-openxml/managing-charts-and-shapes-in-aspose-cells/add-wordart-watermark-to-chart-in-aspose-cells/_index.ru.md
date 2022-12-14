---
title: Добавить водяной знак WordArt на диаграмму в Aspose.Cells
type: docs
weight: 10
url: /ru/net/add-wordart-watermark-to-chart-in-aspose-cells/
---
{{% alert color="primary" %}} 

Вы можете использовать WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растяните заголовок, украсьте текст, придайте тексту предустановленную форму или нанесите измененный текст на область графика диаграммы в качестве водяного знака. WordArt становится объектом, который можно перемещать или размещать в электронных таблицах для украшения.

{{% /alert %}} 

В следующем примере показано, как добавить фигуру WordArt в качестве водяного знака для области графика существующей диаграммы. В примере используется файл шаблона Excel, который уже содержит диаграмму.

**Входной файл** 

![дело:изображение_альтернативный_текст](picture1.png)

**Выходной файл**

![дело:изображение_альтернативный_текст](picture2.png)

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

## **Скачать пример кода**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Скачать пример запуска**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
