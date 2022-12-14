---
title: Genel API Aspose.Cells 17.1.0'daki değişiklikler
type: docs
weight: 380
url: /tr/java/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 16.12.0 sürümünden 17.1.0 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Excel 2016 Grafikleri Desteği**
Aspose.Cells API'ler, ChartType numaralandırmasını geliştirerek birkaç Excel 2016 grafiği için destek ekledi. Aspose.Cells 17.1.0 sürümü ile aşağıdaki yeni alanlar eklenmiştir.

- ChartType.BOX_WHISKER: Seri, kutu ve bıyık olarak düzenlenmiştir.
- ChartType.FUNNEL: Seri, huni şeklinde düzenlenmiştir.
- ChartType.PARETO_LINE: Seri, pareto çizgiler olarak düzenlenmiştir.
- ChartType.SUNBURST: Seri, güneş patlaması olarak düzenlenmiştir.
- ChartType.TREEMAP: Seri, bir ağaç haritası olarak düzenlenmiştir.
- ChartType.WATEFALL: Seri bir şelale olarak düzenlenmiştir.
- ChartType.HISTOGRAM: Seri, histogram olarak düzenlenir.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Excel 2016 Grafik Türlerini Okuma](/cells/tr/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **LoadFilter.LoadDataFilterOptions Özelliği için Ayarlayıcı Eklendi**
Aspose.Cells 17.1.0, m_LoadDataFilterOptions örnek değişkenini değiştirmek için LoadFilter.LoadDataFilterOptions özelliği için ayarlayıcı ekledi. Kullanıcılar, şablon dosyalarını yükleme davranışını değiştirmek için kendi LoadFilter sınıfı uygulamalarında LoadDataFilterOptions özelliğini değiştirebilir.

İşte basit bir kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Özel Şablon Filtreleme](/cells/tr/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **CellsHelper.SignificantDigits Özelliği Eklendi**
Aspose.Cells 17.1.0, bir elektronik tablodaki sayısal değerler için önemli basamak sayısını almaya veya ayarlamaya izin veren CellsHelper sınıfından SignificantDigits özelliğini kullanıma sundu. CellsHelper.SignificantDigits özelliğinin varsayılan değeri 17'dir, ancak yalnızca sonucun XLSX dosya biçiminde saklanması gerekiyorsa uygulanabilir.

İşte CellsHelper.SignificantDigits özelliğinin kullanımını gösteren basit bir senaryo.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Anlamlı Basamak Sayısını Ayarlama](/cells/tr/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **GlowEffect.Color Özelliği Eklendi**
Aspose.Cells 17.1.0, ışıma efektinin rengini almak için kullanılabilecek GlowEffect.Color özelliğini ekledi.

Aşağıdaki kod parçacığı, GlowEffect.Color özelliğini kullanır.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Şeklin Parıltı Rengini Okuma](/cells/tr/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **PageSetup.PaperWidth & PaperHeight Özellikleri Eklendi**
Aspose.Cells 17.1.0, PageSetup sınıfı için PaperWidth & PaperHeight özelliklerini kullanıma sundu. PageSetup.PaperWidth & PageSetup.PaperHeight özellikleri, sayfa yönünü dikkate alırken kağıt genişliğini ve yüksekliğini inç biriminde temsil eden double türündedir.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Çalışma Sayfasının Kağıt Boyutunu Alma](/cells/tr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **WorkbookSettings.CheckCustomNumberFormat Özelliği Eklendi**
Aspose.Cells 17.1.0, WorkbookSettings sınıfına CheckCustomNumberFormat özelliğini ekledi. CheckCustomNumberFormat, Style.Custom özelliğinin doğru ayarlanıp ayarlanmadığını kontrol etmede kullanışlıdır. Style.Custom özelliği yanlış ayarlanmışsa yani; değer geçerli kalıba karşılık gelmiyorsa Aspose.Cells API'leri uygun mesajla CellsException atar.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Özel Formu Doğrulama](/cells/tr/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **DisplayUnitType.PERCENTAGE Alanı Eklendi**
Aspose.Cells 17.1.0 ayrıca PERCENTAGE alanını DisplayUnitType numaralandırmasına maruz bıraktı. DisplayUnitType.PERCENTAGE alanı, tablodaki değerlerin 0,01'e bölünmesi gerektiğini belirtir.
## **Kaldırılan API'ler**
### **Örnek Değişkeni m_LoadDataFilterOptions Kaldırıldı**
Bu sürüm, m_LoadDataFilterOptions örnek değişkenini kaldırmıştır. Bunun yerine LoadFilter.LoadDataFilterOptions özelliğinin kullanılması önerilir.
