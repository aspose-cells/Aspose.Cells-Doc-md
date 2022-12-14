---
title: 使用 Aspose.Cells 将艺术字水印添加到工作表
type: docs
weight: 10
url: /zh/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---
## **Aspose.Cells - 向工作表添加艺术字水印**
使用艺术字为电子表格添加特殊文本效果。例如，在文件顶部拉伸标题、装饰文本并使文本适合预设形状，或将文本作为背景水印应用于 Excel 工作表。艺术字成为一个对象，您可以在电子表格中移动或定位以添加装饰。

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[将艺术字水印添加到工作表](/cells/zh/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
