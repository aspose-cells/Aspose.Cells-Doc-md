---
title: LightCells API sını Kullanma
type: docs
weight: 160
url: /tr/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

Bazen büyük bir veri veya içeriğe sahip büyük Microsoft Excel dosyalarını okumak ve yazmak isteyebilirsiniz. Hafif Hücreler API'sı, bu iş için kullanışlıdır: daha az bellek kullanarak daha iyi performans ve verimlilik elde edersiniz.

{{% /alert %}} 
# Olay Tabanlı Mimari
Aspose.Cells, özellikle bellekte bir veri modeli bloğu oluşturmadan hücre verilerini bir bir işlemek için tasarlanmış olan LightCells API'sını sağlar (Hücre koleksiyonu vb. kullanılmadan). Olay temelli modda çalışır.

Çalışma kitaplarını kaydetmek için kaydederken hücre içeriğini hücre hücre sağlayın ve bileşen bunu doğrudan çıktı dosyasına kaydeder.

Şablon dosyalarını okurken bileşen her hücreyi ayrı ayrı ayrıştırır ve değerlerini tek tek sağlar.

Her iki süreçte de bir Cell nesnesi işlenir ve ardından atılır, Workbook nesnesi koleksiyonu tutmaz. Bu modda, dolayısıyla, çok miktarda bellek kullanan büyük veri kümesi barındıran Microsoft Excel dosyasının içe aktarımı ve dışa aktarımı sırasında bellek kaydedilir.

LightCells API, XLSX ve XLS dosyaları için hücreleri aynı şekilde işlemesine rağmen (bütün hücreleri belleğe yüklemez ama bir hücreyi işler ve ardından atar), XLSX dosyaları için XLS dosyalarına göre belleği daha etkili bir şekilde saklar çünkü iki formatın farklı veri modelleri ve yapıları vardır.

Ancak, **XLS dosyaları için**, geliştiriciler kayıt işlemi sırasında oluşturulan geçici veri için bir geçici konum belirtebilirler. Genellikle **LightCells API'nin kullanılması XLSX dosyası için% 50 veya daha fazla bellek tasarrufu sağlayabilirken**, **XLS için kullanılması% 20-40'a kadar bellek tasarrufu sağlayabilir**.
## Büyük Bir Excel Dosyası Yazma
Aspose.Cells, hafif modda büyük elektronik tablo dosyalarını kaydetmek için uygulamanızda uygulanması gereken bir arayüz olan LightCellsDataProvider'ı sağlar.

Bu modu kullanarak bir çalışma kitabını kaydederken, StartSheet(int), çalışma kitabındaki her çalışma sayfasını kaydederken kontrol edilir. Bir sayfa için, StartSheet(int) doğruysa, o sayfanın tüm verileri ve sıraların ve hücrelerin özellikleri bu sayfanın verilerini uygulayarak kaydedilir. İlk olarak, bir sonraki satırın indeksini kaydedilecek bir satır indeksini almak için NextRow() çağrılır. Geçerli bir satır indeksi döndürülürse (kaydedilecek satırların ilerleyen sıralı olması gerekir), o zaman bu satırı temsil eden bir Satır nesnesi, özelliklerini StartRow(Satır) ile ayarlamak için uygulamaya sağlanır.

Bir satır için, önce NextCell() kontrol edilir. Geçerli bir sütun indeksi döndürülürse (bir satırdaki tüm hücrelerin sıralı sütun indeks olması gerekir), o zaman o hücreyi temsil eden bir Hücre nesnesi, verilerini ve özelliklerini StartCell(Hücre) ile uygulamaya ayarlamak için sağlanır. Hücre verisi ayarlandıktan sonra, hücre doğrudan oluşturulan elektronik tablo dosyasına kaydedilir ve bir sonraki hücre kontrol edilir ve işlenir.
### Büyük Bir Excel Dosyası Yazma:Örnek
Lütfen LightCells API'nin çalışmasını görmek için aşağıdaki örnek kodu inceleyin. Kod segmentlerini ihtiyacınıza göre ekleyin, kaldırın veya güncelleyin.

Program, bir çalışma sayfasında **10.000 (10000x30 matris) kayıt** içeren büyük bir dosya oluşturur ve bu kayıtlara sahte veri doldurur. Main() yöntemindeki rowsCount ve colsCount değişkenlerini değiştirerek kendi matrisinizi belirtebilirsiniz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Büyük Excel Dosyalarını Okuma
Aspose.Cells, büyük elektronik tablo dosyalarını hafif modda okumak için uygulanması gereken LightCellsDataHandler arabirimini sağlar.

Bu modda bir çalışma kitabını okurken, StartSheet her çalışma sayfasını okurken kontrol edilir. Bir sayfa için, StartSheet doğruysa, sayfanın sıralarındaki hücrelerin tüm verileri ve özellikleri bu arabirimin uygulaması tarafından kontrol edilir ve işlenir. Her satır için, satırın işlenmesi gerekip gerekmediğini kontrol etmek için StartRow çağrılır. Bir satırın işlenmesi gerekiyorsa, önce özellikleri okunur ve geliştirici, özelliklerine ProcessRow ile erişebilir. Eğer satırın hücreleri de işlenmesi gerekiyorsa, o zaman ProcessRow true döndürmeli ve sonra satırın her mevcut hücresi için işlenmesi gerekip gerekmediğini kontrol etmek için StartCell çağrılır. Bir hücrenin işlenmesi gerekiyorsa, o zaman hücreyi bu arabirimin uygulaması tarafından işlemek için ProcessCell çağrılır.
### Büyük Excel Dosyalarını Okuma:Örnek
Lütfen LightCells API'nin çalışmasını görmek için aşağıdaki örnek kodu inceleyin. Kod segmentlerini ihtiyacınıza göre ekleyin, kaldırın veya güncelleyin.

Program, bir çalışma kitabında milyonlarca kayıt içeren büyük bir dosyayı okur. Her çalışma sayfasını okumak biraz zaman alır. Örnek kod, dosyayı okur ve her çalışma sayfasında toplam hücre sayısını, dize sayısını ve formül sayısını alır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
