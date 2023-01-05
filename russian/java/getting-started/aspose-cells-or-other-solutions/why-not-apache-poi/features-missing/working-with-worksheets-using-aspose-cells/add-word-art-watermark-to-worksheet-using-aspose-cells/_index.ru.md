---
title: Добавьте водяной знак Word Art на рабочий лист, используя Aspose.Cells
type: docs
weight: 10
url: /ru/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---
## **Aspose.Cells - Добавить водяной знак Word Art на рабочий лист**
Используйте WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растяните заголовок в верхней части файла, украсьте текст и придайте ему заданную форму или нанесите текст на лист Excel в качестве фонового водяного знака. WordArt становится объектом, который можно перемещать или размещать в электронных таблицах для украшения.

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add Watermark

Shape wordart = sheet.getShapes().addTextEffect(MsoPresetTextEffect.TEXT_EFFECT_1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Get the shape's fill format

FillFormat wordArtFormat = wordart.getFill();

//Set the transparency

wordArtFormat.setTransparency(0.9);

//Make the line invisible

wordart.setHasLine(false);

//Save the file

workbook.save(dataDir + "AsposeWatermark_Out.xls");

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Добавить водяной знак WordArt на рабочий лист](/cells/ru/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
