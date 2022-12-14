---
title: Genel API Aspose.Cells 8.9.1'deki değişiklikler
type: docs
weight: 320
url: /tr/java/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.9.0'dan 8.9.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yapılandırılabilir Yazı Tipi Kaynakları**
Aspose.Cells for Java, elektronik tabloları işlemek için yapılandırılabilir yazı tipi kaynaklarına destek sağlamak üzere bir dizi sınıfı kullanıma sunmuştur. Aspose.Cells 8.9.1 ile eklenen sınıfların listesi aşağıdadır.

1. FontConfigs sınıfı, yazı tipi ayarlarını belirtir.
1. FontSourceBase sınıfı, kullanıcının çeşitli yazı tipi kaynakları belirtmesine izin veren sınıflar için soyut bir temel sınıftır.
1. FileFontSource sınıfı, dosya sisteminde depolanan tek TrueType yazı tipi dosyasını temsil eder.
1. FolderFontSource sınıfı, TrueType yazı tipi dosyalarını içeren klasörü temsil eder.
1. MemoryFontSource sınıfı, bellekte depolanan tek TrueType yazı tipi dosyasını temsil eder.
1. FontSourceType numaralandırması, bir yazı tipi kaynağının türünü belirtir.

Yukarıda belirtilen değişikliklerle, Aspose.Cells for Java, yazı tiplerini aşağıda ayrıntılı olarak ayarlamanıza olanak tanır.

1. FontConfigs.setFontFolder yöntemini kullanırken bir özel yazı tipi klasörü ayarlayın.
1. FontConfigs.setFontFolders yöntemini kullanırken birden fazla özel yazı tipi klasörü ayarlayın.
1. FontConfigs.setFontSources yöntemini kullanırken özel bir font klasöründen, tek bir font dosyasından veya bir bayt dizisinden font verilerini ayarlayın.

İşte yukarıda belirtilen yöntemlerin basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[]{ fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[]bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

 FontConfigs.setFontFolder & FontConfigs.setFontFolders yöntemlerinin her ikisi de bir Boole tipi ikinci parametreyi kabul eder. True'yu ikinci parametre olarak iletmek, Aspose.Cells API'lerini yazı tipi dosyaları için alt klasörleri aramaya yönlendirecektir.

{{% /alert %}} 

Aspose.Cells for Java ayrıca yazı tipi değiştirmeyi yapılandırmaya izin verir. Bu mekanizma, dönüştürmenin gerçekleşmesi gereken makinede gerekli bir yazı tipi bulunmadığında yardımcı olur. Kullanıcılar, başlangıçta gerekli olan yazı tipine alternatif olarak bir yazı tipi adları listesi sağlayabilir. Bunu başarmak için Aspose.Cells API'leri, 2 parametreyi kabul eden FontConfigs.setFontSubstitutes yöntemini kullanıma sunmuştur. İlk parametre, değiştirilmesi gereken yazı tipinin adı olması gereken dize türündedir. İkinci parametre, string türünde bir dizidir. Kullanıcılar, orijinal yazı tipi adının (ilk parametrede belirtilen) yerine geçen bir yazı tipi adları listesi sağlayabilir.

İşte FontConfigs.SetFontSubstitutes yönteminin basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java, hangi kaynakların ve ikamelerin ayarlandığı hakkında bilgi toplamak için araçlar da sağlamıştır.

1. FontConfigs.getFontSources yöntemi, belirtilen yazı tipi kaynaklarının listesini içeren FontSourceBase türünde bir dizi döndürür. Hiçbir kaynağın ayarlanmamış olması durumunda, FontConfigs.getFontSources yöntemi boş bir dizi döndürür.
1. FontConfigs.getFontSubstitutes yöntemi, bir ikamenin ayarlandığı yazı tipi adını belirtmeye izin veren dize türünde bir parametre kabul eder. Belirtilen yazı tipi adı için herhangi bir ikame ayarlanmamışsa, FontConfigs.getFontSubstitutes yöntemi null döndürür.

{{% alert color="primary" %}} 

 FontConfig'ler hakkında daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Elektronik Tabloları Oluşturmak için Yazı Tiplerini Yapılandırma](/cells/tr/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **IFilePathProvider Arayüzü & HtmlSaveOptions.FilePathProvider özelliği eklendi**
Aspose.Cells for Java 8.9.1, çalışma sayfalarını ayrı HTML dosyalarına dışa aktarmak için IFilePathProvider'ın alınmasına/ayarlanmasına izin verir. Bu yeni API'ler, bir çalışma sayfasındaki köprülerin başka bir çalışma sayfasındaki bir konuma işaret ettiği ve uygulama gereksiniminin her çalışma sayfasını ayrı bir HTML dosyasına dönüştürmek olduğu senaryolarda yardımcı olur. IFilePathProvider'ı uygulamak, sonuçta ortaya çıkan ayrı bir HTML dosyasında bir konuma işaret ediyor olsalar da yukarıda belirtilen köprülerin bozulmadan kalmasına izin verir.

HtmlSaveOptions.FilePathProvider özelliğinin basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Çalışma Kitabı örneğine bir elektronik tablo yükleyin

Çalışma kitabı kitabı = yeni Çalışma Kitabı(dir + "sample.xlsx");

//Her Çalışma Sayfasını HTML dosyasını ayırmak için kaydedin

 için (int ben = 0; ben< book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

 Bu geliştirme hakkında daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[IFilePathProvider Arayüzünü Uygulama](/cells/tr/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Cells.copyRows Yöntemi için CopyOptions.ReferToDestinationSheet Özelliği ve Aşırı Yükleme eklendi**
Aspose.Cells for Java API, kopyalanacak satırlar aynı zamanda bir grafik ve bunun veri kaynağını içerdiğinde satırları kopyalama işlemini kolaylaştırmak için Boole tipi CopyOptions.ReferToDestinationSheet özelliğini ve Cells.copyRows yönteminin aşırı yüklemesini kullanıma sundu. Geliştiriciler, grafiğin veri kaynağını kaynak veya hedef çalışma sayfalarına yönlendirmek için bu yeni API'leri kullanabilir.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Satırları Kopyalarken Grafiğin Veri Kaynağını Kontrol Edin](/cells/tr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **CalculationOptions.Recursive Özelliği Eklendi**
Aspose.Cells for Java 8.9.1, Boole tipi CalculationOptions.Recursive özelliğini kullanıma sundu. CalculationOptions.Recursive özelliğinin true olarak ayarlanması ve nesnenin Workbook.calculateFormula yöntemine iletilmesi, Aspose.Cells API'lerini, diğer hücrelere bağlı olan hücreleri hesaplarken bağımlı hücreleri yinelemeli olarak hesaplamaya yönlendirir.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Hesaplama Süresini Optimize Edin](/cells/tr/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **Eski API'ler**
### **Eski CellsHelper.FontDir Özellik**
FontConfigs.setFontFolder(String, boolean) yöntemini, bunun yerine yinelemeli klasör ile false olarak kullanmanız önerilir.
### **Eski CellsHelper.FontDirs Özelliği**
FontConfigs.setFontFolders(String[], boolean) yöntemini bunun yerine yinelemeli klasör ile false olarak kullanın.
### **Eski CellsHelper.FontFiles Özelliği**
Bunun yerine FontConfigs.setFontSources(FontSourceBase[]) yöntemini kullanın.
