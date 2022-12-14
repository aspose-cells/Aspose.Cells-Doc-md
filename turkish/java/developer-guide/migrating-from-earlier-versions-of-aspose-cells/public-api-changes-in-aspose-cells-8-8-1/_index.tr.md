---
title: Genel API Aspose.Cells 8.8.1'deki değişiklikler
type: docs
weight: 280
url: /tr/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.8.0'dan 8.8.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yükleme için Verileri Filtrele**
Aspose.Cells for Java 8.8.1, bir şablon dosyasından çalışma kitabı oluşturulurken yüklenmesi gereken veri türünü belirtmek için kullanılabilen LoadOptions.LoadDataFilterOptions özelliğiyle birlikte LoadDataFilterOptions numaralandırmasını kullanıma sundu. Yüklenen verileri filtrelemek, özellikle LightCells API'lerini kullanırken özel amaçlar için performansı iyileştirebilir.

LoadDataFilterOptions numaralandırması aşağıdaki seçimleri sağlar.

1. E-tablodan her şeyi yüklemek için ALL.
1. E-tablodan hiçbir şey yüklemek için HİÇBİRİ.
1. CELL_BLANK, değerleri boş olan hücreleri yükler.
1. CELL_BOOL, değerleri Boolean olan hücreleri yükler.
1. CELL_DATA, değerler, formüller ve biçimlendirme dahil olmak üzere hücre verilerini yükler.
1. CELL_ERROR, değerleri hatalı olan hücreleri yükler.
1. CELL_NUMERIC, değerleri sayısal olan (Tarih ve Saat dahil) hücreleri yükler.
1. CELL_STRING, değerleri metin/dize olan hücreleri yükler.
1. CELL_VALUE yalnızca hücre değerlerini (tüm türler) yükler.
1. CHART yalnızca çizelgeleri yükler.
1. CONDITIONAL_FORMATTING yalnızca koşullu biçimlendirme kurallarını yükler.
1. DATA_VALIDATION yalnızca veri doğrulama kurallarını yükler.
1. DOCUMENT_PROPERTIES yalnızca belge özelliklerini yükler.
1. FORMULA, tanımlı adlar dahil olmak üzere formülleri yükler.
1. MERGED_AREA yalnızca birleştirilmiş hücreleri yükler.
1. PIVOT_TABLE, Pivot Tabloları yükler.
1. AYARLAR yalnızca Çalışma Kitabı ve Çalışma Sayfası ayarlarını yükler.
1. SHAPE yalnızca şekilleri yükler.
1. STYLE, hücre biçimlendirmesini yükler.
1. TABLE, Excel tablolarını/Liste Nesnelerini yükler.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Yükleme için Verileri Filtrele](/cells/tr/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Grafiği Doğrudan PDF'ye Dönüştürün**
Aspose.Cells API'ler, Chart.toPdf yöntemini kullanırken çizelgeleri PDF'ye dönüştürme olanağını zaten sağlamıştır. Bu sürümle birlikte API, söz konusu yöntemin bir OutputStream örneğini kabul edebilen başka bir aşırı yüklenmiş sürümünü ortaya çıkardı ve kullanıcıların grafiğin PDF'sini ByteArrayOutputStream örneğine kaydetmesine izin verdi.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.8.1, tüm elektronik tablo için varsayılan baskı kağıdı boyutunu ayarlamak üzere WorkbookSettings.PaperSize özelliğini kullanıma sundu. WorkbookSettings.PaperSize özelliği, en yaygın kullanılan yazdırma kağıdı türleri için önceden tanımlanmış boyutları içeren PaperSizeType numaralandırmasından bir değer kabul eder.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Shape.TextBody Özelliği Eklendi**
Aspose.Cells for Java API'in bu sürümü, şekillerdeki metnin özelliklerini değiştirmek için Shape.TextBody'yi ortaya çıkardı. Aşağıdaki kod parçacığı, bir TextBox'taki metnin gölge efektini ayarlamak için söz konusu özelliği kullanır.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Metin için Gölge Efekti Ayarlama](/cells/tr/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Çalışma Kitabının bir örneğini oluştur

Çalışma kitabı kitabı = yeni Çalışma Kitabı();

//Çalışma Kitabının ilk çalışma sayfasına erişin

Çalışma sayfası sayfası = book.getWorksheets().get(0);

//ShapeCollection'a bir Metin Kutusu ekleyin

int dizin = sayfa.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = levha.getTextBoxes().get(index);

//TextBox'ın metnini ayarla

textBox.setText("Bu metin aşağıdaki ayarlara sahiptir.\n\nMetin Efektleri > Gölge > Alttan Kaydır");

//Metin için gölge efekti ayarla

 için (int ben = 0; ben< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Worksheet.calculateFormula(dize formülü, CalculationOptions tercihleri) Yöntemi eklendi**
Aspose.Cells for Java 8.8.1, belirli bir formülü doğrudan özel seçeneklerle hesaplama yeteneği sağlayan Worksheet.calculateFormula yöntemi için başka bir aşırı yüklemeye maruz kaldı.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Özel İşlevin Doğrudan Hesaplanması](/cells/tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **GridCell.createValidation Yöntemi Eklendi**
Aspose.Cells.GridWeb, GridCell.createValidation yöntemini kullanırken doğrulama kuralını doğrudan tek bir hücreye ekleme olanağı sağlamıştır. Bahsedilen yöntem 2 parametre gerektirir. Birincisi, doğrulama türünü belirleyen GridValidationType türündeyken, ikinci parametre (isRequied) Boolean türündedir.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells.GridWeb, GridCell.removeValidation yöntemini kullanırken bir GridCell'den veri doğrulama kuralını kaldırma olanağı da sağlamıştır.
## **Eski API'ler**
### **Eski Shape.TextFrame Özelliği**
Bunun yerine Shape.TextBody.TextAlignment özelliğinin kullanılması önerilir.
