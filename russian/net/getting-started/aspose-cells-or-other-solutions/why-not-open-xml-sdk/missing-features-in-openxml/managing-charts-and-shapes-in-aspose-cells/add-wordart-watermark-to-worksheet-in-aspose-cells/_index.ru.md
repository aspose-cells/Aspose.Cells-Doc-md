---
title: Добавить водяной знак WordArt на лист в Aspose.Cells
type: docs
weight: 20
url: /ru/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

Используйте WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растяните заголовок сверху файла, украсьте текст или сделайте его соответствующим предварительно заданной форме или примените текст к листу Excel в качестве фонового водяного знака. WordArt становится объектом, который можно перемещать или позиционировать на листе, добавляя украшения.

{{% /alert %}}

Приведенный ниже пример показывает, как добавить форму WordArt, чтобы установить водяной знак на фон для листа.

После выполнения кода в выходном файле будет содержаться бледный красный водяной знак WordArt.

**Выходной файл** 

![todo:image_alt_text](picture1.png)

**C#**

{{< highlight csharp >}}

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

## **Загрузить образец кода**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **Скачать пример выполнения**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
