---
title: LightCells'i Kullanma API
type: docs
weight: 80
url: /tr/java/using-lightcells-api/
---
{{% alert color="primary" %}}

Bazen, çalışma sayfasında çok sayıda veri veya içerik içeren büyük Microsoft Excel dosyalarını okumanız ve yazmanız gerekir. LightCells API, devasa Excel elektronik tabloları oluşturmak için kullanışlıdır: onunla, belleğe ihtiyacınız olur ve daha iyi performans ve verimlilik elde edersiniz.

{{% /alert %}}

## **Olay Odaklı Mimari**

Aspose.Cells, belleğe eksiksiz bir veri modeli bloğu oluşturmadan (Cell koleksiyonunu kullanarak vb.) temel olarak hücre verilerini tek tek işlemek için tasarlanmış LightCells API'i sağlar. Olay güdümlü modda çalışır.

Çalışma kitaplarını kaydetmek için, kaydederken hücre içeriğini hücre hücre sağlayın ve bileşen bunu doğrudan çıktı dosyasına kaydeder.

Şablon dosyalarını okurken, bileşen her hücreyi ayrıştırır ve değerlerini birer birer sağlar.

Her iki prosedürde de bir Cell nesnesi işlenir ve sonra atılır, Çalışma Kitabı nesnesi koleksiyonu tutmaz. Bu nedenle, bu modda, aksi takdirde çok fazla bellek kullanacak olan büyük bir veri kümesine sahip Microsoft Excel dosyasını içe ve dışa aktarırken bellek kaydedilir.

LightCells API, XLSX ve XLS dosyaları için hücreleri aynı şekilde işlese de (aslında bellekteki tüm hücreleri yüklemez, bir hücreyi işler ve sonra onu atar), XLSX dosyaları için belleği XLS dosyalarından daha etkili bir şekilde kaydeder çünkü iki biçimin farklı veri modelleri ve yapıları.

 Yine de,**XLS dosyaları için** , daha fazla bellek kazanmak için geliştiriciler, Kaydetme işlemi sırasında oluşturulan geçici verileri kaydetmek için geçici bir konum belirtebilir. yaygın olarak,**XLSX dosyasını kaydetmek için LightCells API kullanmak %50 veya daha fazla bellek tasarrufu sağlayabilir** ortak yolu kullanmaktansa,**XLS'yi kaydetmek, yaklaşık %20-40 bellek tasarrufu sağlayabilir**.

### **Büyük Excel Dosyaları Yazma**

Aspose.Cells, programınızda uygulanması gereken LightCellsDataProvider adlı bir arabirim sağlar. Arayüz, büyük elektronik tablo dosyalarını hafif modda kaydetmek için Veri sağlayıcıyı temsil eder.

Bir çalışma kitabını bu modda kaydederken, çalışma kitabındaki her çalışma sayfasını kaydederken startSheet(int) kontrol edilir. Bir sayfa için, startSheet(int) true ise, bu sayfanın satırlarının ve hücrelerinin tüm verilerinin ve özelliklerinin kaydedilmesi bu uygulama tarafından sağlanır. İlk olarak, kaydedilecek bir sonraki satır indeksini almak için nextRow() çağrılır. Geçerli bir satır dizini döndürülürse (satırların kaydedilmesi için satır dizini artan düzende olmalıdır), bu durumda, startRow(Row) ile özelliklerini ayarlamak üzere uygulama için bu satırı temsil eden bir Row nesnesi sağlanır.

Bir satır için önce nextCell() kontrol edilir. Geçerli bir sütun dizini döndürülürse (bir satırdaki tüm hücrelerin kaydedilmesi için sütun dizini artan düzende olmalıdır), bu durumda verileri ve özellikleri startCell(Cell) ile ayarlamak için bu hücreyi temsil eden bir Cell nesnesi sağlanır. Bu hücrenin verileri ayarlandıktan sonra, bu hücre doğrudan oluşturulan elektronik tablo dosyasına kaydedilir ve bir sonraki hücre kontrol edilerek işlenir.

Aşağıdaki örnek, LightCells API'in nasıl çalıştığını gösterir.

Aşağıdaki program, verilerle dolu bir çalışma sayfasında 100.000 kayıt içeren devasa bir dosya oluşturur. Çalışma sayfasındaki belirli hücrelere bazı köprüler, dize değerleri, sayısal değerler ve ayrıca formüller ekledik. Ayrıca, bir dizi hücreyi de biçimlendirdik.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Büyük Excel Dosyalarını Okuma**

Aspose.Cells, programınızda uygulanması gereken LightCellsDataHandler adlı bir arabirim sağlar. Arayüz, büyük elektronik tablo dosyalarını hafif bir modda okumak için veri sağlayıcıyı temsil eder.

Bu modda bir çalışma kitabı okurken, çalışma kitabındaki her çalışma sayfasını okurken startSheet() kontrol edilir. Bir sayfa için, startSheet() işlevi true değerini döndürürse, sayfanın satırlarındaki ve sütunlarındaki hücrelerin tüm verileri ve özellikleri kontrol edilir ve işlenir. Her satır için, işlenmesi gerekip gerekmediğini kontrol etmek için startRow() çağrılır. Bir satırın işlenmesi gerekiyorsa, önce satırın özellikleri okunur ve geliştiriciler processRow() ile özelliklerine erişebilir.

Satırdaki hücrelerin de işlenmesi gerekiyorsa, processRow() işlevi true değerini döndürür ve satırdaki her mevcut hücrenin işlenmesi gerekip gerekmediğini kontrol etmek için startCell() işlevi çağrılır. Olursa, processCell() çağrılır.

Aşağıdaki örnek kod, bu işlemi göstermektedir. Program, milyonlarca kayıt içeren büyük bir dosyayı okur. Çalışma kitabındaki her sayfayı okumak biraz zaman alır. Örnek kod, dosyayı okur ve her çalışma sayfası için toplam hücre sayısını, dize sayısını ve formül sayısını alır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

LightCellsDataHandler arabirimini uygulayan bir sınıf

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
