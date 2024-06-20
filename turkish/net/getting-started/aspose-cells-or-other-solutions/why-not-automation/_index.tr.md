---
title: Neden Otomasyon Yerine
type: docs
weight: 50
url: /tr/net/why-not-automation/
---

{{% alert color="primary" %}}

Aspose bileşenlerinin Microsoft Office Otomasyonundan çok daha iyi bir seçenek olmasının nedenleri nelerdir?

{{% /alert %}}

## **Giriş**

Aspose'da en sık duyduğumuz iki soru vardır:

1. **Ürünlerinizin çalışması için Microsoft Office'in yüklü olması gerekir mi?**
   Basit cevap hayır. Aspose bileşenleri tamamen bağımsızdır ve Microsoft Corporation tarafından yetkilendirilmiş veya onaylanmış değildir.
1. **Microsoft Office otomasyonu yerine neden Aspose ürünlerini kullanmalıyız?**
   Verebileceğimiz en kısa cevap birçok nedenin olduğudur, bu nedenlerden biri de Microsoft'un kendisinin yazılım çözümlerinden Office otomasyonu yerine kesinlikle kaçınmanızı tavsiye etmesidir: [Office'in Sunucu Tarafı Otomasyonu İçin Düşünülmeler](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Otomasyon yerine Aspose bileşenlerinin daha iyi bir alternatif olmasının birkaç nedeni vardır. Ana sebeplerden bazıları:

- Güvenlik
- Kararlılık
- Ölçeklenebilirlik/Hız
- Fiyat
- Özellikler

Ana noktalar aşağıda açıklanmıştır. Ayrıca, bu bölümün sonundaki bağlantıları ziyaret ettiğinizden emin olun.

### **Güvenlik**

Aşağıda belirtilen, yukarıda referans verilen Microsoft makalesinden alınan bir alıntıdır:

*"Office Uygulamaları hiçbir zaman sunucu tarafında kullanım için tasarlanmamıştır ve bu nedenle dağıtılan bileşenlerin karşılaştığı güvenlik sorunlarını dikkate almaz. Office gelen istekleri kimlik doğrulamaz ve sunucu tarafı kodunuzdan yanlışlıkla makroların çalıştırılmasını veya başka bir sunucunun makro çalıştırabileceğine yönelik riskleri sizden korumaz. Anonim bir Web'den sunucuya yüklenen dosyaları açmayın! Son ayarlanan güvenlik ayarlarına dayalı olarak, sunucu ayrıcalıkları ve ağınızı riske atabilecek dolaylı bir şekilde ağınızı riske atabilecek bir Administrator veya Sistem bağlamı altında makroları çalıştırabilir. Ayrıca, Office, işlemi hızlandırmak için müşteri kimlik bilgilerini önbelleğe alabilecek basit MAPI, WinInet ve MSDAIPP gibi birçok istemci tarafı bileşen kullanır. Office sunucu tarafında otomatikleştiriliyorsa, bir örnek birden fazla istemciyi hizmet edebilir ve kimlik bilgileri bu oturum için önbelleğe alındığından, bir istemcinin başka bir istemcinin önbelleğe alınmış kimlik bilgilerini kullanarak, diğer kullanıcıları taklit ederek yönetilen erişim izinlerine sahip olması mümkündür."*

Aspose ürünleri çok güvenlidir. Aspose bileşenleri, tüm ASP.NET uygulamalarıyla aynı kullanıcı bağlamında, ASPNET kullanıcısı altında çalışır. Bu nedenle Aspose bileşenleri, önemli sistem kaynaklarına potansiyel bir risk oluşturmaz. Ayrıca, bir Aspose bileşeni tarafından bir belge açıldığında makrolar otomatik olarak çalıştırılmaz. Aspose bileşenleri, geliştiricilere Ofis dosyaları oluşturma, değiştirme ve kaydetme imkanı sunmak amacıyla oluşturulmuştur. Microsoft Office paketiyle ilişkilendirilen hiçbir risk, Aspose bileşenlerinde yer almaz.

### **Kararlılık**

Yukarıda referans verilen Microsoft makalesinden alınan aşağıdaki alıntıdır:

*"Office 2000, Office XP ve Office 2003, kurulumu ve özelliği, kullanıcı için kurulumu ve özelliği dinamik olarak çalıştırmak veya yapılandırmak için "ilk kullanımda yükle" kavramını tanıtmak için Microsoft Windows Installer (MSI) teknolojisini kullanır (sistem için veya daha sık bir kullanıcı için). Sunucu tarafında, bu hem performansı yavaşlatır hem de kullanıcının kurulumu onaylamasını veya uygun bir kurulum disketi sağlamasını isteyen bir iletişim kutusunun görünebileceği olasılığını artırır. Kullanıcı için bir son ürün olarak direnci artırmak amacıyla tasarlanmış olmasına rağmen, MSI yeteneklerinin Office'ın uygulaması sunucu tarafında kullanım için karşıt olduğu görülmektedir. Ayrıca, genel olarak Office'ın kararlılığı, sunucu tarafında çalıştırmak için tasarlanmamış veya test edilmemiştir, bu nedenle bu tür bir kullanım için kararlılık garanti edilemez. Office'ı ağ sunucusunda bir hizmet bileşeni olarak kullanmayı planlıyorsanız, programı kritik işlevleri etkileyemeyen, gerektiğinde yeniden başlatılabilen özel bir bilgisayara izole etmeye çalışın."*

Aspose bileşenleri tek bir DLL'ye paketlendiği için bunların çalışması için ek parçaların veya parçaların yüklenmesine hiçbir zaman gerek olmayacaktır. Aspose bileşenleri yalnızca .NET uygulamaları tarafından kullanılır ve bileşen kodunun insan yanıtını beklemesi için hiçbir kısmı tasarlanmamıştır. Aspose bileşenleri kapsamlı bir şekilde test edilmiştir. Aspose bileşenleri, IBM, Hilton, Reader's Digest, Bank of America gibi şirketler tarafından kullanılır.

### **Ölçeklenebilirlik/Hız**

Yukarıda referans verilen Microsoft makalesinden alınan aşağıdaki alıntıdır:

*"Sunucu tarafı bileşenlerinin, minimum fazlalığa sahip ve yüksek verimliliğe sahip çoklu istemcilere yönelik olarak tasarlanmış, çoklu-threaded COM bileşenleri olması gerekir. Ofis Uygulamaları neredeyse tüm yönleriyle tamamen zıttır. Onlar, yalnız bir istemci için çeşitli ama kaynak yoğun işlevsellik sağlamak üzere tasarlanmış STA tabanlı Otomasyon sunucularıdır. Sunucu tarafında az ölçeklenebilirlik sağlarlar ve hafıza gibi önemli unsurlara sabit sınırların konulmasını önler. Daha da önemlisi, genel kaynaklar (belleğe haritalanmış dosyalar, global eklentiler veya şablonlar ve paylaşılan Otomasyon sunucuları gibi) kullanabilirler ve eş zamanlı olarak çalışan örneklerin sayısını sınırlayabilir ve çoklu istemci ortamında yarış koşullarına yol açabilirler. Herhangi bir Ofis Uygulaması örneğinin aynı anda birinden fazlasının çalışmasını planlayan geliştiricilerin, potansiyel kilitlenmeleri veya veri bozulmalarını önlemek için Ofis Uygulamasına erişimi "havuzlama" veya serialleştirmeyi düşünmeleri gerekmektedir."*

Aspose bileşenleri yüksek ölçeklenebilirlik ve çok hızlıdır. Office uygulamaları aynı anda yüzlerce veya binlerce kullanıcı tarafından kullanılmak üzere tasarlanmamıştır; ancak Aspose bileşenleri tam olarak bu amaçla tasarlanmıştır. Bileşenlerimiz, tek bir uygulamayı çalıştıran tek bir sunucuda veya kurumsal düzeyde bir uygulamayı destekleyen yük dengelemeli bir web çiftliğinde mükemmel bir şekilde çalışır.

### **Fiyat**

Bir uygulama Microsoft Office otomasyonunu kullandığında, uygulamayı çalıştıran her makine için Microsoft Office'un bir kopyasını satın almak gerekmektedir. Bir uygulamanın bir ofis dosyası oluşturması veya manipüle etmesi gerekebilecek birçok durum vardır ancak kullanıcının Office'a sahip olmasına gerek yoktur. Aspose, sınırsız sayıda kullanıcıya dağıtımı mümkün kılan çok [maliyet etkin](https://purchase.aspose.com/buy), telif hakkı bulunmayan bir dağıtım lisansı sunmaktadır.

Web tabanlı uygulamalar oluştururken, Microsoft Office otomasyon bileşenleri sunucu tarafı çözümler için fiyatlandırılmamış veya lisanslanmamıştır ([Ofis 2000 Web Bileşenlerinin Lisanslanması ve Ofis Sunucusu Uzantıları](#)); bu nedenle, Microsoft Office bileşenlerini kullanan web uygulamalarını dağıtmak için iyi bir lisanslama çözümü mevcut değildir. Aspose, sunucu tabanlı uygulamalar için oldukça maliyet etkin bir çözüm sunmaktadır.

### **Özellikler**

Aspose bileşenleri, Ofis dosyalarını yönetmek için gereken her şeyi ve daha fazlasını sunar. Geliştiricilerin en büyük sonuçları en az çaba ile elde etmelerine olanak tanıma felsefesi ile tasarlanmışlardır. Ofis otomasyonunun aksine, Aspose bileşenleri birçok güçlü, zaman kazandıran işlev sağlar. Örneğin, [Aspose.Cells](https://products.aspose.com/cells/), geliştiricilere **DataTable** veya **DataView**'den Excel Dosyasına doğrudan veri aktarma olanağı sunar. [Aspose.Words](https://products.aspose.com/words/), .NET veri nesnesinden doğrudan Word posta birleştirme belgesine veri doldurma gibi benzer bir özellik sunar. [Her bileşen](https://products.aspose.com/total/) Aspose ailesinde kendi benzersiz, güçlü özellik setini sunar.

Bir Aspose bileşenini veya bileşen paketini satın aldığınızda en iyi kısım, geliştirme ekiplerimize erişiminiz olmasıdır. Geliştirme ekiplerimiz, şirketinizin ihtiyaç duyabileceği bir özelliğin, muhtemelen diğer şirketlerin de ihtiyaç duyacağını fark etmiştir. Her özellik isteği eklenemese de, ekiplerimiz destek sağlarken çok açık fikirli ve esnek olmaya çalışır. Bu zihniyet, Aspose bileşenlerinin güçlü olmasına yardımcı olan bir şeydir. Eğer Office otomasyon nesnelerinden ek özelliklere ihtiyacınız varsa, bu özelliklerin eklenme olasılığı çok çok düşüktür.

## **Sonuç**

{{% alert color="primary" %}}

Bu makale, Aspose bileşenlerinin Ofis otomasyonundan daha iyi bir seçenek olmasının ana nedenlerini kapsamıştır. Farklı Aspose bileşenleri risk içermeyen, zorunlu olmayan [değerlendirme sürümü](https://downloads.aspose.com/total) sunar. Aspose'un uygulamalarınız için neler yapabileceğini daha iyi görebilmek için bu değerlendirmeyi yapmanızı teşvik ediyoruz.


{{% /alert %}}
