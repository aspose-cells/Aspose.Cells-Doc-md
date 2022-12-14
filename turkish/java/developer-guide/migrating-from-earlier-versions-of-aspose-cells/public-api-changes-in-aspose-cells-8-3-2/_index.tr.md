---
title: Genel API Aspose.Cells 8.3.2'deki değişiklikler
type: docs
weight: 130
url: /tr/java/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.3.1'den 8.3.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-3-2/) ve[kaldırılan sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-3-2/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **PivotItem'in Mutlak Konumunu Ayarlama Mekanizması**
 Özelliği sağlamak için[PivotItem'in Mutlak Konumlandırması](/cells/tr/java/specifying-the-absolute-position-of-the-pivot-item/)Aspose.Cells for Java 8.3.2, aşağıda listelenen bir dizi özelliği ve yöntemi ortaya çıkardı.

- PivotItem.setPosition, üst düğümden bağımsız olarak tüm PivotItem'lerde konum dizinini ayarlamak için kullanılabilir.
- PivotItem.setPositionInSameParentNode, aynı üst düğüm altındaki PivotItems içindeki konum dizinini ayarlamak için kullanılabilir.
- PivotItem.move(int count, bool isSameParent) yöntemi, count değerine göre öğeyi yukarı veya aşağı taşımak için kullanılabilir; burada count, PivotItem öğesini yukarı veya aşağı hareket ettirecek konum sayısıdır. Sayım değeri sıfırdan küçükse, öğe yukarı taşınır, burada sayım değeri sıfırdan büyükse, PivotItem aşağı hareket eder, Boolean tipi isSameParent parametresi, taşıma işleminin aynı üst düğümde gerçekleştirilip gerçekleştirilmeyeceğini belirtir. ya da değil.

{{% alert color="primary" %}} 

Lütfen dikkat, PivotItem.setPosition, PivotItem.setPositionInSameParentNode özellikleri ve PivotItem.move(int count, bool isSameParent) yöntemini kullanmadan önce PivotTable.refreshData ve PivotTable.calculateData yöntemlerini çağırmak gerekir.

{{% /alert %}} 
### **Sınıf İmza Satırı Eklendi**
Aspose.Cells 8.3.2, İmza Satırının MS Excel'in eşdeğer özelliğini taklit etmesi için destek sağlar. Bu yayın, SignatureLine sınıfını ve Picture.SignatureLine özelliğini bu amaçla kullanıma sunmuştur.

Aşağıdaki örnek kod, çalışma kitabına Picture.SignatureLine özelliğini kullanarak bir İmza Satırı ekler.

**Java**

{{< highlight "csharp" >}}

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
### **Yöntem Chart.hasAxis Eklendi**
v8.3.2 sürümüyle birlikte Aspose.Cells API, grafiğin belirli bir ekseni olup olmadığını belirlemek için Chart.hasAxis(AxisType eksenType, bool isPrimary) yöntemini sağladı.

Aşağıdaki örnek kod, örnek grafiğin Birincil, İkincil ve Değer eksenine sahip olup olmadığını belirlemek için Chart.hasAxis yönteminin kullanımını gösterir.

**Java**

{{< highlight "csharp" >}}

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
### **Yöntem WorkbookSettings.checkWriteProtectedPassword Eklendi**
Yöntem WorkbookSettings.checkWriteProtectedPassword, geliştiricilerin elektronik tabloyu değiştirmek için verilen parolanın doğru olup olmadığını kontrol etmelerini sağlar.

**Java**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Aşırı Yükleme Yöntemleri WorkbookRender.toPrinter & SheetRender.toPrinter Eklendi**
Aspose.Cells 8.3.2, sırasıyla çalışma kitabı ve çalışma sayfasının sayfa aralığını yazdırmak için WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) ve SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) yöntemlerini sağlamıştır.

Aşağıdaki örnek kod, çalışma kitabının ve çalışma sayfasının 2-5 sayfalarını yazdırmak için yukarıda belirtilen yöntemlerin kullanımını göstermektedir.

**Java**

{{< highlight "csharp" >}}

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
### **Yöntem Worksheet.refreshPivotTables Eklendi**
Yeni eklenen Worksheet.refreshPivotTables yöntemi, belirli bir elektronik tablodaki tüm Pivot Tabloları tek bir çağrıda yenilemeye olanak tanır.

**Java**

{{< highlight "csharp" >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Yöntem Workbook.getNamedStyle Eklendi**
Aspose.Cells 8.3.2, dizeyi parametre olarak kabul eden ve iletilen parametreye göre Style nesnesini alan Workbook.getNamedStyle yöntemini kullanıma sundu.
### **Yöntem Cells.importTwoDimensionArray Eklendi**
Aspose.Cells API, Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) yöntemini göstererek iki boyutlu dizileri elektronik tablo hücrelerine içe aktarmayı mümkün kıldı. Bahsedilen yöntem, iki boyutlu bir veri dizisini, TxtLoadOptions'da tanımlanan daha esnek seçeneklerle bir çalışma sayfasına aktarır.
### **Özellikler OnePagePerSheet, PageIndex & PageCount Eklendi**
Aspose.Cells for Java 8.3.2, XpsSaveOptions sınıfı için OnePagePerSheet, PageIndex & PageCount özelliklerini kullanıma sundu. Kullanıcı, OnePagePerSheet özelliğini kullanarak bir elektronik tablonun tüm içeriğini tek bir XPS sayfasına sığdırabilir ve/veya PageCount özelliğini kullanarak yazdırılacak sayfa sayısını alabilir. PageIndex özelliği, kaydedilecek ilk sayfanın 0 tabanlı dizinini alır/ayarlar.
### **Özellikler NumberDecimalSeparator & NumberGroupSeparator Eklendi**
Aspose.Cells for Java 8.3.2, elektronik tablolardaki sayısal değerleri biçimlendirmek ve ayrıştırmak için kullanılan özel ayırıcıları alabilen/ayarlayabilen NumberDecimalSeparator & NumberGroupSeparator özelliklerini tanıttı.

Aşağıdaki örnek kod, Aspose.Cells API kullanılarak özel ayırıcıların nasıl belirtileceğini gösterir. Aşağıdaki kod, özel Ondalık ve Grup ayırıcılarını sırasıyla nokta ve boşluk olarak belirtir.

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Özellik PdfSaveOptions.setFontSubstitutionCharGranularity Eklendi**
Aspose.Cells for Java 8.3.2, bazı Unicode karakterlerinin belirli bir yazı tipi ailesi kullanılarak görüntülenememesi sorununun üstesinden gelmek için PdfSaveOptions.setFontSubstitutionCharGranularity özelliğini kullanıma sunmuştur. PdfSaveOptions.setFontSubstitutionCharGranularity özelliği true olarak ayarlandığında, yalnızca belirli bir karakterin görüntülenemeyen yazı tipi görüntülenebilir yazı tipine değiştirilir ve kelimenin veya cümlenin geri kalanı orijinal yazı tipinde kalmalıdır.

**Java**

{{< highlight "csharp" >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Kaldırılan API'ler**
### **Kaldırılan Eski Yöntemler**
Aşağıdaki yöntemler Kamudan kaldırıldı API.

- Workbook.open & Workbook.save yöntemleri.
- Workbook.setOleSize yöntemi.
- Workbook.loadData yöntemi.
- WorkbookDesigner.open & WorkbookDesigner.save yöntemleri.
- WorksheetCollection.deleteName yöntemi.
### **Eski Mülkler Kaldırıldı**
Aşağıdaki mülkler Kamudan kaldırıldı API.

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
### **Workbook.saveOptions Özelliği Kullanımdan Kaldırıldı**
 Uygun SaveOptions özellikleri ayarlandıktan sonra, bir SaveOptions nesnesinin Workbook.Save yöntemine iletilmesi gerekir.
### **Property Workbook.Styles & Class StyleCollection Kullanımdan Kaldırıldı**
StyleCollection.add yöntemiyle bir Stil oluşturmak yerine Workbook örneği için stil oluşturmak ve değiştirmek üzere Workbook.createStyle yönteminin kullanılması önerilir. Ayrıca, StyleCollection.get(string) yerine Workbook.getNamedStyle(string) yöntemi kullanılarak stil adı verilir.
### **Yöntem PivotItem.move(int sayısı) Eskimiş**
 Aspose.Cells 8.3.2'nin piyasaya sürülmesiyle API, PivotItem'i üst düğüm içinde taşımak için count için tamsayı parametresini ve boolean parametresini kabul eden PivotItem.move yöntemine başka bir aşırı yükleme getirdi.
