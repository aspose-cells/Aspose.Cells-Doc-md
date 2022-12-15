---
title: عام API التغييرات في Aspose.Cells 8.9.2
type: docs
weight: 330
url: /ar/java/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.9.1 إلى 8.9.2 والتي قد تهم مطوري الوحدات / التطبيقات. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

 يرجى أيضًا التحقق من ملف[API عام التغييرات التي أدخلت في Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية TextOptions Class & FontSettings.TextOptions**
كشف Aspose.Cells for Java فئة TextOptions مع خاصية FontSettings.TextOptions للتحكم في مظهر الأجزاء النصية للشكل.

فيما يلي سيناريو استخدام بسيط لخاصية FontSettings.TextOptions.

**Java**

{{< highlight "csharp" >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Add text to Shape

shape.setText("Aspose");

//Access TextOptions of Shape

TextOptions textOptions =  ((FontSetting)shape.getCharacters().get(0)).getTextOptions();

{{< /highlight >}}
### **تمت إضافة TextOptions.Fill، Outline & Shadow Properties**
 كشف Aspose.Cells for Java 8.9.2 خيارات Text.Fill ، TextOptions ، Outline & TextOptions ، خصائص الظل التي تسمح بالتحكم في جوانب المحتويات النصية للشكل ، مثل التعبئة والظل والمخطط التفصيلي على التوالي.

فيما يلي سيناريو الاستخدام البسيط للخصائص المذكورة أعلاه.

**Java**

{{< highlight "csharp" >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Add text to Shape

shape.setText("Aspose");

//Access TextOptions of Shape

TextOptions textOptions =  ((FontSetting)shape.getCharacters().get(0)).getTextOptions();

//Set shadow 

textOptions.getShadow().setPresetType(PresetShadowType.BELOW);

//Set fill color

textOptions.getFill().setFillType(FillType.SOLID);

textOptions.getFill().getSolidFill().setColor(Color.getRed());

//Set outline color

textOptions.getOutline().setOneColorGradient(Color.getBlue(), 0.3, GradientStyleType.HORIZONTAL, 2);

{{< /highlight >}}
### **تمت إضافة خاصية Shape.Line**
كشف Aspose.Cells for Java خاصية Shape.Line التي ترجع مثيل LineFormat للتحكم في مظهر الخطوط الخارجية للشكل.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Line.

**Java**

{{< highlight "csharp" >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Access LineFormat of Shape

LineFormat line = shape.getLine();

//Set weight of line

line.setWeight(4);

{{< /highlight >}}
### **تمت إضافة خاصية ملء الشكل**
كشف Aspose.Cells for Java 8.9.2 خاصية Shape.Fill التي تُرجع مثيلاً من FillFormat للتحكم في الجوانب المختلفة لمساحة الشكل.

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.Fill.

**Java**

{{< highlight "csharp" >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Access FillFormat of Shape

FillFormat fill = shape.getFill();

//Set color for fill

fill.setFillType(FillType.SOLID);

fill.getSolidFill().setColor(Color.getBlue());

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
