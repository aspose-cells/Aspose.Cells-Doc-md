---
title: Aspose.Cells 9.0.0 中的公共 API 更改
type: docs
weight: 330
url: /zh/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.9.2 到 9.0.0 的 Aspose.Cells API 变化，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还描述了在 Aspose.Cells 后台行为中的任何更改。

{{% /alert %}} 
## **添加的 API**
### **添加了 Shape.TextOptions 属性**
Aspose.Cells for .NET 已经为 Shape 类公开了 TextOptions 属性，以控制形状文本部分的外观。

这里是 Shape.TextOptions 属性的简单使用场景。

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


### **增加了 LoadOptions.CultureInfo 属性**
Aspose.Cells for .NET 9.0.0 已经公开了 LoadOptions.CultureInfo 属性，允许在加载文档到 Workbook 的实例时注入 CultureInfo 的实例。

以下是上述属性的简单使用场景。

{{% alert color="primary" %}} 

查看有关[使用特定CultureInfo加载电子表格](/cells/zh/net/load-the-workbook-with-specific-system-culture-info/)的详细文章。

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


### **添加了 ChartPoint.IsInSecondaryPlot 属性**
Aspose.Cells for .NET 已经公开了 ChartPoint.IsInSecondaryPlot 属性，可用于检测饼图或条形图上的 ChartPoint 是否位于辅助绘图区域。

这里是 Shape.Line 属性的简单使用场景。

{{% alert color="primary" %}} 

请查阅[查找数据点是否位于第二绘图上的详细文章](/cells/zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)。

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


### **添加了OleObject.ClassIdentifier属性**
Aspose.Cells for .NET 9.0.0 已经公开了 OleObject.ClassIdentifier 属性，可用于指定加载 OleObject 的应用程序行为。例如，PPT 文件可以嵌入在电子表格中，并具有两种不同的视图，即演示文稿视图或幻灯片视图，而两种视图具有不同的类标识值。

以下是OleObject.ClassIdentifier属性的简单使用场景。

{{% alert color="primary" %}} 

请查阅[使用 OleObject.ClassIdentifier 的详细文章](/cells/zh/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)。

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
## **已弃用的API**
### **弃用了 Worksheet.SetBackground 方法**
请使用Worksheet.BackgroundImage属性代替。
### **已废弃LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle 属性**
请使用Shape.Line.BeginArrowheadStyle属性作为替代。
### **已废弃LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle 属性**
请使用Shape.Line.EndArrowheadStyle属性作为替代。
### **已废弃LineShape.BeginArrowheadWidth & ArcShape.BeginArrowheadWidth 属性**
请使用Shape.Line.BeginArrowheadWidth属性作为替代。
### **已废弃LineShape.BeginArrowheadLength & ArcShape.BeginArrowheadLength 属性**
请使用Shape.Line.BeginArrowheadLength属性代替。
### **已废弃LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth 属性**
请使用Shape.Line.EndArrowheadWidth属性代替。
### **已废弃LineShape.EndArrowheadLength & ArcShape.EndArrowheadLength 属性**
请使用Shape.Line.EndArrowheadLength属性代替。
## **删除的API**
### **删除了Worksheet.CopyConditionalFormatting方法**
### **删除了Workbook.CheckWriteProtectedPassword方法**
## **重命名的API**
### **重命名为Workbook.RemoveDigitallySign方法**
Workbook.RemoveDigitallySign方法已更名为Workbook.RemoveDigitalSignature。
