---
title: Genel API Aspose.Cells 8.3.2'deki değişiklikler
type: docs
weight: 120
url: /tr/net/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.3.1'den 8.3.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-3-2/) ve[kaldırılan sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-3-2/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **PivotItem'in Mutlak Konumunu Ayarlama Mekanizması**
 Özelliği sağlamak için[PivotItem'in Mutlak Konumlandırması](/cells/tr/net/specifying-the-absolute-position-of-the-pivot-item/)Aspose.Cells for .NET 8.3.2, aşağıda listelenen bir dizi özelliği ve yardımcı yöntemi ortaya çıkarmıştır.

- PivotItem.Position özelliği, üst düğümden bağımsız olarak tüm PivotItem'lerdeki konum dizinini belirtmek için kullanılabilir.
- PivotItem.PositionInSameParentNode özelliği, aynı üst düğüm altındaki PivotItems içindeki konum dizinini belirtmek için kullanılabilir.
- PivotItem.Move(int count, bool isSameParent) yöntemi, count değerine göre öğeyi yukarı veya aşağı taşımak için kullanılabilir; burada count, PivotItem'i yukarı veya aşağı taşımak için konum sayısıdır. Sayım değeri sıfırdan küçükse, öğe yukarı taşınır, burada sayım değeri sıfırdan büyükse, PivotItem aşağı hareket eder, Boolean tipi isSameParent parametresi, taşıma işleminin aynı üst düğümde gerçekleştirilip gerçekleştirilmeyeceğini belirtir. ya da değil.

{{% alert color="primary" %}} 

Lütfen dikkat, PivotItem.Position, PivotItem.PositionInSameParentNode özellikleri ve PivotItem.Move(int count, bool isSameParent) yöntemini kullanmadan önce PivotTable.RefreshData ve PivotTable.CalculateData yöntemlerini çağırmak gerekir.

{{% /alert %}} 
### **Sınıf İmza Satırı Eklendi**
Aspose.Cells for .NET 8.3.2 İmza Satırının MS Excel'in eşdeğer özelliğini taklit etmesi için destek sağlar. Aspose.Cells for .NET numaralı bu sürüm, SignatureLine sınıfını ve Picture.SignatureLine özelliğini bu amaçla kullanıma sunmuştur.

Aşağıdaki örnek kod, çalışma kitabına Picture.SignatureLine özelliğini kullanarak bir İmza Satırı ekler.

**C#**

{{< highlight "csharp" >}}

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


### **Yöntem Chart.HasAxis Eklendi**
v8.3.2 sürümüyle birlikte Aspose.Cells API, grafiğin belirli bir ekseni olup olmadığını belirlemek için Chart.HasAxis(AxisType eksenType, bool isPrimary) yöntemini sağladı.

Aşağıdaki örnek kod, örnek grafiğin Birincil, İkincil ve Değer eksenine sahip olup olmadığını belirlemek için Chart.HasAxis yönteminin kullanımını gösterir.

**C#**

{{< highlight "csharp" >}}

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


### **Yöntem WorkbookSettings.CheckWriteProtectedPassword Eklendi**
Yöntem WorkbookSettings.CheckWriteProtectedPassword, geliştiricilerin elektronik tabloyu değiştirmek için verilen bir parolanın doğru olup olmadığını kontrol etmelerini sağlar.

**C#**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Aşırı Yükleme Yöntemleri WorkbookRender.ToPrinter & SheetRender.ToPrinter Eklendi**
Aspose.Cells for .NET 8.3.2, sırasıyla çalışma kitabı ve çalışma sayfasının sayfa aralığını yazdırmak için WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) ve SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) yöntemlerini sağlamıştır.

Aşağıdaki örnek kod, çalışma kitabının ve çalışma sayfasının 2-5 sayfalarını yazdırmak için yukarıda belirtilen yöntemlerin kullanımını göstermektedir.

**C#**

{{< highlight "csharp" >}}

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


### **Yöntem Worksheet.RefreshPivotTables Eklendi**
Yeni eklenen yöntem Worksheet.RefreshPivotTables, belirli bir elektronik tablodaki tüm Pivot Tabloları tek bir çağrıda yenilemeye olanak tanır.

**C#**

{{< highlight "csharp" >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Yöntem Workbook.GetNamedStyle Eklendi**
Aspose.Cells for .NET API, dizeyi parametre olarak kabul eden ve iletilen parametreye göre Style nesnesini alan Workbook.GetNamedStyle yöntemini kullanıma sundu.
### **Yöntem Cells.ImportTwoDimensionArray Eklendi**
Aspose.Cells for .NET API, Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) yöntemini göstererek iki boyutlu dizileri elektronik tablo hücrelerine içe aktarmayı mümkün kılmıştır. Bahsedilen yöntem, iki boyutlu bir veri dizisini, TxtLoadOptions'da tanımlanan daha esnek seçeneklerle bir çalışma sayfasına aktarır.
### **Özellikler OnePagePerSheet, PageIndex & PageCount Eklendi**
Aspose.Cells for .NET 8.3.2, XpsSaveOptions sınıfı için OnePagePerSheet, PageIndex & PageCount özelliklerini kullanıma sundu. Kullanıcı, OnePagePerSheet özelliğini kullanarak bir elektronik tablonun tüm içeriğini tek bir XPS sayfasına sığdırabilir ve/veya PageCount özelliğini kullanarak yazdırılacak sayfa sayısını alabilir. PageIndex özelliği, kaydedilecek ilk sayfanın 0 tabanlı dizinini alır/ayarlar.
### **Özellikler NumberDecimalSeparator & NumberGroupSeparator Eklendi**
Aspose.Cells for .NET 8.3.2, elektronik tablolardaki sayısal değerleri biçimlendirmek ve ayrıştırmak için kullanılan özel ayırıcıları alabilen/ayarlayabilen NumberDecimalSeparator & NumberGroupSeparator özelliklerini tanıttı.

Aşağıdaki örnek kod, Aspose.Cells API kullanılarak Özel Ayırıcıların nasıl belirtileceğini gösterir. Aşağıdaki kod, özel Ondalık ve Grup ayırıcılarını sırasıyla nokta ve boşluk olarak belirtir.

**C#**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Özellik PdfSaveOptions.IsFontSubstitutionCharGranularity Eklendi**
Aspose.Cells for .NET 8.3.2, bazı Unicode karakterlerinin belirli bir yazı tipi ailesi kullanılarak görüntülenememesi sorununun üstesinden gelmek için PdfSaveOptions.IsFontSubstitutionCharGranularity özelliğini ortaya çıkardı. PdfSaveOptions.IsFontSubstitutionCharGranularity özelliği true olarak ayarlandığında, yalnızca belirli bir karakterin görüntülenemeyen yazı tipi görüntülenebilir yazı tipine değiştirilir ve kelimenin veya cümlenin geri kalanı orijinal yazı tipinde kalmalıdır.

**C#**

{{< highlight "csharp" >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Kaldırılan API'ler**
### **Kaldırılan Eski Yöntemler**
Aşağıdaki yöntemler Kamudan kaldırıldı API.

- Workbook.Open & Workbook.Save yöntemleri.
- Workbook.SetOleSize yöntemi.
- Workbook.LoadData yöntemi.
- WorkbookDesigner.Open & WorkbookDesigner.Save yöntemleri.
- WorksheetCollection.DeleteName yöntemi.
### **Eski Mülkler Kaldırıldı**
Aşağıdaki mülkler Kamudan kaldırıldı API.

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
### **Property Workbook.SaveOptions Kullanımdan Kalktı**
Uygun SaveOptions özellikleri ayarlandıktan sonra, bir SaveOptions nesnesinin Workbook.Save yöntemine iletilmesi gerekir.
### **Property Workbook.Styles & Class StyleCollection Kullanımdan Kaldırıldı**
StyleCollection.Add yöntemiyle bir Stil oluşturmak yerine Workbook örneği için stil oluşturmak ve işlemek üzere Workbook.CreateStyle yönteminin kullanılması önerilir. Ayrıca Workbook.GetNamedStyle(string) yöntemi, StyleCollection[string] yerine adlandırılmış stil almak için kullanılabilir.
### **Yöntem PivotItem.Move(int sayısı) Eskimiş**
Aspose.Cells 8.3.2 sürümüyle birlikte API, PivotItem'i üst düğüm içinde taşımak için count için tamsayı parametresini ve boolean parametresini kabul eden PivotItem.Move yöntemine başka bir aşırı yükleme getirdi.
