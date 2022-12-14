---
title: Добавить водяной знак WordArt на рабочий лист в Aspose.Cells
type: docs
weight: 20
url: /ru/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

Используйте WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растяните заголовок в верхней части файла, украсьте текст и придайте ему заданную форму или нанесите текст на лист Excel в качестве фонового водяного знака. WordArt становится объектом, который можно перемещать или размещать в электронных таблицах для украшения.

{{% /alert %}}

В следующем примере показано, как добавить фигуру WordArt, чтобы установить фоновый водяной знак для рабочего листа.

После запуска кода выходной файл содержит бледно-красный водяной знак WordArt.

**Выходной файл** 

![дело:изображение_альтернативный_текст](picture1.png)

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Worksheet.xlsx";

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.Worksheets[0];

//Add Watermark

Aspose.Cells.Drawing.Shape wordart = sheet.Shapes.AddTextEffect(MsoPresetTextEffect.TextEffect1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Get the fill format of the word art

MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the color

wordArtFormat.ForeColor = System.Drawing.Color.Red;

//Set the transparency

wordArtFormat.Transparency = 0.9;

//Make the line invisible

MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the file

workbook.Save(FileName);

{{< /highlight >}}

## **Скачать пример кода**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **Скачать пример запуска**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
