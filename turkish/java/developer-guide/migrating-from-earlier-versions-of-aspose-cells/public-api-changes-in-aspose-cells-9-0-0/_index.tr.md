---
title: Aspose.Cells 9.0.0 da Genel API Değişiklikleri
type: docs
weight: 340
url: /tr/java/public-api-changes-in-aspose-cells-9-0-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek şekilde Aspose.Cells API'sindeki 8.9.2 sürümünden 9.0.0 sürümüne kadar olan değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemlerin yanı sıra eklenen ve kaldırılan sınıflar vb. gibi konuları içerir, ayrıca Aspose.Cells'in arka planda olan herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Eklenen Shape.TextOptions Özelliği**
Aspose.Cells for Java, Shape sınıfı için metinsel kısımların görünümünü kontrol etmek için TextOptions özelliğini ortaya çıkarmıştır.

İşte Shape.TextOptions özelliğinin basit kullanım senaryosu.

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
### **Eklenen ChartPoint.IsInSecondaryPlot Özelliği**
Aspose.Cells for Java, ChartPoint.IsInSecondaryPlot özelliğini ortaya çıkarmıştır; bu, bir Pasta veya Bar grafiğinin ikincil çizgisinde bir ChartPoint'in olup olmadığını tespit etmek için kullanılabilir.

İşte Shape.Line özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

[Bir Veri Noktasının İkincil Grafiğinde Olup Olmadığını Bulma](/cells/tr/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)'daki detaylı makaleyi kontrol edin

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
### **Eklenen OleObject.ClassIdentifier özelliği**
Aspose.Cells for Java 9.0.0, OleObject.ClassIdentifier özelliğini açığa çıkardı, bu özellikle OleObject'ın yüklenmesi için uygulama davranışını belirtmek için kullanılabilir. Örneğin, bir PPT dosyası, elektronik tabloya 2 farklı görünümle gömülebilir; sunum görünümü veya slayt görünümü, her iki görünümün de farklı sınıf tanımlayıcı değerleri vardır.

OleObject.ClassIdentifier özelliğinin basit kullanım senaryosu aşağıdaki gibidir.

{{% alert color="primary" %}} 

[OleObject.ClassIdentifier kullanımı](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/) hakkındaki detaylı makaleyi kontrol edin

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
## **Eskimiş API'lar**
### **Eskimiş Worksheet.setBackground Metodu**
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
### **Silinmiş Worksheet.copyConditionalFormatting Metodu**
### **Silinmiş Workbook.checkWriteProtectedPassword Metodu**
## **Adı Değişen API'lar**
### **Adı Değişen Workbook.removeDigitallySign Metodu**
Workbook.removeDigitallySign metodu artık Workbook.removeDigitalSignature olarak adlandırılmıştır.
