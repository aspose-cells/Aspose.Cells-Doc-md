---
title: lisanslama
type: docs
weight: 50
url: /tr/python-java/licensing/
---
{{% alert color="primary" %}} 

 değerlendirme sürümünü yükleyebilirsiniz.**Aspose.Cells** for Python via Java ile `pip install aspose-cells`. Değerlendirme sürümü, ürünün lisanslı sürümü ile tamamen aynı yetenekleri sağlar. Ayrıca, bir lisans satın aldığınızda ve lisansı uygulamak için birkaç satır kod eklediğinizde, değerlendirme sürümü kolayca lisanslanır.

 Değerlendirmenizden memnun olduğunuzda**Aspose.Cells** , yapabilirsiniz[lisans satın al](https://purchase.aspose.com)Aspose web sitesinde. Sunulan farklı abonelik türleri hakkında bilgi sahibi olun. Herhangi bir sorunuz varsa, Aspose satış ekibiyle iletişime geçmekten çekinmeyin.

Her Aspose lisansı, bu süre içinde çıkan tüm yeni sürümlere veya düzeltmelere ücretsiz yükseltmeler için bir yıllık abonelik içerir. Teknik destek ücretsiz ve sınırsızdır ve hem lisanslı hem de değerlendirme kullanıcılarına sağlanır.

{{% /alert %}} {{% alert color="primary" %}} 

 test etmek istersen**Aspose.Cells** değerlendirme sürümü sınırlamaları olmadan, 30 günlük bir geçici lisans talep edin. Bakınız[Geçici Lisans nasıl alınır?](https://purchase.aspose.com/temporary-license) daha fazla bilgi için.

{{% /alert %}}

## **Değerlendirme Sürümü Sınırlamaları**

 değerlendirme versiyonu**Aspose.Cells** ürün (belirtilen bir lisans olmadan), tam ürün işlevselliği sağlar, ancak bir programda 100 dosya ve değerlendirme filigranlı fazladan bir çalışma sayfası açmakla sınırlıdır.

Sınırlamalar aşağıda gösterilmiştir:

### **1. Sınırlama: Açılan Dosya Sayısı**

Programınızı çalıştırırken sadece 100 Excel dosyası açabilirsiniz. Uygulamanız bu sayıyı aşarsa bir istisna atılır.

### **2. Sınırlama: Değerlendirme Filigranlı Çalışma Sayfası**

![yapılacaklar:resim_alternatif_Metin](licensing_1.png)

Bu çalışma sayfası her zaman etkin çalışma sayfası olarak gösterilir. Yalnızca lisanslı sürümde, aktif çalışma sayfasını diğer çalışma sayfalarına ayarlayabilirsiniz.

## **Lisans Ayarlama**

Lisans, ürün adı, lisanslandığı geliştirici sayısı, abonelik bitiş tarihi gibi ayrıntıları içeren düz metin bir XML dosyasıdır. Dosya dijital olarak imzalanmıştır, bu nedenle dosyayı değiştirmeyin; dosyaya yanlışlıkla fazladan bir satır sonu eklenmesi bile dosyayı geçersiz kılacaktır.

Değerlendirme sınırlamalarından kaçınmak istiyorsanız, Aspose.Cells'i kullanmadan önce bir lisans ayarlamanız gerekir. Uygulama veya işlem başına yalnızca bir kez lisans ayarlamanız gerekir.

Lisans, aşağıdaki konumlardaki bir dosyadan yüklenebilir:

1. Açık yol.
1. Çalışma klasörü.

 Kullan[Lisans.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License) bileşeni lisanslama yöntemi. Genellikle bir lisans ayarlamanın en kolay yolu, lisans dosyasını Aspose.Cells.jar ile aynı klasöre koymak ve aşağıdaki örnekte gösterildiği gibi yolsuz sadece dosya adını belirtmektir:

### **Örnek**

 Bu örnekte**Aspose.Cells** çalışma klasörünüzdeki lisans dosyasını bulmaya çalışacaktır.

{{< highlight "python" >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
