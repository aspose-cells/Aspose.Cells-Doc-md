---
title: عام API التغييرات في Aspose.Cells 8.9.2
type: docs
weight: 320
url: /ar/net/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.9.1 إلى 8.9.2 والتي قد تهم مطوري الوحدات / التطبيقات. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 يرجى أيضًا التحقق من ملف[API عام التغييرات التي أدخلت في Aspose.Cells for .NET 8.9.1](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية TextOptions Class & FontSettings.TextOptions**
كشف Aspose.Cells for .NET فئة TextOptions مع خاصية FontSettings.TextOptions للتحكم في مظهر الأجزاء النصية للشكل.

فيما يلي سيناريو استخدام بسيط لخاصية FontSettings.TextOptions.

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

{{< /highlight >}}


### **تمت إضافة TextOptions.Fill، Outline & Shadow Properties**
كشف Aspose.Cells for .NET 8.9.2 خيارات Text.Fill ، TextOptions ، Outline & TextOptions ، خصائص الظل التي تسمح بالتحكم في جوانب المحتويات النصية للشكل ، مثل التعبئة والظل والمخطط التفصيلي على التوالي.

فيما يلي سيناريو الاستخدام البسيط للخصائص المذكورة أعلاه.

**C#**

{{< highlight "csharp" >}}

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
كشف Aspose.Cells for .NET خاصية Shape.Line التي تُرجع مثيل LineFormat للتحكم في مظهر الخطوط الخارجية للشكل.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Line.

**C#**

{{< highlight "csharp" >}}

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


### **تمت إضافة خاصية ملء الشكل**
كشف Aspose.Cells for .NET 8.9.2 خاصية Shape.Fill التي تُرجع مثيلاً من FillFormat للتحكم في الجوانب المختلفة لمساحة الشكل.

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.Fill.

**C#**

{{< highlight "csharp" >}}

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
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **فئة ShapeFont التي عفا عليها الزمن**
الرجاء استخدام فئة TextOptions بدلاً من ذلك.
### **فئة FormatFormat عفا عليها الزمن**
الرجاء استخدام خصائص Shape.Fill و Shape.Line مباشرةً.
### **شكل قديم. خاصية التنسيق**
الرجاء استخدام خصائص Shape.Fill و Shape.Line مباشرةً.
### **شكل قديم. خاصية LineFormat**
الرجاء استخدام خاصية Shape.Line بدلاً من ذلك.
### **شكل قديم. خاصية FillFormat**
الرجاء استخدام خاصية Shape.Fill بدلاً من ذلك.
### **خاصية FontSetting.ShapeFont قديمة**
الرجاء استخدام الخاصية FontSetting.TextOptions بدلاً من ذلك.
