---
title: Sayfa Düzeni ve Yazdırma Seçenekleri
type: docs
weight: 60
url: /tr/python-net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Bazen geliştiricilerin baskı işlemini kontrol etmek için sayfa düzeni ve yazdırma ayarlarını yapılandırması gerekir. Sayfa düzeni ve yazdırma ayarları çeşitli seçenekler sunar ve Aspose.Cells for Python via .NET'de tamamen desteklenir.

Bu makale, Visual Studio.Net'te nasıl bir konsol uygulaması oluşturulacağını ve birkaç basit satır kod kullanarak Aspose.Cells for Python via .NET API'si ile bir çalışma sayfasına sayfa düzeni ve yazdırma seçenekleri uygulamayı gösterir.

{{% /alert %}}

## **Sayfa ve Yazdırma Ayarları İle Çalışma**

Bu örnekte, Microsoft Excel'de bir çalışma kitabı oluşturduk ve Aspose.Cells for Python via .NET kullanarak sayfa düzeni ve yazdırma seçeneklerini ayarladık.

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


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPageSetup-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPrintingOptions-1.py" >}}
