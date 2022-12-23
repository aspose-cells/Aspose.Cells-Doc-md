---
title: Akıllı İşaretleyicileri İşleyerek Grafik Oluşturun
type: docs
weight: 180
url: /tr/java/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells API'ler, WorkbookDesigner sınıfının, biçimlendirmenin ve formüllerin tasarımcı elektronik tablolarına yerleştirildiği ve ardından verileri Akıllı İşaretleyicilere göre doldurmak için belirtilen veri kaynaklarına göre işlendiği Akıllı İşaretleyicilerle çalışmasını sağlar. Aşağıdaki adımları gerektiren Akıllı İşaretleyicileri işleyerek Excel grafikleri oluşturmak da mümkündür.

- Tasarımcı e-tablosunun oluşturulması
- Belirtilen veri kaynağına göre tasarımcı elektronik tablosu işleniyor
- Doldurulmuş verilere dayalı grafiğin oluşturulması

{{% /alert %}} 
## **Tasarımcı Elektronik Tablosunun Oluşturulması**
Bir tasarımcı elektronik tablosu, Microsoft Excel uygulaması veya Aspose.Cells API'leri ile oluşturulmuş, içeriğin çalışma zamanında doldurulacağı görsel biçimlendirmeyi, formülleri ve akıllı işaretçileri içeren basit bir Excel dosyasıdır.

{{% alert color="primary" %}} 

 Akıllı İşaretleyiciler hakkında detaylı bilgi mevcuttur[Burada](/cells/tr/java/smart-markers/).

{{% /alert %}} 

Basitlik adına, Aspose.Cells for Java API'i kullanarak tasarımcı elektronik tablosunu oluşturacağız ve daha sonra gösteri amacıyla dinamik olarak oluşturulmuş bir veri kaynağına karşı işleyeceğiz.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access the first (default) Worksheet from the collection

Worksheet dataSheet = book.getWorksheets().get(0);

//Name the first Worksheet for referencing

dataSheet.setName("ChartData");

//Access the CellsCollection of ChartData Worksheet

Cells cells = dataSheet.getCells();

//Place the markers in the Worksheet according to desired layout

cells.get("A1").putValue("&=$Headers(horizontal)");

cells.get("A2").putValue("&=$Year2000(horizontal)");

cells.get("A3").putValue("&=$Year2005(horizontal)");

cells.get("A4").putValue("&=$Year2010(horizontal)");

cells.get("A5").putValue("&=$Year2015(horizontal)");

{{< /highlight >}}

Bu aşamada ortaya çıkan elektronik tabloyu kaydederseniz, çalışma tablosundaki veriler aşağıdaki gibi görünecektir.

![yapılacaklar:resim_alternatif_metin](generate-chart-by-processing-smart-markers_1.png)
## **İşleme Tasarımcısı Elektronik Tablosu**
 Tasarımcı elektronik tablosunu işlemek için, tasarımcı elektronik tablosunda kullanılan Akıllı İşaretleyicilere karşılık gelen bir veri kaynağına sahip olmamız gerekir. Örneğin, şu şekilde bir Akıllı İşaretleyici girişi oluşturduk:**&=$Başlıklar(yatay)** değişkeni Headers adına göre temsil ederken, anahtar**(yatay)** verilerin yatay olarak doldurulması gerektiğini önerir.

Bu kullanım örneğini göstermek için, veri kaynağını sıfırdan oluşturacağız ve onu önceki adımda oluşturulan tasarımcı elektronik tablosuna göre işleyeceğiz. Ancak, gerçek zamanlı senaryoda, veriler daha sonraki işlemler için zaten mevcut olabilir, bu nedenle veriler zaten mevcutsa veri kaynağının oluşturulmasını atlayabilirsiniz.

**Java**

{{< highlight "csharp" >}}

 //Create string arrays which will serve as data sources to the smart markers

String[]headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[]year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[]year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[]year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[]year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

Akıllı İşaretleyicilerin işlenmesi aşağıdaki gibi oldukça basittir.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner();

//Set the Workbook property for the instance of WorkbookDesigner

designer.setWorkbook(book);

//Set data sources for smart markers

designer.setDataSource("Headers", headers);

designer.setDataSource("Year2000", year2000);

designer.setDataSource("Year2005", year2005);

designer.setDataSource("Year2010", year2010);

designer.setDataSource("Year2015", year2015);

//Process the designer spreadsheet against the provided data sources

designer.process();

{{< /highlight >}}

Bu aşamada elektronik tabloyu kaydederseniz, veriler aşağıdaki gibi görünecektir.

![yapılacaklar:resim_alternatif_metin](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Yukarıdaki kod parçacığı, ilk adımda oluşturulan Workbook sınıfının mevcut örneğini kullanır. Diskte veya bellekte tasarımcı elektronik tablosu dosyanız zaten varsa, mevcut tasarımcı elektronik tablosunu yükleyerek Workbook sınıfının bir örneğini oluşturabilirsiniz.

{{% /alert %}} 
## **Grafiğin Oluşturulması**
Veriler yerleştirildikten sonra, tek yapmamız gereken veri kaynağına dayalı bir grafik oluşturmaktır. Örneği basit tutmak için, grafiği daha fazla yapılandırmamıza gerek kalmaması için Chart.setChartDataRange yöntemini kullanacağız.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Son tablo aşağıdaki gibi görünüyor.

![yapılacaklar:resim_alternatif_metin](generate-chart-by-processing-smart-markers_3.png)
