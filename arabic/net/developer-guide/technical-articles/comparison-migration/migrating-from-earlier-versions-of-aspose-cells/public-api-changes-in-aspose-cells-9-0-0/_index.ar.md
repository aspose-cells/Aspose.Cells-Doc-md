---
title: تغييرات API العامة في Aspose.Cells 9.0.0
type: docs
weight: 330
url: /ar/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.9.2 إلى 9.0.0 التي قد تثير اهتمام مطوري الوحدات/التطبيقات. وتشمل ليس فقط الطرق العامة الجديدة والمحدثة، والفئات المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **خاصية TextOptions الجديدة**
Aspose.Cells for .NET قد عرضت خاصية TextOptions لفئة Shape للتحكم في مظهر الأجزاء النصية لشكل.

فيما يلي سيناريو استخدام بسيط لخاصية TextOptions للشكل.

**C#**

{{< highlight csharp >}}

 // Initialize an instance of Workbook

var book = new Workbook();

// Get the default Worksheet from the Workbook

var sheet = book.Worksheets[0];

// Add a TextBox to the collection

var textboxIndex = sheet.TextBoxes.Add(2, 1, 160, 200);

// Get the TextBox object

var textbox = sheet.TextBoxes[textboxIndex];

// Add text to the TextBox

textbox.Text = "Hello Aspose!";

// Format the textual contents

textbox.TextOptions.Color = System.Drawing.Color.Red;

textbox.TextOptions.IsItalic = true;

{{< /highlight >}}


### **تمت إضافة خاصية LoadOptions.CultureInfo.**
Aspose.Cells for .NET 9.0.0 قد عرضت خاصية LoadOptions.CultureInfo التي تسمح بحقن مثيل من CultureInfo أثناء تحميل مستند في مثيل من Workbook.

فيما يلي سيناريو استخدام بسيط للخصائص المذكورة.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [تحميل جدول بيانات بثقافة معينة](/cells/ar/net/load-the-workbook-with-specific-system-culture-info/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of CultureInfo and populate its properties

var culture = new CultureInfo("en-GB");

culture.NumberFormat.NumberDecimalSeparator = ",";

culture.DateTimeFormat.DateSeparator = "-";

culture.DateTimeFormat.ShortDatePattern = "dd-MM-yyyy";

// Create an instance of LoadOptions and set the CultureInfo property

var options = new LoadOptions(LoadFormat.Html);

options.CultureInfo = culture;

// Load a HTML or TXT file in an instance of Workbook with instance of  LoadOptions

var book = new Workbook(dir + "input.html", options);

{{< /highlight >}}


### **تمت إضافة خاصية ChartPoint.IsInSecondaryPlot**
Aspose.Cells for .NET قد عرضت خاصية ChartPoint.IsInSecondaryPlot التي يمكن استخدامها لاكتشاف ما إذا كان ChartPoint يقع على مؤامرة ثانوية لرسم بياني دائري أو شريطي.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Line.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [العثور على نقطة بيانات تقع في المؤامرة الثانية](/cells/ar/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load an existing spreadsheet containing a Pie chart

var book = new Workbook(dir + "PieBar.xlsx");

// Load the Worksheet at 0 index

var sheet = book.Worksheets[0];

// Load the first chart from the collection

var chart = sheet.Charts[0];

// Calculate the chart before accessing its properties

chart.Calculate();

// Accessing chart's first series

var series = chart.NSeries[0];

// Loop over the ChartPoint collection

foreach (ChartPoint point in series.Points)

{

    // Detect if ChartPoint resides on secondary plot

    Console.WriteLine(point.IsInSecondaryPlot);

}

{{< /highlight >}}


### **تمت إضافة خاصية OleObject.ClassIdentifier**
Aspose.Cells for .NET 9.0.0 قد عرضت خاصية OleObject.ClassIdentifier التي يمكن استخدامها لتحديد سلوك التطبيق لتحميل كائن OleObject. على سبيل المثال، يمكن تضمين ملف PPT في جدول بيانات بعرضين مختلفين، ألا وهما؛ عرض العرض أو عرض الشريحة، حيث يحتوي كلا العرضين على قيم معرف الصف الدراسي مختلفة.

فيما يلي سيناريو استخدام بسيط لخاصية OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [استخدام OleObject.ClassIdentifier](/cells/ar/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet containing a presentation as OleObject

var book = new Workbook(dir + "embeddedPresentation.xls");

// Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[] imageData = null;

int x = 0;

int y = 0;

byte[] objData = null;

string progID = "";

FileFormatType fileFormatType = FileFormatType.Unknown;

string sourceFullName = "";

bool isDisplayAsIcon = false;

byte[] classId = null;

// Get the first worksheet from the collection

var sheet = book.Worksheets[0];

// Get the first OleObject from the collection

var frame = sheet.OleObjects[0];

// Store the properties in variables

upperLeftRow = frame.UpperLeftRow;

upperLeftColumn = frame.UpperLeftColumn;

height = frame.Height;

width = frame.Width;

imageData = frame.ImageData;

x = frame.X;

y = frame.Y;

objData = frame.ObjectData;

progID = frame.ProgID;

fileFormatType = frame.FileFormatType;

sourceFullName = frame.ObjectSourceFullName;

isDisplayAsIcon = frame.DisplayAsIcon;

classId = frame.ClassIdentifier;

// Initialize a new Workbook instance

book = new Workbook();

// Access first worksheet from the collection

sheet = book.Worksheets[0];

// Insert the OleObject to the worksheet

int oleNumber = sheet.OleObjects.Add(upperLeftRow, upperLeftColumn, height, width, imageData);

// Access newly inserted OleObject

var embeddedObject = sheet.OleObjects[oleNumber];

// Assign previously stored properties to new OleObject

embeddedObject.X = x;

embeddedObject.Y = y;

embeddedObject.ObjectData = objData;

embeddedObject.ProgID = progID;

embeddedObject.FileFormatType = fileFormatType;

embeddedObject.DisplayAsIcon = isDisplayAsIcon;

embeddedObject.ObjectSourceFullName = sourceFullName;

embeddedObject.IsAutoSize = false;

if (classId != null)

{

    embeddedObject.ClassIdentifier = classId;

}

// Save the resultant spreadsheet

book.Save(dir  + "output.xls");

{{< /highlight >}}
## **واجهات برمجة التطبيق القديمة**
### **واجهة برمجة تطبيقات قد قدمت طريقة Obsoleted Worksheet.SetBackground**
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
### **طرق النسخ المحذوفة للورقة العمل**
### **طريقة Workbook.CheckWriteProtectedPassword المحذوفة**
## **تغيير أسماء الواجهات البرمجية**
### **طريقة Workbook.RemoveDigitallySign تمت إعادة تسميتها إلى Workbook.RemoveDigitalSignature.**
تمت إعادة تسمية طريقة Workbook.RemoveDigitallySign إلى Workbook.RemoveDigitalSignature.
