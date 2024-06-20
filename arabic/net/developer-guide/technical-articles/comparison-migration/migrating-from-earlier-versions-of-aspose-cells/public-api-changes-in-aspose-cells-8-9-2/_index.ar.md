---
title: تغييرات في واجهة برمجة التطبيقات العامة في Aspose.Cells 8.9.2
type: docs
weight: 320
url: /ar/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.9.1 إلى 8.9.2 التي قد تكون مهمة لمطوري الوحدات/التطبيقات. يشمل ليس فقط الطرق العامة الجديدة والمحدثة والأصناف المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصف لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

يرجى أيضًا التحقق من [التغييرات العامة في واجهة برمجة التطبيقات المقدمة في Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة فئة TextOptions وخاصية FontSettings.TextOptions**
Aspose.Cells for .NET قد عرضت فئة TextOptions مع خاصية FontSettings.TextOptions من أجل التحكم في مظهر الأجزاء النصية للشكل.

فيما يلي سيناريو استخدام بسيط لخاصية FontSettings.TextOptions.

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

{{< /highlight >}}


### **تمت إضافة خصائص TextOptions.Fill، Outline و Shadow**
Aspose.Cells for .NET 8.9.2 قد عرضت خصائص TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow التي تسمح بالتحكم في جوانب محتويات النصوص للشكل، مثل التعبئة، الظل & التفصيل على التوالي.

فيما يلي سيناريو استخدام بسيط للخصائص المذكورة.

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Set text for TextBox

shape.Text = "Aspose";

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

// Set shadow 

textOptions.Shadow.PresetType = PresetShadowType.Below;

// Set fill color

textOptions.Fill.FillType = FillType.Solid;

textOptions.Fill.SolidFill.Color = Color.Red;

// Set outline color

textOptions.Outline.SetOneColorGradient(Color.Blue, 0.3, GradientStyleType.Horizontal, 2);

{{< /highlight >}}


### **تمت إضافة خاصية Shape.Line**
Aspose.Cells for .NET قد عرضت ممتلك Shape.Line الذي يعيد نسخة من LineFormat من أجل التحكم في مظهر مخططات الشكل.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Line.

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access LineFormat of Shape

var line = shape.Line;

// Set weight of line

line.Weight = 1;

{{< /highlight >}}


### **تمت إضافة خاصية Shape.Fill**
بواسطة الاصدار Aspose.Cells for .NET 8.9.2 تم عرض خاصية Shape.Fill التي تعيد مثيلًا لـ FillFormat للتحكم في جوانب مختلفة لمنطقة الشكل.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Fill.

**C#**

{{< highlight csharp >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access FillFormat of Shape

var fill = shape.Fill;

// Set color for fill

fill.SetOneColorGradient(Color.Red, 0.1, GradientStyleType.Horizontal, 2);

{{< /highlight >}}
## **واجهات برمجة التطبيق القديمة**
### **فئة ShapeFont الغير مستخدمة**
الرجاء استخدام فئة TextOptions بدلاً من ذلك.
### **فئة ShapeFormat الغير مستخدمة**
الرجاء استخدام ملكيات Shape.Fill وShape.Line مباشرة.
### **خاصية Format للشكل غير مستخدمة**
الرجاء استخدام ملكيات Shape.Fill وShape.Line مباشرة.
### **خاصية LineFormat للشكل غير مستخدمة**
الرجاء استخدام ملكية Shape.Line بدلاً من ذلك.
### **خاصية FillFormat للشكل غير مستخدمة**
الرجاء استخدام ملكية Shape.Fill بدلاً من ذلك.
### **خاصية ShapeFont لـ FontSetting غير مستخدمة**
الرجاء استخدام ملكية TextOptions لـ FontSetting بدلاً من ذلك.
