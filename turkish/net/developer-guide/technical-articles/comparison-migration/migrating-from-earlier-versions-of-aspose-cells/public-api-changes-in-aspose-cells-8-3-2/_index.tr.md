---
title: Aspose.Cells 8.3.2 de Genel API Değişiklikleri
type: docs
weight: 120
url: /tr/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 8.3.1'den 8.3.2'ye Aspose.Cells API'sinde yapılacak değişiklikleri, modül/uygulama geliştiricilerinin ilgisini çekebileceklerini açıklamaktadır. Sadece yeni ve güncellenmiş genel yöntemleri, [eklenen sınıflar vs.](/cells/tr/net/public-api-changes-in-aspose-cells-8-3-2/) ve [kaldırılan sınıflar vs.](/cells/tr/net/public-api-changes-in-aspose-cells-8-3-2/) değil, aynı zamanda Aspose.Cells'in arka planda işlevlerindeki herhangi bir değişikliği açıklamaktadır.

{{% /alert %}} 
## **Eklenen API'lar**
### **PivotItem'ın Mutlak Konumunu Ayarlama Mekanizması**
Aspose.Cells for .NET 8.3.2, [PivotItem'ın Mutlak Konumlandırma](/cells/tr/net/specifying-the-absolute-position-of-the-pivot-item/) özelliğini sağlamak için aşağıda listelenen bir dizi özelliği ve yardımcı yöntemleri ortaya çıkarmıştır.

- PivotItem.Position özelliği, üst düğümünden bağımsız olarak tüm PivotItem'ların konum dizinini belirtmek için kullanılabilir.
- PivotItem.PositionInSameParentNode özelliği, aynı üst düğüm altındaki PivotItem'ların konum dizinini belirtmek için kullanılabilir.
- PivotItem.Move(int count, bool isSameParent) yöntemi, PivotItem'ın belirli sayıda konumu yukarı veya aşağı taşımak için kullanılabilir, burada count, PivotItem'ın yukarı veya aşağı taşınacak konumu belirler. Eğer count değeri sıfırdan küçükse, öğe yukarı taşınır, count değeri sıfırdan büyükse, PivotItem aşağı taşınır, Boolean tipindeki isSameParent parametresi taşıma işleminin aynı üst düğümde gerçekleştirilip gerçekleştirilmeyeceğini belirtir.

{{% alert color="primary" %}} 

Lütfen, PivotItem.Position, PivotItem.PositionInSameParentNode özelliklerini ve PivotItem.Move(int count, bool isSameParent) yöntemini kullanmadan önce PivotTable.RefreshData ve PivotTable.CalculateData yöntemlerini çağırmak gereklidir.

{{% /alert %}} 
### **Class SignatureLine Eklendi**
Aspose.Cells for .NET 8.3.2, MS Excel'in eşdeğer özelliğini taklit etmek için Signature Line'ı destekler. Bu sürümde Aspose.Cells for .NET, bu amaçla SignatureLine sınıfını ve Picture.SignatureLine özelliğini açığa çıkarmıştır.

Aşağıdaki örnek kod, Picture.SignatureLine özelliğini kullanarak bir İmza Satırı ekler.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Chart.HasAxis Yöntemi Eklendi**
v8.3.2'nin piyasaya sürülmesiyle, Aspose.Cells API, belirli bir eksenin grafikte var olup olmadığını belirlemek için Chart.HasAxis(AxisType axisType, bool isPrimary) yöntemini sağlamıştır.

Aşağıdaki örnek kod, Chart.HasAxis yönteminin kullanımını göstermektedir; örnek grafikte Birincil, İkincil ve Değer eksenlerinin olup olmadığını belirler.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **WorkbookSettings.CheckWriteProtectedPassword Yöntemi Eklendi**
WorkbookSettings.CheckWriteProtectedPassword yöntemi, geliştiricilere İtibarı değiştirmek için verilen şifrenin doğru olup olmadığını kontrol etme olanağı sağlar.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Overload Yöntemler WorkbookRender.ToPrinter & SheetRender.ToPrinter Eklendi**
Aspose.Cells for .NET 8.3.2, WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) ve SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) yöntemlerini sağlamıştır; sırasıyla çalışma kitabının ve çalışma sayfasının sayfa aralığını yazdırmak için.

Aşağıdaki örnek kod, belirtilen yöntemlerin kullanımını, elektronik tablonun ve çalışma sayfasının 2-5 sayfalarını yazdırmak için göstermektedir.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Worksheet.RefreshPivotTables Yöntemi Eklendi**
Yeni eklenen yöntem Worksheet.RefreshPivotTables, verilen bir elektronik tabloda yer alan tüm Pivot Tablolarını tek bir çağrıda yenilemeye olanak tanır.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Workbook.GetNamedStyle Yöntemi Eklendi**
Aspose.Cells for .NET API, parametre olarak bir dize kabul eden ve parametreye göre Stil nesnesini alabilen Workbook.GetNamedStyle yöntemini açığa çıkarmıştır.
### **Cells.ImportTwoDimensionArray Yöntemi Eklendi**
Aspose.Cells for .NET API, Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) yöntemini açığa çıkararak iki boyutlu dizilerin elektronik tablo hücrelerine aktarılmasını mümkün kılmıştır. Söz konusu yöntem, TxtLoadOptions içinde tanımlanan daha esnek seçenekler ile veri iki boyutlu bir diziden bir çalışma sayfasına aktarır.
### **OnePagePerSheet, PageIndex ve PageCount Özellikleri Eklendi**
Aspose.Cells for .NET 8.3.2, XpsSaveOptions sınıfı için OnePagePerSheet, PageIndex & PageCount özelliklerini açığa çıkarmıştır. Kullanıcı, OnePagePerSheet özelliğini kullanarak bir elektronik tablonun tüm içeriğini XPS'nin tek bir sayfasına sığdırabilir ve/veya PageCount özelliğini kullanarak yazdırılacak sayfa sayısını alabilir. PageIndex özelliği, kaydedilecek ilk sayfanın 0 tabanlı dizinini alır/ayarlar.
### **NumberDecimalSeparator ve NumberGroupSeparator Özellikleri Eklendi**
Aspose.Cells for .NET 8.3.2, sayısal değerlerin biçimlendirilmesi ve ayrıştırılmasında kullanılan özel ayraçları almak/ayarlamak için NumberDecimalSeparator & NumberGroupSeparator özelliklerini tanıtmıştır.

Aşağıdaki örnek kod, Aspose.Cells API kullanarak Özel Ayraçlarını belirtmek için nasıl kullanılacağını açıklar. Aşağıdaki kod, Özel Ondalık ve Grup ayraçlarını sırasıyla nokta ve boşluk olarak belirtir.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **PdfSaveOptions.IsFontSubstitutionCharGranularity Özelliği Eklendi**
Aspose.Cells for .NET 8.3.2, bazı Unicode karakterlerinin belirli bir yazıtipi kullanılarak gösterilememesi sorununun üstesinden gelmek için PdfSaveOptions.IsFontSubstitutionCharGranularity özelliğini açığa çıkarmıştır. PdfSaveOptions.IsFontSubstitutionCharGranularity özelliği true olarak ayarlandığında, gösterilemeyen belirli karakterin yazıtipi yalnızca değiştirilerek gösterilebilir hale gelir, cümlenin geri kalanı ise orijinal yazıtipiyle kalır.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Removed APIs**
### **Kaldırılan Eski Yöntemler**
Aşağıdaki yöntemler Genel API'dan kaldırılmıştır.

- Workbook.Open ve Workbook.Save yöntemleri.
- Workbook.SetOleSize yöntemi.
- Workbook.LoadData yöntemi.
- WorkbookDesigner.Open ve WorkbookDesigner.Save yöntemleri.
- WorksheetCollection.DeleteName yöntemi.
### **Kaldırılan Eski Özellikler**
Aşağıdaki özellikler Genel API'dan kaldırılmıştır.

- Workbook.IsProtected özelliği.
- Workbook.Language özelliği.
- Workbook.Region özelliği.
- WorkbookSettings.ReCalcOnOpen özelliği.
- WorkbookSettings.Language özelliği.
- WorkbookSettings.Encoding özelliği.
- WorkbookSettings.ConvertNumericData özelliği.
- WorksheetCollection.HidePivotFieldList özelliği.
- WorksheetCollection.EnableHTTPCompression özelliği.
- WorksheetCollection.IsMinimized özelliği.
- WorksheetCollection.IsHidden özelliği.
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
### **Eski Workbook.SaveOptions Özelliği**
SaveOptions'un uygun SaveOptions özelliklerini ayarladıktan sonra Workbook.Save yöntemine geçirilmesi gereken bir SaveOptions nesnesi.
### **Eski Workbook.Styles Özelliği ve StyleCollection Sınıfı**
Bir StyleCollection.Add yöntemi ile Stil oluşturmak yerine Workbook.CreateStyle yönteminin kullanılması önerilir
### **Eski PivotItem.Move(int count) Yöntemi**
Aspose.Cells 8.3.2'nin yayınlanmasıyla, API, PivotItem.Move yönteminin, sayıyı taşımak için bir integer parametresi ve ebeveyn düğüm içinde bir PivotItem'ı taşımak için boolean parametresini kabul eden başka bir aşırı yükleme ile tanıtmıştır.
