---
title: API العام التغييرات في Aspose.Cells 9.0.0
type: docs
weight: 330
url: /ar/net/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.9.2 إلى 9.0.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية Shape.TextOptions**
كشف Aspose.Cells for .NET خاصية TextOptions لفئة الشكل للتحكم في مظهر الأجزاء النصية للشكل.

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.TextOptions.

**C#**

{{< highlight "csharp" >}}

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


### **تمت إضافة خاصية LoadOptions.CultureInfo**
كشف Aspose.Cells for .NET 9.0.0 خاصية LoadOptions.CultureInfo التي تسمح بحقن مثيل CultureInfo في وقت تحميل مستند في مثيل Workbook.

فيما يلي سيناريو الاستخدام البسيط للخصائص المذكورة أعلاه.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[تحميل جدول بيانات بمعلومات ثقافية محددة](/cells/ar/net/load-the-workbook-with-specific-system-culture-info/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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
كشف Aspose.Cells for .NET خاصية ChartPoint.IsInSecondaryPlot التي يمكن استخدامها لاكتشاف ما إذا كانت ChartPoint موجودة في مخطط ثانوي لمخطط دائري أو شريطي.

فيما يلي سيناريو استخدام بسيط لخاصية Shape.Line.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العثور على DataPoint يكمن في قطعة الأرض الثانية](/cells/ar/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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
كشف Aspose.Cells for .NET 9.0.0 خاصية OleObject.ClassIdentifier التي يمكن استخدامها لتحديد سلوك التطبيق لتحميل OleObject. على سبيل المثال ، يمكن تضمين ملف PPT في جدول بيانات بطريقتين مختلفتين ، أي ؛ عرض العرض التقديمي أو عرض الشرائح ، في حين أن كلا العرضين لهما قيم معرف فئة مختلفة.

فيما يلي سيناريو الاستخدام البسيط لخاصية OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[استخدام OleObject.ClassIdentifier](/cells/ar/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a spreadsheet containing a presentation as OleObject

var book = new Workbook(dir + "embeddedPresentation.xls");

// Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[]imageData = null;

int x = 0;

int y = 0;

byte[]objData = null;

string progID = "";

FileFormatType fileFormatType = FileFormatType.Unknown;

string sourceFullName = "";

bool isDisplayAsIcon = false;

byte[]classId = null;

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
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **ورقة عمل قديمة**
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
### **طريقة تنسيق ورقة العمل المحذوفة**
### **المصنف المحذوف. طريقة CheckWriteProtectedPassword**
## **إعادة تسمية واجهات برمجة التطبيقات**
### **إعادة تسمية المصنف. طريقة RemoveDigitallySign**
تمت إعادة تسمية طريقة Workbook.RemoveDigitallySign إلى Workbook.RemoveDigitalSignature.
