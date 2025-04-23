---
title: Aspose.Cells 17.1.0 da Genel API Değişiklikleri
type: docs
weight: 370
url: /tr/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 16.12.0'den 17.1.0'a Aspose.Cells API'sindeki değişiklikleri açıklar ve modül/uygulama geliştiricileri için ilgi çekebilecek değişiklikleri içerir. Yalnızca yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. değil, aynı zamanda Aspose.Cells'in arka planda davranışında herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Excel 2016 Grafikleri için Destek**
Aspose.Cells API'leri, ChartType numaralandırmasını geliştirerek birkaç Excel 2016 grafiği için destek ekledi. Aspose.Cells 17.1.0 sürümüyle şu yeni alanlar eklenmiştir.

- ChartType.BoxWhisker: Seri kutu ve balyoz olarak düzenlenmiştir.
- ChartType.Funnel: Seri huni olarak düzenlenmiştir.
- ChartType.ParetoLine: Seri pareto çizgileri olarak düzenlenmiştir.
- ChartType.Sunburst: Seri güneş patlaması olarak düzenlenmiştir.
- ChartType.Treemap: Seri tre haritası olarak düzenlenmiştir.
- ChartType.Waterfall: Seri şelale olarak düzenlenmiştir.
- ChartType.Histogram: Seri histogram olarak düzenlenmiştir.

{{% alert color="primary" %}} 

Detaylı makale için [Excel 2016 Grafik Türlerini Okuma](/cells/tr/net/read-and-manipulate-excel-2016-charts/) adresini ziyaret edin

{{% /alert %}} 
### **LoadFilter.LoadDataFilterOptions Özelliği için Setter eklendi**
Aspose.Cells 17.1.0, LoadFilter.LoadDataFilterOptions özelliği için setter ekledi ve m_LoadDataFilterOptions örnek değişkenini değiştirmek üzere LoadFilter sınıfının kendi uygulamasında LoadDataFilterOptions özelliğini değiştirebilecek olan kullanıcılar, yük şablonu dosyalarının davranışını değiştirebilir.

İşte basit bir kullanım senaryosu.

{{% alert color="primary" %}} 

[Özel Şablon Filtreleme](/cells/tr/net/filter-objects-while-loading-workbook-or-worksheet/) konusundaki detaylı makaleyi kontrol edin

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **Added CellsHelper.SignificantDigits Özelliği**
Aspose.Cells 17.1.0, CellsHelper sınıfından SignificantDigits özelliğini açığa çıkardı ve elektronik tablodaki sayısal değerler için anlamlı basamak sayısını almak veya ayarlamak için kullanılmasını sağlar. CellsHelper.SignificantDigits özelliğinin varsayılan değeri 17'dir ve yalnızca sonucun XLSX dosya formatında depolanması gerektiğinde geçerlidir.

CellsHelper.SignificantDigits özelliğinin kullanımını gösteren basit bir senaryo burada.

{{% alert color="primary" %}} 

[Depolanan Excel Dosyasında Belirtilecek Önemli Basamak Sayısını Ayarlama](/cells/tr/net/specifying-significant-digits-to-be-stored-in-excel-file/) konusundaki detaylı makaleyi kontrol edin

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Added GlowEffect.Color Özelliği**
Aspose.Cells 17.1.0, GlowEffect.Color özelliğini eklediği ve ışıltı efektinin rengini almak için kullanılabileceği.

Işıl Işıl Efektin Rengini Okuma](/cells/tr/java/read-color-of-the-shape-s-glow-effect/) hakkındaki detaylı makaleye göz atın

{{% alert color="primary" %}} 

[Şeklin Işıltı Rengini Okuma](/cells/tr/net/read-color-of-shape-s-glow-effect/) konusundaki detaylı makaleyi kontrol edin

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **Added PageSetup.PaperWidth ve PaperHeight Özellikleri**
Aspose.Cells 17.1.0, PageSetup sınıfı için PaperWidth ve PaperHeight özelliklerini açığa çıkardı. PageSetup.PaperWidth ve PageSetup.PaperHeight özellikleri, sayfa yönlendirmesini dikkate alarak inç biriminde kağıt genişliğini ve yüksekliğini temsil eden double türündendir.

{{% alert color="primary" %}} 

[Çalışma Sayfası Kağıt Boyutunu Alma](/cells/tr/net/get-paper-width-and-height-of-page-setup-of-worksheet/) konusundaki detaylı makaleyi kontrol edin

{{% /alert %}} 
### **Added WorkbookSettings.CheckCustomNumberFormat Özelliği**
Aspose.Cells 17.1.0, WorkbookSettings sınıfına CheckCustomNumberFormat özelliğini ekledi. CheckCustomNumberFormat, Style.Custom özelliğinin uygun şekilde ayarlanıp ayarlanmadığını kontrol etmede kullanışlıdır. Eğer Style.Custom özelliği yanlış şekilde ayarlanmışsa yani; değer geçerli bir desene karşılık gelmiyorsa, Aspose.Cells API'ları uygun mesajla CellsException fırlatacaktır.

{{% alert color="primary" %}} 

[Özel Formatı Doğrulama](/cells/tr/net/check-custom-number-format-when-setting-style-custom-property/) konusundaki detaylı makaleyi kontrol edin

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **DisplayUnitType.Percentage Alanı Eklendi**
Aspose.Cells 17.1.0, DisplayUnitType numaralandırmasına yüzde alanını da eklemiştir. DisplayUnitType.Percentage alanı, grafikteki değerlerin 0.01'e bölünmesini gösterir.
## **Removed APIs**
### **Örnek Değişken m_LoadDataFilterOptions Kaldırıldı**
Bu sürüm, m_LoadDataFilterOptions örnek değişkenini kaldırdı. LoadFilter.LoadDataFilterOptions özelliğini kullanmanız önerilir.
{{< app/cells/assistant language="csharp" >}}
