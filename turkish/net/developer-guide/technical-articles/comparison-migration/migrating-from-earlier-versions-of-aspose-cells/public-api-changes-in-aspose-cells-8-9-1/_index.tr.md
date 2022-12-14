---
title: Genel API Aspose.Cells 8.9.1'deki değişiklikler
type: docs
weight: 310
url: /tr/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.9.0'dan 8.9.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yapılandırılabilir Yazı Tipi Kaynakları**
Aspose.Cells for .NET, elektronik tabloları işlemek için yapılandırılabilir yazı tipi kaynaklarına destek sağlamak üzere bir dizi sınıfı kullanıma sunmuştur. Aspose.Cells 8.9.1 ile eklenen sınıfların listesi aşağıdadır.

1. FontConfigs sınıfı, yazı tipi ayarlarını belirtir.
1. FontSourceBase sınıfı, kullanıcının çeşitli yazı tipi kaynakları belirtmesine izin veren sınıflar için soyut bir temel sınıftır.
1. FileFontSource sınıfı, dosya sisteminde depolanan tek TrueType yazı tipi dosyasını temsil eder.
1. FolderFontSource sınıfı, TrueType yazı tipi dosyalarını içeren klasörü temsil eder.
1. MemoryFontSource sınıfı, bellekte depolanan tek TrueType yazı tipi dosyasını temsil eder.
1. FontSourceType numaralandırması, bir yazı tipi kaynağının türünü belirtir.

Yukarıda belirtilen değişikliklerle, Aspose.Cells for .NET, yazı tiplerini aşağıda ayrıntılı olarak ayarlamanıza olanak tanır.

1. FontConfigs.SetFontFolder yöntemini kullanırken bir özel yazı tipi klasörü ayarlayın.
1. FontConfigs.SetFontFolders yöntemini kullanırken birden fazla özel yazı tipi klasörü ayarlayın.
1. FontConfigs.SetFontSources yöntemini kullanırken özel bir font klasöründen, tek bir font dosyasından veya bir bayt dizisinden font verilerini ayarlayın.

İşte yukarıda belirtilen yöntemlerin basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.SetFontFolder & FontConfigs.SetFontFolders yöntemlerinin her ikisi de bir Boole tipi ikinci parametreyi kabul eder. True'yu ikinci parametre olarak iletmek, Aspose.Cells API'lerini yazı tipi dosyaları için alt klasörleri aramaya yönlendirecektir.

{{% /alert %}} 

Aspose.Cells for .NET ayrıca yazı tipi değiştirmeyi yapılandırmaya izin verir. Bu mekanizma, dönüştürmenin gerçekleşmesi gereken makinede gerekli bir yazı tipi bulunmadığında yardımcı olur. Kullanıcılar, başlangıçta gerekli olan yazı tipine alternatif olarak bir yazı tipi adları listesi sağlayabilir. Bunu başarmak için Aspose.Cells API'leri, 2 parametreyi kabul eden FontConfigs.SetFontSubstitutes yöntemini kullanıma sunmuştur. İlk parametre, değiştirilmesi gereken yazı tipinin adı olması gereken dize türündedir. İkinci parametre, string türünde bir dizidir. Kullanıcılar, orijinal yazı tipi adının (ilk parametrede belirtilen) yerine geçen bir yazı tipi adları listesi sağlayabilir.

İşte FontConfigs.SetFontSubstitutes yönteminin basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET, hangi kaynakların ve ikamelerin ayarlandığı hakkında bilgi toplamak için araçlar da sağlamıştır.

1. FontConfigs.GetFontSources yöntemi, belirtilen yazı tipi kaynaklarının listesini içeren FontSourceBase türünde bir dizi döndürür. Hiçbir kaynağın ayarlanmamış olması durumunda, FontConfigs.GetFontSources yöntemi boş bir dizi döndürür.
1. FontConfigs.GetFontSubstitutes yöntemi, bir ikamenin ayarlandığı yazı tipi adını belirtmeye izin veren dize türünde bir parametre kabul eder. Belirtilen yazı tipi adı için herhangi bir ikame ayarlanmamışsa, FontConfigs.GetFontSubstitutes yöntemi null değerini döndürür.

{{% alert color="primary" %}} 

 FontConfig'ler hakkında daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Elektronik Tabloları Oluşturmak için Yazı Tiplerini Yapılandırma](/cells/tr/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **IFilePathProvider Arayüzü & HtmlSaveOptions.FilePathProvider özelliği eklendi**
Aspose.Cells for .NET 8.9.1, çalışma sayfalarını ayrı HTML dosyalarına dışa aktarmak için IFilePathProvider'ın alınmasına/ayarlanmasına izin verir. Bu yeni API'ler, bir çalışma sayfasındaki köprülerin başka bir çalışma sayfasındaki bir konuma işaret ettiği ve uygulama gereksiniminin her çalışma sayfasını ayrı bir HTML dosyasına dönüştürmek olduğu senaryolarda yardımcı olur. IFilePathProvider'ı uygulamak, sonuçta ortaya çıkan ayrı bir HTML dosyasında bir konuma işaret ediyor olsalar da yukarıda belirtilen köprülerin bozulmadan kalmasına izin verir.

HtmlSaveOptions.FilePathProvider özelliğinin basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Çalışma Kitabı örneğine bir elektronik tablo yükleyin

var book = new Workbook(dir + "sample.xlsx");

// Her Çalışma Sayfasını HTML dosyasını ayırmak için kaydedin

 için (int ben = 0; ben< book.Worksheets.Count; i++)

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



IFilePathProvider arabiriminin nasıl uygulanacağı aşağıda açıklanmıştır.

**C#**

{{< highlight "csharp" >}}

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

 Bu geliştirme hakkında daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[IFilePathProvider Arayüzünü Uygulama](/cells/tr/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Cells.CopyRows Yöntemi için CopyOptions.ReferToDestinationSheet Özelliği ve Aşırı Yükleme eklendi**
Aspose.Cells for .NET API, kopyalanacak satırlar aynı zamanda bir grafik ve bunun veri kaynağını içerdiğinde satırları kopyalama işlemini kolaylaştırmak için Cells.CopyRows yönteminin aşırı yüklemesiyle birlikte Boole tipi CopyOptions.ReferToDestinationSheet özelliğini kullanıma sundu. Geliştiriciler, grafiğin veri kaynağını kaynak veya hedef çalışma sayfalarına yönlendirmek için bu yeni API'leri kullanabilir.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Satırları Kopyalarken Grafiğin Veri Kaynağını Kontrol Edin](/cells/tr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **CalculationOptions.Recursive Özelliği Eklendi**
Aspose.Cells for .NET 8.9.1, Boole tipi CalculationOptions.Recursive özelliğini kullanıma sundu. CalculationOptions.Recursive özelliğinin true olarak ayarlanması ve nesnenin Workbook.CalculateFormula yöntemine iletilmesi, Aspose.Cells API'lerini, diğer hücrelere bağlı olan hücreleri hesaplarken bağımlı hücreleri yinelemeli olarak hesaplamaya yönlendirir.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Hesaplama Süresini Optimize Edin](/cells/tr/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Eski API'ler**
### **Eski CellsHelper.FontDir Özellik**
FontConfigs.SetFontFolder(string, bool) yöntemini, bunun yerine yinelemeli klasör ile false olarak kullanmanız önerilir.
### **Eski CellsHelper.FontDirs Özelliği**
FontConfigs.SetFontFolders(string[], bool) yöntemini, bunun yerine yinelemeli klasör ile false olarak kullanın.
### **Eski CellsHelper.FontFiles Özelliği**
Bunun yerine FontConfigs.SetFontSources(FontSourceBase[]) yöntemini kullanın.
