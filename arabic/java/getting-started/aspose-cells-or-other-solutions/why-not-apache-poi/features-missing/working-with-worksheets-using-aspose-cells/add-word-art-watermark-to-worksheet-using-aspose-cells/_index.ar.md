---
title: أضف علامة مائية Word Art إلى ورقة العمل باستخدام Aspose.Cells
type: docs
weight: 10
url: /ar/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---
## **Aspose.Cells - إضافة علامة مائية Word Art إلى ورقة العمل**
استخدم WordArt لإضافة تأثيرات نصية خاصة إلى جداول البيانات. على سبيل المثال ، قم بتمديد عنوان عبر الجزء العلوي من الملف ، وقم بتزيين النص ، وجعل النص يلائم شكلًا محددًا مسبقًا ، أو قم بتطبيق نص على ورقة Excel كعلامة مائية للخلفية. يصبح WordArt عنصرًا يمكنك نقله أو وضعه في جداول البيانات لإضافة زخرفة.

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[أضف علامة WordArt المائية إلى ورقة العمل](/cells/ar/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
