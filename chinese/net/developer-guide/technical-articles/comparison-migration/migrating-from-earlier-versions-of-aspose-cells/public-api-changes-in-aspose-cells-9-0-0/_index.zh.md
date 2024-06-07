---
title: Aspose.Cells 9.0.0中的公共API更改
type: docs
weight: 330
url: /zh/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

该文档描述了从版本8.9.2到9.0.0的Aspose.Cells API中可能对模块/应用程序开发人员感兴趣的更改。它不仅包括新的和更新的公共方法，添加和删除的类等，还包括对Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **新增Shape.TextOptions属性**
Aspose.Cells for .NET已公开了Shape类的TextOptions属性，以控制Shape的文本部分的外观。

以下是Shape.TextOptions属性的简单使用场景。

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


### **新增LoadOptions.CultureInfo属性**
Aspose.Cells for .NET 9.0.0已经公开了LoadOptions.CultureInfo属性，允许在加载文档到Workbook实例时注入CultureInfo实例。

以下是上述属性的简单用法场景。

{{% alert color="primary" %}} 

查看[使用特定CultureInfo加载电子表格](/cells/zh/net/load-the-workbook-with-specific-system-culture-info/)上的详细文章。

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


### **新增ChartPoint.IsInSecondaryPlot属性**
Aspose.Cells for .NET已公开了ChartPoint.IsInSecondaryPlot属性，可用于检测ChartPoint是否位于饼图或条形图的辅助绘图上。

以下是Shape.Line属性的简单用法场景。

{{% alert color="primary" %}} 

查看[查找数据点是否位于第二个绘图上](/cells/zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)上的详细文章。

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


### **新增OleObject.ClassIdentifier属性**
Aspose.Cells for .NET 9.0.0已经公开了OleObject.ClassIdentifier属性，可用于指定加载OleObject的应用程序行为。例如，PPT文件可以嵌入到具有2个不同视图的电子表格中，即演示视图或幻灯片视图，而这两个视图具有不同的类标识符值。

以下是OleObject.ClassIdentifier属性的简单使用场景。

{{% alert color="primary" %}} 

查看[使用OleObject.ClassIdentifier](/cells/zh/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)上的详细文章。

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
## **已废弃的API**
### **已过时的Worksheet.SetBackground方法**
请改用Worksheet.BackgroundImage属性。
### **已过时的LineShape.BeginArrowheadStyle和ArcShape.BeginArrowheadStyle属性**
请改用Shape.Line.BeginArrowheadStyle属性作为替代。
### **已过时的LineShape.EndArrowheadStyle和ArcShape.EndArrowheadStyle属性**
请改用Shape.Line.EndArrowheadStyle属性作为替代。
### **已过时的LineShape.BeginArrowheadWidth和ArcShape.BeginArrowheadWidth属性**
请改用Shape.Line.BeginArrowheadWidth属性作为替代。
### **已过时的LineShape.BeginArrowheadLength和ArcShape.BeginArrowheadLength属性**
请改用Shape.Line.BeginArrowheadLength属性。
### **弃用LineShape.EndArrowheadWidth和ArcShape.EndArrowheadWidth属性。**
请改用Shape.Line.EndArrowheadWidth属性。
### **弃用LineShape.EndArrowheadLength和ArcShape.EndArrowheadLength属性。**
请改用Shape.Line.EndArrowheadLength属性。
## **已删除的API**
### **已删除的Worksheet.CopyConditionalFormatting方法**
### **已删除的Workbook.CheckWriteProtectedPassword方法**
## **API已重命名**
### **已重命名的Workbook.RemoveDigitallySign方法**
Workbook.RemoveDigitallySign方法已重命名为Workbook.RemoveDigitalSignature。
