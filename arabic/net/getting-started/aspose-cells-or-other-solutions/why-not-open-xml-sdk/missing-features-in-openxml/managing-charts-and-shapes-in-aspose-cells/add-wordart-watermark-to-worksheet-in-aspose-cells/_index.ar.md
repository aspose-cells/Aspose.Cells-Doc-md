---
title: أضف علامة WordArt المائية إلى ورقة العمل في Aspose.Cells
type: docs
weight: 20
url: /ar/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

استخدم WordArt لإضافة تأثيرات نصية خاصة إلى جداول البيانات. على سبيل المثال ، قم بتمديد عنوان عبر الجزء العلوي من الملف ، وقم بتزيين النص ، وجعل النص يتناسب مع شكل معين مسبقًا ، أو قم بتطبيق نص على ورقة Excel كعلامة مائية في الخلفية. يصبح WordArt عنصرًا يمكنك نقله أو وضعه في جداول البيانات لإضافة زخرفة.

{{% /alert %}}

يوضح المثال التالي كيفية إضافة شكل WordArt لتعيين علامة مائية في الخلفية لورقة عمل.

بعد تشغيل الكود ، يحتوي ملف الإخراج على علامة مائية WordArt حمراء شاحبة.

**ملف الإخراج** 

![ما يجب القيام به: image_بديل_نص](picture1.png)

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

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **تحميل مثال الجري**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
