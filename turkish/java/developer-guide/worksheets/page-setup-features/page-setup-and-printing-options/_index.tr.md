---
title: Sayfa Düzeni ve Yazdırma Seçenekleri
type: docs
weight: 10
url: /tr/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler yazdırma sürecini kontrol etmek için sayfa düzeni ve yazdırma ayarlarını yapılandırmak isteyebilir. Sayfa düzeni ve yazdırma ayarları çeşitli seçenekler sunar ve Aspose.Cells tarafından tamamen desteklenir.

Bu makale, Aspose.Cells API'sini kullanarak birkaç basit kod satırı ile bir konsol uygulaması oluşturmayı ve çalışma sayfasına sayfa ayarı ve yazdırma seçeneklerini uygulamanın nasıl gösterdiğini gösterir.

{{% /alert %}}

## **Sayfa ve Yazdırma Ayarları İle Çalışma**

Bu örnekte, Microsoft Excel'de bir çalışma kitabı oluşturduk ve Aspose.Cells kullanarak sayfa düzeni ve yazdırma seçeneklerini ayarladık.

### **Sayfa Ayarı Seçeneklerini Ayarlama**

Öncelikle Microsoft Excel'de basit bir çalışma sayfası oluşturun. Sonra ona sayfa düzeni seçenekleri uygulayın. Kodu yürüttüğünüzde, aşağıdaki ekran görüntüsünde görülen gibi Sayfa Düzeni seçeneklerini değiştirir.

**Çıkış dosyası** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. Microsoft Excel'de bazı veriler içeren bir çalışma sayfası oluşturun:
   1. Microsoft Excel'de yeni bir çalışma kitabı açın.
   1. Bazı veriler ekleyin.
      Aşağıda dosyanın ekran görüntüsü bulunmaktadır.

      **Giriş dosyası**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. Sayfa düzeni seçeneklerini ayarlayın:
   Ayarları dosyaya uygulayın. Yeni ayarların uygulanmadan önceki varsayılan seçeneklerin ekran görüntüsü aşağıda verilmiştir.

   **Varsayılan sayfa ayarı seçenekleri**

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. Aspose.Cells'i indirin ve kurun:
   1. [İndir](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Geliştirme bilgisayarınızda zip dosyasını açın.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun bir zaman limiti yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun.
   Örneğin Eclipse gibi bir Java düzenleyici kullanarak bir proje oluşturun veya bir metin düzenleyici kullanarak basit bir program oluşturun.
1. Bir sınıf yolu ekleyin.
   1. Aspose.Cells.jar ve dom4j_1.6.1.jar dosyalarını Aspose.Cells.zip'ten çıkartın.
   1. Eclipse'te proje classpath'ini ayarlayın:
   Eclipse'te projenizi seçin ve ardından **Proje** ve ardından **Özellikler**'i tıklayın.
   1. Diyaloğun solundaki **Java Build Path**'i seçin.
   1. Kütüphaneler sekmesini seçin, **Add JARs** veya **Add External JARs**'ı tıklayarak Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçin ve build yollarına ekleyin.
      Ya da bunu Windows'ta bir DOS komut isteminden çalışma zamanında da ayarlayabilirsiniz:

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. API'leri çağıran uygulamayı yazın:
   Bu örnekte bileşen tarafından kullanılan kod aşağıdadır:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

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
**Giriş belgesi**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

Kodun çalıştırılması yazdırma seçeneklerini değiştirir.
**Çıkış dosyası**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Özet**

{{% alert color="primary" %}}

Bu makale, Aspose.Cells kullanarak sayfa kurulumu ve sayfa yazdırma seçeneklerini ayarlamanın nasıl yapıldığını göstermektedir. Umarım size bazı fikirler verir ve bu seçenekleri kendi senaryolarınızda kullanabilirsiniz.

Aspose.Cells, yılların araştırma, tasarım ve dikkatli ayarlama çalışmalarının bir sonucu olarak faydalanmaktadır. [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9) adresinden sorularınızı, yorumlarınızı ve önerilerinizi içtenlikle bekliyoruz. Hızlı bir yanıt garantisi vermekteyiz.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
