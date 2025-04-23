---
title: Aspose.Cells 8.3.2 de Genel API Değişiklikleri
type: docs
weight: 130
url: /tr/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.3.1'den 8.3.2'ye olan değişiklikleri açıklar ve modül / uygulama geliştiricileri için ilginç olabilecek sadece yeni ve güncellenmiş genel yöntemleri, [eklenmiş sınıfları vs.](/cells/tr/java/aspose-cells-8-3-2-surecinde-genel-api-degisiklikleri/) ve [kaldırılmış sınıfları vs.](/cells/tr/java/aspose-cells-8-3-2-surecinde-genel-api-degisiklikleri/) değil, aynı zamanda Aspose.Cells'in arka planda olan değişikliklerinin de açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **PivotItem'ın Mutlak Konumunu Ayarlama Mekanizması**
[PivotItem'ın Mutlak Konumlandırması](/cells/tr/java/specifying-the-absolute-position-of-the-pivot-item/) özelliğini sağlamak için, Aspose.Cells for Java 8.3.2 aşağıda listelenen bir dizi özellik ve bir yöntemi açığa çıkarmıştır.

- PivotItem.setPosition, ebeveyn düğümünden bağımsız olarak tüm PivotItem'ların konum indeksini ayarlamak için kullanılabilir.
- PivotItem.setPositionInSameParentNode, aynı ebeveyn düğümü altındaki PivotItem'ın konum indeksini ayarlamak için kullanılabilir.
- PivotItem.move(int count, bool isSameParent) yöntemi, PivotItem'ı, count değerine göre yukarı veya aşağı taşımak için kullanılabilir. Count değeri, PivotItem'ı yukarı veya aşağı taşımak için hareket edilecek konum sayısını belirtir. Eğer count değeri sıfırdan küçükse, öğe yukarı taşınır; eğer count değeri sıfırdan büyükse, PivotItem aşağı taşınır. Boolean tipindeki isSameParent parametresi, taşıma işleminin aynı ebeveyn düğümünde gerçekleştirilip gerçekleştirilmeyeceğini belirtir.

{{% alert color="primary" %}} 

Lütfen, PivotItem.setPosition, PivotItem.setPositionInSameParentNode özellikleri ve PivotItem.move(int count, bool isSameParent) yöntemi kullanmadan önce PivotTable.refreshData ve PivotTable.calculateData yöntemlerini çağırmak gereklidir.

{{% /alert %}} 
### **Class SignatureLine Eklendi**
Aspose.Cells 8.3.2, MS Excel'in karşılık gelen özelliğini taklit etmek için Signature Line desteği sağlamaktadır. Bu sürüm, bu amaçla SignatureLine sınıfını ve Picture.SignatureLine özelliğini açığa çıkarmıştır.

Aşağıdaki örnek kod, Picture.SignatureLine özelliğini kullanarak bir İmza Satırı ekler.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **Chart.hasAxis Yöntemi Eklendi**
v8.3.2'nin yayınlanmasıyla, Aspose.Cells API'ı, belirli bir ekseni içeren bir grafik olup olmadığını belirlemek için Chart.hasAxis(EksenTürü eksenTürü, bool isPrimary) yöntemini sağlamıştır.

Aşağıdaki örnek kod, Chart.hasAxis yönteminin kullanımını göstermektedir, örnek grafikte Birincil, İkincil ve Değer ekseni olup olmadığını belirlemek için.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **WorkbookSettings.checkWriteProtectedPassword Yöntemi Eklendi**
Method WorkbookSettings.checkWriteProtectedPassword, elektronik tabloyu değiştirmek için verilen şifrenin doğru olup olmadığını kontrol etmeye olanak tanımaktadır.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Overload Metotlar WorkbookRender.toPrinter ve SheetRender.toPrinter Eklendi**
Aspose.Cells 8.3.2, belirli bir aralığın sayfalarını yazdırmak için WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) ve SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) yöntemlerini sağlamıştır.

Aşağıdaki örnek kod, belirtilen yöntemlerin kullanımını, elektronik tablonun ve çalışma sayfasının 2-5 sayfalarını yazdırmak için göstermektedir.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Worksheet.refreshPivotTables Yöntemi Eklendi**
Yeniden eklenen Worksheet.refreshPivotTables yöntemi, verilen elektronik tablodaki tüm Pivot Tablolarını tek bir çağrıda yenilemeye olanak tanır.

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Workbook.getNamedStyle Yöntemi Eklendi**
Aspose.Cells 8.3.2, string parametre kabul eden ve geçilen parametreye göre Style nesnesini alabilen Workbook.getNamedStyle yöntemini açığa çıkarmıştır.
### **Cells.importTwoDimensionArray Yöntemi Eklendi**
Aspose.Cells API, Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) yöntemi ile iki boyutlu dizilerin elektronik tablo hücrelerine aktarılmasını mümkün kılmıştır. Söz konusu yöntem, TxtLoadOptions'da belirtilen daha esnek seçeneklerle verilerin iki boyutlu dizisini bir elektronik tabloya aktarır.
### **OnePagePerSheet, PageIndex ve PageCount Özellikleri Eklendi**
Aspose.Cells for Java 8.3.2, XpsSaveOptions sınıfı için OnePagePerSheet, PageIndex ve PageCount özelliklerini açığa çıkarmıştır. Kullanıcı, OnePagePerSheet özelliğini kullanarak elektronik tablonun tüm içeriğini bir XPS sayfasına sığdırabilir ve/veya PageCount özelliğini kullanarak yazdırılacak sayfa sayısını alabilir. PageIndex özelliği, kaydedilecek ilk sayfanın 0 tabanlı dizinini alır/ayarlar.
### **NumberDecimalSeparator ve NumberGroupSeparator Özellikleri Eklendi**
Aspose.Cells for Java 8.3.2, sayısal değerleri biçimlendirme ve ayrıştırmak için kullanılan özel ayırıcıları alabilen/getirebilen NumberDecimalSeparator ve NumberGroupSeparator özelliklerini tanıtmıştır.

Aşağıdaki örnek kod, Aspose.Cells API'i kullanarak özel ayırıcıları nasıl belirteceği göstermektedir. Aşağıdaki kod, özel Nokta ve Boşluk ayırıcılarını belirtir.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **PdfSaveOptions.setFontSubstitutionCharGranularity Özelliği Eklendi**
Aspose.Cells for Java 8.3.2, PdfSaveOptions.setFontSubstitutionCharGranularity özelliği, bazı Unicode karakterlerinin belirli bir font ailesi kullanılarak görüntülenememesi sorununu aşmak için ortaya çıkmıştır. PdfSaveOptions.setFontSubstitutionCharGranularity özelliği true olarak ayarlandığında, sadece görüntülenemeyen belirli karakterin fontu değiştirilir ve geri kalan kelime veya cümlenin orijinal fontta kalması gerekmektedir.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Removed APIs**
### **Kaldırılan Eski Yöntemler**
Aşağıdaki yöntemler Genel API'dan kaldırılmıştır.

- Workbook.open ve Workbook.save yöntemleri.
- Workbook.setOleSize yöntemi.
- Workbook.loadData yöntemi.
- WorkbookDesigner.open ve WorkbookDesigner.save yöntemleri.
- WorksheetCollection.deleteName yöntemi.
### **Kaldırılan Eski Özellikler**
Aşağıdaki özellikler Genel API'dan kaldırılmıştır.

- Workbook.isProtected özelliği.
- Workbook.Language özelliği.
- Workbook.Region özelliği.
- WorkbookSettings.ReCalcOnOpen özelliği.
- WorkbookSettings.Language özelliği.
- WorkbookSettings.Encoding özelliği.
- WorkbookSettings.ConvertNumericData özelliği.
- WorksheetCollection.HidePivotFieldList özelliği.
- WorksheetCollection.EnableHTTPCompression özelliği.
- WorksheetCollection.isMinimized özelliği.
- WorksheetCollection.isHidden özelliği.
- WorksheetCollection.SheetTabBarWidth özelliği.
- WorksheetCollection.WindowLeft özelliği.
- WorksheetCollection.WindowLeftInch özelliği.
- WorksheetCollection.WindowLeftCM özelliği.
- WorksheetCollection.WindowTop özelliği.
- WorksheetCollection.WindowTopInch özelliği.
- WorksheetCollection.WindowTopCM özelliği.
- WorksheetCollection.WindowWidth özelliği.
- WorksheetCollection.WindowWidthInch özelliği.
- WorksheetCollection.WindowWidthCM özelliği.
- WorksheetCollection.WindowHeight özelliği.
- WorksheetCollection.WindowHeightInch özelliği.
- WorksheetCollection.WindowHeightCM özelliği.
- Worksheet.HPageBreaks özelliği.
- Worksheet.VPageBreaks özelliği.
- HtmlSaveOptions.DisplayHTMLCrossString özelliği.
- HtmlSaveOptions.ExportChartImageFormat özelliği.
- SaveOptions.ExpCellNameToXLSX özelliği.
- SaveOptions.DefaultFont özelliği.
- SaveOptions.Compliance özelliği.
- SaveOptions.PdfBookmark özelliği.
- SaveOptions.PdfImageCompression özelliği.
- TxtSaveOptions.AlwaysQuoted özelliği.
## **Eski API'ler**
### **Kaldırılan Workbook.saveOptions Özelliği**
SaveOptions'un uygun SaveOptions özelliklerini ayarladıktan sonra Workbook.Save yöntemine geçirilmesi gereken bir SaveOptions nesnesi. 
### **Kaldırılan Workbook.Styles & Class StyleCollection Özelliği**
Workbook.createStyle yönteminin, StyleCollection.add yöntemiyle Stil oluşturmak yerine ve StyleCollection.get(string) yerine Workbook.getNamedStyle(string) yönteminin adlandırılmış stil almak için kullanılması tavsiye edilir.
### **Kaldırılan PivotItem.move(int count) Yöntemi**
Aspose.Cells 8.3.2'nin piyasaya sürülmesiyle, API, PivotItem.move yönteminde bir PivotItem'ı ebeveyn düğümü içinde taşımak için sağlayan başka bir aşırı yükleme yöntemi tanıttı. 
{{< app/cells/assistant language="java" >}}
