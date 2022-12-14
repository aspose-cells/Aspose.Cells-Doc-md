---
title: Genel API Aspose.Cells 9.0.0'daki değişiklikler
type: docs
weight: 340
url: /tr/java/public-api-changes-in-aspose-cells-9-0-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.9.2 sürümünden 9.0.0 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Shape.TextOptions Özelliği Eklendi**
Aspose.Cells for Java, bir Shape'in metinsel bölümlerinin görünümünü kontrol etmek için Shape sınıfı için TextOptions özelliğini kullanıma sundu.

İşte Shape.TextOptions özelliğinin basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

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
### **ChartPoint.IsInSecondaryPlot Özelliği Eklendi**
Aspose.Cells for Java, ChartPoint.IsInSecondaryPlot özelliğini ortaya çıkardı ve bu özellik, bir ChartPoint'in Pasta veya Çubuk grafiğinin ikincil çiziminde bulunup bulunmadığını algılamak için kullanılabilir.

İşte Shape.Line özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Bir DataPoint bulmak, İkinci Çizimde bulunur](/cells/tr/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Pasta grafiği içeren mevcut bir e-tabloyu yükleyin

Çalışma kitabı kitabı = yeni Çalışma Kitabı(dir + "PieBar.xlsx");

//Çalışma Sayfasını 0 dizinine yükleyin

Çalışma sayfası sayfası = book.getWorksheets().get(0);

//Koleksiyondan ilk grafiği yükle

Grafik grafiği = sayfa.getCharts().get(0);

//Özelliklerine erişmeden önce grafiği hesapla

chart.calculate();

//Grafiğin ilk serisine erişim

Seri dizi = chart.getNSeries().get(0);

//ChartPoint koleksiyonu üzerinde döngü

 for(int p = 0 ; p< series.getPoints().getCount(); p++)

{

	ChartPoint point = series.getPoints().get(p);



	//Detect if ChartPoint resides on secondary plot

	System.out.println(point.isInSecondaryPlot());

}

{{< /highlight >}}
### **OleObject.ClassIdentifier özelliği eklendi**
Aspose.Cells for Java 9.0.0, bir OleObject yüklemek için uygulama davranışını belirtmek üzere kullanılabilen OleObject.ClassIdentifier özelliğini kullanıma sundu. Örneğin, bir PPT dosyası bir elektronik tabloya 2 farklı görünümle gömülebilir, yani; sunum görünümü veya slayt görünümü, oysa her iki görünüm de farklı sınıf tanımlayıcı değerlerine sahiptir.

OleObject.ClassIdentifier özelliğinin basit kullanım senaryosu aşağıdadır.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[OleObject.ClassIdentifier'ı kullanma](https://docs.aspose.com/cells/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet containing a presentation as OleObject

Workbook book = new Workbook(dir + "embeddedPresentation.xls");

//Initialize variables to store properties of OleObject

int upperLeftRow = 0;

int upperLeftColumn = 0;

int height = 0;

int width = 0;

byte[]imageData = null;

int x = 0;

int y = 0;

byte[]objData = null;

String progID = "";

int fileFormatType = 0;

String sourceFullName = "";

Boolean isDisplayAsIcon = false;

byte[]classId = null;

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
## **Eski API'ler**
### **Eski Worksheet.setBackground Yöntemi**
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
### **Silinmiş Worksheet.copyConditionalFormatting Yöntemi**
### **Silinmiş Workbook.checkWriteProtectedPassword Yöntemi**
## **Yeniden adlandırılan API'ler**
### **Workbook.removeDigitallySign Yöntemi yeniden adlandırıldı**
Workbook.removeDigitalSign yöntemi, Workbook.removeDigitalSignature olarak yeniden adlandırıldı.
