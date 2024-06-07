---
title: 使用Aspose.Cells向工作表添加Word Art水印
type: docs
weight: 10
url: /zh/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---

## **Aspose.Cells - 将Word Art水印添加到工作表**
使用WordArt来向电子表格添加特殊文本效果。例如，在文件顶部拉伸标题，装饰文本，将文本适应预设形状，或将文本应用于Excel工作表作为背景水印。WordArt成为您可以在电子表格中移动或定位以添加装饰的对象。

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[向工作表添加WordArt水印] (/cells/zh/java/add-wordart-watermark-to-worksheet)

{{% /alert %}}
