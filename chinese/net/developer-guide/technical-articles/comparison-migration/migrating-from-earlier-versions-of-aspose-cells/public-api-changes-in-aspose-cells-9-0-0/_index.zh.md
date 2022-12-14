---
title: 公共 API Aspose.Cells 9.0.0 的变化
type: docs
weight: 330
url: /zh/net/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.9.2 到 9.0.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **添加了 Shape.TextOptions 属性**
Aspose.Cells for .NET 公开了 Shape 类的 TextOptions 属性，以控制 Shape 文本部分的外观。

这是 Shape.TextOptions 属性的简单使用场景。

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


### **添加了 LoadOptions.CultureInfo 属性**
Aspose.Cells for .NET 9.0.0 公开了 LoadOptions.CultureInfo 属性，允许在工作簿实例中加载文档时注入 CultureInfo 实例。

这是上述属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[加载具有特定 CultureInfo 的电子表格](/cells/zh/net/load-the-workbook-with-specific-system-culture-info/).

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


### **添加了 ChartPoint.IsInSecondaryPlot 属性**
Aspose.Cells for .NET 公开了 ChartPoint.IsInSecondaryPlot 属性，该属性可用于检测 ChartPoint 是否驻留在饼图或条形图的辅助图上。

下面是 Shape.Line 属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[查找数据点驻留在第二个图上](/cells/zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

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


### **添加了 OleObject.ClassIdentifier 属性**
Aspose.Cells for .NET 9.0.0 公开了 OleObject.ClassIdentifier 属性，可用于指定加载 OleObject 的应用程序行为。例如，一个 PPT 文件可以嵌入到具有 2 个不同视图的电子表格中，即；演示视图或幻灯片视图，而这两个视图具有不同的类标识符值。

以下是 OleObject.ClassIdentifier 属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[使用 OleObject.ClassIdentifier](/cells/zh/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

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
## **过时的 API**
### **废弃的 Worksheet.SetBackground 方法**
请改用 Worksheet.BackgroundImage 属性。
### **废弃的 LineShape.BeginArrowheadStyle 和 ArcShape.BeginArrowheadStyle 属性**
请使用 Shape.Line.BeginArrowheadStyle 属性作为替代。
### **废弃的 LineShape.EndArrowheadStyle 和 ArcShape.EndArrowheadStyle 属性**
请使用 Shape.Line.EndArrowheadStyle 属性作为替代。
### **废弃的 LineShape.BeginArrowheadWidth 和 ArcShape.BeginArrowheadWidth 属性**
请使用 Shape.Line.BeginArrowheadWidth 属性作为替代。
### **废弃的 LineShape.BeginArrowheadLength 和 ArcShape.BeginArrowheadLength 属性**
请改用 Shape.Line.BeginArrowheadLength 属性。
### **废弃的 LineShape.EndArrowheadWidth 和 ArcShape.EndArrowheadWidth 属性**
请改用 Shape.Line.EndArrowheadWidth 属性。
### **废弃的 LineShape.EndArrowheadLength 和 ArcShape.EndArrowheadLength 属性**
请改用 Shape.Line.EndArrowheadLength 属性。
## **已删除的 API**
### **删除了 Worksheet.CopyConditionalFormatting 方法**
### **已删除的 Workbook.CheckWriteProtectedPassword 方法**
## **重命名的 API**
### **重命名 Workbook.RemoveDigitallySign 方法**
Workbook.RemoveDigitallySign 方法已重命名为 Workbook.RemoveDigitalSignature。
