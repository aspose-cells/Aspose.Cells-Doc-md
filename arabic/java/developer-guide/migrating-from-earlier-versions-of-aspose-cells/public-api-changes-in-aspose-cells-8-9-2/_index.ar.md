---
title: تغييرات في واجهة برمجة التطبيقات العامة في Aspose.Cells 8.9.2
type: docs
weight: 330
url: /ar/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.9.1 إلى 8.9.2 التي قد تكون مهمة لمطوري الوحدات/التطبيقات. يشمل ليس فقط الطرق العامة الجديدة والمحدثة والأصناف المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصف لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}} 

يرجى أيضًا التحقق من [التغييرات العامة في واجهة برمجة التطبيقات التي تم إدخالها في Aspose.Cells for Java 8.9.1](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة فئة TextOptions وخاصية FontSettings.TextOptions**
Aspose.Cells for Java قد قام بتعريض فئة TextOptions مع خاصية FontSettings.TextOptions للتحكم في مظهر الأجزاء النصية لشكل ما.

فيما يلي سيناريو استخدام بسيط لخاصية FontSettings.TextOptions.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة خصائص TextOptions.Fill، Outline و Shadow**
Aspose.Cells for Java 8.9.2 قد قام بتعريض خصائص TextOptions.Fill، TextOptions.Outline و TextOptions.Shadow والتي تسمح بالتحكم في جوانب المحتوى النصي للشكل، مثل التعبير، الظل، والإطار على التوالي. 

فيما يلي سيناريو استخدام بسيط للخصائص المذكورة.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java قد قام بتعريض خاصية Shape.Line التي تُرجع مثيلًا من LineFormat من أجل التحكم في مظهر مخططات الشكل.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Line.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة خاصية Shape.Fill**
Aspose.Cells for Java 8.9.2 قد قام بتعريض خاصية Shape.Fill التي تُرجع مثيلًا من FillFormat من أجل التحكم في جوانب مختلفة لمساحة الشكل.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Fill.

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
