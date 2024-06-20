---
title: Akıllı İşaretlerin İşlenmesiyle Grafik Oluşturma
type: docs
weight: 180
url: /tr/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells API'leri, Smart Markers ile çalışmak için WorkbookDesigner sınıfını sağlar; burada biçimlendirme ve formüller tasarımcı elektronik tablolarına yerleştirilir ve ardından belirtilen veri kaynağı(ları)na göre veri akıllı işaretlere göre doldurularak Excel grafikleri oluşturulabilir. Bu şu adımları gerektirir:

- Tasarımcı elektronik tablosunun oluşturulması
- Belirtilen veri kaynağına göre tasarımcı elektronik tablonun işlenmesi
- Popüle edilmiş veriye dayalı olarak grafik oluşturulması

{{% /alert %}} 
## **Tasarımcı Tablonun Oluşturulması**
Bir tasarımcı tablo, Microsoft Excel uygulaması veya Aspose.Cells API'leri ile oluşturulan basit bir Excel dosyasıdır. Görsel biçimlendirme, formüller ve akıllı işaretçiler içerir ve içerikler çalışma zamanında doldurulur.

{{% alert color="primary" %}} 

Akıllı İşaretçiler hakkında detaylı bilgi [burada](/cells/tr/java/smart-markers/) bulunmaktadır.

{{% /alert %}} 

Basitlik açısından tasarımcı tabloyu Aspose.Cells for Java API kullanarak oluşturacağız ve daha sonra gösterim amaçları için dinamik olarak oluşturulmuş bir veri kaynağına karşı işleyeceğiz.

**Java**

{{< highlight csharp >}}

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

Bu aşamada oluşan tabloyu kaydedersek, çalışma sayfasındaki veriler aşağıdaki gibi görünecek.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **Tasarımcı Tablonun İşlenmesi**
Tasarımcı tablonun işlenmesi için, tasarımcı tabloda kullanılan Akıllı İşaretçilere uygun bir veri kaynağına sahip olmalıyız. Örneğin, **&=$Headers(horizontal)** gibi bir Akıllı İşaretçi girişi oluşturduk, bu, Headers adındaki değişkeni temsil ederken **(horizontal)** anahtarının ise verinin yatay olarak doldurulmasını önerdiğini gösterir.

Bu kullanım durumunu göstermek için veri kaynağını sıfırdan oluşturacağız ve bu durumda tasarımcı tablo karşısında işlem yapacağız. Ancak gerçek zamanlı senaryoda veri zaten mevcut olabilir, bu durumda veri kaynağının oluşturulmasını atlayabilirsiniz.

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

Akıllı İşaretçilerin İşlenmesi oldukça basittir ve aşağıdaki gibidir.

**Java**

{{< highlight csharp >}}

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

Bu aşamada tabloyu kaydedersek, veri aşağıdaki gibi görünecektir.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Yukarıdaki kod parçacığı, ilk adımda oluşturulan Workbook sınıfının mevcut örneğini kullanır. Eğer zaten diskte ya da hafızada tasarımcı tablo dosyasınız varsa, mevcut tasarımcı tablosunu yükleyerek Workbook sınıfının bir örneğini oluşturabilirsiniz.

{{% /alert %}} 
## **Grafik Oluşturulması**
Veri hazır olduğunda yapmamız gereken tek şey, veri kaynağına dayalı bir grafik oluşturmaktır. Örneği basit tutmak için, Chart.setChartDataRange yöntemini kullanacağız, böylece grafikleri daha fazla yapılandırmamız gerekmez.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Son grafik aşağıdaki gibi görünmektedir.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
