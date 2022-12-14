---
title: قفل علامة WordArt المائية في Aspose.Cells
type: docs
weight: 40
url: /ar/net/locking-wordart-watermark-in-aspose-cells/
---
{{% alert color="primary" %}} 

تسمح واجهات برمجة التطبيقات Aspose.Cells بإضافة علامات مائية لـ WordArt على ورقة العمل بطريقة تجعل WordArt كائنًا يمكنك نقله ووضعه في ورقة العمل. من الممكن أيضًا قفل عنصر WordArt لأي تفاعل مثل التحرير والحركة والاختيار. تشرح هذه المقالة استخدام طريقة Shape.SetLockedProperty لقفل بعض جوانب العلامة المائية.

{{% /alert %}} 

تسمح واجهات برمجة التطبيقات Aspose.Cells بقفل جوانب معينة من العلامة المائية بحيث يمكن تقييد تفاعل المستخدم أو حظره تمامًا. يوضح مقتطف الشفرة التالي استخدام Aspose.Cells for .NET API لقفل التحديد والحركة والتحرير وإعادة تغيير حجم العلامة المائية عن طريق إنشاء جدول بيانات من البداية.

**C#**

{{< highlight "csharp" >}}

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
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
## **تحميل مثال الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
