---
title: Sayısı Nasıl Tarih Olarak Biçimlendirilir
type: docs
weight: 10
url: /tr/nodejs-cpp/format-number-to-date/
description: Bu makale, Aspose.Cells for Node.js via C++ API sini kullanarak sayıları tarih formatına nasıl biçimlendireceğinizi tanıtacaktır.
keywords: numarayı tarih olarak biçimlendirme, hücre sayı ayarları, sayıyı tarihe biçimlendirme, tarih ayarları, tarih formatı.
---

## **Olası Kullanım Senaryoları**
Excel'de (ve herhangi bir elektronik tablo yazılımında) sayıları tarihe biçimlendirmek birkaç nedenle önemlidir, özellikle zaman veya takvim bilgisi içeren verilerle çalışırken. İşte neden sayıları tarihe formatlamanın faydalı olduğu:

1. Tarih Değerlerinin Doğru Yorumlanması: Excel'de tarihleri serisel sayılar olarak saklar (örneğin, 1 Ocak 1900 için 1 ve 6 Eylül 2021 için 44210). Bu sayılar uygun şekilde biçimlendirilmediğinde, kullanıcılar anlamsız sayılar görebilir, hatalı görüntüleyebilir. Doğru biçimlendirmeler, Excel'in bunları gerçek tarihler olarak görüntülemesine olanak tanır (örneğin, 09/06/2021 yerine 44210).
1. Zamanla İlgili Hesaplamaları Basitleştirir: Excel, iki tarih arasındaki gün sayısını hesaplama, gün ekleme veya çıkarma veya haftanın gününü belirleme gibi birçok hesaplama yapabilir. Sayılar tarih formatında değilse, Excel bu işlemleri etkili şekilde yapamaz. Örneğin, 09/01/2023 ve 10/01/2023 arasındaki gün sayısını öğrenmek istiyorsanız, sayılar tarih biçimindeyse, Excel kolayca hesaplayabilir.
1. Tutarlılığı Sağlar: Tüm tarih ile ilgili değerler doğru biçimlendirilmişse, tüm tarihler uyumlu, okunabilir bir tarzda görünür. Bu tutarlılık, işletme raporları, proje takvimleri ve veritabanlarında tarih tutarlılığının kritik olduğu durumlarda önemlidir.
Farklı bölgeler farklı tarih biçimleri kullanır (örneğin, ABD'de MM/Ay/GG, diğer birçok ülkede GG/Ay/MM), bu nedenle biçimlendirme, tarihlerinin doğru yorumlanmasını sağlar.
1. Okunabilirliği Artırır: Standart formatta sunulan tarihler (örneğin, 01/01/2024) ham seri numaralarına göre (örneğin 45000) daha kolay okunur. Doğru tarih biçimlendirmesi, elektronik tablonuzu daha kullanıcı dostu yapar ve karışıklığı önler. Bu, takvim, zaman çizelgeleri, etkinlik planlaması veya tarihsel veriler gibi durumlarda özellikle önemlidir.
1. Sıralama ve Filtreleme İşlevlerini Kolaylaştırır: Tarihler doğru biçimlendirildiğinde, Excel bunları gerçek tarihler olarak tanır ve bu da veriyi kronolojik olarak sıralamayı veya filtrelemeyi kolaylaştırır. Örneğin, bir olay listesini tarihe göre sıralayabilir veya belirli iki tarih arasında kayıtlar gösterecek şekilde filtre uygulayabilirsiniz. Uygun tarih biçimi olmadan, sıralama ham sayı değerine göre yapılabilir.
1. Tarih Fonksiyonlarının Kullanımını Etkinleştirir: Excel, şunlar gibi güçlü tarih fonksiyonları sağlar: BUGÜN(), DATEDIF(), İŞGÜNÜ(), YIL(), AY(), GÜN(). Bu fonksiyonların doğru hesaplamalar yapabilmesi için tarihlerin doğru biçimde ayarlanması gerekir.
1. Görselleştirmeyi Destekler (Grafikler/Zaman Çizelgeleri): Doğru biçimlendirilmiş tarihler, zamanın ana eksen olduğu grafik ve çizelgeler oluşturmak için kullanılabilir. Örneğin, bir zaman çizelgesi grafiğinde, Excel'in olayları doğru şekilde gösterebilmesi için tarihler tanınan biçimde olmalıdır. Yanlış biçimlendirilmiş veya biçimlendirilmemiş sayılar, anlamlı olmayan veya yanlış bilgiler içeren grafiklere yol açabilir.
1. Yanlış Yorumlamayı Önler: Ham sayılar kolaylıkla yanlış yorumlanabilir. Örneğin, 44210 genelleme sayısal bir değer olarak görülebilir, ancak tarih biçiminde olduğunda, 6 Eylül 2021'i temsil ettiği açıktır. Doğru biçimlendirilmiş tarihler, verilerin yanlış yorumlanmasını önler.
1. Veri Girişini Kolaylaştırır: Hücreler tarih biçiminde biçimlendirildiğinde, kullanıcılar geçerli bir tarih formatında veri girmeye teşvik edilir, bu da veri giriş hatalarını önler ve tarih değerlerinin doğru şekilde kaydedilmesini sağlar.
1. Programlamada ve Takipte Kritik: Herhangi bir durumda zamanlama, takip veya son teslim tarihleriyle ilgili (proje yönetimi, finansal tahmin veya zaman hassas raporlar gibi), sayıların tarih formatında olması doğruluk ve anlaşılabilirlik için çok önemlidir. Bu, daha iyi planlama ve yürütme sağlar.


## **Excel'de Sayıyı Tarehe Formatlama Kılavuzu**
Excel'de bir sayıyı tarihe dönüştürmek için şu adımları izleyin:

### **Şeridi Kullanarak (Giriş Sekmesi)**
1. Tarih olarak biçimlendirmek istediğiniz sayıların bulunduğu hücreleri seçin.
1. Şerideki Giriş sekmesine gidin.
1. Sayı Grubunda, Sayı Biçimi kutusundaki açılır oka tıklayın (varsayılan olarak "Genel" veya "Sayı" gösterilebilir).
1. Açılır menüden Kısa Tarih veya Uzun Tarih seçin. Kısa Tarih: tarihi kısaca gösterir, ör. AA/GG/YYYY (ABD formatı) veya GG/AA/YYYY (uluslararasıFormat). Uzun Tarih: tarihi daha açıklayıcı biçimde gösterir, ör. Pazartesi, 1 Ocak 2024.
<br>
<img src="1.png" width=60% />

### **Hücreleri Biçimlendir Diyalog Kutusunu Kullanarak**
1. Biçimlendirmek istediğiniz hücreleri seçin.
1. Seçili hücrelere sağ tıklayın ve Biçim Hücreleri’ni seçin veya Ctrl + 1 (Windows) veya Cmd + 1 (Mac) tuşlarına basın.
1. Biçim Hücreleri iletişim kutusundaki Sayı sekmesine gidin.
1. Sol taraftaki listeden Tarih seçeneğini seçin.
1. Sağdaki listeden istenen tarih formatını seçin (ör., AA/GG/YYYY, GG/AA/YYYY veya özel biçimler).
<br>
<img src="2.png" width=60% />
1. Tamam’a tıklayarak tarih formatını uygulayın.

## **Aspose.Cells ile Sayıyı Tarihe Formatlama Yöntemi**

Excel dosyalarıyla çalışmak için Aspose.Cells for Node.js via C++ kütüphanesinde sayıları tarihe dönüştürmek için hücrelere programlı biçimde tarih formatı uygulayabilirsiniz. İşte Aspose.Cells for Node.js via C++ kullanarak nasıl yapacağınız:

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FormatNumberToDate.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
