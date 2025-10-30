---
title: Sayısal Veriyi Özelleştirilmiş Forma biçimlendirme rehberi
type: docs
weight: 10
url: /tr/nodejs-cpp/how-to-format-number-to-special/
description: Bu makale, Aspose.Cells for Node.js via C++ API kullanarak Sayısal Veriyi Özelleştirilmiş Forma biçimlendirmenin nasıl yapılacağını anlatacaktır.
keywords: Sayısal Veriyi özel bir desene göre biçimlendirin, Numaraları biçimlendirmek için belirli bir desen uygulayın, Sayı biçimlendirmesini benzersiz bir stile göre özelleştirin, Sayıların sunumunu farklı bir formata ayarlayın, Sayıları belirli bir biçimlendirme kuralına uydurun, Sayısal Veriyi Özelleştirilmiş Forma biçimlendirme
---

## **Olası Kullanım Senaryoları**
Excel'de sayıları özel bir formata biçimlendirmek, kullanıcıların sayıları daha okunabilir, anlaşılır veya standart hale getirilmiş şekilde görüntülemesine olanak tanıyan güçlü bir özelliktir. Bu özellik, finansal raporlama, veri analizi ve günlük tablo hesapları gibi çeşitli senaryolarda özellikle faydalı olabilir. İşte Excel'de sayıları özel forma biçimlendirmek istemenizin bazı nedenleri:

1. **Gelişmiş Okunabilirlik**: Özel biçimlendirme, sayıların okunmasını ve anlaşılmasını kolaylaştırabilir. Örneğin, bir sayıyı telefon numarası (ör. (123) 456-7890) veya sosyal güvenlik numarası (ör. 123-45-6789) olarak biçimlendirmek, bu sayıları anında tanınabilir ve daha okunabilir hale getirir.

2. **Tutarlılık**: Özel bir biçim uygulamak, verinizde tutarlılık sağlar ve bu, başkalarıyla paylaşılan raporlar veya kullanılacak veri setleri için çok önemlidir. Sayıların biçimlendirilmesindeki tutarlılık, veriyi karşılaştırmaya ve profesyonel standartları korumaya yardımcı olur.

3. **Veri Yorumlama**: Belirli biçimler, veri yorumlamayı hızlandırabilir. Örneğin, sayıları para birimi olarak biçimlendirmek, finansal değerleri hemen gösterebilir; yüzde biçimleri ise oranları veya karşılaştırmaları vurgulayabilir, ek hesaplama veya açıklama yapmaya gerek kalmadan.

4. **Hata Azaltma**: Sayıları belirli bir şekilde biçimlendirerek, veri girişi veya yorumlama sırasında hataları azaltabilirsiniz. Örneğin, bir hücreyi tarihleri gösterecek şekilde biçimlendirmek, tüm tarih girişlerinin aynı yapıya uymasını sağlar ve yanlış yorumlama ihtimalini azaltır.

5. **Alan Tasarrufu**: Bilimsel gösterim gibi özel biçimler, büyük sayıları daha kompakt hale getirebilir, böylece tablo alanını korur ve bilgi kaybı yaşanmaz. Bu, özellikle çok büyük ya da çok küçük sayılarla çalışırken yararlı olur.

6. **Uyumluluk ve Standartlar**: Birçok alanda, sayıların nasıl görüntülenmesi gerektiğine dair belirli standartlar vardır (örn. muhasebe, bilim, mühendislik). Özel biçimler kullanmak, verinizin bu standartlara uygun olmasını sağlar.

7. **Koşullu Biçimlendirme**: Sadece statik biçimlendirme ile sınırlı olmamakla beraber, Excel'de hücre değeri temelinde biçim değiştirilen koşullu biçimlendirme de mümkündür (örn., bütçe aşılınca kırmızıya döndürmek). Bu dinamik yaklaşım, verinizde önemli bilgiler veya eğilimleri vurgulamaya yardımcı olur.

8. **Otomasyon ve Verimlilik**: Bir hücre veya hücre aralığı için belirli bir biçim ayarladıktan sonra, Excel yeni girilen verilerde otomatik olarak bu biçimi uygular. Bu, zaman kazandırır ve manuel ayar yapmadan tutarlılığı sağlar.

Excel, para birimi, muhasebe, tarih, saat, telefon numarası, posta kodu ve sosyal güvenlik numarası gibi önceden tanımlanmış pek çok özel biçim sunar. Ayrıca, kullanıcıların özel sayı biçimleri oluşturmasına olanak tanıyan özellikler de mevcuttur.

## **Excel'de Sayıyı Özelleştirilmiş Forma Biçimlendirme**
Excel'de sayıları özel bir formata dönüştürmek, telefon numaraları, posta kodları, sosyal güvenlik numaraları veya ihtiyaç duyduğunuz başka herhangi bir özel formatta daha okunabilir veya kişiselleştirilmiş şekilde göstermenize olanak tanır. İşte Excel'de sayıları özel bir forma biçimlendirme yöntemi:

### Yerleşik Özel Formatları Kullanma

1. **Hücreleri Seçin**: Biçimlendirmek istediğiniz hücre veya hücre aralığını tıklayın.
2. **Hücreleri Biçimlendirme Diyaloğunu Açın**: Seçili hücrelere sağ tıklayın ve "Hücreleri Biçimlendir" seçeneğini seçin veya klavyenizde `Ctrl`+`1` tuşlarına basarak Hücreleri Biçimlendir kutusunu açın.
3. **Özel Seçeneğine Geçin**: Hücreleri Biçimlendir penceresinde, "Sayı" sekmesine gidin ve kategori listesinde "Özel" seçeneğini seçin.
4. **Bir Biçim Seçin**: Burada Posta Kodu, Telefon Numarası ve Sosyal Güvenlik Numarası gibi önceden tanımlanmış özel biçimlerin listesi görebilirsiniz. İhtiyacınıza uygun olanı seçin.
5. **Uygula ve TAMAM**: Seçilen biçimi uygulamak için "TAMAM" düğmesine tıklayın.

### Özel Biçimler Oluşturma

Yerleşik özel biçimler ihtiyaçlarınızı karşılamıyorsa, kendi özel biçiminizi oluşturabilirsiniz:

1. **Hücreleri Seçin**: Biçimlendirmek istediğiniz hücreyi veya hücre alanını vurgulayın.
2. **Hücreleri Biçimlendirme Diyaloğunu Açın**: Sağ tıklayın ve "Hücreleri Biçimlendir" seçeneğini seçin veya `Ctrl` + `1` tuşlarına basın.
3. **Özel Sekmesine Gidin**: Hücreleri Biçimlendirme diyalog kutusunda, "Sayı" sekmesini seçin, ardından Kategori listesinden "Özel" seçeneğini seçin.
4. **Özel Biçim Girin**: Tür kutusuna, özel biçim kodunu girin. Örneğin:
   - 10 haneli telefon numarasını biçimlendirmek için şu kullanabilirsiniz: `(###) ###-####`
   - İki harfle başlar ve ardından üç rakam gelen ürün kodu için: `"XX"###`
5. **Uygula ve TAMAM**: Kendi özel biçiminizi uygulamak için "TAMAM" düğmesine tıklayın.

### Özel Sayı Biçimi İçin İpuçları

- Opsiyonel rakamlar için `#` kullanın. Excel, rakam mevcutsa gösterir.
- Bir rakam yeri tutucusu olarak `0` kullanın; bu, o pozisyonda rakam yoksa sıfırları gösterir.
- Önemsiz sıfırlar için alan eklemek amacıyla `?` kullanabilirsiniz; bu, ondalık sayıların hizalanmasına yardımcı olur.
- Özel biçimlerde metin, tırnak işaretleri içinde eklenebilir.

### Örnek Özel Biçim Kodları

- **Sosyal Güvenlik Numarası (SSN)**: `000-00-0000`
- **Telefon Numarası (ABD)**: `(###) ###-####`
- **Ürün Kodu**: `"PRD-"0000`
- **Tarihle Metin**: `"Gün" dd "günü" mmmm, yyyy`

Unutmayın, özel biçim özelliği çok güçlüdür ve sadece özel sayı biçimlerinin ötesinde çok çeşitli biçimlendirme seçenekleri sunar. Koşulları, renkleri ve daha fazlasını birleştirerek Excel’de verilerinizi yüksek derecede özelleştirilmiş şekilde görüntüleyebilirsiniz.

## **Aspose.Cells for Node.js via C++ için Sayı Formatını Özelleştirme Yöntemleri**
Aspose.Cells for Node.js via C++'te, sayı biçimlendirmek için hücreyle ilişkili olan `Style` nesnesini kullanmak gerekir. `Style` nesnesi, çeşitli biçimlendirme seçenekleri, sayı biçimleri dahil olmak üzere ayarlamanıza olanak tanır. Özel sayı biçimleri, tarih, saat, telefon numarası, posta kodu veya uygulamak istediğiniz herhangi bir özel sayı biçimini içerebilir.

İşte Aspose.Cells for Node.js via C++ kullanarak sayıyı özel bir biçime biçimlendirme adım adım rehberi:

### Adım 1: Aspose.Cells'i Projenize Ekleyin

İlk olarak, projenizde Aspose.Cells for Node.js via C++ referansını bulundurmanız gerekir. Bunu Aspose sitesinden edinebilirsiniz.

### Adım 2: Bir Çalışma Kitabı Oluşturun ve Bir Çalışma Sayfasına Erişin
Yeni bir çalışma kitabı oluşturabilir veya var olanı açabilirsiniz. 

### Adım 3: Bir Hücreye Veri Erişimi veya Ekleme
Verileri özel biçimlendirmek istediğiniz çalışma sayfasına erişmelisiniz. Yeni bir çalışma kitabı ile çalışıyorsanız, muhtemelen ilk çalışma sayfasında olacaksınız.

### Adım 4: Sayıyı Özel Bir Formata Dönüştürme
Bir hücreyi özel gösterime biçimlendirmek için, onun özel formatını ayarlamanız gerekir.

### Adım 5: Çalışma Kitabını Kaydet
Hücreleri ihtiyaçlarınıza göre biçimlendirdikten sonra, çalışma kitabınızı kaydetmeyi unutmayın. Bu, hücreler bilimsel gösterimde biçimlendirilmiş çalışma kitabınızı kaydedecektir.

### Özel Sayı Formatları

`style.Custom` özelliği, özel sayı formatları tanımlamanıza olanak sağlar. İşte birkaç örnek:

- **Telefon Numarası:** `"(###) ###-####"`
- **Posta Kodu:** `"#####-####"`
- **Sosyal Güvenlik Numarası:** `"###-##-####"`
- **Tarih Formatı:** `"yyyy-aa-gg"`

İhtiyacınıza göre format dizesini belirterek hemen hemen herhangi bir sayı formatı oluşturabilirsiniz.

### Örnek Kod

İşte bu adımları gösteren kod parçası:
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FormatNumberToSpecial.js" >}}

### Sonuç

Aspose.Cells for Node.js via C++ ile sayıları özel biçimlere dönüştürmek, hücrenin stilinin özel sayı biçimini ayarlamayı içerir. Bu, çeşitli biçimlendirme seçeneklerine olanak tanır ve verilerinizi tam istediğiniz gibi gösterir. Unutmayın, özel biçimlerin anahtarı sağlayacağınız biçim dizesidir; bu, sayının nasıl görüntüleneceğini belirler.

{{< app/cells/assistant language="nodejs-cpp" >}}
