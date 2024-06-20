---
title: قفل الرسم البياني WordArt في Aspose.Cells
type: docs
weight: 40
url: /ar/net/locking-wordart-watermark-in-aspose-cells/
---

{{% alert color="primary" %}} 

تسمح واجهات برمجة التطبيقات في Aspose.Cells باضافة علامات مائية WordArt على ورقة العمل بحيث يصبح WordArt كائن يمكن نقله وتحديده على ورقة العمل. كما يمكن قفل كائن WordArt لأي تفاعل مثل التحرير والحركة والتحديد. يشرح هذا المقال استخدام طريقة Shape.SetLockedProperty لقفل بعض جوانب العلامة المائية.

{{% /alert %}} 

تسمح واجهات برمجة التطبيقات في Aspose.Cells بقفل بعض جوانب العلامة المائية بحيث يمكن تقييدها أو منع التفاعل بشكل كامل. يظهر قطع الشيفة التالية استخدام Aspose.Cells for .NET لقفل التحديد والحركة والتحرير وتغيير مقاس العلامة المائية بإنشاء جدول بيانات من البداية.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Locking WordArt Watermark.xlsx";

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.Worksheets[0];

//Add Watermark

Aspose.Cells.Drawing.Shape wordart = sheet.Shapes.AddTextEffect(MsoPresetTextEffect.TextEffect1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Lock Shape Aspects

wordart.IsLocked = true;

wordart.SetLockedProperty(ShapeLockType.Selection, true);

wordart.SetLockedProperty(ShapeLockType.ShapeType, true);

wordart.SetLockedProperty(ShapeLockType.Move, true);

wordart.SetLockedProperty(ShapeLockType.Resize, true);

wordart.SetLockedProperty(ShapeLockType.Text, true);

//Get the fill format of the word art

MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the color

wordArtFormat.ForeColor = Color.Red;

//Set the transparency

wordArtFormat.Transparency = 0.9;

//Make the line invisible

MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the file

workbook.Save(FileName);

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **تنزيل مثال التشغيل**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
