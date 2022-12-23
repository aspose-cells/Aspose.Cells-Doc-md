---
title: VSTO'yu Aspose.Cells for .NET ile karşılaştırma
type: docs
weight: 20
url: /tr/net/comparing-vsto-with-aspose-cells-for-net/
---
{{% alert color="primary" %}}

Bu makale, Microsoft Office tabanlı çözümler geliştirmek için VSTO (Office için Visual Studio Araçları) kullanımını diğer yaklaşımlarla karşılaştırır. Özellikle Aspose.Cells'e bakar ve iki çözümün nasıl çalıştığına dair bir karşılaştırma sağlar. Makaleler, geliştiricilerin bir çözümü benimsemeden önce farklı seçenekleri analiz etmek, karşılaştırmak ve değerlendirmek için kullanabilecekleri bilgiler sağlar.

{{% /alert %}}

## **genel bakış**

Microsoft Excel, her türlü sektörde işletmeler ve bireyler tarafından yaygın olarak kullanılmaktadır. Elektronik tablo uygulaması neredeyse her yerde bulunur ve kullanıcıların yalnızca verileri depolamasına ve düzenlemesine değil, aynı zamanda formüllerle karmaşık modeller oluşturmasına ve gelişmiş biçimlendirme ve çizelgeyle verileri net bir şekilde sunmasına olanak tanır.

VSTO, Microsoft Office belgelerinin bir .NET derlemesine sarılmış kodu yürütmesine izin verir. Microsoft Office dosyaları ve özellikleri ile çalışan uygulamalar geliştirmek için kullanılır. Geliştiriciler yıllardır uygulamalarda ASP, Office Web bileşenleri ve COM birlikte çalışmasını kullandılar. Microsoft, uygulamaları geliştirmek ve dağıtmak ve bellek yönetimini iyileştirmek için geliştirilmiş VSTO'ya sahiptir. Ancak soru şu: VSTO, günümüzde mevcut olan diğer yaklaşımlara göre kullanımı daha kolay ve daha güvenilir olacak şekilde mi tasarlandı? Geliştiriciler, gelişmiş performans, güvenlik, ölçeklenebilirlik, kararlılık, güvenilirlik veya özellikler açısından kendilerini yarı yolda bırakmayacak çözümlerle çalışmak isterler.

[Aspose](http://www.aspose.com/)harika bir .NET, Java, Bulut ve Android API serisi sağlar. Aspose API'ler, yardımcı olan API'ler olan Aspose.Cells, Aspose.Words, Aspose.Pdf ve Aspose.Slides gibi ürünleri içerir.[geliştiriciler, XLS, XLSX, DOC, DOCX, HTML, PDF, PPT dahil olmak üzere çeşitli biçimlerdeki belgeleri açar, değiştirir, oluşturur, kaydeder, birleştirir ve dönüştürür.

Bu yazımızda VSTO'yu Aspose.Cells for .NET ile karşılaştırdık.

[Aspose.Cells]](https://products.aspose.com/cells/net/) istemci veya sunucu tarafında Microsoft Excel yüklü olmadan Microsoft Excel elektronik tablolarını okuyan ve yazan bağımsız bir Microsoft Excel elektronik tablo düzenlemesi API'dir. Aspose.Cells, zengin özelliklere sahip bir bileşendir ve temel veri aktarımından çok daha fazlasını sunar. Aspose.Cells ile geliştiriciler verileri dışa aktarabilir, elektronik tabloları biçimlendirebilir, görüntüleri içe aktarabilir, içe aktarabilir, grafikler oluşturabilir ve değiştirebilir, Excel verilerini aktarabilir ve çeşitli biçimlerde kaydedebilir. Ürün ve özellikleri hakkında daha fazla bilgi edinmek için:

-  Kontrol et[Aspose.Cells belgeleri](https://docs.aspose.com/cells/net/).
-  nasıl çalıştığını görün[çevrimiçi demolar](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
-  Denemek:[indirmek](https://downloads.aspose.com/cells/net)ücretsiz bir değerlendirme sürümü.

Bu makale, VSTO ve Aspose.Cells'i Microsoft Excel ile ilgili farklı açılardan karşılaştırır. Liste tam değildir ancak karar vericilerin bir yaklaşımı benimsemeden önce nihai bir karar vermeden önce anlaması gereken birkaç konuyu temsil eder.

### **.NET Çerçeve Gereksinimi**

VSTO, son uygulamayı yürütmek için istemci tarafında .NET Çerçevesini (Office SE Çalışma Zamanı için Visual Studio Araçları dahil) gerektirir. Çoğu kurumsal ortamda, özellikle web senaryolarında, son kullanıcılar uygulama yazılımını ve ilgili çalışma zamanı çerçevelerini kuramaz. Bu gereklilik tek başına VSTO tabanlı uygulamaları sorunlu hale getirir. VSTO'ya dayalı kullanıma hazır uygulamaları pratik olarak dışlar.

Aksine, Aspose.Cells for .NET, temel senaryo için istemci tarafında mutlaka .NET Çerçevesini talep etmez. Bileşenle oluşturulan Office uygulamaları hafiftir ve önemli yük altında Microsoft Windows sistemlerinde çalışması garantilidir.

### **Özellikleri**

VSTO'nun sağladığı özellikler, yüklediğiniz VSTO ve Visual Studio ürünleri kombinasyonuna bağlıdır. Microsoft Office Excel 2003 için VSTO tarafından gerçekleştirilen yaygın görevler arasında Cells'e veri ekleme, çalışma kitaplarını oluşturma, açma ve kaydetme, çalışma sayfalarını ekleme, taşıma ve gizleme, çalışma sayfalarını koruma, adlandırılmış aralıklar, liste nesnesi, stiller biçimlendirme, hücrelerde metin arama, verileri sıralama, yazdırma ve Excel formül hesaplamaları.

Aspose.Cells, Microsoft Office Excel dosyalarını yönetmek için gereken her şeyi ve çok daha fazlasını sağlar. API, geliştiricilere en az çabayla harika sonuçlar verir. Aspose.Cells, birçok güçlü, zaman kazandıran işlev sunar. API, Microsoft Excel'in sağladığı hemen hemen tüm özellikleri kapsayan, her türlü elektronik tablo yönetimi etkinliği için kullanımı kolay API'ler sağlar. VSTO için listelenen tüm görevler Aspose.Cells ile kolayca yapılabilir.

Aspose.Cells ayrıca Akıllı İşaretleyiciler desteği, çeşitli veri kaynaklarına, nesnelere ve Excel dosyalarına veri alma ve verme, COM istemcileri desteği (ASP istemcisi) Bileşenle birlikte çalışabilirlik, Excel dosyalarını PDF formatına dönüştürme dahil olmak üzere birçok gelişmiş özelliği destekler , Excel grafiklerini ve çalışma sayfalarını görüntü dosyaları olarak kaydetme.

### **Güvenlik**

Varsayılan olarak, VSTO uygulamaları, kısmen güvenilen arayanlara izin vermediğinden yürütme için Tam Güven izinleri gerektirir. Barındırılan bir ortamda bir web uygulamasını kilitlemek ve ek bir uygulama yalıtımı düzeyi sağlamak için, uygulamanın erişebileceği kaynakları ve gerçekleştirebileceği ayrıcalıklı işlemleri kısıtlamak için kod erişim güvenliğini kullanabilirsiniz. Ancak .NET güvenliğini anlamak için biraz zaman ve çaba harcamanız gerekiyor.

Birçok farklı şirketin birden çok uygulamasını barındıran İnternet Servis Sağlayıcıları (ISP'ler), uygulamaların birbirlerinin verilerini okuyamamasını veya birbirini etkilememesini sağlamaya yardımcı olmak için sıklıkla orta güven düzeyini kullanır. Güvenlik nedeniyle, ISP'ler paylaşılan sunuculardaki bireysel web uygulamalarını Kısmi Güven ile sınırlayabilir.

Aspose.Cells for .NET, Medium Trust güvenlik seviyesinde çalışabilir. Derlemeyi barındırılan bir ortamda çalıştırmak için özel ayrıcalıklar gerekmez. Orta düzeyde güven, uygulamaların erişebileceği paylaşılan sistem kaynaklarının türlerine kısıtlamalar getirir. Birçok web uygulaması Web Hosting sunucularında çalışmaktadır. Web barındırma modunda, çoğu yalnızca Orta Güven güvenlik seviyesi altında çalışabilir. Aspose.Cells for .NET bu konuda ihtiyaçlarına çok iyi hizmet edebilir.

### **Verim**

Bir çözüm oluşturmak için herhangi bir yaklaşım veya metodoloji seçerken performans en kritik faktördür.

Bir VSTO uygulamasının performansı, bazı kullanıcıların raporuna göre VBA ve COM yaklaşımlarına bağlıdır. VSTO performansını etkileyen birkaç faktör vardır ve bu faktörleri bir perspektife oturtmak önemlidir.

- .NET başlangıç maliyeti doğası gereği pahalıdır. .NET ile yazılan uygulamalar, Tam Zamanında (JIT) derlemesinin ek yüküne tabi olmalıdır, bu nedenle JIT derlemesinden kaçınılamaz.
- VSTO tabanlı uygulamaları etkileyen başka bir performans faktörü, Microsoft Office COM nesnelerini saran kalın otomasyon kaplaması katmanlarını arama masrafıyla ilgilidir. Microsoft Office ile etkileşime girecek şekilde oluşturulmuş ve optimize edilmiş VBA, .NET'den daha kısa bir mesafeye sahiptir.
- Son olarak, Excel nesnelerini Visual Studio IDE'de barındırmak, kaynaklar açısından pahalıdır. VSTO uygulamaları, VBA uygulamalarından daha büyük bir bellek ayak izine sahiptir. VSTO Excel uygulamaları çok fazla bellek kullanır ve Microsoft Excel'in tüm örnekleri kapatılana kadar asla işletim sistemine geri bırakmaz.

Microsoft Office teknolojisi için bir geliştirme platformu olarak VSTO'yu benimsemeyi düşünüyorsanız, bu öznitelikleri tanımak için kaynaklara biraz zaman ayırın.

Ayrıca, güncellemeleri her zaman denetlemenin performans üzerindeki etkisi çözüm için uygun olmayabilir (daha yavaş dağıtım sunucuları, daha yavaş ağ bağlantıları veya yalnızca sunucuya sık sık erişememek, yükleme sürelerini olumsuz etkileyebilir).

Buna karşılık, Aspose.Cells for .NET yüksek düzeyde ölçeklenebilir, esnek ve hızlıdır. Genel olarak, Office uygulamaları aynı anda 100'lerce ve 1000'lerce kullanıcı tarafından kullanılmak üzere tasarlanmamıştır; ancak, Aspose.Cells'dir. API kararlıdır ve elektronik tablo görevlerini tek bir sunucuda, tek bir uygulamaya güç vererek veya kurumsal çapta bir uygulamaya güç veren yük dengeli bir web çiftliğinde kusursuz bir şekilde gerçekleştirebilir.

### **sistem gereksinimleri**

Bu iki yaklaşım için sistem gereksinimlerini analiz ederek, VSTO'nun daha pahalı olduğunu ve daha fazla temel öğeye ihtiyaç duyduğunu görüyoruz.

VSTO'nun uzun bir ön koşul listesi vardır:

- **Desteklenen İşletim Sistemleri**: Windows 2000; Windows Sunucu 2003; Windows Vista; Windows XP
- **.NET Desteklenen çerçeve sürümleri**: yalnızca .NET çerçeve 2.0 veya üstü.
- Aşağıdaki Office için Visual Studio Araçları sürümlerinden biri veya daha fazlası:
 - Microsoft Microsoft Office Sistemi için Visual Studio 2005 Araçları
 - Microsoft 2007 Microsoft Office Sistemi için Visual Studio 2005 Araçları
 - Visual Studio 2008 Professional Sürümü
 - Visual Studio 2008 Takım Paketi Sürümü
 - Microsoft Office'in bir sürümü:
 - Microsoft Office Professional 2003 SP1
 -2007 Microsoft ofis sistemi

Aspose.Cells, elektronik tablo oluşturma motoru olduğu için Microsoft Excel'in istemcide veya sunucuda yüklenmesini gerektirmez. Ancak Microsoft Excel belgelerini görüntülemek için sistemde en az Microsoft Excel Viewer kurulu olmalıdır.

- **Desteklenen İşletim Sistemleri**: Windows 2000; Windows Sunucu 2003; Windows Vista; Windows XP
- **.NET Desteklenen çerçeve sürümleri**: tüm .NET çerçeveleri desteklenir, 1.0, 1.1, 2.0, 3.x vb.

### **Kurulum ve Dağıtım**

VSTO'yu yüklemek büyük ve zahmetli bir görev olabilir. Bazen bir kurulum, araçların özelliklerini manuel olarak yeniden kurmanızı ve bunları da manuel olarak kaydetmenizi gerektirir. Karmaşık olabilir.

Öte yandan, Aspose.Cells for .NET, tek bir DLL'de paketlenmiştir, bu nedenle ek uygulamalar yüklemeye gerek yoktur. Bileşen yalnızca .NET uygulamaları tarafından kullanılır ve bileşen kodunun hiçbir bölümü insan yanıtını bekleyecek şekilde tasarlanmamıştır. Sadece Aspose.Cells'i ziyaret edin[indirme sayfası](https://downloads.aspose.com/cells/net) ve en son Aspose.Cells yükleyicisini indirin. İndirilen dosyayı çalıştırın ve yükleyici talimatlarını izleyin. Ardından, bileşeni kullanmak için projenizde ona başvurun.

## **Örnek Görev**

İki yaklaşım arasındaki farkları göstermek için aşağıdaki kod, bir şablon dosyasını verilerle doldurmak için hem VSTO hem de Aspose.Cells API'lerinin nasıl kullanılacağını gösterir.

1. Şablon olarak bir Microsoft Excel dosyası (TempBook.xls) kullanılır.
 Çalışma kitabı, verilerle dolu birkaç hücre içeren birkaç çalışma sayfası içerir.
1. Örnek kod, şablon Excel dosyasındaki ilk çalışma sayfasına 1000*20 kayıt koyar.
 Çalışma sayfası, hücrelere sabit (kukla) verilerle doldurulur.

Görev, Microsoft Windows XP Professional işletim sisteminde Intel(R) Celeron(R) CPU 2.40 GHz, 760 MB RAM'e sahip bir sistemde gerçekleştirilir.

Aşağıdaki kod bölümleri, her bir API ile bu görevlerin nasıl gerçekleştirileceğini göstermektedir.

### **VSTO Kodu**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-VSTOCode-1.cs" >}}

### **Aspose.Cells Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-UsingAsposeCells-1.cs" >}}

### **Sonuçlar**

Sonuçlar, VSTO API kullanımının görevi bitirmesinin yaklaşık 2,5 dakika (yaklaşık 150 saniyeden fazla) sürdüğünü, Aspose.Cells'in ise normal sistem yapılandırmalarına sahip ortak bir donanımda 1 saniyeden daha kısa sürdüğünü gösterdi.

Döngü uzatılırsa, örneğin 10.000*20 hücreyi doldurmak için Aspose.Cells'in işi yapması yaklaşık 5,5 saniye sürer.

## **Çözüm**

Bir iş çözümünde Microsoft Office teknolojisini kullanmayı düşünüyorsanız, öncelikle mevcut alternatifleri öğrenin. Farklı ürünlere dayalı bazı testler yapın ve ne kadar iyi performans gösterdiklerini görmek için bunları yük ve stres gibi çeşitli gerçek dünya koşullarına maruz bırakın.

Aspose.Cells, dünya çapında müşteri tabanına sahip istikrarlı ve olgun bir üründür ve ağır yükler altında iyi performans gösterecek kadar ölçeklenebilir.

VSTO'nun performansı henüz rafine edilmedi. Bu performans sorunlarından bazılarının VSTO'nun kendisiyle ilgili olmaması, bunun yerine .NET JIT derleme işlemleriyle bağlantılı olması oldukça olasıdır. Ancak yine de, yük arttıkça VSTO uygulamalarının kendilerinin ölçeklenip ölçeklenmeyeceği konusunda bazı şüpheler var. VSTO'nun daha yeni modeli, belge işleme için Excel'in web sunucusunda bulunmasını gerektirmez, ancak VSTO'nun gerçek bir etki yaratmak için kat etmesi gereken uzun bir yol olduğunu düşünüyorum.
