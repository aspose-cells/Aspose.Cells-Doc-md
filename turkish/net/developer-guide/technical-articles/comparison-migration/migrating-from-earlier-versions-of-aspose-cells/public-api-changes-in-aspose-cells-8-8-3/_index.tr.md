---
title: Aspose.Cells 8.8.3 te Genel API Değişiklikleri
type: docs
weight: 290
url: /tr/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için Aspose.Cells API'sinde 8.8.2'den 8.8.3'e yapılan değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells arkasındaki davranışlardaki değişikliklerin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **ActiveX Kontrollerini Destekleme**
Aspose.Cells for .NET 8.8.3, ShapeCollection'a ActiveX kontrolü eklemek için kullanılan AddActiveXControl yöntemini ortaya çıkardı. Yukarıda belirtilen yöntem, kontrol türünü, kontrolü yerleştirmek için konumu ve kontrolün boyutunu belirlemek için 7 parametreyi gerektirir. Tür, ControlType numaralandırmasını kullanarak belirtilebilir ve şu olası değerlere sahiptir.

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
1. ControlType.Unknown

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [AktivX Kontrollerini Çalışma Tablosuna Ekleme](/cells/tr/net/aspose-cells-kullanarak-activex-kontrollerini-ekleme/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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


### **LoadOptions.SetPaperSize Method Eklendi**
Aspose.Cells for .NET 8.8.3, varsayılan yazıcı ayarlarında belirtilen kağıt boyutunu ayarlamak için yeni ortaya çıkarılmış LoadOptions.SetPaperSize yöntemini kullanmaya izin verir. Lütfen dikkat edin, söz konusu yönteme gelen giriş parametresi, önceden tanımlanmış kağıt boyutlarını içeren PaperSizeType numaralandırmasından gelen değeri içerir.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Belirli Kağıt Boyutuyla Çalışma Kitaplarını Yükleme](/cells/tr/net/belirtilmis-printer-kağıt-boyutu-ile-calisma-kitaplarini-yukleme/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Hücre.GetKarakterler(bayrak) Yöntemi Eklendi**
Aspose.Cells API'leri, Hücre.GetKarakterler yöntemini kullanarak Karakter nesnelerini FontSetting dizisi formunda almayı sağlar. Bu sürümde, Aspose.Cells for .NET API, bir ListObject'un bir parçasıysa hücreye tablo stili uygulanması gerekip gerekmediğini belirten Boolean'ı parametre olarak kabul edebilen Hücre.GetKarakterler'in aşırı yüklenmiş bir sürümünü ortaya çıkardı.

**C#**

{{< highlight csharp >}}

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


### **Added OleObject.AutoLoad Property**
Aspose.Cells for .NET 8.8.3, OleObject.AutoLoad özelliğini ortaya çıkardı. Bu özellik, temel nesnenin içeriğinin/değerinin değiştiğinde OleObject'in görüntüsünü yenilemeye izin verir. Bahsedilen özellik true olarak ayarlandığında, sonuçlanan elektronik tablonun yüklenmesi sırasında Excel uygulamasını OleObject'in görüntüsünü yenilemeye zorlar.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla detay için, [Aspose.Cells ile Microsoft Excel Üzerinden OleObjects'u Otomatik Yenileme](/cells/tr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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


### **Added HTMLLoadOptions.SupportDivTag Property**
Aspose.Cells for .NET 8.8.3, HTMLLoadOptions.SupportDivTag özelliğini ortaya çıkardı. Bu özellik, Aspose.Cells nesne modelindeki HTML dosyalarını/snippet'ları yüklerken TD etiketlerine gömülü DIV etiketlerini ayrıştırmaya izin verir. Boolean türündeki özellik, varsayılan olarak false değerine sahiptir.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla detay için, [HTML Yüklerken Gömülü DIV Etiketlerini Destekleme](/cells/tr/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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


### **Added HtmlSaveOptions.ExportGridLines Property**
Aspose.Cells for .NET 8.8.3, HtmlSaveOptions.ExportGridLines özelliğini ortaya çıkardı. Bu özellik, elektronik tabloyu HTML biçimine dışa aktarırken ızgara çizgilerini renderlamaya izin verir. Boolean türündeki özellik, varsayılan olarak false değere sahiptir, ancak true olarak ayarlandığında API, mevcut veri aralığı için ızgara çizgilerini HTML biçimine renderlar.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla detay için, [HTML'ye Izgara Çizgilerini Renderlama](/cells/tr/net/export-excel-to-html-with-gridlines/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Added ListObject.Comment Property**
Aspose.Cells API'leri artık bir ListObject'in yorumlarını alıp ayarlamayı sağlar. Yukarıda bahsedilen özelliği sağlamak için, Aspose.Cells API'leri ListObject.Comment özelliğini açığa çıkardı.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla detay için, [ListObjects için Yorum Ekleme](/cells/tr/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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
.NET için Aspose.Cells.GridWeb 8.8.3, ViewState Oturum Modu olduğunda oturum saklama yolunu alıp ayarlamaya izin veren SessionStorePath özelliğini ortaya çıkardı. Bahsedilen özellik, mevcut web uygulama Taban Dizini'ne göre göreceli yol alır veya ayarlar.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla detay için, [Geçici Oturum Dosyaları İçin Yol Belirtme](/cells/tr/net/specify-the-path-where-gridweb-stores-temporary-session-files/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.
## **Removed APIs**
### **Workbook.Decrypt Yöntemi Kaldırıldı**
Söz konusu özellik bir süre önce eski olarak işaretlendi. Bu sürümde, söz konusu özelliği tamamen halka açık API'den kaldırdı. Aynı hedefe ulaşmak için WorkbookSettings.Password özelliğini null olarak ayarlamak tavsiye edilir.
