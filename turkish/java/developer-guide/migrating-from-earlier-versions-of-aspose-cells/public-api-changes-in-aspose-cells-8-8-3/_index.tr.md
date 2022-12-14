---
title: Genel API Aspose.Cells 8.8.3'teki değişiklikler
type: docs
weight: 300
url: /tr/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.8.2 sürümünden 8.8.3 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **ActiveX Denetimleri için Destek**
Aspose.Cells for Java 8.8.3, ShapeCollection'a bir ActiveX denetimi eklemeye izin veren addActiveXControl yöntemini kullanıma sundu. Yukarıda belirtilen yöntem, kontrol tipini, kontrolün yerleştirileceği yeri ve kontrolün boyutunu belirtmek için 7 parametre gerektirir. Tip, aşağıdaki olası değerlerle ControlType numaralandırması kullanılarak belirtilebilir.

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

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Çalışma Sayfasına ActiveX Denetimleri Ekleme](/cells/tr/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.8.3, aşağıda gösterildiği gibi yeni kullanıma sunulan LoadOptions.setPaperSize yöntemini kullanırken varsayılan yazıcının ayarından varsayılan baskı kağıdı boyutunun ayarlanmasına izin verir. Lütfen yukarıda belirtilen yöntemin giriş parametresinin, önceden tanımlanmış kağıt boyutlarını içeren PaperSizeType numaralandırmasından gelen değer olduğunu unutmayın.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Elektronik Tabloları Belirtilen Kağıt Boyutuyla Yükleyin](/cells/tr/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Cell.getCharacters(flag) Yöntemi Eklendi**
Aspose.Cells API'leri, Cell.getCharacters yöntemini kullanarak karakter nesnelerini FontSetting dizisi biçiminde almaya izin verir. Bu sürümle birlikte, Aspose.Cells for Java API, Cell.getCharacters'ın Boolean'ı parametre olarak kabul edebilen aşırı yüklenmiş bir sürümünü kullanıma sunmuştur; bu, hücre bir ListObject'in parçasıysa tablo stilinin hücreye uygulanması gerekip gerekmediğini belirtir.

**Java**

{{< highlight "csharp" >}}

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

FontSetting[]characters = cell.getCharacters(true);

{{< /highlight >}}
### **OleObject.AutoLoad Özelliği Eklendi**
Aspose.Cells for Java 8.8.3, temel alınan nesnenin içeriği/verileri değiştirilmişse OleObject görüntüsünün yenilenmesine izin veren OleObject.AutoLoad özelliğini ortaya çıkardı. Yukarıda belirtilen özellik, true olarak ayarlandığında, sonuç elektronik tablosu yüklendiğinde Excel uygulamasını OleObject'in görüntüsünü yenilemeye zorlar.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[OleObjects'i Otomatik Olarak Yenile](/cells/tr/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
### **HTMLLoadOptions.SupportDivTag Özelliği eklendi**
Aspose.Cells for Java 8.8.3, Aspose.Cells nesne modelinde HTML dosyaları/snippet'i yüklerken TD etiketlerine gömülü DIV etiketlerinin ayrıştırılmasına izin veren HTMLLoadOptions.SupportDivTag özelliğini kullanıma sundu. Boole tipi özelliğinin varsayılan değeri false'tur.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[HTML Yüklerken İç DIV Etiketlerini Destekleyin](/cells/tr/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
### **HtmlSaveOptions.ExportGridLines Özelliği Eklendi**
Aspose.Cells for Java 8.8.3, elektronik tabloyu HTML formatına dışa aktarırken ızgara çizgilerini oluşturmaya izin veren HtmlSaveOptions.ExportGridLines özelliğini ortaya çıkardı. Boole türü özelliğinin varsayılan değeri false'tur, ancak true olarak ayarlandığında API, kullanılabilir veri aralığı için ızgara çizgilerini HTML biçiminde işler.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Izgara Çizgilerini HTML'ye Dönüştür](/cells/tr/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **ListObject.Comment Özelliği Eklendi**
Aspose.Cells API'ler artık bir ListObject örneği için yorumların alınmasına ve ayarlanmasına izin veriyor. Yukarıda belirtilen özelliği sağlamak için Aspose.Cells API'leri ListObject.Comment özelliğini kullanıma sunmuştur.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[ListObjects için Yorum Ekleme](/cells/tr/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
## **Kaldırılan API'ler**
### **Workbook.decrypt Yöntemi Kaldırıldı**
Söz konusu mülk bir süre önce eski olarak işaretlendi. Bu sürüm, onu genel kullanımdan tamamen kaldırdı API. Aynı hedefe ulaşmak için WorkbookSettings.Password özelliğinin null olarak ayarlanması tavsiye edilir.
