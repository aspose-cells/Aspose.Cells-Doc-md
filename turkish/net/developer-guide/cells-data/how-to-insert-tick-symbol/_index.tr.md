---
title: İşaret Düğmesi (Tick) Ekleme Nasıl Yapılır
type: docs
weight: 10
url: /tr/net/how-to-insert-tick-symbol-to-excel/
description: Bu makale, Aspose.Cells for .NET API kullanarak nasıl onay işareti (tick) simgesi eklenebileceğini tanıtacaktır.
keywords: İşaret simgesini kopyalayıp yapıştırın, Sembol veya Ekle menüsünü kullanın, Alt kodu girin, OtomDüzen veya kısayollar kullanın, Emojiler/simgeler panelini kullanın, Bir kutu / oy pusulası üzerine onay işareti ekleyin
---

## **Olası Kullanım Senaryoları**
Bir onay işareti (✓) eklemek, bağlama bağlı olarak çeşitli amaçlara hizmet edebilir. İşte birinin neden onay işareti ekleyebileceğine dair bazı yaygın nedenler:

1. **Tamamlandı veya Başarıyla Tamamlandı Göstergesi**: Bir görevi tamamlandığını veya bir şeyin başarıyla gerçekleştirildiğini göstermek için yaygın olarak kullanılır. Örneğin, yapılacaklar listesindeki bir görev tamamlandığında bir onay işareti kullanabilirsiniz.

2. **Kontrol Listeleri ve Anketler**: Anketlerde, formlarda veya kontrol listelerinde, seçilen seçenekleri göstermek veya belirli bir öğenin gereken kriterleri karşıladığını belirtmek için bir onay işareti kullanılır.

3. **Onay veya Doğrulama**: Bir onay işareti, bir işlem, karar veya belgenin onayını veya doğrulamasını gösterebilir. Genellikle resmi veya yarı-resmi bağlamlarda kullanılır.

4. **Tasarım Estetiği**: Bazı durumlarda, onay işareti sadece görsel çekiciliği için veya logo, infografik ya da sunum gibi tasarım öğelerinin bir parçası olarak kullanılır.

5. **Olumlu veya Doğru Yanıt**: Eğitim materyallerinde doğru cevapları veya bir şeyin olumlu sonucunu vurgulamak için kullanılabilir.

6. **Anlaşma veya Onay Göstergesi**: Bir onay işareti, bir kişinin bir ifade veya koşula katıldığını, onayladığını veya kabul ettiğini gösterebilir.


## **Excel'de Onay İşareti Nasıl Eklenir**
İşte Excel'de çeşitli yöntemler kullanarak onay işareti (✓ veya ✔) sembolünü nasıl ekleyeceğinize dair açık bir rehber:

### Sembol Menüsünü Kullanarak

1. Onay işaretini istediğiniz hücreye tıklayın.
2. Şerit üzerindeki Ekle sekmesine gidin.
3. Sembol'e tıklayın (sağ en sağda).
4. Sembol iletişim kutusunda: Yazı Tipi olarak Wingdings veya Segoe UI Symbol'u seçin, ve (✔ Karakter kodu 252 veya ✓ Karakter kodu 2713) seçeneğini arayın.
5. Ekle'ye tıklayın, ardından Kapat.

### Klavye Kısayollarını Kullanarak
1. Alt Kodu (yalnızca Windows): Alt tuşuna basılı tutun ve sayısal tuş takımını kullanarak kodu yazın: Alt + 0252 (✔) — Wingdings yazı tipi, Alt + 10003 (✓) — Segoe UI Symbol
2. Yazdıktan sonra, Alt tuşunu bırakın ve sembolü eklemek için serbest bırakın.

### Kopyala ve Yapıştır
Bir onay işaretini kopyalayıp herhangi bir Excel hücresine yapıştırabilirsiniz: ✓ (U+2713) ve ✔ (U+2714). Buradan kopyalayın ve doğrudan bir hücreye yapıştırın.

### Koşullu Biçimlendirme ile Formül Kullanımı
Formüller ve koşullu biçimlendirme ile otomatik işaretler oluşturabilirsiniz:

1. Böyle bir formül girin: =EĞER(A1="evet"; "✓"; "")
2. Görünüm için yazı tipi boyutunu ve hizalamayı özelleştirin.

### CHAR Fonksiyonu (Wingdings Yazı Tipi) ile Ekleme
Wingdings kullanıyorsanız: =CHAR(252)  →  ✔, Sonra hücre yazı tipini Wingdings yaparak doğru şekilde görüntülenmesini sağlayabilirsiniz.

### Excel Onay Kutuları ile Ekleme (İsteğe Bağlı)

İnteraktif onay kutuları için:
1. Geliştirici sekmesine gidin (Geliştirici'yi Seçenekler'den etkinleştirin).
2. Ekle → Form Denetimleri → Onay Kutusu seçin.
3. Onay kutusunu sayfaya yerleştirin.

## **Aspose.Cells for .NET ile İşaret Simgesi Nasıl Eklenir**
Aspose.Cells for .NET kullanarak bir hücreye işaret simgesi (✓) eklemek için aşağıdaki yöntemleri kullanabilirsiniz.

1. Unicode (U+2713) kullanarak işaret sembolü ekleyin.
2. Sembol yazı tipi (Wingdings 2 veya Webdings) kullanarak işaret sembolü ekleyin.
3. Görsel kullanarak işaret sembolü ekleyin.
4. Onay kutusu kontrolü kullanarak işaret sembolü ekleyin.
5. Koşullu biçimlendirme kullanarak işaret sembolü ekleyin.
6. Formül kullanarak işaret sembolü ekleyin.

İşte Aspose.Cells for .NET hücresine temel bir işaret sembolü ekleme örneği:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-insert-tick-symbol.cs" >}}

## **Sonuç Çıktısı**

Aşağıdaki ekran görüntüsü, çıktı Excel dosyasında Aspose.Cells for .NET tarafından oluşturulan tik sembollerini göstermektedir.
<br>
<img src="tick_result.png" width=70% />

{{< app/cells/assistant language="csharp" >}}
