---
title: Bir İlerleme Çubuğu nasıl oluşturulur
description: Aspose.Cells for .NET kullanarak nasıl ilerleme çubuğu oluşturulacağını öğrenin. 
keywords: Aspose.Cells for .NET, İlerleme Çubuğu, İlerleme Çubuğu oluştur, Bir İlerleme Çubuğu ekle, İlerleme Çubuğu yerleştir.
type: docs
weight: 73
url: /tr/net/how-to-create-a-progress-bar/
---

## **Olası Kullanım Senaryoları**
Excel'de ilerleme çubuğu oluşturmaktaki temel amaç, ham sayıları anında anlaşılır görsel ölçüme dönüştürmek ve karmaşık veriyi bir bakışta kavranmasını kolaylaştırmaktır.

1. Artırılmış Görsel Netlik ve Anında İçgörü: "75%", "8/10" veya "15000/20000" gibi sayılar içeren tablo, yorumlamak için bilişsel çaba gerektirir. Bir ilerleme çubuğu, kıdemli yöneticiden takım üyesine kadar herkesin durumu, performansı veya tamamlanma seviyesini anında anlamasını sağlar, sayıları okumaya gerek kalmadan.

2. Durum ve Eğilimlerin Hızlı Tanımlanması: Beynimiz, uzunluk ve renk gibi görsel bilgileri metinden daha hızlı işlemeye programlanmıştır. Hızlıca görebilirsiniz: İzlenen mi? (Uzun, yeşil çubuklar), Geride mi? (Kısa, kırmızı çubuklar) ve Neredeyse tamamlandı mı? (Çok dolu çubuklar). Bu, daha hızlı karar verme ve önceliklendirme sağlar.

3. Geliştirilmiş Gösterge Paneli ve Raporlar: İlerleme çubukları, etkili gösterge panellerinin temel taşlarındandır. Raporları daha çekici, profesyonel ve sunması daha kolay hale getirir. Temel performans göstergeleri (KPI'lar) için ilerleme çubuklarına sahip bir gösterge paneli, sayıların doldurulduğu bir sayfadan çok daha etkilidir.

4. Motivasyon ve Performans Takibi: Satış ekipleri, proje takipçileri veya kişisel hedefler için, ilerlemenin görsel temsili oldukça motive edicidir. Çubuğun dolmasıyla birlikte açık ve tatmin edici bir başarı duygusu sağlar.

5. Verimli İletişim: Toplantılarda veya sunumlarda, bir ilerleme çubuğu, "Üç aylık hedefimizin %72.5'inde olduğumuzu" söylemekten çok daha etkili bir şekilde mesaj iletir. Görsel, konuşmayı yapar, zaman kazandırır ve yanlış anlaşılmayı engeller.


## **Excel'de İlerleme Çubuğu Nasıl Oluşturulur**

Excel'de ilerleme çubuğu oluşturmak, görev tamamlanmasını, proje ilerlemesini veya veri trendlerini görselleştirmenin harika bir yoludur. İşte farklı yöntemler kullanarak nasıl oluşturulacağına dair bir rehber ve bazı özelleştirme ipuçları.

### **Koşullu Biçimlendirme (Veri Çubukları) Kullanımı**
1. Verilerinizi Hazırlayın: En az bir sütunda ilerlemeyi temsil eden değerler olsun, tercihen yüzdeler olarak (örneğin, 0.5 %50 için). Bunu aşağıdaki formülle hesaplayabilirsiniz =ŞuAnki_Değer/Hedef_Değer.
2. Hücreleri Seçin: Yüzde değerlerinizin bulunduğu hücreleri vurgulayın.
3. Veri Çubuklarını Uygula: Giriş sekmesine > Koşullu Biçimlendirme > Veri Çubukları. İster Gradyan Doldurma, ister Düz Doldurma seçeneğini seçin.
4. Özelleştir (İsteğe Bağlı): Daha fazla kontrol için Koşullu Biçimlendirme > Kuralları Yönetin > Kuralı Düzenle bölümüne gidin.
5. Minimum ve Maksimum türlerini Sayı olarak ayarlayın, sırasıyla 0 ve 1 değerleriyle, böylece doğru yüzde 0-100% görüntülemesi sağlanır.
6. Burada renkleri ve sınır stillerini ayarlayın. Hem sayıyı hem de çubuğu göstermek için, kuralı düzenleyin ve "Sadece Çubuğu Göster" seçeneğinin işaretli olmadığından emin olun.

### **Metin tabanlı Çubuk (REPT Fonksiyonu) Kullanımı**
1. Formülü Girin: Bir hücreye şu formülü kullanın =REPT("█", B2*10) & REPT("░", 10 - B2*10), burada B2 ilerleme yüzdesini içerir. Bu örnek 10 karakterlik çubuk oluşturur: tamamlanmış için dolu kareler (█), kalan için hafif kareler (░).
2. Ayarlama ve Formatlama: İstediğiniz uzunluğa göre çarpanı ayarlayın (örneğin, *20 için 20 karakterlik bir çubuk). Uygun hizalama için Courier New gibi monospaced bir font kullanın.

### **Grafik Kullanımı (Gösterge Panelleri İçin)**
1. Veri Yapısı: Değerleri hesaplamak için bir tablo oluşturun:
|**Numara**|**A**|**B**|
| :- | :- | :- |
|1|İlerleme|Kalan|
|2|=Mevcut_Değer/Hedef_Değer|=1-A2|
<br>
2. Grafik Ekle: Verileri seçin > Ekle sekmesi > Grafikler > 2-Boyutlu Yığılmış Çubuk Grafik.
3. Grafik Formatı: Grafik başlığı, açıklamalar ve grid çizgilerini kaldırın, temiz bir görünüm için. "Kalan" veri serisine sağ tıklayın > Veri Serisini Biçimlendir > Dolgu > Dolu Renk Yok. "İlerleme" serisine sağ tıklayın > Veri Serisini Biçimlendir > Serilerin Çakışma Yüzdesini %100 yapın ve Boşluk Genişliğini 0% olarak ayarlayın. Yatay ekseni biçimlendirin: Sınırlar > Minimum 0, Maksimum 1 olarak ayarlayın.

## **Aspose.Cells'de İlerleme Çubuğu Nasıl Oluşturulur**

### **İlerleme Çubuğu Oluşturmak için REPT Fonksiyonu (Metin tabanlı Çubuk) kullanın**
Lütfen aşağıdaki örnek kodu inceleyin. Yeni bir çalışma kitabı oluşturur ve bazı örnek veriler ekler. Daha sonra başlangıç verilerine göre REPT Fonksiyonu (Metin tabanlı Çubuk) ekler. Son olarak, çalışma kitabını xlsx dosyasına kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan koşullu biçimlendirme (Veri Çubukları) içeren çıktı Excel dosyasını gösterir.
<br>
<img src="formula.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Using-Formula.cs" >}}

### **Koşullu Biçimlendirme (Veri Çubukları) kullanarak İlerleme Çubuğu oluşturun**
Lütfen aşağıdaki örnek kodu inceleyin. Yeni bir çalışma kitabı oluşturur ve bazı örnek veriler ekler. Daha sonra başlangıç verilerine göre koşullu biçimlendirme (Veri Çubukları) ekler ve ilgili özellikleri ayarlar. Son olarak, çalışma kitabını xlsx dosyasına kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan koşullu biçimlendirme (Veri Çubukları) içeren çıktı Excel dosyasını gösterir.
<br>
<img src="databar.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Using-ConditionalFormats.cs" >}}


### **Çubuk Birleştirilmiş Grafik Kullanarak İlerleme Çubuğu Oluşturun**
Lütfen aşağıdaki örnek kodu inceleyin. Birkaç örnek veri içeren [örnek Excel dosyasını](sample.xlsx) yükler. Daha sonra başlangıç verilerine göre yığın çubuk grafik oluşturur ve ilgili özellikleri ayarlar. Son olarak, çalışma kitabını çıktı XLSX formatında kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan ilerleme çubuğunu gösterir.

<br>
<img src="barchart.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Use-BarStacked-Chart.cs" >}}
