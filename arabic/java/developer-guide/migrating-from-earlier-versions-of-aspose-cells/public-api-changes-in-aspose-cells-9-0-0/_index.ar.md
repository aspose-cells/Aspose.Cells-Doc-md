---
title: API العام التغييرات في Aspose.Cells 9.0.0
type: docs
weight: 340
url: /ar/java/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.9.2 إلى 9.0.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية Shape.TextOptions**
كشف Aspose.Cells for Java خاصية TextOptions لفئة الشكل للتحكم في مظهر الأجزاء النصية للشكل.

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.TextOptions.

**Java**

{{< highlight "csharp" >}}

 //Initialize an instance of Workbook

Workbook book = new Workbook();

//Get the default Worksheet from the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the collection

int textboxIndex = sheet.getTextBoxes().add(2, 1, 160, 200);

//Get the TextBox object

TextBox textbox = sheet.getTextBoxes().get(textboxIndex);

//Add text to the TextBox

textbox.setText("Hello Aspose!");

//Format the textual contents

textbox.getTextOptions().setColor(Color.getRed());

textbox.getTextOptions().setItalic(true);

textbox.getTextOptions().setBold(true);

{{< /highlight >}}
### **تمت إضافة خاصية ChartPoint.IsInSecondaryPlot**
كشف Aspose.Cells for Java خاصية ChartPoint.IsInSecondaryPlot التي يمكن استخدامها لاكتشاف ما إذا كانت ChartPoint موجودة في مخطط ثانوي لمخطط دائري أو شريطي.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Line.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العثور على DataPoint يكمن في قطعة الأرض الثانية](/cells/ar/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 // تحميل جدول بيانات موجود يحتوي على مخطط دائري

كتاب المصنف = مصنف جديد (dir + "PieBar.xlsx") ؛

// قم بتحميل ورقة العمل في فهرس 0

ورقة عمل = book.getWorksheets (). get (0)؛

// قم بتحميل الرسم البياني الأول من المجموعة

مخطط الرسم البياني = sheet.getCharts (). get (0)؛

// احسب المخطط قبل الوصول إلى خصائصه

chart.calculate () ،

// الوصول إلى السلسلة الأولى من الرسم البياني

سلسلة السلسلة = chart.getNSeries (). get (0)؛

// حلقة فوق مجموعة ChartPoint

 لـ (int ص = 0 ؛ ص< series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **تمت إضافة خاصية OleObject.ClassIdentifier**
كشف Aspose.Cells for Java 9.0.0 خاصية OleObject.ClassIdentifier التي يمكن استخدامها لتحديد سلوك التطبيق لتحميل OleObject. على سبيل المثال ، يمكن تضمين ملف PPT في جدول بيانات بطريقتين مختلفتين ، أي ؛ عرض العرض التقديمي أو عرض الشرائح ، في حين أن كلا العرضين لهما قيم معرف فئة مختلفة.

فيما يلي سيناريو الاستخدام البسيط لخاصية OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[استخدام OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet containing a presentation as OleObject

Workbook book = new Workbook(dir + "embeddedPresentation.xls");

//Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[]imageData = null;

int x = 0;

int y = 0;

byte[]objData = null;

String progID = "";

int fileFormatType = 0;

String sourceFullName = "";

Boolean isDisplayAsIcon = false;

byte[]classId = null;

//Get the first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Get the first OleObject from the collection

OleObject frame = sheet.getOleObjects().get(0);

//Store the properties in variables

upperLeftRow = frame.getUpperLeftRow();

upperLeftColumn = frame.getUpperLeftColumn();

height = frame.getHeight();

width = frame.getWidth();

imageData = frame.getImageData();

x = frame.getX();

y = frame.getY();

objData = frame.getObjectData();

progID = frame.getProgID();

fileFormatType = frame.getFileFormatType();

sourceFullName = frame.getObjectSourceFullName();

isDisplayAsIcon = frame.getDisplayAsIcon();

classId = frame.getClassIdentifier();

//Initialize a new Workbook instance

book = new Workbook();

//Access first worksheet from the collection

sheet = book.getWorksheets().get(0);

//Insert the OleObject to the worksheet

int oleNumber = sheet.getOleObjects().add(upperLeftRow, upperLeftColumn, height, width, imageData);

//Access newly inserted OleObject

OleObject embeddedObject = sheet.getOleObjects().get(oleNumber);

//Assign previously stored properties to new OleObject

embeddedObject.setX(x);

embeddedObject.setY(y);

embeddedObject.setObjectData(objData);

embeddedObject.setProgID(progID);

embeddedObject.setFileFormatType(fileFormatType);

embeddedObject.setDisplayAsIcon(isDisplayAsIcon);

embeddedObject.setObjectSourceFullName(sourceFullName);

embeddedObject.setAutoSize(false);

if (classId != null)

{

	embeddedObject.setClassIdentifier(classId);

}

{{< /highlight >}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **Worksheet.setBackground طريقة قديمة**
الرجاء استخدام الخاصية Worksheet.BackgroundImage بدلاً من ذلك.
### **LineShape.Begin ArrowheadStyle و ArcShape.BeginArrowheadStyle Properties**
الرجاء استخدام خاصية Shape.Line.BeginArrowheadStyle كبديل.
### **LineShape.EndArrowheadStyle و ArcShape.End ArrowheadStyle Properties**
الرجاء استخدام خاصية Shape.Line.EndArrowheadStyle كبديل.
### **LineShape.egin.ArrowheadWidth & ArcShape.BeginArrowheadWidth Properties**
الرجاء استخدام خاصية Shape.Line.BeginArrowheadWidth كبديل.
### **خط متقادم الشكل ، بداية السهم ، الطول والشكل المقوس. بداية السهم ، خصائص الطول**
الرجاء استخدام خاصية Shape.Line.BeginArrowheadLength بدلاً من ذلك.
### **LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth خصائص**
الرجاء استخدام خاصية Shape.Line.EndArrowheadWidth بدلاً من ذلك.
### **خط متقادم الشكل.رأس السهمالطول والشكل القوسي. نهاية السهم**
الرجاء استخدام خاصية Shape.Line.EndArrowheadLength بدلاً من ذلك.
## **واجهات برمجة التطبيقات المحذوفة**
### **طريقة تنسيق Worksheet.copyConditionalFormatting المحذوفة**
### **Workbook.checkWriteProtectedPassword الأسلوب المحذوف**
## **إعادة تسمية واجهات برمجة التطبيقات**
### **إعادة تسمية Workbook.removeDigitallySign Method**
تمت إعادة تسمية طريقة Workbook.removeDigitallySign إلى Workbook.removeDigitalSignature.
