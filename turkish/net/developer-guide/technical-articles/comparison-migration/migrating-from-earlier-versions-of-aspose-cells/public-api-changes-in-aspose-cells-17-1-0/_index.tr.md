---
title: Genel API Aspose.Cells 17.1.0'daki değişiklikler
type: docs
weight: 370
url: /tr/net/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 16.12.0 sürümünden 17.1.0 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Excel 2016 Grafikleri Desteği**
Aspose.Cells API'ler, ChartType numaralandırmasını geliştirerek birkaç Excel 2016 grafiği için destek ekledi. Aspose.Cells 17.1.0 sürümü ile aşağıdaki yeni alanlar eklenmiştir.

- ChartType.BoxWhisker: Seri, kutu ve bıyık olarak düzenlenmiştir.
- ChartType.Funnel: Seri, bir huni olarak düzenlenir.
- ChartType.ParetoLine: Seri, pareto çizgileri olarak düzenlenmiştir.
- ChartType.Sunburst: Seri, bir sunburst olarak düzenlenmiştir.
- ChartType.Treemap: Seri, bir ağaç haritası olarak düzenlenir.
- ChartType.Waterfall: Seri bir şelale olarak düzenlenmiştir.
- ChartType.Histogram: Seri, histogram olarak düzenlenir.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Excel 2016 Grafik Türlerini Okuma](/cells/tr/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **LoadFilter.LoadDataFilterOptions Özelliği için Ayarlayıcı Eklendi**
Aspose.Cells 17.1.0, m_LoadDataFilterOptions örnek değişkenini değiştirmek için LoadFilter.LoadDataFilterOptions özelliği için ayarlayıcı ekledi. Kullanıcılar, şablon dosyalarını yükleme davranışını değiştirmek için kendi LoadFilter sınıfı uygulamalarında LoadDataFilterOptions özelliğini değiştirebilir.

İşte basit bir kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Özel Şablon Filtreleme](/cells/tr/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **CellsHelper.SignificantDigits Özelliği Eklendi**
Aspose.Cells 17.1.0, bir elektronik tablodaki sayısal değerler için önemli basamak sayısını almaya veya ayarlamaya izin veren CellsHelper sınıfından SignificantDigits özelliğini kullanıma sundu. CellsHelper.SignificantDigits özelliğinin varsayılan değeri 17'dir, ancak yalnızca sonucun XLSX dosya biçiminde saklanması gerekiyorsa uygulanabilir.

İşte CellsHelper.SignificantDigits özelliğinin kullanımını gösteren basit bir senaryo.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Anlamlı Basamak Sayısını Ayarlama](/cells/tr/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **GlowEffect.Color Özelliği Eklendi**
Aspose.Cells 17.1.0, ışıma efektinin rengini almak için kullanılabilecek GlowEffect.Color özelliğini ekledi.

Aşağıdaki kod parçacığı, GlowEffect.Color özelliğini kullanır.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Şeklin Parıltı Rengini Okuma](/cells/tr/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **PageSetup.PaperWidth & PaperHeight Özellikleri Eklendi**
Aspose.Cells 17.1.0, PageSetup sınıfı için PaperWidth & PaperHeight özelliklerini kullanıma sundu. PageSetup.PaperWidth & PageSetup.PaperHeight özellikleri, sayfa yönünü dikkate alırken kağıt genişliğini ve yüksekliğini inç biriminde temsil eden double türündedir.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Çalışma Sayfasının Kağıt Boyutunu Alma](/cells/tr/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **WorkbookSettings.CheckCustomNumberFormat Özelliği Eklendi**
Aspose.Cells 17.1.0, WorkbookSettings sınıfına CheckCustomNumberFormat özelliğini ekledi. CheckCustomNumberFormat, Style.Custom özelliğinin doğru ayarlanıp ayarlanmadığını kontrol etmede kullanışlıdır. Style.Custom özelliği yanlış ayarlanmışsa yani; değer geçerli kalıba karşılık gelmiyorsa Aspose.Cells API'leri uygun mesajla CellsException atar.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Özel Formatı Doğrulama](/cells/tr/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells 17.1.0 ayrıca Yüzde alanını DisplayUnitType numaralandırmasına maruz bıraktı. DisplayUnitType.Percentage alanı, tablodaki değerlerin 0,01'e bölünmesi gerektiğini belirtir.
## **Kaldırılan API'ler**
### **Örnek Değişkeni m_LoadDataFilterOptions Kaldırıldı**
Bu sürüm, m_LoadDataFilterOptions örnek değişkenini kaldırmıştır. Bunun yerine LoadFilter.LoadDataFilterOptions özelliğinin kullanılması önerilir.
