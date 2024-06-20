---
title: Aspose.Cells 9.0.0 da Genel API Değişiklikleri
type: docs
weight: 330
url: /tr/net/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek şekilde Aspose.Cells API'sindeki 8.9.2 sürümünden 9.0.0 sürümüne kadar olan değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemlerin yanı sıra eklenen ve kaldırılan sınıflar vb. gibi konuları içerir, ayrıca Aspose.Cells'in arka planda olan herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Eklenen Shape.TextOptions Özelliği**
Aspose.Cells for .NET, Shape sınıfı için metinsel kısımların görünümünü kontrol etmek amacıyla TextOptions özelliğini sunmuştur.

İşte Shape.TextOptions özelliğinin basit kullanım senaryosu.

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


### **LoadOptions.CultureInfo Özelliği Eklendi**
Aspose.Cells for .NET 9.0.0, LoadOptions.CultureInfo özelliğini ortamın yüklenme anında CultureInfo örneğine enjekte etmeye olanak tanıyor.

Yukarıdaki özelliklerin basit kullanım senaryosu aşağıda gösterilmektedir.

{{% alert color="primary" %}} 

[Belirli Bir CultureInfo ile Elektronik Tablo Yükleme](/cells/tr/net/belirli-sistem-culture-info-ile-elektronik-tabloyu-yukleme/) hakkındaki detaylı makaleyi kontrol edin.

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


### **Eklenen ChartPoint.IsInSecondaryPlot Özelliği**
Aspose.Cells for .NET, ChartPoint.IsInSecondaryPlot özelliğini ekleyerek bir ChartPoint'un bir Pasta veya Sütun grafiğinin ikincil parçasında olup olmadığını belirlemek için kullanılabiliyor.

İşte Shape.Line özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

[Bir DataPoint'in İkinci Parçada Olup Olmadığını Bulma](/cells/tr/net/pasta-vb-pasta-grafiginde-dataponit-lerin-ikinci-parça-da-olup-olmadığını-bulmak/) hakkındaki detaylı makaleyi kontrol edin.

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


### **Eklenen OleObject.ClassIdentifier özelliği**
Aspose.Cells for .NET 9.0.0, OleObject.ClassIdentifier özelliğini kullanarak bir OleObject'in yüklenmesi için uygulama davranışını belirtmek için kullanılabiliyor. Örneğin, bir PPT dosyası, sunum görünümü veya slayt görünümü olmak üzere 2 farklı görünümde elektronik tabloya gömülebilir, her iki görünümün de farklı class identifier değerleri bulunuyor.

OleObject.ClassIdentifier özelliğinin basit kullanım senaryosu aşağıdaki gibidir.

{{% alert color="primary" %}} 

[OleObject.ClassIdentifier Kullanımı](/cells/tr/net/gömülü-ole-nesnesinin-class-identifier-değerini-getirme-veya-ayarlama/) hakkındaki detaylı makaleyi kontrol edin.

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
## **Eskimiş API'lar**
### **Eskimiş Worksheet.SetBackground Yöntemi**
Lütfen bunun yerine Worksheet.BackgroundImage özelliğini kullanın.
### **Eskimiş LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle Özellikleri**
Lütfen alternatif olarak Shape.Line.BeginArrowheadStyle özelliğini kullanın.
### **Eskimiş LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle Özellikleri**
Lütfen alternatif olarak Shape.Line.EndArrowheadStyle özelliğini kullanın.
### **Eskimiş LineShape.BeginArrowheadWidth & ArcShape.BeginArrowheadWidth Özellikleri**
Lütfen alternatif olarak Shape.Line.BeginArrowheadWidth özelliğini kullanın.
### **Eskimiş LineShape.BeginArrowheadLength & ArcShape.BeginArrowheadLength Özellikleri**
Lütfen bunun yerine Shape.Line.BeginArrowheadLength özelliğini kullanın.
### **Eskimiş LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth Özellikleri**
Lütfen bunun yerine Shape.Line.EndArrowheadWidth özelliğini kullanın.
### **Eskimiş LineShape.EndArrowheadLength & ArcShape.EndArrowheadLength Özellikleri**
Lütfen bunun yerine Shape.Line.EndArrowheadLength özelliğini kullanın.
## **Silinmiş API'lar**
### **Silinmiş Worksheet.CopyConditionalFormatting Yöntemi**
### **Silinmiş Workbook.CheckWriteProtectedPassword Metodu**
## **Adı Değişen API'lar**
### **Yeniden Adlandırılmış Workbook.RemoveDigitallySign Metodu**
Workbook.RemoveDigitallySign metodu Workbook.RemoveDigitalSignature olarak yeniden adlandırıldı.
