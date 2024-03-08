---
title: Değerlendirme Sürümü Sınırlamaları
type: docs
weight: 110
url: /tr/net/evaluation-version-limitations/
description: Aspose.Cells for .NET, farklı satın alma planları sunar veya C#'deki Lisanslama ve Abonelik politikalarını kullanarak değerlendirme için Ücretsiz Deneme ve 30 günlük Geçici Lisans sunar.
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---
##  **Aspose.Cells Değerlendirme Sürümü Nasıl Alınır?**

Değerlendirme sürümünü indirebilirsiniz.**Aspose.Cells** NET için[indirme sayfası](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repo. Değerlendirme sürümü, ürünün lisanslı sürümüyle tamamen aynı yetenekleri sağlar. Ayrıca, bir lisans satın aldığınızda ve lisansı uygulamak için birkaç satır kod eklediğinizde değerlendirme sürümü kolayca lisanslanır.

 *Aspose.Cells** değerlendirmenizden memnun kaldığınızda,[lisans satın al](https://purchase.aspose.com) Aspose web sitesinde. Sunulan farklı abonelik türlerine aşina olun. Herhangi bir sorunuz varsa Aspose satış ekibiyle iletişime geçmekten çekinmeyin.

Her Aspose lisansı, bu süre içinde çıkan tüm yeni sürümlere veya düzeltmelere yönelik ücretsiz yükseltmeler için bir yıllık abonelik taşır. Teknik destek ücretsiz ve sınırsızdır ve hem lisanslı hem de değerlendirme kullanıcılarına sağlanır.

##  **Değerlendirme Sürümü Sınırlamaları Olmadan Aspose.Cells Nasıl Test Edilir**

 Test etmek istiyorsanız**Aspose.Cells**değerlendirme sürümü sınırlaması olmaksızın 30 günlük geçici lisans isteyin. Bakınız[Geçici Lisans nasıl alınır?](https://purchase.aspose.com/temporary-license) daha fazla bilgi için.


##  **Değerlendirme Sürümü Sınırlamaları**

 Değerlendirme sürümü**Aspose.Cells** ürün (lisans belirtilmeden) tam ürün işlevselliği sağlar, ancak bir programda 100 dosya ve değerlendirme filigranı içeren ekstra bir çalışma sayfası açmakla sınırlıdır.

Sınırlamalar aşağıda gösterilmiştir:

###  **1. Sınırlama: Açılan Dosya Sayısı**

Programınızı çalıştırırken yalnızca 100 adet Excel dosyasını açabilirsiniz. Başvurunuz bu sayıyı aşarsa bir istisna atılacaktır.

###  **2. Sınırlılık: Değerlendirme Filigranı İçeren Çalışma Sayfası**
Bu çalışma sayfası her zaman etkin çalışma sayfası olarak gösterilecektir. Yalnızca lisanslı sürümde etkin çalışma sayfasını diğer çalışma sayfalarına ayarlayabilirsiniz.
<br>
<image src="1.png" width="70%" />
<br>

###  **3. Sınırlama: Değerlendirme Bilgilerini İçeren Düz Metin**
Aspose.Cells numaralı çıktı Düz Metin dosyasında, belgenin sonuna bir değerlendirme bilgisi eklenecektir.
<br>
<image src="2.png" width="70%" />
<br>

###  **4. Sınırlama: PDF ve Değerlendirme Filigranı İçeren Resim**
PDF çıktısında veya Aspose.Cells görüntü dosyasında, belgenin/görüntünün üst kısmına bir değerlendirme filigranı yapıştırılır. Değerlendirme Telif Hakkı Uyarısını (ek çalışma sayfası) GridWeb kontrolünde de gizleyemezsiniz, her zaman eklenecektir (çalışma sayfası sekmelerinin sonunda) kontrolde.
<br>
<image src="3.png" width="70%" />
<br>

###  **5. Sınırlama: Yapılandırma dosyası ayarları (Aspose.Cells.GridWeb)**
Aşağıdaki kod satırlarını yapılandırma bölümüne (örneğin web.config dosyasına) ekleyerek komut dosyasının yolunu yeniden belirleyemezsiniz. Acw_client, dosyaları içeren bir klasördür ve Aspose.Cells.GridWeb, dahili yapılandırmasını yönetmek için bu klasörü kullanır. İçinde GridWeb'in davranışını belirlemek ve diğer işlemleri ayarlamak için komut dosyaları, görüntü dosyaları ve diğer dosyalar bulunur. Yapılandırma dosyası, kontrolün bazı durumlarda/senaryolarda yararlı olan gömülü istemci kaynaklarını (resimler, komut dosyaları vb.) kullanmasını önlemek için kullanılır. Ayrıca web.config dosyasındaki bu yapılandırma ayarları yalnızca kontrolün LİSANSLI sürümünde geçerli olacaktır.

**XML**
{{< highlight "csharp" >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Dosya Sistemi Web Sitelerinde veya MS Ajax uzantılarında vb. Aspose.Cells.GridWeb kontrolünü kullanıyorsanız bazı durumlarda/senaryolarda bu ayarlar zorunlu olabilir.

{{% /alert %}}