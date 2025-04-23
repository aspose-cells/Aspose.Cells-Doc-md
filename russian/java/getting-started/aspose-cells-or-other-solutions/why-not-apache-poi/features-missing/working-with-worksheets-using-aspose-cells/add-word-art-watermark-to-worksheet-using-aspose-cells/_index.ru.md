---
title: Добавление водяного знака WordArt на лист рабочей книги с использованием Aspose.Cells
type: docs
weight: 10
url: /ru/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---

## **Aspose.Cells - Добавление водяного знака WordArt на лист рабочей книги**
Используйте WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растягивайте заголовок вверху файла, украшайте текст и заставляйте его подгоняться под заданную форму или применяйте текст к электронной таблице Excel в качестве заднего водяного знака. WordArt становится объектом, который можно перемещать или располагать в электронных таблицах для добавления украшений.

**Java**

{{< highlight java >}}

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
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

За более подробной информацией посетите [Добавление водяного знака WordArt на лист рабочей книги](/cells/ru/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
