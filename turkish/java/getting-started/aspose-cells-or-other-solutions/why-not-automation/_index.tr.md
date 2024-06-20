---
title: Neden Otomasyon Yerine
type: docs
weight: 20
url: /tr/java/why-not-automation/
---

{{% alert color="primary" %}}

Aspose bileşenlerinin Microsoft Office Otomasyonundan çok daha iyi bir seçenek olmasının nedenleri nelerdir?

Aspose'da en sık duyduğumuz iki soru vardır:

1. **Ürünlerinizin çalışması için Microsoft Office'in yüklü olması gerekir mi?** 
   Basit cevap hayır. Aspose bileşenleri tamamen bağımsızdır ve Microsoft Corporation tarafından yetkilendirilmiş veya onaylanmış değildir.
1. **Microsoft Office otomasyonu yerine neden Aspose ürünlerini kullanmalıyız?**
   Verebileceğimiz en kısa cevap birçok nedenin olduğudur, bu nedenlerden biri de Microsoft'un kendisinin yazılım çözümlerinden Office otomasyonu yerine kesinlikle kaçınmanızı tavsiye etmesidir: [Office'in Sunucu Tarafı Otomasyonu İçin Düşünülmeler](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Otomasyon yerine Aspose bileşenlerinin daha iyi bir alternatif olmasının birkaç nedeni vardır. Ana sebeplerden bazıları:

- [Güvenlik](/cells/tr/java/why-not-automation/#security)
- [Kararlılık](/cells/tr/java/why-not-automation/#security)
- [Ölçeklenebilirlik/Hız](/cells/tr/java/why-not-automation/#security)
- [Fiyat](/cells/tr/java/why-not-automation/#security)
- [Özellikler](/cells/tr/java/why-not-automation/#security)

Ana noktalar aşağıda açıklanmıştır. Ayrıca, bu bölümün sonundaki bağlantıları ziyaret ettiğinizden emin olun.

{{% /alert %}}

## **Güvenlik**

Yukarıdaki Microsoft makalesinden direkt alıntı şöyledir: *"Office Uygulamaları asla sunucu tarafında kullanılmak üzere tasarlanmamıştır, bu nedenle dağıtılan bileşenler tarafından karşılaşılan güvenlik sorunlarını dikkate almazlar. Office gelen istekleri kimlik doğrulamaz ve sunucu tarafında yerel olarak makroların yanlışlıkla çalışmasını veya başka bir sunucunun makroları çalıştırmasını engellemez. Sunucuya anonim Web'den yüklenen dosyaları açmayın! Son ayarlanan güvenlik ayarlarına dayanarak, sunucu yönetici veya Sistem içeriği altında tam ayrıcalıklarla makroları çalıştırabilir ve ağınızı tehlikeye atabilir! Ayrıca, Office çok sayıda istemci tarafı bileşeni (örneğin Basit MAPI, WinInet ve MSDAIPP) kullanır ve hızlı işlem yapmak için istemci kimlik doğrulama bilgilerini önbelleğe alabilir. Office sunucu tarafında otomatik olarak etkinleştiriliyorsa, bir örneğin birden fazla istemciye hizmet etmesi mümkündür ve oturumun önbelleğe alınmış kimlik doğrulama bilgilerini kullandığı için, bir istemci başka bir istemcinin önbelleğe alınmış kimlik bilgilerini kullanabilir ve böylece diğer kullanıcıları taklit ederek kazanılmamış erişim izinleri kazanabilir."*

Aspose ürünleri çok güvenlidir. Aspose bileşenleri, tüm ASP.NET uygulamalarıyla aynı kullanıcı bağlamında, ASPNET kullanıcısı altında çalışır. Bu nedenle Aspose bileşenleri, önemli sistem kaynaklarına potansiyel bir risk oluşturmaz. Ayrıca, bir Aspose bileşeni tarafından bir belge açıldığında makrolar otomatik olarak çalıştırılmaz. Aspose bileşenleri, geliştiricilere Ofis dosyaları oluşturma, değiştirme ve kaydetme imkanı sunmak amacıyla oluşturulmuştur. Microsoft Office paketiyle ilişkilendirilen hiçbir risk, Aspose bileşenlerinde yer almaz.

## **Kararlılık**

Aşağıdaki alıntı yukarıda bahsedilen Microsoft makalesinden alınmıştır: *"Office 2000, Office XP ve Office 2003, kurulumu ve otomatik onarımı kullanıcı için daha kolay hale getirmek için Microsoft Windows Installer (MSI) teknolojisini kullanır. MSI, "ilk kullanımda yükle" kavramını tanıtır, bu da özelliklerin çalışma zamanında dinamik olarak yüklenmesine veya yapılandırılmasına (sistem için veya daha sık olarak belirli bir kullanıcı için) olanak tanır. Bir sunucu tarafı ortamında bu, performansı yavaşlatır ve kullanıcının yüklemeyi onaylamasını veya uygun bir yükleme diski sağlamasını isteyen bir iletişim kutusunun görünme olasılığını artırır. Office'un MSI özelliklerinin uygulanması, son kullanıcı ürünü olarak Office'un dayanıklılığını artırmak amacıyla tasarlanmış olmasına rağmen, sunucu tarafı ortamında karşı üretken bir şekilde çalışır. Ayrıca, genel olarak Office'un kararlılığı, bu tür kullanımlar için tasarlanmamış veya test edilmemiştir. Office sunucu tarafında bir hizmet bileşeni olarak kullanmayı planlıyorsanız, programı kritik işlevleri etkileyemeyen ve ihtiyaç duyulduğunda yeniden başlatılabilen bir özel bir bilgisayara izole etmeye çalışın."*

Aspose bileşenleri tek bir DLL'ye paketlendiği için bunların çalışması için ek parçaların veya parçaların yüklenmesine hiçbir zaman gerek olmayacaktır. Aspose bileşenleri yalnızca .NET uygulamaları tarafından kullanılır ve bileşen kodunun insan yanıtını beklemesi için hiçbir kısmı tasarlanmamıştır. Aspose bileşenleri kapsamlı bir şekilde test edilmiştir. Aspose bileşenleri, IBM, Hilton, Reader's Digest, Bank of America gibi şirketler tarafından kullanılır.

## **Ölçeklenebilirlik/Hız**

Aşağıdaki alıntı yukarıda bahsedilen Microsoft makalesinden alınmıştır: *"Sunucu tarafı bileşenleri, minimum ağır yük ve yüksek birden çok istemci için yüksek çalışma kapasitesi olan yeniden girişli, çok iş parçacıklı COM bileşenleri olmalıdır. Office Uygulamaları neredeyse tüm açılardan tam olarak aksine. Yeniden girilemez, STA tabanlı Otomasyon sunucularıdır ve tek bir istemci için çeşitli ancak kaynak yoğun işlevsellik sağlaması için tasarlanmıştır. Bunlar sunucu tarafı çözümü olarak pek ölçeklenebilirlik sunmazlar ve özellikle hafızaya değiştirilemeyen sabit sınırlara sahiptirler. Daha da önemlisi, bunlar (hafıza haritalı dosyalar, genel eklentiler veya şablonlar ve paylaşılan Otomasyon sunucuları gibi) genel kaynaklar kullanır, bu da eşzamanlı olarak çalışan örneklerin sayısını sınırlayabilir ve çoklu istemci ortamında yapılandırılırlarsa yarış koşullarına yol açabilir. Herhangi bir Office Uygulamasının aynı anda birden fazla örneğini çalıştırmayı planlayan geliştiricilerin potansiyel kilitlenmelerden veya veri bozulmalarından kaçınmak için Office Uygulamasına erişimi "havuzlamak" veya serileştirmek için düşünmeleri gerekmektedir."*

Aspose bileşenleri yüksek ölçeklenebilirlik ve çok hızlıdır. Office uygulamaları aynı anda yüzlerce veya binlerce kullanıcı tarafından kullanılmak üzere tasarlanmamıştır; ancak Aspose bileşenleri tam olarak bu amaçla tasarlanmıştır. Bileşenlerimiz, tek bir uygulamayı çalıştıran tek bir sunucuda veya kurumsal düzeyde bir uygulamayı destekleyen yük dengelemeli bir web çiftliğinde mükemmel bir şekilde çalışır.

## **Fiyat**

Bir uygulama Microsoft Office otomasyonunu kullandığında, uygulamayı çalıştıran her makine için Microsoft Office'un bir kopyasını satın almak gerekmektedir. Bir uygulamanın bir ofis dosyası oluşturması veya manipüle etmesi gerekebilecek birçok durum vardır ancak kullanıcının Office'a sahip olmasına gerek yoktur. Aspose, sınırsız sayıda kullanıcıya dağıtımı mümkün kılan çok [maliyet etkin](https://purchase.aspose.com/buy), telif hakkı bulunmayan bir dağıtım lisansı sunmaktadır.

Web tabanlı uygulamalar oluşturulurken, Microsoft Office bileşenleri için fiyatlandırma veya lisanslama yapılmamakta, bu nedenle Microsoft Ofis bileşenlerini kullanan web uygulamalarının dağıtımı için iyi bir lisanslama çözümü bulunmamaktadır. Aspose, sunucu tabanlı uygulamalar için çok maliyet etkin bir çözüm sunmaktadır.

## **Özellikler**

Aspose bileşenleri, Ofis dosyalarını yönetmek için gereken her şeyi ve daha fazlasını sunar. Geliştiricilerin en büyük sonuçları en az işle yaparak elde etmelerine olanak tanıyan bir felsefe ile tasarlanmışlardır. Ofis otomasyonunun aksine, Aspose bileşenleri birçok güçlü, zaman kazandırıcı işlev sunar. Örneğin, [Aspose.Cells](https://products.aspose.com/cells/java/), geliştiricilere bir **DataTable** veya **DataView** 'den doğrudan bir Excel Dosyasına aktarma yeteneği sunar. Aspose ailesindeki [her bileşen](https://products.aspose.com/total/), kendi benzersiz, güçlü özellik setini sunar.

Bir Aspose bileşenini veya bileşen paketini satın aldığınızda en iyi kısım, geliştirme ekiplerimize erişiminiz olmasıdır. Geliştirme ekiplerimiz, şirketinizin ihtiyaç duyabileceği bir özelliğin, muhtemelen diğer şirketlerin de ihtiyaç duyacağını fark etmiştir. Her özellik isteği eklenemese de, ekiplerimiz destek sağlarken çok açık fikirli ve esnek olmaya çalışır. Bu zihniyet, Aspose bileşenlerinin güçlü olmasına yardımcı olan bir şeydir. Eğer Office otomasyon nesnelerinden ek özelliklere ihtiyacınız varsa, bu özelliklerin eklenme olasılığı çok çok düşüktür.

## **Sonuç**

{{% alert color="primary" %}}

Bu makale, Aspose bileşenlerinin Neden Office otomasyonundan daha iyi bir seçenek olduğu konusundaki temel noktaları ele almıştır. Farklı Aspose bileşenlerinin hepsi risksiz, hiçbir yükümlülük olmayan bir [değerlendirme sürümü](https://products.aspose.com/total/) sunmaktadır. Aspose'nin uygulamalarınız için neler yapabileceğini daha iyi anlamanız için bu değerlendirmeyi yapmanızı teşvik ediyoruz.

Daha fazla bilgi için, aşağıdaki İnternet makalelerine bakın:

- [Office'nin Sunucu Tarafı Otomasyonu için Düşünceler](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
