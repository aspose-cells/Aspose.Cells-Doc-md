---
title: Aspose.Cells 8.9.1 deki Genel API Değişiklikleri
type: docs
weight: 320
url: /tr/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.9.0'dan 8.9.1'e yapılan değişiklikleri modül/uygulama geliştiricilerinin ilgisini çekebilecek şekilde açıklar. Sadece yeni ve güncellenmiş genel yöntemleri, eklenmiş ve kaldırılmış sınıfları vb. içermekle kalmaz, aynı zamanda Aspose.Cells'in arka plandaki davranışında herhangi bir değişikliğin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Yapılandırılabilir Yazı Tipi Kaynakları**
Aspose.Cells for Java, elektronik tabloları renderlamak için yapılandırılabilir yazı tipi kaynaklarını desteklemek için bir dizi sınıfı açıklar. İşte Aspose.Cells for Java 8.9.1 ile eklenen sınıfların listesi.

1. FontConfigs sınıfı yazı tipi ayarlarını belirtir.
1. FontSourceBase sınıfı, kullanıcının çeşitli yazı tipi kaynaklarını belirtmesini sağlayan sınıflar için soyut bir temel sınıftır.
1. FileFontSource sınıfı, dosya sistemine depolanan tek TrueType yazı tipi dosyasını temsil eder.
1. FolderFontSource sınıfı, TrueType yazı tipi dosyalarını içeren klasörü temsil eder.
1. MemoryFontSource sınıfı, bellekte depolanan tek TrueType yazı tipi dosyasını temsil eder.
1. FontSourceType numaralandırması bir yazı tipi kaynağının türünü belirtir.

Yukarıda belirtilen değişikliklerle, Aspose.Cells for Java, aşağıda ayrıntıları belirtilmiş olan yazı tiplerini ayarlamayı mümkün kılar.

1. FontConfigs.setFontFolder yöntemini kullanırken özel bir yazı tipi klasörü ayarlayın.
1. FontConfigs.setFontFolders yöntemini kullanırken birden fazla özel yazı tipi klasörü ayarlayın.
1. FontConfigs.setFontSources yöntemini kullanırken özel yazı tipi klasöründen, tek bir yazı tipi dosyasından veya bayt dizisinden yazı tipi kaynaklarını ayarlayın.

Yukarıda belirtilen yöntemlerin basit kullanım senaryosu aşağıda verilmiştir.

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

FontConfigs.setFontFolder ve FontConfigs.setFontFolders yöntemleri, ikinci parametre olarak Boolean türünde bir değer kabul eder. İkinci parametre olarak true geçmek, Aspose.Cells API'larını font dosyaları için alt klasörleri aramak üzere yönlendirecektir. 

{{% /alert %}} 

Aspose.Cells for Java, ayrıca yazı tipi yerine koymayı yapılandırmak için de izin verir. Bu mekanizma, dönüştürmenin gerçekleşeceği makinede gereken bir yazı tipinin bulunmaması durumunda yardımcı olur. Kullanıcılar, Aspose.Cells API'ları tarafından sunulan FontConfigs.setFontSubstitutes yöntemini kullanarak asıl gereken yazı tipinin yerine koymak için bir dizi yazı tipi adı sağlayabilir. FontConfigs.setFontSubstitutes yöntemi, 2 parametre kabul eder. İlk parametre, yerine konması gereken yazı tipinin adı olmalıdır. İkinci parametre, string türünde bir dizi olup kullanıcılar orijinal yazı tipinin yerine konması için bir yazı tipi listesi sağlayabilir.

FontConfigs.SetFontSubstitutes yönteminin basit kullanım senaryosu aşağıda verilmiştir.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Aspose.Cells for Java, ayrıca hangi kaynakların ve yerine koymaların ayarlandığı bilgilerini toplamanın da bir yolunu sağlar.

1. FontConfigs.getFontSources yöntemi, belirtilen yazı tipi kaynaklarının listesini içeren FontSourceBase türünde bir dizi döndürür. Hiçbir kaynak belirlenmemişse, FontConfigs.getFontSources yöntemi boş bir dizi döndürecektir.
1. FontConfigs.getFontSubstitute yöntemi, yazı tipi yerine koyması belirlenmiş bir yazı tipi için belirtilmiş olan fontadını kabul eden bir parametre alır. Belirtilen yazı tipi için herhangi bir yerine koyma belirlenmemişse, FontConfigs.getFontSubstitutes yöntemi null döndürecektir.

{{% alert color="primary" %}} 

Daha fazla FontConfigs detayı için lütfen [Çizelgeleri Görselleştirmek İçin Yazı Tiplerini Yapılandırmak](/cells/tr/java/configuring-fonts-for-rendering-spreadsheets/) makalesine göz atın.

{{% /alert %}} 
### **IFilePathProvider Arayüzü ve HtmlSaveOptions.FilePathProvider özelliği eklendi**
Aspose.Cells for Java 8.9.1 sayesinde çalışma sayfalarını ayrı HTML dosyalarına dışa aktarma için IFilePathProvider'ın alınmasına ve ayarlanmasına izin verir. Bu yeni API'lar, bir çalışma sayfasındaki hiperbağlantıların başka bir çalışma sayfasına yerleşim oluşturduğu senaryolarda yardımcıdır ve uygulamanın her çalışma sayfasını ayrı bir HTML dosyasına dönüştürme gereksinimini karşılar. IFilePathProvider'ı uygulamak, bahsedilen hiperbağlantıları, ayrı bir sonuç HTML dosyasına da işaretlense bile, korumaya izin verir.

HtmlSaveOptions.FilePathProvider özelliğinin basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

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

Bu geliştirme hakkında daha fazla detay için lütfen [IFilePathProvider Arayüzünü Uygulamak](/cells/tr/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/) makalesine göz atın.

{{% /alert %}} 
### **CopyOptions.ReferToDestinationSheet Özelliği ve Cells.copyRows Metodunun Overload'u eklendi**
Aspose.Cells for Java API, kopyalanacak satırların aynı zamanda bir grafik ve veri kaynağı içerdiği durumlarda satırları kopyalamayı kolaylaştırmak için Boolean türünde CopyOptions.ReferToDestinationSheet özelliğini ve Cells.copyRows metodunun overload'unu açığa çıkardı. Geliştiriciler, bu yeni API'ları kullanarak, grafik veri kaynağını kaynak veya hedef çalışma sayfasına yönlendirebilirler.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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

Bu özellik hakkında daha fazla detay için lütfen [Satırları Kopyalarken Grafiklerin Veri Kaynağını Kontrol Etme](/cells/tr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/) makalesine göz atın.

{{% /alert %}} 
### **CalculationOptions.Recursive Özelliği eklendi**
Aspose.Cells for Java 8.9.1, Boolean türünde CalculationOptions.Recursive özelliğini açığa çıkardı. CalculationOptions.Recursive özelliğini true olarak ayarlamak ve nesneyi Workbook.calculateFormula metoduna iletmek, Aspose.Cells API'lerini, diğer hücrelere bağımlı olan hücreleri hesaplarken bağımlı hücreleri de özyineli olarak hesaplamaya yönlendirir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Bu özellik hakkında daha fazla detay için lütfen [Hesaplama Süresini Optimize Etme](/cells/tr/java/decrease-the-calculation-time-of-cell-calculate-method/) makalesine göz atın.

{{% /alert %}}
## **Eskimiş API'lar**
### **Eski CellsHelper.FontDir Özelliği**
Eski CellsHelper.FontDir özelliğinin recursive olarak false ayarlanmış FontConfigs.setFontFolder(String, boolean) yöntemini kullanmanız önerilir.
### **Eski CellsHelper.FontDirs Özelliği**
Eski CellsHelper.FontDirs özelliğinin recursive olarak false ayarlanmış FontConfigs.setFontFolders(String[], boolean) yöntemini kullanmanız önerilir.
### **Eski CellsHelper.FontFiles Özelliği**
Eski CellsHelper.FontFiles özelliğinin FontConfigs.setFontSources(FontSourceBase[]) yöntemi ile değiştirilmiştir.
