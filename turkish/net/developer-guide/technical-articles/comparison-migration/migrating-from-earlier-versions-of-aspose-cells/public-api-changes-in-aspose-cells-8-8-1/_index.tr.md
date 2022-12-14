---
title: Genel API Aspose.Cells 8.8.1'deki değişiklikler
type: docs
weight: 270
url: /tr/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.8.0'dan 8.8.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yükleme için Verileri Filtrele**
Aspose.Cells for .NET 8.8.1, bir şablon dosyasından çalışma kitabı oluşturulurken yüklenmesi gereken veri türünü belirtmek için kullanılabilen LoadOptions.LoadDataFilterOptions özelliğiyle birlikte LoadDataFilterOptions numaralandırmasını kullanıma sundu. Yüklenen verileri filtrelemek, özellikle LightCells API'lerini kullanırken özel amaçlar için performansı iyileştirebilir.

LoadDataFilterOptions numaralandırması aşağıdaki seçimleri sağlar.

1. Elektronik tablodan her şeyi yüklemek için Tümü.
1. E-tablodan hiçbir şey yüklemek için Yok.
1. CellBlank, değerleri boş olan hücreleri yükler.
1. CellBool, değerleri Boolean olan hücreleri yükler.
1. CellData, değerler, formüller ve biçimlendirme dahil olmak üzere hücre verilerini yükler.
1. CellError, değerleri hatalı olan hücreleri yükler.
1. CellNumeric, değerleri sayısal olan (Tarih ve Saat dahil) hücreleri yükler.
1. CellString, değerleri metin/dize olan hücreleri yükler.
1. CellValue yalnızca hücre değerlerini (tüm türler) yükler.
1. Grafik yalnızca çizelgeleri yükler.
1. Koşullu Biçimlendirme yalnızca koşullu biçimlendirme kurallarını yükler.
1. DataValidation yalnızca veri doğrulama kurallarını yükler.
1. DocumentProperties yalnızca belge özelliklerini yükler.
1. Formül, tanımlı adlar dahil olmak üzere formülleri yükler.
1. MergedArea yalnızca birleştirilmiş hücreleri yükler.
1. PivotTable, Pivot Tabloları yükler.
1. Ayarlar yalnızca Çalışma Kitabı ve Çalışma Sayfası ayarlarını yükler.
1. Şekil yalnızca şekilleri yükler.
1. Stil, hücre biçimlendirmesini yükler.
1. Tablo, Excel tablolarını/Liste Nesnelerini yükler.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Yükleme için Verileri Filtrele](/cells/tr/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Grafiği Doğrudan PDF'ye Dönüştürün**
Aspose.Cells API'ler, Chart.ToPdf yöntemini kullanırken çizelgeleri PDF'ye dönüştürme olanağını zaten sağlamıştır. Bu sürümle birlikte API, söz konusu yöntemin bir Stream örneğini kabul edebilen başka bir aşırı yüklenmiş sürümünü ortaya çıkardı ve kullanıcıların grafiğin PDF'sini bir MemoryStream örneğine kaydetmesine izin verdi.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **WorkbookSettings.PaperSize Özelliği Eklendi**
Aspose.Cells for .NET 8.8.1, tüm elektronik tablo için varsayılan baskı kağıdı boyutunu ayarlamak üzere WorkbookSettings.PaperSize özelliğini kullanıma sundu. WorkbookSettings.PaperSize özelliği, en yaygın kullanılan yazdırma kağıdı türleri için önceden tanımlanmış boyutları içeren PaperSizeType numaralandırmasından bir değer kabul eder.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Shape.TextBody Özelliği Eklendi**
Aspose.Cells for .NET API'in bu sürümü, şekillerdeki metnin özelliklerini değiştirmek için Shape.TextBody'yi ortaya çıkardı. Aşağıdaki kod parçacığı, bir TextBox'taki metnin gölge efektini ayarlamak için söz konusu özelliği kullanır.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Metin için Gölge Efekti Ayarlama](/cells/tr/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 //Çalışma Kitabının bir örneğini oluştur

var kitap = yeni Çalışma Kitabı();

//Çalışma Kitabının ilk çalışma sayfasına erişin

var sayfası = kitap.Çalışma Sayfaları[0];

//ShapeCollection'a bir Metin Kutusu ekleyin

var textBox = levha.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//TextBox'ın metnini ayarla

textBox.Text = "Bu metin aşağıdaki ayarlara sahiptir.\n\nMetin Efektleri > Gölge > Alttan Kaydır";

//Metin için gölge efekti ayarla

 için (int ben = 0; ben< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Worksheet.CalculateFormula(dize formülü, CalculationOptions opts) Yöntemi Eklendi**
Aspose.Cells for .NET 8.8.1, belirli bir formülü doğrudan özel seçeneklerle hesaplama yeteneği sağlayan CalculateFormula yöntemi için başka bir aşırı yüklemeye maruz kaldı.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Özel İşlevin Doğrudan Hesaplanması](/cells/tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **GridCell.CreateValidation Yöntemi Eklendi**
Aspose.Cells.GridWeb, GridCell.CreateValidation yöntemini kullanırken doğrulama kuralını doğrudan tek bir hücreye ekleme olanağı sağlamıştır. Bahsedilen yöntem 2 parametre gerektirir. Birincisi, doğrulama türünü belirleyen GridValidationType türündeyken, ikinci parametre (isRequied) Boolean türündedir.



**C#**

{{< highlight "csharp" >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **GridCell.RemoveValidation Yöntemi Eklendi**
Aspose.Cells.GridWeb, GridCell.RemoveValidation yöntemini kullanırken bir GridCell'den veri doğrulama kuralını kaldırma olanağı da sağlamıştır.
## **Eski API'ler**
### **Eski Shape.TextFrame Özelliği**
Bunun yerine Shape.TextBody.TextAlignment özelliğinin kullanılması önerilir.
