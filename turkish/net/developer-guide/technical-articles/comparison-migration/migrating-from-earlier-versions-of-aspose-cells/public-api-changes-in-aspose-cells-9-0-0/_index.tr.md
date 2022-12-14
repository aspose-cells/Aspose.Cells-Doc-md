---
title: Genel API Aspose.Cells 9.0.0'daki değişiklikler
type: docs
weight: 330
url: /tr/net/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.9.2 sürümünden 9.0.0 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Shape.TextOptions Özelliği Eklendi**
Aspose.Cells for .NET, bir Shape'in metinsel bölümlerinin görünümünü kontrol etmek için Shape sınıfı için TextOptions özelliğini kullanıma sundu.

İşte Shape.TextOptions özelliğinin basit kullanım senaryosu.

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


### **LoadOptions.CultureInfo Özelliği Eklendi**
Aspose.Cells for .NET 9.0.0, bir Workbook örneğine belge yüklerken bir CultureInfo örneğinin enjekte edilmesine izin veren LoadOptions.CultureInfo özelliğini kullanıma sundu.

İşte yukarıda belirtilen özelliklerin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Elektronik Tabloyu Belirli CultureInfo ile Yükleme](/cells/tr/net/load-the-workbook-with-specific-system-culture-info/).

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


### **ChartPoint.IsInSecondaryPlot Özelliği Eklendi**
Aspose.Cells for .NET, ChartPoint.IsInSecondaryPlot özelliğini ortaya çıkardı ve bu özellik, bir ChartPoint'in Pasta veya Çubuk grafiğinin ikincil çiziminde bulunup bulunmadığını algılamak için kullanılabilir.

İşte Shape.Line özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Bir DataPoint bulmak, İkinci Çizimde bulunur](/cells/tr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/).

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


### **OleObject.ClassIdentifier özelliği eklendi**
Aspose.Cells for .NET 9.0.0, bir OleObject yüklemek için uygulama davranışını belirtmek üzere kullanılabilen OleObject.ClassIdentifier özelliğini kullanıma sundu. Örneğin, bir PPT dosyası bir elektronik tabloya 2 farklı görünümle gömülebilir, yani; sunum görünümü veya slayt görünümü, oysa her iki görünüm de farklı sınıf tanımlayıcı değerlerine sahiptir.

OleObject.ClassIdentifier özelliğinin basit kullanım senaryosu aşağıdadır.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[OleObject.ClassIdentifier'ı kullanma](/cells/tr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/).

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
## **Eski API'ler**
### **Eski Worksheet.SetBackground Yöntemi**
Lütfen bunun yerine Worksheet.BackgroundImage özelliğini kullanın.
### **Eski LineShape.BeginArrowheadStyle & ArcShape.BeginArrowheadStyle Özellikler**
Lütfen alternatif olarak Shape.Line.BeginArrowheadStyle özelliğini kullanın.
### **Eskimiş LineShape.EndArrowheadStyle & ArcShape.EndArrowheadStyle Özellikler**
Lütfen alternatif olarak Shape.Line.EndArrowheadStyle özelliğini kullanın.
### **Eski LineShape.BeginArrowheadWidth & ArcShape.BeginArrowheadWidth Özellikler**
Lütfen alternatif olarak Shape.Line.BeginArrowheadWidth özelliğini kullanın.
### **Eski LineShape.BeginArrowheadLength & ArcShape.BeginArrowheadLength Özellikler**
Lütfen bunun yerine Shape.Line.BeginArrowheadLength özelliğini kullanın.
### **Eskimiş LineShape.EndArrowheadWidth & ArcShape.EndArrowheadWidth Özellikler**
Lütfen bunun yerine Shape.Line.EndArrowheadWidth özelliğini kullanın.
### **Eski LineShape.EndArrowheadLength & ArcShape.EndArrowheadLength Özellikler**
Lütfen bunun yerine Shape.Line.EndArrowheadLength özelliğini kullanın.
## **Silinmiş API'ler**
### **Silinmiş Worksheet.CopyConditionalFormatting Yöntemi**
### **Silinmiş Workbook.CheckWriteProtectedPassword Yöntemi**
## **Yeniden adlandırılan API'ler**
### **Workbook.RemoveDigitallySign Yöntemi yeniden adlandırıldı**
Workbook.RemoveDigitalSign yöntemi, Workbook.RemoveDigitalSignature olarak yeniden adlandırıldı.
