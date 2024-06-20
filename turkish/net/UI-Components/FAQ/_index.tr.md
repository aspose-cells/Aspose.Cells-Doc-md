---
title: SSS
type: docs
weight: 400
url: /tr/net/grid-faq/
---

## **Aspose.Cells Grid Kontrolleri değerlendirme sürümünde herhangi bir kısıtlama var mı?**
Hayır, bu Kontrollerin değerlendirme sürümünde özellik kısıtlaması yoktur.

Değerlendirme sürümü, lisanslı sürümün tüm özelliklerini sunar ancak çıktı dosyalarına (Değerlendirme Telif Hakkı Uyarısı içeren **Ek Değerlendirme Çalışma Sayfası**) ekler.


## **Pazarda birçok Izgara denetimi bulunmaktadır. Neden Aspose.Cells Izgara Denetimlerini satın almalıyım?**
Aspose.Cells Izgara Denetimleri, tüm kullanıcı türleri için uygun fiyatlı olacak şekilde çok uygun fiyatlandırılmıştır. Çok makul bir fiyata,

Windows ve Web Uygulamalarında çalışmak üzere iki denetim paketi sunar. 

Ayrıca bu sadece basit bir Izgara değildir, aynı anda**Elektronik Tablo Görüntüleyici, Düzenleyici & Oluşturucusu**'dur. 

Yalnızca herhangi bir Veri Kaynağıyla (normal Izgara denetimleri gibi) bağlayamazsınız, aynı zamanda Excel dosyaları oluşturup yönetebilirsiniz. Ayrıca, Aspose.Cells Izgara paketinin desteklediği gibi sadece yerleşik işlevleri değil, aynı zamanda tarafınızca tanımlanan özel formüllerin hesaplaması için sağlam ve zengin bir **Formül Hesaplama Motoru** sunar. Aspose.Cells Izgara paketinin çok daha fazla özelliği vardır ki burada kapsanamaz, lütfen daha detaylı özellik listesi için Sürüm Tipleri sayfasına bakınız.

## **Son zamanlarda Aspose.Cells Izgara Denetimleri lisansımı satın aldım. Bu lisansı Aspose.Cells Izgara Denetimlerindeki uygulamamda nasıl kullanabilirim?**
Lütfen Aspose.Cells Izgara Denetimleri'nin [Lisanslama](/cells/tr/net/licensing/) sayfasına bakınız. 

Uygulamalarınızda Aspose.Cells Izgara Denetimleri ile lisansı nasıl kullanacağınız hakkında tam bilgi sağlar.



## **Aspose.Cells.GridWeb tabanlı web projemi/çözümümü Sunucu üzerine nasıl dağıtabilirim?**
Eğer GridWeb denetimi içeren web uygulamasını dağıtmanız gerekiyorsa, "acw_client" dizinini projeniz klasörüne en az kopyalamanız gerekir, aksi halde web uygulamanız (sunucuda dağıtılmış) onu bulamaz.

Her zaman VS.NET Projenizdeki yapılandırma bölümüne (örneğin web.config dosyasına) aşağıdaki kod satırlarını ekleyerek komut dosyasını belirtebilirsiniz. "acw_client", dosya ve Aspose.Cells.GridWeb'in davranışını belirlemek için bu klasörü kullanır ve iç benzersiz konfigrasyonunu yönetmek için gereken betik dosyalarını, resim dosyalarını ve diğer dosyaları içerir. Yerleşik istemci kaynaklarının (resimler, komut dosyaları vs.) kullanılmasını önlemek için config dosyası, bazı durumlarda / senaryolarda yararlıdır.

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Yol her zaman proje dizinleriyle ilgilidir. Proje dizinlerinizin dışında olan herhangi bir dizini kullanmamalısınız. Bu nedenle, "acw_client" dizinini (GridWeb kurulum klasöründeki) proje dizinine kopyalamanız gerekir.

{{% /alert %}} 
## **Aspose.Cell.GridWeb'i Internet Explorer'da çalıştırmak**
Mevcut olarak Aspose.Cells.GridWeb artık Internet Explorer'ı desteklemiyor, çok eski bir tarayıcıdır. 
Chrome, Edge, Firefox, Safari, Opera'yı destekliyoruz



