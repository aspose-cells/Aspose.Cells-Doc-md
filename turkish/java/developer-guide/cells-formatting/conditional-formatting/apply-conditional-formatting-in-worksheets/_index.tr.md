---
title: Çalışma Sayfalarında Koşullu Biçimlendirme Uygula
type: docs
weight: 40
url: /tr/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasındaki bir dizi hücreye koşullu biçimlendirmenin nasıl ekleneceğine ilişkin ayrıntılı bir anlayış sağlamak için tasarlanmıştır.

Koşullu biçimlendirme, Microsoft Excel'de bulunan ve bir hücre aralığına biçimler uygulamanıza ve bu biçimlendirmenin hücrenin değerine veya bir formülün değerine bağlı olarak değişmesini sağlayan gelişmiş bir özelliktir. Örneğin, bir hücrenin arka planı negatif bir değeri vurgulamak için kırmızı olabilir veya pozitif bir değer için metin rengi yeşil olabilir. Hücrenin değeri biçim koşulunu karşıladığında biçim uygulanır. Hücrenin değeri biçim koşulunu karşılamıyorsa, hücrenin varsayılan biçimlendirmesi kullanılır.

Microsoft Office Otomasyonu ile koşullu biçimlendirme uygulamak mümkündür, ancak bunun dezavantajları vardır. İlgili birkaç neden ve sorun vardır: örneğin, güvenlik, kararlılık, ölçeklenebilirlik ve hız. Başka bir çözüm bulmanın ana nedeni, Microsoft'in kendisinin yazılım çözümleri için Office Otomasyonu'nu şiddetle önermesidir.

Bu makale, bir konsol uygulamasının nasıl oluşturulacağını, Aspose.Cells API'i kullanarak en basit birkaç kod satırıyla hücrelere koşullu biçimlendirme eklemeyi gösterir.

{{% /alert %}}

## **Koşullu Biçimlendirme ile Çalışma**

Bu makale aşağıdaki görevlerde çalışır:

1. [Hücre değerine göre koşullu biçimlendirme uygulamak için Aspose.Cells'i kullanma](/cells/tr/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Bir formüle dayalı koşullu biçimlendirme uygulamak için Aspose.Cells'i kullanma](/cells/tr/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Görev 1: Cell Değerine Göre Koşullu Biçimlendirmeyi Uygulamak için Aspose.Cells'i Kullanma**

1. **Aspose.Cells.zip dosyasını indirin ve yükleyin**:
   1. [İndirmek](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Geliştirme bilgisayarınızda sıkıştırılmış dosyayı açın.
 Tüm Aspose bileşenleri kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.
1. **proje oluştur**.
 Eclipse gibi bir Java Düzenleyici kullanarak bir proje oluşturun veya bir metin düzenleyici kullanarak basit bir program oluşturun.
1. **Sınıf yolu ekle**.
 Eclipse kullanarak bir Sınıf Yolu ayarlamak için lütfen aşağıdaki adımları gerçekleştirin:
1. Aspose.Cells.jar ve dom4j_1.6.1.jar'ı Aspose.Cells.zip'ten çıkarın.
 1. Eclipse'de projenin sınıf yolunu ayarlayın:
 1. Eclipse'de projenizi seçin ve ardından**Özellikler** dan**Proje** Menü.
 1. İletişim kutusunun solundaki "Java Derleme Yolu"nu seçin.
 1. üzerinde**kütüphaneler** sekme, seç**JAR ekle** veya**Harici JAR'lar Ekle** Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçip derleme yollarına eklemek için.
 1. Aspose'in bileşenlerinin API'lerini çağırmak için uygulama yazın.
 Veya yolu çalışma zamanında Windows'de bir DOS komut isteminde ayarlayabilirsiniz.

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Hücre değerine göre koşullu biçimlendirme uygula**.
 Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıdadır. Bir hücreye koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki "A1" hücresine koşullu biçimlendirme uygulanır. A1'e uygulanan koşullu biçimlendirme, hücre değerine bağlıdır. A1'in hücre değeri 50 ile 100 arasındaysa, uygulanan koşullu biçimlendirme nedeniyle arka plan rengi kırmızıdır. Lütfen oluşturulan XLS dosyasının aşağıdaki ekran görüntülerine bakın.

**A1 değeri 50'den küçük olan Excel dosyası çıktısı**

![yapılacaklar:resim_alternatif_metin](apply-conditional-formatting-in-worksheets_1.png)

**50 ile 100 arasında A1 ile çıktı Excel dosyası**

![yapılacaklar:resim_alternatif_metin](apply-conditional-formatting-in-worksheets_2.png)

### **Görev 2: Bir Formüle Dayalı Koşullu Biçimlendirmeyi Uygulamak için Aspose.Cells'i Kullanma**

1. **Formüle bağlı olarak koşullu biçimlendirme uygula**.
 Görevi gerçekleştirmek için bileşen tarafından kullanılan asıl kod aşağıdadır. “B3” üzerinde koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki "B3" hücresine koşullu biçimlendirme uygulanır. Uygulanan koşullu biçimlendirme, “B3” değerini B1 ve B2'nin toplamı olarak hesaplayan formüle bağlıdır. Lütfen oluşturulan XLS dosyasının aşağıdaki ekran görüntülerine bakın.

**B3 değeri 100'den az olan Excel dosyası çıktısı**

![yapılacaklar:resim_alternatif_metin](apply-conditional-formatting-in-worksheets_3.png)

**B3 değeri 100'den büyük olan Excel dosyasının çıktısını alın**

![yapılacaklar:resim_alternatif_metin](apply-conditional-formatting-in-worksheets_4.png)

### **Çözüm**

{{% alert color="primary" %}}

Bu makale, Aspose.Cells API ile bir çalışma sayfasındaki hücrelere koşullu biçimlendirmenin nasıl uygulanacağını gösterir. Umarız, bu seçenekleri kendi senaryolarınızda kullanabilmeniz için size biraz bilgi verir.

Aspose.Cells, çözümler için büyük esneklik sunar ve belirli iş uygulaması gereksinimlerini karşılamak için olağanüstü hız, verimlilik ve güvenilirlik sağlar. Aspose.Cells, yıllarca süren araştırma, tasarım ve dikkatli ayarlamadan yararlanır.

 Soru, görüş ve önerilerinizi sayfamıza bekliyoruz.[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Hızlı bir cevap garanti ediyoruz.

{{% /alert %}}
