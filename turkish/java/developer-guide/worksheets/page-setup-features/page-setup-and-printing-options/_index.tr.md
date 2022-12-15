---
title: Sayfa Yapısı ve Yazdırma Seçenekleri
type: docs
weight: 10
url: /tr/java/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

Bazen, geliştiricilerin yazdırma sürecini kontrol etmek için sayfa düzenini ve yazdırma ayarlarını yapılandırması gerekir. Sayfa yapısı ve yazdırma ayarları, çeşitli seçenekler sunar ve Aspose.Cells'de tamamen desteklenir.

Bu makale, Aspose.Cells API kullanarak birkaç basit kod satırıyla bir konsol uygulamasının nasıl oluşturulacağını ve sayfa düzeni ve yazdırma seçeneklerinin bir çalışma sayfasına nasıl uygulanacağını gösterir.

{{% /alert %}}

## **Sayfa ve Yazdırma Ayarları ile Çalışma**

Bu örnek için, Microsoft Excel'de bir çalışma kitabı oluşturduk ve sayfa düzenini ve yazdırma seçeneklerini ayarlamak için Aspose.Cells'i kullandık.

### **Sayfa Yapısı Seçeneklerini Ayarlama**

Önce Microsoft Excel'de basit bir çalışma sayfası oluşturun. Ardından ona sayfa yapısı seçeneklerini uygulayın. Kodu çalıştırmak, aşağıdaki ekran görüntüsündeki gibi Sayfa Düzeni seçeneklerini değiştirir.

**Çıktı dosyası** 

![yapılacaklar:resim_alternatif_Metin](page-setup-and-printing-options_1.png)

1. Microsoft Excel'de bazı verilerle bir çalışma sayfası oluşturun:
 1. Microsoft Excel'de yeni bir çalışma kitabı açın.
 1. Biraz veri ekleyin.
 Aşağıda dosyanın bir ekran görüntüsü var.

      **Giriş dosyası**

![yapılacaklar:resim_alternatif_Metin](page-setup-and-printing-options_2.png)

1. Sayfa kurulum seçeneklerini ayarlayın:
 Dosyaya sayfa yapısı seçeneklerini uygulayın. Yeni seçenekler uygulanmadan önce, varsayılan seçeneklerin ekran görüntüsü aşağıdadır.

   **Varsayılan sayfa kurulum seçenekleri**

![yapılacaklar:resim_alternatif_Metin](page-setup-and-printing-options_3.png)

1. Aspose.Cells'i indirin ve yükleyin:
   1. [İndirmek](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Geliştirme bilgisayarınızda sıkıştırılmış dosyayı açın.
 Herşey[Aspose](http://www.aspose.com/) bileşenler kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.
1. Bir proje oluşturun.
 Eclipse gibi bir Java düzenleyici kullanarak bir proje oluşturun veya bir metin düzenleyici kullanarak basit bir program oluşturun.
1. Bir sınıf yolu ekleyin.
1. Aspose.Cells.jar ve dom4j_1.6.1.jar'ı Aspose.Cells.zip'ten çıkarın.
 1. Eclipse'de projenin sınıf yolunu ayarlayın:
 1. Eclipse'de projenizi seçin ve ardından tıklayın**proje** bunu takiben**Özellikleri**.
 1. Seçin**Java Derleme Yolu**iletişim kutusunun solunda.
 1. Kitaplıklar sekmesini seçin, tıklayın**JAR ekle** veya**Harici JAR'lar Ekle** Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçip derleme yollarına eklemek için.
 Veya çalışma zamanında Windows'de bir DOS komut isteminde ayarlayabilirsiniz:

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. API'leri çağıran uygulamayı yazın:
 Bu örnekte bileşen tarafından kullanılan kod aşağıdadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Yazdırma seçeneklerini ayarlama**

Sayfa yapısı ayarları ayrıca, kullanıcıların çalışma sayfası sayfalarının nasıl yazdırılacağını denetlemesine olanak tanıyan çeşitli yazdırma seçenekleri (sayfa seçenekleri olarak da adlandırılır) sağlar. Kullanıcıların şunları yapmasına izin verir:

- Bir çalışma sayfasının belirli bir yazdırma alanını seçin.
- Başlıkları yazdırın.
- Kılavuz çizgilerini yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Yazdırma hücresi hataları.
- Sayfa sıralamasını tanımlayın.

Aşağıdaki örnek, yukarıdaki örnekte oluşturulan dosyaya (PageSetup.xls) yazdırma seçeneklerini uygular. Aşağıdaki ekran görüntüsü, yeni seçenekler uygulanmadan önceki varsayılan yazdırma seçeneklerini gösterir.
**Giriş belgesi**

![yapılacaklar:resim_alternatif_Metin](page-setup-and-printing-options_4.png)

Kodun çalıştırılması yazdırma seçeneklerini değiştirir.
**Çıktı dosyası**

![yapılacaklar:resim_alternatif_Metin](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Özet**

{{% alert color="primary" %}}

Bu makale, Aspose.Cells'i kullanarak sayfa düzeni ve sayfa yazdırma seçeneklerinin nasıl ayarlanacağını gösterir. Umarız size biraz bilgi verir ve bu seçenekleri kendi senaryolarınızda kullanabilirsiniz.

 Aspose.Cells, yıllarca süren araştırma, tasarım ve dikkatli ayarlamadan yararlanır. Soru, görüş ve önerilerinizi memnuniyetle karşılıyoruz.[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Hızlı yanıt garantisi veriyoruz.

{{% /alert %}}
