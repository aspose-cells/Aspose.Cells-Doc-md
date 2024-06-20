---
title: Lisanslama
type: docs
weight: 50
url: /tr/python-java/licensing/
---

{{% alert color="primary" %}} 

**Aspose.Cells** için Python via Java sürümünü `pip install aspose-cells` komutu ile yükleyebilirsiniz. Değerlendirme sürümü, ürünün lisanslı sürümü ile tamamen aynı yetenekleri sağlar. Ayrıca, değerlendirme sürümü, bir lisans satın aldığınızda ve lisansı uygulamak için birkaç satır kod eklediğinizde basitçe lisanslı hale gelir.

**Aspose.Cells** değerlendirmenizden memnun kalırsanız, Aspose web sitesinden [lisans satın alabilirsiniz](https://purchase.aspose.com). Sunulan farklı abonelik türleri hakkında bilgi edinin. Herhangi bir sorunuz varsa, Aspose satış ekibiyle iletişime geçmekten çekinmeyin.

Her Aspose lisansı, bu süre zarfında ortaya çıkan yeni sürümlere veya düzeltmelere ücretsiz yükseltmeler için bir yıllık abonelik içerir. Teknik destek, lisanslı ve değerlendirme kullanıcılara ücretsiz ve sınırsız olarak sağlanır.

{{% /alert %}} {{% alert color="primary" %}} 

**Aspose.Cells**'i değerlendirme sınırlamaları olmadan test etmek istiyorsanız, 30 günlük geçici bir lisans isteyin. Daha fazla bilgi için [Geçici Lisans Nasıl Alınır?](https://purchase.aspose.com/temporary-license) sayfasına başvurun.

{{% /alert %}}

## **Değerlendirme Sürümü Kısıtlamaları**

Lisans belirtilmeden **Aspose.Cells** ürününün değerlendirme sürümü, tam ürün işlevselliği sağlar, ancak bir programda 100 dosyayı açmak ve ek bir çalışma sayfası ile sınırlıdır.

Sınırlamalar aşağıda gösterilmiştir:

### **1. Sınırlama: Açılan Dosya Sayısı**

Programınızı çalıştırdığınızda, yalnızca 100 Excel dosyasını açabilirsiniz. Uygulamanız bu sayıyı aşarsa, bir istisna fırlatılacaktır.

### **2. Sınırlama: Değerlendirme Filigranı ile Çalışma Sayfası**

![todo:image_alt_text](licensing_1.png)

Bu çalışma sayfası her zaman etkin çalışma sayfası olarak gösterilir. Yalnızca lisanslı sürümde etkin çalışma sayfasını diğer çalışma sayfalarına ayarlayabilirsiniz.

## **Lisans Ayarlama**

Lisans, ürün adı, lisanslanan geliştiricilerin sayısı, abonelik bitiş tarihi gibi detayları içeren düz metin XML dosyasıdır. Dosya dijital olarak imzalanmıştır, bu nedenle dosyayı değiştirmeyin; hatta dosyaya yanlışlıkla ek bir satır aralığı eklemek bile geçersiz kılacaktır.

Aspose.Cells kullanmadan önce lisansı ayarlamanız gerekmektedir. Bir uygulama veya işlem başına yalnızca bir kez lisans ayarlamanız gerekmektedir.

Lisans, aşağıdaki konumlardan bir dosyadan yüklenebilir:

1. Açık yol.
1. Çalışma klasörü.

Bileşeni lisanslamak için [License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License) yöntemini kullanın. Lisansı ayarlamak için genellikle en kolay yol, lisans dosyasını Aspose.Cells.jar ile aynı klasöre koymak ve sadece dosya adını belirtmektir, yol olmadan aşağıdaki örnekte gösterildiği gibi.

### **Örnek**

Bu örnekte **Aspose.Cells**, lisans dosyasını çalışma klasörünüzde bulmaya çalışacaktır.

{{< highlight python >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
