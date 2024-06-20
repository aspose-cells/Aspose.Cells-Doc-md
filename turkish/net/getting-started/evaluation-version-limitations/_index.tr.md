---
title: Değerlendirme Sürümü Sınırlamaları
type: docs
weight: 110
url: /tr/net/evaluation-version-limitations/
description: Aspose.Cells for .NET, C# Lisanslama ve Abonelik politikaları kullanarak satın alma için farklı planlar veya Ücretsiz Deneme ve değerlendirme için 30 günlük Geçici Lisans sunar.
keywords: Değerlendirme Sürümü Sınırlamaları, Değerlendirme Sürümünde Açılan Dosya Sayısı, Değerlendirme Sürümü Kullanarak Değerlendirme Filigranı
---

## ****Aspose.Cells**'in Değerlendirme Sürümünü Nasıl Alınır**

**Aspose.Cells**'in .NET için değerlendirme sürümünü [indirme sayfasından](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) indirebilirsiniz. Değerlendirme sürümü, lisanslı sürümü ile tamamen aynı yetenekleri sunar. Ayrıca, değerlendirme sürümü, lisans satın aldığınızda ve lisansı uygulamak için birkaç satır kod eklediğinizde lisanslı hale gelir.

**Aspose.Cells** değerlendirmenizden memnun kalırsanız, Aspose web sitesinden [lisans satın alabilirsiniz](https://purchase.aspose.com). Sunulan farklı abonelik türleri hakkında bilgi edinin. Herhangi bir sorunuz varsa, Aspose satış ekibiyle iletişime geçmekten çekinmeyin.

Her Aspose lisansı, bu süre zarfında ortaya çıkan yeni sürümlere veya düzeltmelere ücretsiz yükseltmeler için bir yıllık abonelik içerir. Teknik destek, lisanslı ve değerlendirme kullanıcılara ücretsiz ve sınırsız olarak sağlanır.

## **Değerlendirme Sürümü Sınırlamaları olmadan Aspose.Cells'ı Nasıl Test Edebilirsiniz**

**Aspose.Cells**'i değerlendirme sınırlamaları olmadan test etmek istiyorsanız, 30 günlük geçici bir lisans isteyin. Daha fazla bilgi için [Geçici Lisans Nasıl Alınır?](https://purchase.aspose.com/temporary-license) sayfasına başvurun.


## **Değerlendirme Sürümü Kısıtlamaları**

Lisans belirtilmeden **Aspose.Cells** ürününün değerlendirme sürümü, tam ürün işlevselliği sağlar, ancak bir programda 100 dosyayı açmak ve ek bir çalışma sayfası ile sınırlıdır.

Sınırlamalar aşağıda gösterilmiştir:

### **1. Sınırlama: Açılan Dosya Sayısı**

Programınızı çalıştırdığınızda, yalnızca 100 Excel dosyasını açabilirsiniz. Uygulamanız bu sayıyı aşarsa, bir istisna fırlatılacaktır.

### **2. Sınırlama: Değerlendirme Filigranı ile Çalışma Sayfası**
Bu çalışma sayfası her zaman etkin çalışma sayfası olarak gösterilir. Yalnızca lisanslı sürümde etkin çalışma sayfasını diğer çalışma sayfalarına ayarlayabilirsiniz.
<br>
<image src="1.png" width="70%" />
<br>

### **3. Sınırlama: Değerlendirme bilgileriyle Düz Metin**
Aspose.Cells tarafından üretilen çıktı Düz Metin dosyasında, bir değerlendirme bilgisi belgenin sonuna eklenecektir.
<br>
<image src="2.png" width="70%" />
<br>

### **4. Sınırlama: PDF ve Değerlendirme Filigranı içeren Görüntü**
Aspose.Cells tarafından üretilen çıktı PDF veya görüntü dosyasında, bir değerlendirme filigranı belgenin/ görüntünün üstüne yapıştırılacaktır. Ayrıca Değerlendirme Telif Uyarısı (ek çalışma sayfası) GridWeb kontrolünde gizlenemez, her zaman kontrolde (çalışma sayfası sekmelerinde sona eklenecek şekilde) olacaktır.
<br>
<image src="3.png" width="70%" />
<br>

### **5. Sınırlama: Yapılandırma dosyası ayarları (Aspose.Cells.GridWeb)**
Aşağıdaki kod satırlarını ekleyerek (örneğin web.config dosyasında) betik yolunu yeniden belirtemezsiniz. acw_client, dosya ve Aspose.Cells.GridWeb'in iç konfigürasyonunu yönetmek için kullandığı betik dosyaları, görüntü dosyaları ve GridWeb'in davranışını belirlemek ve diğer işlemleri ayarlamak için bu klasörü içeren bir klasördür. Yapılandırma dosyası, gömülü istemci kaynaklarının (görüntüler, betikler vb.) denetimin kullanımını engellemek için kullanılır, bu bazı durumlarda / senaryolarda kullanışlıdır. Dahası, web.config dosyasındaki bu yapılandırma ayarları sadece denetimin LİSANSLI sürümü ile etki edecektir.

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Bu ayarlar, dosya sistemli web sitelerinde veya MS Ajax uzantıları vb. kullanıyorsanız bazı durumlarda zorunlu olabilir.

{{% /alert %}}
