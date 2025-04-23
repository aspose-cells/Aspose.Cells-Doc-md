---
title: تغييرات API العامة في Aspose.Cells 9.0.0
type: docs
weight: 340
url: /ar/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.9.2 إلى 9.0.0 التي قد تثير اهتمام مطوري الوحدات/التطبيقات. وتشمل ليس فقط الطرق العامة الجديدة والمحدثة، والفئات المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **خاصية TextOptions الجديدة**
تمكين Aspose.Cells for Java الخاصية TextOptions لفئة Shape للتحكم في ظهور الأجزاء النصية للشكل.

فيما يلي سيناريو استخدام بسيط لخاصية TextOptions للشكل.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java قد فتح الخاصية ChartPoint.IsInSecondaryPlot التي يمكن استخدامها لاكتشاف ما إذا كانت ChartPoint يقع على رسم ثانوي لرسم بياني لـ Pie أو Bar.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Line.

{{% alert color="primary" %}} 

تحقق من المقال المفصل على [العثور على DataPoint يقع على Second Plot](/cells/ar/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load an existing spreadsheet containing a Pie chart

Workbook book = new Workbook(dir + "PieBar.xlsx");

//Load the Worksheet at 0 index

Worksheet sheet = book.getWorksheets().get(0);

//Load the first chart from the collection

Chart chart = sheet.getCharts().get(0);

//Calculate the chart before accessing its properties

chart.calculate();

//Accessing chart's first series

Series series = chart.getNSeries().get(0);

//Loop over the ChartPoint collection

for(int p = 0 ; p < series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **تمت إضافة خاصية OleObject.ClassIdentifier**
Aspose.Cells for Java 9.0.0 قد فتح الخاصية OleObject.ClassIdentifier والتي يمكن استخدامها لتحديد سلوك التطبيق لتحميل كائن OleObject. على سبيل المثال ، يمكن تضمين ملف PPT في ورقة النشر مع وجهتي نظر مختلفتين ، وهي عرض العرض أو عرض الشريحة ، في حين أن كلا العرضين لهما قيم معرف فئة مختلفة.

فيما يلي سيناريو استخدام بسيط لخاصية OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

تحقق من المقال المفصل على [استخدام OleObject.ClassIdentifier](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet containing a presentation as OleObject

Workbook book = new Workbook(dir + "embeddedPresentation.xls");

//Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[] imageData = null;

int x = 0;

int y = 0;

byte[] objData = null;

String progID = "";

int fileFormatType = 0;

String sourceFullName = "";

Boolean isDisplayAsIcon = false;

byte[] classId = null;

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
## **واجهات برمجة التطبيق القديمة**
### **الواجهة القديمة Worksheet.setBackground تم إهمالها**
يرجى استخدام خاصية Worksheet.BackgroundImage بدلاً منها.
### **تم إهمال خصائص LineShape.BeginArrowheadStyle و ArcShape.BeginArrowheadStyle**
يرجى استخدام خاصية Shape.Line.BeginArrowheadStyle كبديل.
### **تم إهمال خصائص LineShape.EndArrowheadStyle و ArcShape.EndArrowheadStyle**
يرجى استخدام خاصية Shape.Line.EndArrowheadStyle كبديل.
### **تم إهمال خصائص LineShape.BeginArrowheadWidth و ArcShape.BeginArrowheadWidth**
يرجى استخدام خاصية Shape.Line.BeginArrowheadWidth كبديل.
### **تم الاستغناء عن خصائص Obsoleted LineShape.BeginArrowheadLength و ArcShape.BeginArrowheadLength**
يرجى استخدام خاصية Shape.Line.BeginArrowheadLength بدلاً من ذلك.
### **تم الاستغناء عن خصائص Obsoleted LineShape.EndArrowheadWidth و ArcShape.EndArrowheadWidth**
يرجى استخدام خاصية Shape.Line.EndArrowheadWidth بدلاً من ذلك.
### **تم الاستغناء عن خصائص Obsoleted LineShape.EndArrowheadLength و ArcShape.EndArrowheadLength**
يرجى استخدام خاصية Shape.Line.EndArrowheadLength بدلاً من ذلك.
## **حذف واجهات برمجة التطبيق**
### **حذف أسلوب Worksheet.copyConditionalFormatting**
### **حذف أسلوب Workbook.checkWriteProtectedPassword**
## **تغيير أسماء الواجهات البرمجية**
### **تمت تسمية أسلوب Workbook.removeDigitallySign**
تم تغيير أسم أسلوب Workbook.removeDigitallySign إلى Workbook.removeDigitalSignature.
{{< app/cells/assistant language="java" >}}
