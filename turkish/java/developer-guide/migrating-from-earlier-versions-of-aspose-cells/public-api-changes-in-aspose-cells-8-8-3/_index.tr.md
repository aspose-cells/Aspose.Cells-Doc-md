---
title: Aspose.Cells 8.8.3 te Genel API Değişiklikleri
type: docs
weight: 300
url: /tr/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için Aspose.Cells API'sinde 8.8.2'den 8.8.3'e yapılan değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells arkasındaki davranışlardaki değişikliklerin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **ActiveX Kontrollerini Destekleme**
Aspose.Cells for Java 8.8.3, ShapeCollection'e bir ActiveX kontrolü eklemeye izin veren addActiveXControl yöntemini açığa çıkardı. Söz konusu yöntem, kontrol türünü, kontrolü yerleştirmek için konumu ve kontrolün boyutunu belirtmek için 7 parametreyi gerektirir. Tür, ControlType numaralandırmasını, aşağıdaki olası değerleri kullanarak belirtilebilir.

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Worksheet'e ActiveX Kontrolleri Ekleme](/cells/tr/java/add-activex-controls-using-aspose-cells/) başlıklı detaylı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **LoadOptions.setPaperSize Yöntemi Eklendi**
Aspose.Cells for Java 8.8.3, varsayılan baskı kağıdı boyutunu varsayılan yazıcının ayarlarından ayarlamak için yeni ortaya çıkarılan LoadOptions.setPaperSize yöntemine izin verir. Lütfen dikkat, söz konusu yönteme gelen giriş parametresi, önceden tanımlanmış kağıt boyutlarını içeren PaperSizeType numaralandırmasından gelen değerdir.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Belirli Kağıt Boyutu ile Elektronik Tablo Yükleme](/cells/tr/java/load-workbook-with-specified-printer-paper-size/) başlıklı detaylı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Added Cell.getCharacters(flag) Method**
Aspose.Cells API'leri, Cell.getCharacters yöntemini kullanarak FontSetting dizisi olarak karakter nesnelerini almayı sağlar. Bu sürümle birlikte, Aspose.Cells for Java API, hücrenin bir ListObject'un parçası olup olmadığını gösteren bir Boolean parametresini kabul edebilen Cell.getCharacters'ın aşırı yüklenmiş bir sürümünü ortaya çıkardı.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **Added OleObject.AutoLoad Property**
Aspose.Cells for Java 8.8.3, OleObject.AutoLoad özelliğini açığa çıkardı; bu özellik, temel nesnenin içeriği / verileri değiştiğinde OleObject'in görüntüsünü yenilemeyi sağlar. Söz konusu özellik true olarak ayarlandığında, API, sonuçlandırma elek tablosu yüklendiğinde OleObject'in görüntüsünü yenilemeye zorlar.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için [OleObjects Otomatik Yenile] başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **Added HTMLLoadOptions.SupportDivTag Property**
Aspose.Cells for Java 8.8.3, HTMLLoadOptions.SupportDivTag özelliğini açığa çıkardı; bu özellik, Aspose.Cells nesne modelindeki HTML dosyalarını/snippet'leri yüklerken TD etiketlerine gömülü DIV etiketlerini ayrıştırmayı sağlar. Boolean tipi özelliğin varsayılan değeri false'dur.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için [HTML Yüklenirken İçe Gömülü DIV Etiketlerini Destekleme] başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Added HtmlSaveOptions.ExportGridLines Property**
Aspose.Cells for Java 8.8.3, HtmlSaveOptions.ExportGridLines özelliğini açığa çıkardı; bu özellik, elek tablosunun HTML biçimine dışa aktarılırken ızgaraların görüntülenmesine izin verir. Boolean tipi özelliğin varsayılan değeri false'dur, ancak true olarak ayarlandığında API, HTML biçiminde mevcut veri aralığı için ızgaraları oluşturur.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için [HTML'ye Izgara Çizgilerini Yansıtma] başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Added ListObject.Comment Property**
Aspose.Cells API'leri artık bir ListObject'in yorumlarını alıp ayarlamayı sağlar. Yukarıda bahsedilen özelliği sağlamak için, Aspose.Cells API'leri ListObject.Comment özelliğini açığa çıkardı.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için [ListObjectlere Yorumlar Ekleme] başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **Removed APIs**
### **Removed Workbook.decrypt Method**
Söz konusu özellik bir süre önce eski olarak işaretlendi. Bu sürümde, söz konusu özelliği tamamen halka açık API'den kaldırdı. Aynı hedefe ulaşmak için WorkbookSettings.Password özelliğini null olarak ayarlamak tavsiye edilir.
