---
title: Sayfa Düzeni ve Yazdırma Seçenekleri
type: docs
weight: 60
url: /tr/net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler yazdırma sürecini kontrol etmek için sayfa düzeni ve yazdırma ayarlarını yapılandırmak isteyebilir. Sayfa düzeni ve yazdırma ayarları çeşitli seçenekler sunar ve Aspose.Cells tarafından tamamen desteklenir.

Bu makale, Visual Studio.Net'te bir konsol uygulaması oluşturmayı ve Aspose.Cells API'sını kullanarak birkaç basit kod satırı ile bir çalışma sayfasına sayfa düzeni ve yazdırma seçeneklerini uygulamayı göstermektedir.

{{% /alert %}}

## **Sayfa ve Yazdırma Ayarları İle Çalışma**

Bu örnekte, Microsoft Excel'de bir çalışma kitabı oluşturduk ve Aspose.Cells kullanarak sayfa düzeni ve yazdırma seçeneklerini ayarladık.

### **Aspose.Cells Kullanarak Sayfa Düzeni Seçenekleri Ayarlama**

Öncelikle Microsoft Excel'de basit bir çalışma sayfası oluşturun. Sonra ona sayfa düzeni seçenekleri uygulayın. Kodu yürüttüğünüzde, aşağıdaki ekran görüntüsünde görülen gibi Sayfa Düzeni seçeneklerini değiştirir.

|**Çıktı dosyası.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Microsoft Excel'de bazı veriler içeren bir çalışma sayfası oluşturun:
   1. Microsoft Excel'de yeni bir çalışma kitabı açın.
   1. Bazı veriler ekleyin.
1. Sayfa düzeni seçeneklerini ayarlayın:
   Ayarları dosyaya uygulayın. Yeni ayarların uygulanmadan önceki varsayılan seçeneklerin ekran görüntüsü aşağıda verilmiştir.

|**Varsayılan sayfa düzeni seçenekleri.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Aspose.Cells'i indirin ve kurun:
   1. Aspose.Cells for .Net'i [indirin](https://downloads.aspose.com/cells/net).
   1. Geliştirme bilgisayarınıza kurun.
      Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun:
   1. Visual Studio. Net'i başlatın.
   1. Yeni bir konsol uygulaması oluşturun.
      Bu örnek bir C# konsol uygulamasını gösterecek, ancak VB.NET'i de kullanabilirsiniz.
1. Referanslar ekleyin:
   1. Bu örnek Aspose.Cells kullanır, bu bileşene projeye bir referans ekleyin. Örneğin:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. API'yi çağıran uygulamayı yazın:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Yazdırma seçeneklerini ayarlama**

Sayfa ayarı ayarları ayrıca kullanıcıların çalışma sayfalarının nasıl yazdırılacağını kontrol etmelerine olanak tanıyan birkaç yazdırma seçeneği (aynı zamanda sayfa seçenekleri de denir) sağlar. Kullanıcılara şunları yapma olanağı tanırlar:

- Bir çalışma sayfasının belirli bir baskı alanını seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.

Aşağıdaki örnek yeni seçeneklerin uygulandığı dosyaya (Yukarıdaki örnekte oluşturulan PageSetup.xls) yazdırma seçeneklerini uygular. Aşağıdaki ekran görüntüsü, yeni seçenekler uygulanmadan önceki varsayılan yazdırma seçeneklerini gösterir.

|**Giriş belgesi**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Kodun çalıştırılması yazdırma seçeneklerini değiştirir.

|**Çıktı dosyası**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
