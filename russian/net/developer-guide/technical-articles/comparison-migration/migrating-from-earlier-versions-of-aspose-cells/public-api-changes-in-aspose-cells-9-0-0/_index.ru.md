---
title: Общедоступный API Изменения в Aspose.Cells 9.0.0
type: docs
weight: 330
url: /ru/net/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.9.2 до 9.0.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство Shape.TextOptions**
Aspose.Cells for .NET предоставил свойство TextOptions для класса Shape, чтобы управлять внешним видом текстовых частей Shape.

Вот простой сценарий использования свойства Shape.TextOptions.

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


### **Добавлено свойство LoadOptions.CultureInfo.**
Aspose.Cells for .NET 9.0.0 предоставляет свойство LoadOptions.CultureInfo, которое позволяет вставлять экземпляр CultureInfo во время загрузки документа в экземпляр Workbook.

Вот простой сценарий использования вышеупомянутых свойств.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Загрузка электронной таблицы с определенной информацией о культуре](/cells/ru/net/load-the-workbook-with-specific-system-culture-info/).

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


### **Добавлено свойство ChartPoint.IsInSecondaryPlot**
Aspose.Cells for .NET предоставил свойство ChartPoint.IsInSecondaryPlot, которое можно использовать для определения того, находится ли ChartPoint на вторичном графике круговой или гистограммы.

Вот простой сценарий использования свойства Shape.Line.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Поиск DataPoint находится на втором графике](/cells/ru/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

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


### **Добавлено свойство OleObject.ClassIdentifier.**
Aspose.Cells for .NET 9.0.0 предоставило свойство OleObject.ClassIdentifier, которое можно использовать для указания поведения приложения при загрузке OleObject. Например, файл PPT может быть встроен в электронную таблицу с двумя разными представлениями, то есть; представление презентации или представление слайдов, тогда как оба представления имеют разные значения идентификатора класса.

Ниже приведен простой сценарий использования свойства OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Использование OleObject.ClassIdentifier](/cells/ru/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

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
## **Устаревшие API**
### **Устаревший метод Worksheet.SetBackground**
Вместо этого используйте свойство Worksheet.BackgroundImage.
### **Устаревшие свойства LineShape.BeginArrowheadStyle и ArcShape.BeginArrowheadStyle**
В качестве альтернативы используйте свойство Shape.Line.BeginArrowheadStyle.
### **Устаревшие свойства LineShape.EndArrowheadStyle и ArcShape.EndArrowheadStyle**
В качестве альтернативы используйте свойство Shape.Line.EndArrowheadStyle.
### **Устаревшие свойства LineShape.BeginArrowheadWidth и ArcShape.BeginArrowheadWidth**
В качестве альтернативы используйте свойство Shape.Line.BeginArrowheadWidth.
### **Устаревшие свойства LineShape.BeginArrowheadLength и ArcShape.BeginArrowheadLength**
Вместо этого используйте свойство Shape.Line.BeginArrowheadLength.
### **Устаревшие свойства LineShape.EndArrowheadWidth и ArcShape.EndArrowheadWidth**
Вместо этого используйте свойство Shape.Line.EndArrowheadWidth.
### **Устаревшие свойства LineShape.EndArrowheadLength и ArcShape.EndArrowheadLength**
Вместо этого используйте свойство Shape.Line.EndArrowheadLength.
## **Удаленные API**
### **Удаленный метод Worksheet.CopyConditionalFormatting**
### **Удаленный метод Workbook.CheckWriteProtectedPassword**
## **Переименованные API**
### **Метод Workbook.RemoveDigitallySign переименован.**
Метод Workbook.RemoveDigitallySign был переименован в Workbook.RemoveDigitalSignature.
