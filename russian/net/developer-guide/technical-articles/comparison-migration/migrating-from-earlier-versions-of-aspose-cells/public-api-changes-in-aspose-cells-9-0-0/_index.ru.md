---
title: Изменения в общедоступном API в Aspose.Cells 9.0.0
type: docs
weight: 330
url: /ru/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.9.2 по 9.0.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные открытые методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство Shape.TextOptions.**
Aspose.Cells for .NET добавил свойство TextOptions для класса Shape для управления внешним видом текстовых частей формы.

Вот простой сценарий использования свойства Shape.TextOptions.

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


### **Добавлено свойство LoadOptions.CultureInfo**
Aspose.Cells for .NET 9.0.0 предоставил свойство LoadOptions.CultureInfo, которое позволяет вставлять экземпляр CultureInfo во время загрузки документа в экземпляр Workbook.

Вот простой сценарий использования вышеперечисленных свойств.

{{% alert color="primary" %}} 

Проверьте подробную статью по ссылке [Загрузка электронной таблицы с определенной CultureInfo](/cells/ru/net/load-the-workbook-with-specific-system-culture-info/).

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


### **Добавлено свойство ChartPoint.IsInSecondaryPlot.**
Aspose.Cells for .NET предоставил свойство ChartPoint.IsInSecondaryPlot, которое может использоваться для определения того, находится ли ChartPoint на вторичном графике круговой или столбчатой диаграммы.

Вот простой сценарий использования свойства Shape.Line.

{{% alert color="primary" %}} 

Проверьте подробную статью по ссылке [Поиск точки данных находится на втором графике](/cells/ru/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

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


### **Добавлено свойство OleObject.ClassIdentifier.**
Aspose.Cells for .NET 9.0.0 предоставил свойство OleObject.ClassIdentifier, которое может использоваться для указания поведения приложения при загрузке OleObject. Например, файл PPT можно встроить в электронную таблицу с 2 разными видами: видом презентации или видом слайда, причем оба вида имеют разные значения идентификатора класса.

Ниже приведен простой сценарий использования свойства OleObject.ClassIdentifier.

{{% alert color="primary" %}} 

Проверьте подробную статью по ссылке [Использование OleObject.ClassIdentifier](/cells/ru/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

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
## **Устаревшие API**
### **Метод Worksheet.SetBackground устарел**
Вместо этого используйте свойство Worksheet.BackgroundImage.
### **Свойства LineShape.BeginArrowheadStyle и ArcShape.BeginArrowheadStyle устарели**
В качестве альтернативы используйте свойство Shape.Line.BeginArrowheadStyle.
### **Свойства LineShape.EndArrowheadStyle и ArcShape.EndArrowheadStyle устарели**
В качестве альтернативы используйте свойство Shape.Line.EndArrowheadStyle.
### **Свойства LineShape.BeginArrowheadWidth и ArcShape.BeginArrowheadWidth устарели**
В качестве альтернативы используйте свойство Shape.Line.BeginArrowheadWidth.
### **Свойства LineShape.BeginArrowheadLength и ArcShape.BeginArrowheadLength устарели**
Используйте свойство Shape.Line.BeginArrowheadLength вместо.
### **Свойства LineShape.EndArrowheadWidth и ArcShape.EndArrowheadWidth устарели**
Используйте свойство Shape.Line.EndArrowheadWidth вместо.
### **Свойства LineShape.EndArrowheadLength и ArcShape.EndArrowheadLength устарели**
Используйте свойство Shape.Line.EndArrowheadLength вместо.
## **Удаленные API**
### **Удален метод Worksheet.CopyConditionalFormatting**
### **Удален метод Workbook.CheckWriteProtectedPassword**
## **Переименованные API**
### **Переименован метод Workbook.RemoveDigitallySign**
Метод Workbook.RemoveDigitallySign был переименован в Workbook.RemoveDigitalSignature.
{{< app/cells/assistant language="csharp" >}}
