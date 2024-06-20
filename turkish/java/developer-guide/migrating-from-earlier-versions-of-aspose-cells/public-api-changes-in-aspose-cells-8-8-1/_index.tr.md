---
title: Aspose.Cells 8.8.1 da Genel API Değişiklikleri
type: docs
weight: 280
url: /tr/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Bu belge, 8.8.0'den 8.8.1'e Aspose.Cells API'deki değişiklikleri modül/uygulama geliştiricilerin ilgisini çekebilecek herhangi bir değişikliği içermektedir. Yeni ve güncellenmiş genel yöntemler, eklendi ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içermektedir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Yükleme için Verileri Filtrele**
Aspose.Cells for Java 8.8.1, LoadDataFilterOptions numaratörünü ve LoadOptions.LoadDataFilterOptions özelliğini sergiledi. Bu, bir şablon dosyasından çalışma kitabını oluşturulurken yüklenmesi gereken veri türünü belirtmek için kullanılabilir. Yüklenmiş verilerin filtrelenmesi özellikle LightCells API'lerini kullanırken performansı özel amaçlar için artırabilir.

LoadDataFilterOptions numaratörü aşağıdaki seçenekleri sağlar.

1. SPREADSHEET'ten her şeyi yüklemek için TÜM.
1. SPREADSHEET'ten hiçbir şey yüklemek için HİÇBİR.
1. BLANK_CELL, değerleri boş olan hücreleri yükler.
1. BOOL_CELL, değerleri Boolean olan hücreleri yükler.
1. DATA_CELL, değerleri, formülleri ve biçimlendirmeyi içeren hücre verilerini yükler.
1. ERROR_CELL, değerleri hata olan hücreleri yükler.
1. NUMERIC_CELL, değerleri sayısal olan hücreleri yükler (Tarih ve Saat dahil).
1. STRING_CELL, değerleri metin/dize olan hücreleri yükler.
1. VALUE_CELL, yalnızca hücre değerlerini yükler (tüm türler).
1. GRAFİK, yalnızca grafikleri yükler.
1. KOŞULLU_FORMAT, yalnızca koşullu biçimlendirme kurallarını yükler.
1. VERI_DOGRULAMA, yalnızca veri doğrulama kurallarını yükler.
1. BELGE_ÖZELLIKLERİ, yalnızca belge özelliklerini yükler.
1. FORMÜL, tanımlı adları içeren formülleri yükler.
1. BİRLEŞTİRİLMİŞ_ALAN, yalnızca birleştirilmiş hücreleri yükler.
1. PIVOT_TABLO, Pivot Tabloları yükler.
1. AYARLAR, yalnızca Çalışma Kitabı ve Çalışsayfa ayarlarını yükler.
1. ŞEKİL, yalnızca şekilleri yükler.
1. STIL, hücre biçimlendirmesini yükler.
1. TABLO, Excel tablolarını/Liste Nesnelerini yükler.

{{% alert color="primary" %}} 

Bu özelliğin daha fazla ayrıntısı için [Yükleme için Veri Filtreleme](/cells/tr/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/) başlıklı ayrıntılı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Doğrudan Grafikleri PDF'e Dönüştür**
Aspose.Cells API'leri zaten Chart.toPdf yöntemini kullanarak grafikleri PDF'ye dönüştürme olanağı sağlamıştır. Bu sürümle birlikte, API, anılan yöntemin başka bir aşırı yüklenmiş versiyonunu sergilemiştir. Bu sayede kullanıcılar, grafiklerin PDF'ini ByteArrayOutputStream örneğinde kaydedebilirler.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **WorkbookSettings.PaperSize Özelliği Eklendi**
Aspose.Cells for Java 8.8.1, tüm çalışma kitabı için varsayılan baskı kağıdı boyutunu ayarlamak için WorkbookSettings.PaperSize özelliğini sergiledi. WorkbookSettings.PaperSize özelliği, en yaygın kullanılan baskı kağıdı tipleri için önceden tanımlanmış boyutları içeren PaperSizeType numaratöründen bir değer alır.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Shape.TextBody Özelliği Eklendi**
Aspose.Cells for Java API'nin bu sürümü, metin şekillerinde metnin özelliklerini manipüle etmek için Shape.TextBody'i açığa çıkardı. Aşağıdaki kod parçası, belirtilen özelliği kullanarak bir TextBox'taki metnin gölge etkisini ayarlamak için kullanılır.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Metin Gölge Etkisi Ayarlama](/cells/tr/java/setting-shadow-of-text-effects-of-shape-or-textbox/) başlıklı detaylı makaleyi inceleyin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Worksheet.calculateFormula(string formula, CalculationOptions opts) Yöntemi Eklendi**
Aspose.Cells for Java 8.8.1, hesap formülünü özel seçeneklerle doğrudan hesaplama yeteneği sağlayan Worksheet.calculateFormula yönteminin başka bir yüklemesini açığa çıkardı.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Özel Fonksiyonun Doğrudan Hesaplanması](/cells/tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/) başlıklı detaylı makaleyi inceleyin.

{{% /alert %}} 
### **GridCell.createValidation Yöntemi Eklendi**
Aspose.Cells.GridWeb, GridCell.createValidation yöntemini kullanarak tek bir hücreye doğrudan doğrulama kuralı eklemeyi sağladı. Söz konusu yöntem 2 parametre gerektirir. İlk parametre, doğrulama türünü belirleyen GridValidationType türündedir, ikinci parametre (isRequied) ise Boolean türündedir.

**Java**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **GridCell.removeValidation Yöntemi Eklendi**
Aspose.Cells.GridWeb, GridCell.removeValidation yöntemi kullanılarak bir GridCell'den veri doğrulama kuralını kaldırma yeteneği de sağladı.
## **Eskimiş API'lar**
### **Eskimiş Shape.TextFrame Özelliği**
Bu yerine Shape.TextBody.TextAlignment özelliğinin kullanılması tavsiye edilir.
