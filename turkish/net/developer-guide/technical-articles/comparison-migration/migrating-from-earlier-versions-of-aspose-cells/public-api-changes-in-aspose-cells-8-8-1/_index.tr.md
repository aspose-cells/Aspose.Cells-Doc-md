---
title: Aspose.Cells 8.8.1 da Genel API Değişiklikleri
type: docs
weight: 270
url: /tr/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Bu belge, 8.8.0'den 8.8.1'e Aspose.Cells API'deki değişiklikleri modül/uygulama geliştiricilerin ilgisini çekebilecek herhangi bir değişikliği içermektedir. Yeni ve güncellenmiş genel yöntemler, eklendi ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içermektedir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Yükleme için Verileri Filtrele**
Aspose.Cells for .NET 8.8.1, LoadDataFilterOptions numaralandırmasını ve LoadOptions.LoadDataFilterOptions özelliğini serbest bıraktı, bu özellik, bir şablon dosyasından çalışma kitabı oluşturulurken yüklenmesi gereken veri türünü belirtmek için kullanılabilir. Yüklenen verileri filtrelemek, özellikle LightCells API’leri kullanırken özel amaçlar için performansı iyileştirebilir.

LoadDataFilterOptions numaratörü aşağıdaki seçenekleri sağlar.

1. Sayfa içeriğinden her şeyi yüklemek için All.
1. Sayfa içeriğinden hiçbir şeyi yüklememek için None.
1. Hücrelerin değeri boş olanlarını yükler için CellBlank.
1. Boolean değerlere sahip hücreleri yükler için CellBool.
1. Değerler, formüller ve biçimlendirmeleri içeren hücre verilerini yükler için CellData.
1. Hücre değeri hata olanları yükler için CellError.
1. Sayısal değerlere (Tarih ve Zaman dahil) sahip hücreleri yükler için CellNumeric.
1. Metin/dizi olan hücreleri yükler için CellString.
1. Yalnızca hücre değerlerini (tüm tipleri) yükler için CellValue.
1. Yalnızca grafikleri yükler için Chart.
1. Yalnızca koşullu biçimlendirme kurallarını yükler için ConditionalFormatting.
1. Yalnızca veri doğrulama kurallarını yükler için DataValidation.
1. Yalnızca belge özelliklerini yükler için DocumentProperties.
1. Tanımlanmış adları içeren formülleri yükler için Formula.
1. Yalnızca birleştirilmiş hücreleri yükler için MergedArea.
1. Pivot Tablolarını yükler için PivotTable.
1. Yalnızca çalışma kitabı ve çalışma sayfası ayarlarını yükler için Settings.
1. Yalnızca şekilleri yükler için Shape.
1. Hücre biçimlendirmesini yükler için Style.
1. Excel tablolarını/Liste Nesnelerini yükler için Table.

{{% alert color="primary" %}} 

Bu özelliğin daha fazla detayını görmek için, [Yüklenirken Veri Filtreleme](/cells/tr/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/) üzerindeki ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Doğrudan Grafikleri PDF'e Dönüştür**
Aspose.Cells API'leri zaten Chart.ToPdf yöntemini kullanırken grafikleri PDF'e dönüştürme olanağı sağlamıştır. Bu sürümle birlikte, API başka bir yüklenmiş versiyonu serbest bırakmıştır ki bu versiyon Stream örneğini kabul edebilecek ve kullanıcıların grafik PDF'lerini MemoryStream örneğinde kaydetmelerine olanak sağlayacaktır.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.8.1, WorkbookSettings.PaperSize özelliğini serbest bırakmıştır, bu özellik, tüm elektronik tablonun varsayılan yazdırma kağıdı boyutunu ayarlamak için kabul eder. WorkbookSettings.PaperSize özelliği, en yaygın kullanılan yazdırma kağıtları türleri için önceden tanımlanmış boyutlar içeren PaperSizeType numaralandırmasından bir değeri kabul eder.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Shape.TextBody Özelliği Eklendi**
Aspose.Cells for .NET API'nin bu sürümü, metinlerin şekillerin içindeki özelliklerini manipüle etmek için Shape.TextBody'i ortaya çıkardı. Aşağıdaki kod parçası, belirtilen özelliği kullanarak TextBox'ın içindeki metnin gölge efektini ayarlamak için kullanılır.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Metin İçin Gölge Efektini Ayarlama](/cells/tr/net/metin-golge-efekti-ayarlama/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Worksheet.CalculateFormula(string formula, CalculationOptions opts) Method Eklendi**
Aspose.Cells for .NET 8.8.1, CalculateFormula yöntemi için başka bir aşırı yüklemeyi ortaya çıkardı, bu da belirli seçeneklerle doğrudan belirli bir formülü hesaplama yeteneği sağlar.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Özel Fonksiyonun Doğrudan Hesaplanması](/cells/tr/net/calculator-custom-fonksiyonun-calisildigi-sayfa-icerisine-yazmadan-direkt-hesaplama/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 
### **GridCell.CreateValidation Method Eklendi**
Aspose.Cells.GridWeb, GridCell.CreateValidation yöntemini kullanırken tek bir hücreye doğrudan doğrulama kuralı eklemek için yetenek sağladı. Söz konusu yöntem 2 parametre gerektirir. İlk parametre, doğrulama türünü belirleyen GridValidationType türündedir, ikinci parametre (isRequied) Boolean türündedir.



**C#**

{{< highlight csharp >}}

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


### **GridCell.RemoveValidation Method Eklendi**
Aspose.Cells.GridWeb ayrıca GridCell.RemoveValidation yöntemini kullanarak bir GridCell'den veri doğrulama kuralını kaldırma yeteneği sağladı.
## **Eskimiş API'lar**
### **Eskimiş Shape.TextFrame Özelliği**
Bu yerine Shape.TextBody.TextAlignment özelliğinin kullanılması tavsiye edilir.
