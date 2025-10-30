---
title: Sayıyı Yerel Dil Biçimine Nasıl Formatlarım
type: docs
weight: 10
url: /tr/net/how-to-format-number-to-local-language-format/
description: Bu makale, Sayıyı Yerel Dil Biçimine Formatlama API si Aspose.Cells for .NET yi anlatacaktır.
keywords: Bir sayıyı yerel dil formatına dönüştürün, Bir rakamı yerel dil formatına çevirin, Bir sayıyı karşılık gelen yerel dil formatına değiştirin, Sayısal değeri yerel dil formatına uygun biçimde formatlayın, Bir sayıyı yerel dil formatında ifade edin, Sayıyı yerel dil formatına dönüştür.
---

## **Olası Kullanım Senaryoları**

Excel'de sayıları yerel formatlara biçimlendirmek, verilerin farklı bölgeler ve kültürler arasında net anlaşılmasını, doğru yorumlanmasını ve profesyonelce sunulmasını sağlamak için önemlidir.

1. **Kültürel ve Bölgesel Uyarlama**: Farklı bölgeler ondalıklar, binlik ayırıcılar, para birimleri ve tarih formatları için çeşitli sayı formatları kullanır. 
1. **Profesyonellik ve Netlik**: Yerel formatların kullanılması, elektronik tablonuzun profesyonel görünümünü artırır. Detaylara özen gösterdiğinizi ve izleyiciyi dikkate aldığınızı gösterir; bu, raporlar, finansal tablolar ve paydaşlarla paylaşılan verilerde çok önemlidir.
1. **Veri Görüntüleme Tutarlılığı**: Yerel formatlama, farklı bölgelerden ekipler veya müşterilerle iş birliği yaparken tutarlılık sağlar. Ondalık ayırıcıların karışıklığı gibi hataları önler.
1. **Dış Sistemlerle Uyumluluk**: Veriyi diğer formatlara (ör. CSV) dışa aktarırken, yerel formatlama veri bütünlüğünü korumaya yardımcı olur.
1. **Erişilebilirlik ve Kullanıcı Dostu Olma**: Yerel formatlama, yabancı biçimleri bilmeyen kullanıcılar için veriyi daha erişilebilir kılar. Örneğin, "DD/MM/YYYY" (İngiltere'de yaygın) yerine "MM/DD/YYYY" (ABD'de yaygın) tarih formatıyla gösterim kafa karışıklığını önler.
1. **Veri Doğrulama ve Doğruluk**: Yanlış formatlama, hesaplama hatalarına yol açabilir. Örneğin, ondalık ayırıcı sorunları nedeniyle bir sayı yanlış anlaşılırsa, formüller yanlış sonuçlar üretebilir. Yerel formatlar kullanmak, kullanıcıların girdiği verilerin bölgesel standartlarla uyumlu olmasını sağlar ve veri girişinde veya analiz sırasında hataları azaltır.

## **Excel'de Sayı Nasıl Yerel Dil Formatına Dönüştürülür**

Excel'de sayıları yerel dil formatına biçimlendirmek için, çeşitli yerleşik özellikler ve fonksiyonlar kullanabilirsiniz; bunlar farklı bölgesel ayarlara uyum sağlar. 

1. **Excel'in Yerel Ayar Ayarlarını Kullanma**: Dosya > Seçenekler > Bölgesel Ayarlar (veya benzeri, Excel sürümüne bağlı olarak). İstediğiniz dil/bölgeyi seçin (ör. Dolar işareti ondalık ayırıcılar için Almanca, Nokta ayırıcılar için İngilizce). Mevcut değerler ve formüller otomatik olarak yeni formata dönüşür.
1. **Özel Yerelleştirilmiş Biçimlendirme İçin METİN Fonksiyonunu Kullanma**: METİN fonksiyonu, yerel ayarlara özel desenler kullanarak sayıların biçimlendirilmesini sağlar; telefon numaraları veya para birimleri gibi sayıların gösterilmesinde kullanışlıdır. Söz dizimi: =METİN(değer, "biçim_kodu").
1. **Programatik İşlem (VBA/APIs)**: VBA kullanan geliştiriciler için, NumberFormat kullanabilirsiniz; ör. "#.##" gibi ABD İngilizcesi biçim dizileriyle. Excel, kullanıcının bölgesel ayarlarına otomatik uyum sağlar. Bölgesel-format dizileri kullanmak isterseniz, NumberFormatLocal kullanmayın.
1. **Sistem Ayırıcılarını Belirli Durumlar İçin Geçersiz Kılma**: Yerel biçimlendirme beklenmedik şekilde davranıyorsa (ör. Windows güncellemeleri ayırıcıları etkilediyse), varsayılanları manuel olarak geçersiz kılabilirsiniz: Excel seçeneklerinde "Sistem ayırıcılarını kullan" seçeneğini kaldırın ve özel ondalık/binlik ayırıcılar tanımlayın.
1. **Özel Format Kullanarak Sayı Biçimlendirme**: Hücreye sağ tıklayın, 'Hücreleri Biçimlendir' seçeneğini seçin, sonra 'Sayı'->'İleri' ve istenen özel sayı türünü ayarlayın. Çin ortamında özel sayı formatları ayarlamaya örnek olarak alınmıştır.
<br>
<img src="1.png" width=60% />


## **Aspose.Cells for .NET numarasına yerel dil formatı nasıl uygulanır?**

Aspose.Cells for .NET numarasını yerel dil formatına dönüştürmek için, hücre veya hücre aralığıyla ilişkili `Style` nesnesini kullanabilirsiniz. `Style` nesnesi, çeşitli biçimlendirme seçenekleri ve özel sayı formatı ayarlarına izin verir. 

Aşağıda, Aspose.Cells for .NET numarasını içeren bir hücreye yerel dil sayı biçimi uygulamanın temel bir örneği verilmiştir:

1. **Aspose.Cells Referansı**: Projenizde Aspose.Cells for .NET referanslı olduğundan emin olun. NuGet veya Aspose web sitesinden edinebilirsiniz.

2. **Bir Çalışma Kitabı Oluşturun veya Açın**: Yeni bir çalışma kitabı oluşturabilir veya mevcut birini açabilirsiniz.

3. **İstenen Hücreyi Erişin**: Biçimlendirmek istediğiniz hücreyi veya hücre aralığını belirleyin ve erişin.

4. **Özel Sayı Formatını Uygula**: Hücrenin sayı formatını Çin dili sayı biçimine ayarlayın.

4. **Örnek Kod**: İşlemleri gösteren bir kod parçacığı burada.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-FormatNumber-To-LocalLanguageFormat.cs" >}}

## **Örnek kodla üretilen çıktı**
İşte yukarıdaki örnek kodun pdf sonucu.
<br>
<img src="2.png" width=60% />

{{< app/cells/assistant language="csharp" >}}
