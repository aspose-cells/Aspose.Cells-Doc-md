---
title: إضافة علامة مائية WordArt إلى ورقة العمل في Aspose.Cells
type: docs
weight: 20
url: /ar/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

استخدام كلمة الفن لإضافة تأثيرات نص خاصة إلى جداول البيانات، على سبيل المثال، تمدد عنوان عبر الجزء العلوي من الملف، زينة النص، وجعل النص يتناسب مع شكل محدد مسبقًا، أو تطبيق النص إلى ورقة Excel كعلامة مائية خلفية. تصبح كلمة الفن كائنًا يمكنك نقله أو تحديد موقعه في جداول البيانات لإضافة زخرفة.

{{% /alert %}}

المثال التالي يوضح كيفية إضافة شكل WordArt لتعيين علامة مائية في الخلفية لورقة العمل.

بعد تشغيل الكود، يحتوي ملف الإخراج على علامة مائية WordArt حمراء شاحبة.

ملف الإخراج 

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

## **تحميل رمز عينة**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **تنزيل مثال التشغيل**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
