---
title: Aspose.Cells 17.1.0 da Genel API Değişiklikleri
type: docs
weight: 380
url: /tr/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 16.12.0'den 17.1.0'a Aspose.Cells API'sindeki değişiklikleri açıklar ve modül/uygulama geliştiricileri için ilgi çekebilecek değişiklikleri içerir. Yalnızca yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. değil, aynı zamanda Aspose.Cells'in arka planda davranışında herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Excel 2016 Grafikleri için Destek**
Aspose.Cells API'leri, ChartType numaralandırmasını geliştirerek birkaç Excel 2016 grafiği için destek ekledi. Aspose.Cells 17.1.0 sürümüyle şu yeni alanlar eklenmiştir.

- ChartType.BOX_WHISKER: Seri, kutu ve çıtalar olarak yerleştirilir.
- ChartType.FUNNEL: Seri, huni olarak yerleştirilir.
- ChartType.PARETO_LINE: Seri, pareto çizgileri olarak yerleştirilir.
- ChartType.SUNBURST: Seri, güneş patlaması olarak yerleştirilir.
- ChartType.TREEMAP: Seri, ağaç haritası olarak yerleştirilir.
- ChartType.WATERFALL: Seri bir şelale olarak düzenlenir.
- ChartType.HISTOGRAM: Seri bir histogram olarak düzenlenir.

{{% alert color="primary" %}} 

[Reading Excel 2016 Chart Types](/cells/tr/java/read-and-manipulate-excel-2016-charts/) hakkındaki detaylı makaleye göz atın

{{% /alert %}} 
### **LoadFilter.LoadDataFilterOptions Özelliği için Setter eklendi**
Aspose.Cells 17.1.0, LoadFilter.LoadDataFilterOptions özelliği için setter ekledi ve m_LoadDataFilterOptions örnek değişkenini değiştirmek üzere LoadFilter sınıfının kendi uygulamasında LoadDataFilterOptions özelliğini değiştirebilecek olan kullanıcılar, yük şablonu dosyalarının davranışını değiştirebilir.

İşte basit bir kullanım senaryosu.

{{% alert color="primary" %}} 

[Özel Şablon Filtreleme](/cells/tr/java/filter-objects-while-loading-workbook-or-worksheet/) hakkındaki detaylı makaleye göz atın

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Added CellsHelper.SignificantDigits Özelliği**
Aspose.Cells 17.1.0, CellsHelper sınıfından SignificantDigits özelliğini açığa çıkardı ve elektronik tablodaki sayısal değerler için anlamlı basamak sayısını almak veya ayarlamak için kullanılmasını sağlar. CellsHelper.SignificantDigits özelliğinin varsayılan değeri 17'dir ve yalnızca sonucun XLSX dosya formatında depolanması gerektiğinde geçerlidir.

CellsHelper.SignificantDigits özelliğinin kullanımını gösteren basit bir senaryo burada.

{{% alert color="primary" %}} 

[Depolanacak Yapılan Anlamlı Basamak Sayısını Belirtme](/cells/tr/java/specifying-significant-digits-to-be-stored-in-excel-file/) hakkındaki detaylı makaleye göz atın

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Added GlowEffect.Color Özelliği**
Aspose.Cells 17.1.0, GlowEffect.Color özelliğini eklediği ve ışıltı efektinin rengini almak için kullanılabileceği.

Işıl Işıl Efektin Rengini Okuma](/cells/tr/java/read-color-of-the-shape-s-glow-effect/) hakkındaki detaylı makaleye göz atın

{{% alert color="primary" %}} 

[Şeklin Parlama Rengini Okuma](/cells/tr/java/read-color-of-the-shape-s-glow-effect/) konusundaki detaylı makaleyi kontrol edin
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Added PageSetup.PaperWidth ve PaperHeight Özellikleri**
Aspose.Cells 17.1.0, PageSetup sınıfı için PaperWidth ve PaperHeight özelliklerini açığa çıkardı. PageSetup.PaperWidth ve PageSetup.PaperHeight özellikleri, sayfa yönlendirmesini dikkate alarak inç biriminde kağıt genişliğini ve yüksekliğini temsil eden double türündendir.

{{% alert color="primary" %}} 

[Çalışma Sayfasının Kağıt Boyutunu Alın](/cells/tr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/) hakkındaki detaylı makaleye göz atın

{{% /alert %}} 
### **Added WorkbookSettings.CheckCustomNumberFormat Özelliği**
Aspose.Cells 17.1.0, WorkbookSettings sınıfına CheckCustomNumberFormat özelliğini ekledi. CheckCustomNumberFormat, Style.Custom özelliğinin uygun şekilde ayarlanıp ayarlanmadığını kontrol etmede kullanışlıdır. Eğer Style.Custom özelliği yanlış şekilde ayarlanmışsa yani; değer geçerli bir desene karşılık gelmiyorsa, Aspose.Cells API'ları uygun mesajla CellsException fırlatacaktır.

{{% alert color="primary" %}} 

[Özel Formayı Doğrulama](/cells/tr/java/check-custom-number-format-when-setting-style-custom-property/) hakkındaki detaylı makaleye göz atın

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Eklenen DisplayUnitType.PERCENTAGE Alanı**
Aspose.Cells 17.1.0, DisplayUnitType numaralandırmasına aynı zamanda PERCENTAGE alanını da açığa çıkardı. DisplayUnitType.PERCENTAGE alanı, grafikteki değerlerin 0,01 ile bölüneceğini belirtir.
## **Removed APIs**
### **Örnek Değişken m_LoadDataFilterOptions Kaldırıldı**
Bu sürüm, m_LoadDataFilterOptions örnek değişkenini kaldırdı. LoadFilter.LoadDataFilterOptions özelliğini kullanmanız önerilir.
