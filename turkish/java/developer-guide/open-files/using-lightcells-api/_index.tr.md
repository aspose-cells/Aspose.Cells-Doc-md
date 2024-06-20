---
title: LightCells API sını Kullanma
type: docs
weight: 80
url: /tr/java/using-lightcells-api/
---

{{% alert color="primary" %}}

Bazen büyük veri kümesine sahip Microsoft Excel dosyalarını okuyup yazmanız gerekir. LightCells API, büyük Excel elektronik tabloları oluşturmak için kullanışlıdır: bu sayede hafıza ihtiyacı azalır ve daha iyi performans ve verimlilik elde edilir.

{{% /alert %}}

## **Olay Temelli Mimarilik**

Aspose.Cells, özellikle bellekte bir veri modeli bloğu oluşturmadan hücre verilerini bir bir işlemek için tasarlanmış olan LightCells API'sını sağlar (Hücre koleksiyonu vb. kullanılmadan). Olay temelli modda çalışır.

Çalışma kitaplarını kaydetmek için kaydederken hücre içeriğini hücre hücre sağlayın ve bileşen bunu doğrudan çıktı dosyasına kaydeder.

Şablon dosyalarını okurken bileşen her hücreyi ayrı ayrı ayrıştırır ve değerlerini tek tek sağlar.

Her iki süreçte de bir Cell nesnesi işlenir ve ardından atılır, Workbook nesnesi koleksiyonu tutmaz. Bu modda, dolayısıyla, çok miktarda bellek kullanan büyük veri kümesi barındıran Microsoft Excel dosyasının içe aktarımı ve dışa aktarımı sırasında bellek kaydedilir.

LightCells API, XLSX ve XLS dosyaları için hücreleri aynı şekilde işlemesine rağmen (bütün hücreleri belleğe yüklemez ama bir hücreyi işler ve ardından atar), XLSX dosyaları için XLS dosyalarına göre belleği daha etkili bir şekilde saklar çünkü iki formatın farklı veri modelleri ve yapıları vardır.

Ancak, **XLS dosyaları için**, geliştiriciler kayıt işlemi sırasında oluşturulan geçici veri için bir geçici konum belirtebilirler. Genellikle **LightCells API'nin kullanılması XLSX dosyası için% 50 veya daha fazla bellek tasarrufu sağlayabilirken**, **XLS için kullanılması% 20-40'a kadar bellek tasarrufu sağlayabilir**.

### **Büyük Excel Dosyaları Yazma**

Aspose.Cells, programınızda uygulanması gereken LightCellsDataProvider arabirimini sağlar. Bu arabirim, hafif modda büyük elektronik tablo dosyalarını kaydetme için veri sağlayıcısını temsil eder.

Bu modda bir çalışma kitabı kaydedilirken, her çalışma tablosu her okunduğunda startSheet(int) kontrol edilir. Bir sayfa için, eğer startSheet(int) true ise, bu sayfanın satırlarındaki hücrelerin veri ve özellikleri bu uygulama tarafından sağlanır. İlk olarak, bir sonraki satır endeksini kaydedilmek üzere çağrılır. Eğer geçerli bir satır endeksi dönerse (satır endeksi kaydedilecek satırların artan sırayla olması gerekir), bu satırı temsil eden bir Row nesnesi uygulamaya verilir ve özellikleri startRow(Row) ile ayarlaması beklenir.

Bir satır için, öncelikle nextCell() kontrol edilir. Eğer geçerli bir sütun endeksi dönerse (bir satırın tüm hücreleri sırasıyla kaydedilmek üzere artan sırada sütun endeksi olmalıdır), bu hücreyi temsil eden bir Cell nesnesi uygulamaya verilir ve veri ve özellikleri startCell(Cell) ile ayarlanması beklenir. Bu hücrenin verileri ayarlandıktan sonra bu hücre doğrudan oluşturulan elektronik tablo dosyasına kaydedilir ve bir sonraki hücre kontrol edilir ve işlenir.

Aşağıdaki örnek, LightCells API'nin nasıl çalıştığını gösterir.

Aşağıdaki program, çalışma sayfasında 100.000 kayıtlı devasa bir dosya oluşturur, veriyle doldurulur. Bazı hiperbağlantılar, dize değerleri, sayısal değerler ve belirli hücrelere formüller ekledik. Ayrıca, bazı hücre aralıklarını biçimlendirdik.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Büyük Excel Dosyaları Okuma**

Aspose.Cells, programınızda uygulanması gereken LightCellsDataHandler arabirimini sağlar. Bu arabirim, hafif modda büyük elektronik tablo dosyalarını okuma için veri sağlayıcısını temsil eder.

Bu modda bir çalışma kitabı okunurken, her çalışma tablosu her okunduğunda startSheet() kontrol edilir. Bir sayfa için, eğer startSheet() true dönerse, bu sayfanın satırlarındaki hücrelerin veri ve özellikleri kontrol edilir ve işlenir. Her satır için, processRow() çalıştığı ve satırın hücreleri de işlenmesi gerekiyorsa, startCell() her hücre için kontrol edilir.

Hücrelerin de işlenmesi gerekiyorsa, processRow() true döner ve her satırdaki mevcut hücre için startCell() kontrol edilir. Eğer işlenmesi gerekiyorsa, processCell() çalıştırılır.

Aşağıdaki örnek kod bu süreci açıklar. Program, milyonlarca kaydı içeren büyük bir dosyayı okur. Kitaptaki her çalışma sayfasını okumak biraz zaman alır. Örnek kod, dosyayı okur ve her çalışma sayfası için toplam hücre sayısını, dize sayısını ve formül sayısını alır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

LightCellsDataHandler arabirimini uygulayan bir sınıf

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
