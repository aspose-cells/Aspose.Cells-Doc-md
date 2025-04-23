---
title: Aspose.Cells 8.9.1 deki Genel API Değişiklikleri
type: docs
weight: 310
url: /tr/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.9.0'dan 8.9.1'e yapılan değişiklikleri modül/uygulama geliştiricilerinin ilgisini çekebilecek şekilde açıklar. Sadece yeni ve güncellenmiş genel yöntemleri, eklenmiş ve kaldırılmış sınıfları vb. içermekle kalmaz, aynı zamanda Aspose.Cells'in arka plandaki davranışında herhangi bir değişikliğin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Yapılandırılabilir Yazı Tipi Kaynakları**
Aspose.Cells for .NET, elektronik tabloları render etme için yapılandırılabilir yazı tipi kaynaklarını desteklemek için bir dizi sınıfı açıklamıştır. Aşağıda Aspose.Cells for .NET 8.9.1 ile eklenen sınıfların listesi bulunmaktadır.

1. FontConfigs sınıfı yazı tipi ayarlarını belirtir.
1. FontSourceBase sınıfı, kullanıcının çeşitli yazı tipi kaynaklarını belirtmesini sağlayan sınıflar için soyut bir temel sınıftır.
1. FileFontSource sınıfı, dosya sistemine depolanan tek TrueType yazı tipi dosyasını temsil eder.
1. FolderFontSource sınıfı, TrueType yazı tipi dosyalarını içeren klasörü temsil eder.
1. MemoryFontSource sınıfı, bellekte depolanan tek TrueType yazı tipi dosyasını temsil eder.
1. FontSourceType numaralandırması bir yazı tipi kaynağının türünü belirtir.

Yukarıda belirtilen değişikliklerle, Aspose.Cells for .NET aşağıda ayrıntılı olarak belirtildiği gibi yazı tiplerini ayarlamaya izin verir.

1. FontConfigs.SetFontFolder yöntemini kullanırken özel bir yazı tipi klasörü ayarlayın.
1. FontConfigs.SetFontFolders yöntemini kullanırken birçok özel yazı tipi klasörü ayarlayın.
1. FontConfigs.SetFontSources yöntemini kullanırken özel bir yazı tipi klasöründen, tek bir yazı tipi dosyasından veya bayt dizisinden yazı tipi kaynakları ayarlayın.

Yukarıda belirtilen yöntemlerin basit kullanım senaryosu aşağıda verilmiştir.

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.SetFontFolder ve FontConfigs.SetFontFolders yöntemleri her ikisi de ikinci bir parametre olarak Boolean türünü kabul eder. İkinci parametre olarak true geçmek, Aspose.Cells API'larının yazı tipleri dosyaları için alt klasörleri aramasını sağlayacaktır.

{{% /alert %}} 

Aspose.Cells for .NET, dönüşümün gerçekleştiği makinede gereken yazı tipi bulunmadığında yardımcı olabilecek bir mekanizma da sağlar. Kullanıcılar, 2 parametre kabul eden FontConfigs.SetFontSubstitutes yöntemini kullanabilir. İlk parametre, yerine konulması gereken yazı tipi adı olmalıdır. İkinci parametre dizi türünde olup, alternatif yazı tipleri listesi sağlar.

FontConfigs.SetFontSubstitutes yönteminin basit kullanım senaryosu aşağıda verilmiştir.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET, belirtilen kaynakları ve yerine koymaları toplamak için de araçlar sağlar.

1. FontConfigs.GetFontSources yöntemi, belirtilen yazı tipi kaynaklarının listesini içeren FontSourceBase türünde bir dizi döndürür. Hiçbir kaynak belirlenmemişse, FontConfigs.GetFontSources yöntemi boş bir dizi döndürür.
1. FontConfigs.GetFontSubstitutes yöntemi, yerine koyma yapılan yazı tipi adını belirlemek için dize türünde bir parametre kabul eder. Belirtilen yazı tipi adı için hiçbir yerine koyma belirlenmemişse, FontConfigs.GetFontSubstitutes yöntemi null döndürecektir.

{{% alert color="primary" %}} 

FontConfigs hakkında daha fazla bilgi için, [Hücre Ele Algoritması için Yazı Tiplerini Yapılandırma](/cells/tr/net/configuring-fonts-for-rendering-spreadsheets/) makalesini inceleyin.

{{% /alert %}} 
### **IFilePathProvider Arayüzü ve HtmlSaveOptions.FilePathProvider özelliği eklendi**
Aspose.Cells for .NET 8.9.1, çalışsayfalarını ayrı HTML dosyalarına dışa aktarmak için IFilePathProvider almasına ve ayarlamasına olanak sağlar. Bu yeni API'ler, bir çalışsayfadaki hiperbağlantıların başka bir çalışsayfada bir konuma işaret ettiği senaryolarda faydalıdır ve uygulama gereksinimi, her çalışsayfayı ayrı bir HTML dosyasına dönüştürmektir. IFilePathProvider'ı uygulamak, bahsedilen hiperbağlantıların, ayrı sonuç HTML dosyasına işaret ediyor olsalar da orijinallerini korumayı sağlar.

HtmlSaveOptions.FilePathProvider özelliğinin basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



IFilePathProvider arayüzünü uygulamanın nasıl olduğu aşağıda özetlenmiştir.

**C#**

{{< highlight csharp >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Bu geliştirme hakkında daha fazla bilgi için, [IFilePathProvider Arayüzünü Uygulama](/cells/tr/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/) makalesine göz atın.

{{% /alert %}} 
### **CopyOptions.ReferToDestinationSheet Özelliği ve Cells.CopyRows Yöntemi için aşırı yükleme eklendi.**
Aspose.Cells for .NET API'si, hücreleri kopyalamak için kullanılan aşırı yükleme ile birlikte Boolean türünde CopyOptions.ReferToDestinationSheet özelliğini ortaya çıkarmıştır. Geliştiriciler, yeni bu API'leri kullanarak kopyalanacak hücrelerin aynı zamanda bir grafik ve veri kaynağı içerdiği durumda, grafik veri kaynağını kaynak veya hedef çalışsayfalara yönlendirebilirler.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Bu özellik hakkında daha fazla bilgi için, [Satırları Kopyalarken Grafiğin Veri Kaynağını Kontrol Etme](/cells/tr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/) makalesine göz atın.

{{% /alert %}} 
### **CalculationOptions.Recursive Özelliği eklendi**
Aspose.Cells for .NET 8.9.1, Boolean türünde CalculationOptions.Recursive özelliğini ortaya çıkarmıştır. CalculationOptions.Recursive özelliğini doğru olarak ayarlamak ve nesneyi Workbook.CalculateFormula yöntemine iletme, bağımlı hücreleri hesaplarken Aspose.Cells API'larını diğer hücrelere bağlı olarak rekürsif olarak hesaplamaya yönlendirir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Bu özellik hakkında daha fazla bilgi için, [Hesaplama Zamanını Optimize Etme](/cells/tr/net/decrease-the-calculation-time-of-cell-calculate-method/) makalesine göz atın.

{{% /alert %}}
## **Eskimiş API'lar**
### **Eski CellsHelper.FontDir Özelliği**
FontConfigs.SetFontFolder(string, bool) yönteminin, recursive özelliği false olarak klasör kullanımı önerilir.
### **Eski CellsHelper.FontDirs Özelliği**
FontConfigs.SetFontFolders(string[], bool) yönteminin, recursive özelliği false olarak klasör kullanımı önerilir.
### **Eski CellsHelper.FontFiles Özelliği**
FontConfigs.SetFontSources(FontSourceBase[]) yöntemi kullanımı önerilir.
{{< app/cells/assistant language="csharp" >}}
