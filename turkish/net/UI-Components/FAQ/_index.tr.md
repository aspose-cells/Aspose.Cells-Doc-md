---
title: SSS
type: docs
weight: 400
url: /tr/net/grid-faq/
---
## **Aspose.Cells Grid Controls değerlendirme versiyonunda herhangi bir sınırlama var mı?**
 Hayır, Aspose.Cells Grid Controls değerlendirme sürümünde herhangi bir özellik sınırlaması yoktur. Değerlendirme sürümü, fazladan bir çalışma sayfası eklemesi dışında lisanslı sürümün tüm özelliklerini sağlar (içeren**Değerlendirme Telif Hakkı Uyarısı** ) çıkış dosyalarına.
## **Piyasada pek çok Grid kontrolü mevcuttur. Neden Aspose.Cells Grid Controls satın almalıyım?**
 Aspose.Cells Şebeke Kontrolleri, her tür kullanıcı için uygun fiyatlı olacak şekilde çok iyi fiyatlandırılmıştır. Çok makul bir fiyata, size Windows ve Web Uygulamaları üzerinde çalışmak için iki kontrol paketi sunar. Üstelik bu sadece basit bir Grid değil, sizin**Elektronik Tablo Görüntüleyici, Düzenleyici ve Oluşturucu** aynı zamanda. Onu yalnızca herhangi bir Veri Kaynağıyla (normal Izgara kontrolleri gibi) bağlayamazsınız, aynı zamanda Excel dosyaları oluşturup yönetebilirsiniz. Aynı zamanda güçlü ve zengin bir**Formül Hesaplama Motoru** yalnızca yerleşik işlevleri (Aspose.Cells Izgara Kontrolleri tarafından desteklenir) değil, aynı zamanda sizin tanımladığınız özel formülleri de hesaplamak için. Aspose.Cells Grid suite'in burada ele alınamayan çok daha fazla özelliği var, daha ayrıntılı özellikler listesi için lütfen Sürüm Türleri sayfasına bakın.
## **Yakın zamanda Aspose.Cells Grid Controls lisansımı satın aldım. Aspose.Cells Grid Control ile başvurumda o lisansı nasıl kullanabilirim?**
Lütfen şuraya bakın:[lisanslama](/cells/tr/net/licensing/) sayfa Aspose.Cells Izgara Kontrolleri. Aspose.Cells Grid Controls ile lisansı uygulamalarınızda nasıl kullanacağınıza dair tüm detayları sağlar.
## **Aspose.Cells Kılavuz Denetimleri, Visual Studio.NET 2005'te destekleniyor mu?**
Evet, Aspose.Cells Kılavuz Denetimleri, Visual Studio.NET 2005 ve sonraki sürümlerde tam olarak desteklenir.
## **Web sitemde Visual Studio.NET 2005 kullanarak Aspose.Cells.GridWeb kontrolünü kullanıyorum. Ancak, hiç çalışmıyor. Sorun ne?**
 Aspose.Cells.GridWeb her ikisini de destekler**Dosya sistemi** ve**HTTP** Visual Studio.NET 2005 modları. Hâlâ kafanız karıştıysa, lütfen Visual Studio.NET 2005 kullanarak Aspose.Cells.GridWeb ile çalışma için adım adım kılavuza bakın.
## **Aspose.Cells.GridWeb tabanlı web projemi/çözümümü Sunucu üzerinde nasıl devreye alabilirim?**
GridWeb kontrolüne sahip web uygulamasını dağıtmanız gerekirse, "acw_client" dizinini proje klasörünüze ekleyin, en azından web uygulamanız (sunucu üzerinden dağıtılan) onu bulamadı. Yapılandırma bölümüne aşağıdaki kod satırlarını ekleyerek komut dosyası yolunu her zaman belirtebilirsiniz (örn. VS.NET Projesi). "acw_client", dosyaları içeren bir klasördür ve Aspose.Cells.GridWeb, dahili yapılandırmasını yönetmek için bu klasörü kullanır, GridWeb'in davranışını belirtmek ve diğer işlemleri ayarlamak için betik dosyaları, görüntü dosyaları ve diğer dosyalara sahiptir. Yapılandırma dosyası, kontrolün bazı durumlarda/senaryolarda yararlı olan yerleşik istemci kaynaklarını (resimler, komut dosyaları vb.) kullanmak.

**xml**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Yol her zaman projenin dizini ile ilişkilidir. Proje dizini dışında herhangi bir dizini kullanmamalısınız. Bu nedenle, "acw_client" dizinini (@GridWeb kurulum klasörünüzü) projenin dizinine kopyalamanız gerekir.

{{% /alert %}} 
## **Aspose.Cell.GridWeb'i Internet Explorer 10 veya 11'de çalıştırma**
 Şu anda Aspose.Cells.GridWeb, Internet Explorer 10 veya 11'de çok iyi çalışmıyor, bu nedenle IE10/11 tarayıcı türünde onunla çalışmak için IE8/9'un uyumluluk modunu kullanmanız gerekiyor. Aşağıdaki satırı eklemelisiniz**<meta>** başlık bölümündeki etiket**.aspx** sayfa:



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

