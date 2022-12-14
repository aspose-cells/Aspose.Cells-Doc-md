---
title: Genel API Aspose.Cells 8.8.3'teki değişiklikler
type: docs
weight: 290
url: /tr/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.8.2 sürümünden 8.8.3 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **ActiveX Denetimleri için Destek**
Aspose.Cells for .NET 8.8.3, ShapeCollection'a bir ActiveX denetimi eklemeye izin veren AddActiveXControl yöntemini kullanıma sundu. Yukarıda belirtilen yöntem, kontrol tipini, kontrolün yerleştirileceği yeri ve kontrolün boyutunu belirtmek için 7 parametre gerektirir. Tip, aşağıdaki olası değerlerle ControlType numaralandırması kullanılarak belirtilebilir.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Bilinmeyen

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Çalışma Sayfasına ActiveX Denetimleri Ekleme](/cells/tr/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **LoadOptions.SetPaperSize Yöntemi Eklendi**
Aspose.Cells for .NET 8.8.3, aşağıda gösterildiği gibi yeni kullanıma sunulan LoadOptions.SetPaperSize yöntemini kullanırken varsayılan yazıcının ayarından varsayılan baskı kağıdı boyutunun ayarlanmasına izin verir. Lütfen yukarıda belirtilen yöntemin giriş parametresinin, önceden tanımlanmış kağıt boyutlarını içeren PaperSizeType numaralandırmasından gelen değer olduğunu unutmayın.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Elektronik Tabloları Belirtilen Kağıt Boyutuyla Yükleyin](/cells/tr/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Cell.GetCharacters(flag) Yöntemi Eklendi**
Aspose.Cells API'leri, Cell.GetCharacters yöntemini kullanarak karakter nesnelerini FontSetting dizisi biçiminde almaya izin verir. Bu sürümle birlikte, Aspose.Cells for .NET API, Cell.GetCharacters'ın Boolean'ı parametre olarak kabul edebilen aşırı yüklenmiş bir sürümünü kullanıma sunmuştur; bu, hücre bir ListObject'in parçasıysa tablo stilinin hücreye uygulanması gerekip gerekmediğini gösterir.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **OleObject.AutoLoad Özelliği Eklendi**
Aspose.Cells for .NET 8.8.3, temel alınan nesnenin içeriği/verileri değiştirilmişse OleObject görüntüsünün yenilenmesine izin veren OleObject.AutoLoad özelliğini ortaya çıkardı. Yukarıda belirtilen özellik, true olarak ayarlandığında, sonuç elektronik tablosu yüklendiğinde Excel uygulamasını OleObject'in görüntüsünü yenilemeye zorlar.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[OleObjects'i Otomatik Olarak Yenile](/cells/tr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **HTMLLoadOptions.SupportDivTag Özelliği eklendi**
Aspose.Cells for .NET 8.8.3, Aspose.Cells nesne modelinde HTML dosyaları/snippet'i yüklerken TD etiketlerine gömülü DIV etiketlerinin ayrıştırılmasına izin veren HTMLLoadOptions.SupportDivTag özelliğini kullanıma sundu. Boole tipi özelliğinin varsayılan değeri false'tur.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[HTML Yüklerken İç DIV Etiketlerini Destekleyin](/cells/tr/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **HtmlSaveOptions.ExportGridLines Özelliği Eklendi**
Aspose.Cells for .NET 8.8.3, elektronik tabloyu HTML formatına dışa aktarırken ızgara çizgilerini oluşturmaya izin veren HtmlSaveOptions.ExportGridLines özelliğini ortaya çıkardı. Boole türü özelliğinin varsayılan değeri false'tur, ancak true olarak ayarlandığında API, kullanılabilir veri aralığı için ızgara çizgilerini HTML biçiminde işler.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Izgara Çizgilerini HTML'ye Dönüştür](/cells/tr/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **ListObject.Comment Özelliği Eklendi**
Aspose.Cells API'ler artık bir ListObject örneği için yorumların alınmasına ve ayarlanmasına izin veriyor. Yukarıda belirtilen özelliği sağlamak için Aspose.Cells API'leri ListObject.Comment özelliğini kullanıma sunmuştur.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[ListObjects için Yorum Ekleme](/cells/tr/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **GridWeb.SessionStorePath Özelliği Eklendi**
Aspose.Cells.GridWeb for .NET 8.8.3, Oturum Modu ViewState olduğunda oturum deposu yolunu almaya veya ayarlamaya izin veren SessionStorePath özelliğini kullanıma sundu. Yukarıda belirtilen özellik, geçerli web uygulaması Temel Dizinine ilişkin göreli yolu alır veya ayarlar.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Geçici Oturum Dosyaları İçin Yol Belirtin](/cells/tr/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.
## **Kaldırılan API'ler**
### **Workbook.Decrypt Yöntemi Kaldırıldı**
Söz konusu mülk bir süre önce eski olarak işaretlendi. Bu sürüm, onu genel kullanımdan tamamen kaldırdı API. Aynı hedefe ulaşmak için WorkbookSettings.Password özelliğinin null olarak ayarlanması tavsiye edilir.
