---
title: Sayfa Yapısı ve Yazdırma Seçenekleri
type: docs
weight: 60
url: /tr/net/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

Bazen, geliştiricilerin yazdırma sürecini kontrol etmek için sayfa düzenini ve yazdırma ayarlarını yapılandırması gerekir. Sayfa yapısı ve yazdırma ayarları, çeşitli seçenekler sunar ve Aspose.Cells'de tamamen desteklenir.

Bu makale, Visual Studio.Net'te bir konsol uygulamasının nasıl oluşturulacağını ve Aspose.Cells API kullanarak birkaç basit kod satırıyla sayfa düzeni ve yazdırma seçeneklerini bir çalışma sayfasına nasıl uygulayacağınızı gösterir.

{{% /alert %}}

## **Sayfa ve Yazdırma Ayarları ile Çalışma**

Bu örnek için, Microsoft Excel'de bir çalışma kitabı oluşturduk ve sayfa düzenini ve yazdırma seçeneklerini ayarlamak için Aspose.Cells'i kullandık.

### **Sayfa Yapısı Seçeneklerini ayarlamak için Aspose.Cells'i kullanma**

Önce Microsoft Excel'de basit bir çalışma sayfası oluşturun. Ardından ona sayfa yapısı seçeneklerini uygulayın. Kodu çalıştırmak, aşağıdaki ekran görüntüsündeki gibi Sayfa Yapısı seçeneklerini değiştirir.

|**Çıktı dosyası.**|
|:- |
|![yapılacaklar:resim_alternatif_metin](page-setup-and-printing-options_1.png)|

1. Microsoft Excel'de bazı verilerle bir çalışma sayfası oluşturun:
 1. Microsoft Excel'de yeni bir çalışma kitabı açın.
 1. Biraz veri ekleyin.
1. Sayfa kurulum seçeneklerini ayarlayın:
 Dosyaya sayfa yapısı seçeneklerini uygulayın. Yeni seçenekler uygulanmadan önce, varsayılan seçeneklerin ekran görüntüsü aşağıdadır.

|**Varsayılan sayfa kurulum seçenekleri.**|
|:- |
|![yapılacaklar:resim_alternatif_metin](page-setup-and-printing-options_2.png)|

1. Aspose.Cells'i indirin ve yükleyin:
   1. [İndirmek](https://downloads.aspose.com/cells/net) .Net için Aspose.Cells.
 1. Geliştirme bilgisayarınıza kurun.
 Tüm Aspose bileşenleri kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.
1. Bir proje oluşturun:
 1. Visual Studio'yu başlatın. Açık.
 1. Yeni bir konsol uygulaması oluşturun.
 Bu örnek, bir C# konsol uygulamasını gösterecektir, ancak VB.NET'i de kullanabilirsiniz.
1. Referans ekle:
 1. Bu örnek Aspose.Cells'i kullanır, bu nedenle projeye o bileşene bir referans ekleyin. Örneğin:
 …\Program Dosyaları\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. API'i çağıran uygulamayı yazın:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Yazdırma seçeneklerini ayarlama**

Sayfa yapısı ayarları ayrıca, kullanıcıların çalışma sayfası sayfalarının nasıl yazdırılacağını denetlemesine olanak tanıyan çeşitli yazdırma seçenekleri (sayfa seçenekleri olarak da adlandırılır) sağlar. Kullanıcıların şunları yapmasına izin verir:

- Bir çalışma sayfasının belirli bir yazdırma alanını seçin.
- Başlıkları yazdırın.
- Kılavuz çizgilerini yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Yazdırma hücresi hataları.
- Sayfa sıralamasını tanımlayın.

Aşağıdaki örnek, yukarıdaki örnekte oluşturulan dosyaya (PageSetup.xls) yazdırma seçeneklerini uygular. Aşağıdaki ekran görüntüsü, yeni seçenekler uygulanmadan önceki varsayılan yazdırma seçeneklerini gösterir.

|**Giriş belgesi**|
|:- |
|![yapılacaklar:resim_alternatif_metin](page-setup-and-printing-options_3.png)|
Kodun çalıştırılması yazdırma seçeneklerini değiştirir.

|**Çıktı dosyası**|
|:- |
|![yapılacaklar:resim_alternatif_metin](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
