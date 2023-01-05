---
title: LightCells'i Kullanma API
type: docs
weight: 160
url: /tr/net/using-lightcells-api/
---
{{% alert color="primary" %}} 

Bazen, çalışma sayfasında çok sayıda veri veya içerik içeren büyük Microsoft Excel dosyalarını okumanız ve yazmanız gerekir. LightCells API, devasa Excel elektronik tabloları oluşturmak için kullanışlıdır: onunla daha az belleğe ihtiyacınız olur ve daha iyi performans ve verimlilik elde edersiniz.

{{% /alert %}} 
# Olay Odaklı Mimari
Aspose.Cells, belleğe eksiksiz bir veri modeli bloğu oluşturmadan (Cell koleksiyonunu kullanarak vb.) temel olarak hücre verilerini tek tek işlemek için tasarlanmış LightCells API'i sağlar. Olay güdümlü modda çalışır.

Çalışma kitaplarını kaydetmek için, kaydederken hücre içeriğini hücre hücre sağlayın ve bileşen bunu doğrudan çıktı dosyasına kaydeder.

Şablon dosyalarını okurken, bileşen her hücreyi ayrıştırır ve değerlerini birer birer sağlar.

Her iki prosedürde de bir Cell nesnesi işlenir ve sonra atılır, Çalışma Kitabı nesnesi koleksiyonu tutmaz. Bu nedenle, bu modda, aksi takdirde çok fazla bellek kullanacak olan büyük bir veri kümesine sahip Microsoft Excel dosyasını içe ve dışa aktarırken bellek kaydedilir.

LightCells API, XLSX ve XLS dosyaları için hücreleri aynı şekilde işlese de (aslında hafızadaki tüm hücreleri yüklemez, bir hücreyi işler ve sonra onu atar), XLSX dosyaları için hafızayı XLS dosyalarına göre daha etkili bir şekilde kaydeder. iki biçimin farklı veri modelleri ve yapıları.

 Yine de,**XLS dosyaları için** , daha fazla bellek kazanmak için geliştiriciler, Kaydetme işlemi sırasında oluşturulan geçici verileri kaydetmek için geçici bir konum belirtebilir. yaygın olarak,**XLSX dosyasını kaydetmek için LightCells API kullanmak %50 veya daha fazla bellek tasarrufu sağlayabilir** ortak yolu kullanmaktansa,**XLS'i kaydetmek, yaklaşık %20-40 bellek tasarrufu sağlayabilir**.
## Büyük Bir Excel Dosyası Yazmak
Aspose.Cells, programınızda uygulanması gereken LightCellsDataProvider adlı bir arabirim sağlar. Arayüz, büyük elektronik tablo dosyalarını hafif modda kaydetmek için veri sağlayıcıyı temsil eder.

Bir çalışma kitabını bu modda kaydederken, çalışma kitabındaki her çalışma sayfasını kaydederken StartSheet(int) kontrol edilir. Bir sayfa için, StartSheet(int) true ise, bu sayfanın satırlarının ve hücrelerinin tüm verilerinin ve özelliklerinin kaydedilmesi bu uygulama tarafından sağlanır. İlk olarak, kaydedilecek bir sonraki satır indeksini almak için NextRow() çağrılır. Geçerli bir satır dizini döndürülürse (satırların kaydedilmesi için satır dizini artan düzende olmalıdır), bu durumda, StartRow(Row) ile özelliklerini ayarlamak üzere uygulama için bu satırı temsil eden bir Row nesnesi sağlanır.

Bir satır için önce NextCell() kontrol edilir. Geçerli bir sütun dizini döndürülürse (bir satırdaki tüm hücrelerin kaydedilmesi için sütun dizini artan düzende olmalıdır), o zaman bu hücreyi temsil eden bir Cell nesnesi, StartCell(Cell) tarafından veri ve özelliklerini ayarlamak üzere uygulama için sağlanır. Hücrenin verileri ayarlandıktan sonra, hücre doğrudan oluşturulan elektronik tablo dosyasına kaydedilir ve bir sonraki hücre kontrol edilerek işlenir.
### Büyük Bir Excel Dosyası Yazmak:Örnek
LightCells API'in çalışmasını görmek için lütfen aşağıdaki örnek koda bakın. İhtiyaçlarınıza göre kod segmentlerini ekleyin ve kaldırın veya güncelleyin.

 Program ile büyük bir dosya oluşturur**10.000 (10000x30 matris) kayıt** bir çalışma sayfasında ve bunları sahte verilerle doldurur. Main() yönteminde rowsCount ve colsCount değişkenlerini değiştirerek kendi matrisinizi belirtebilirsiniz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Büyük Excel Dosyalarını Okuma
Aspose.Cells, programınızda uygulanması gereken LightCellsDataHandler adlı bir arabirim sağlar. Arayüz, büyük elektronik tablo dosyalarını hafif modda okumak için Veri sağlayıcıyı temsil eder.

Bu modda bir çalışma kitabı okurken, çalışma kitabındaki her çalışma sayfasını okurken StartSheet kontrol edilir. Bir sayfa için, StartSheet true değerini döndürürse, sayfanın satır ve sütunlarındaki hücrelerin tüm verileri ve özellikleri bu arayüzün uygulanmasıyla kontrol edilir ve işlenir. Her satır için, işlenmesi gerekip gerekmediğini kontrol etmek için StartRow çağrılır. Bir satırın işlenmesi gerekiyorsa, önce özellikleri okunur ve geliştirici, ProcessRow ile özelliklerine erişebilir. Satırdaki hücrelerin de işlenmesi gerekiyorsa, ProcessRow true döndürmeli ve ardından bir hücrenin işlenmesi gerekip gerekmediğini kontrol etmek için satırdaki mevcut her hücre için StartCell çağrılmalıdır. Bir hücrenin işlenmesi gerekiyorsa, bu arayüzün uygulanmasıyla hücreyi işlemek için ProcessCell çağrılır.
### Büyük Excel Dosyalarını Okuma:Örnek
LightCells API'in çalışmasını görmek için lütfen aşağıdaki örnek koda bakın. İhtiyaçlarınıza göre kod segmentlerini ekleyin ve kaldırın veya güncelleyin.

Program, bir çalışma sayfasında milyonlarca kayıt içeren devasa bir dosyayı okur. Çalışma kitabındaki her sayfayı okumak biraz zaman alır. Örnek kod, dosyayı okur ve her çalışma sayfasındaki toplam hücre sayısını, dize sayısını ve formül sayısını alır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
