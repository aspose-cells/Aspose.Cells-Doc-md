---
title: Çalışma Kitaplarında Koşullu Biçimlendirme Uygulama
type: docs
weight: 40
url: /tr/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasındaki hücre aralığına koşullu biçimlendirme eklemenin detaylı bir anlayışını sağlamak amacıyla tasarlanmıştır.

Koşullu biçimlendirme, Microsoft Excel'de gelişmiş bir özelliktir ve bir hücrenin değerine veya bir formülün değerine bağlı olarak biçimlendirme uygulamanıza olanak tanır. Örneğin, bir hücrenin arka planı, negatif bir değeri vurgulamak için kırmızı olabilir veya pozitif bir değer için metin rengi yeşil olabilir. Hücrenin değeri biçim koşulunu karşıladığında, biçim uygulanır. Hücrenin değeri biçim koşulunu karşılamadığında, hücrenin varsayılan biçimlendirmesi kullanılır.

Microsoft Office Automation ile koşullu biçimlendirme uygulamak mümkündür ancak bunun dezavantajları vardır. Örneğin, güvenlik, istikrar, ölçeklenebilirlik ve hız gibi çeşitli nedenler ve sorunlar bulunmaktadır. Başka bir çözüm bulma ana nedeni, Microsoft'un kendisinin yazılım çözümleri için Office Automation'a kesinlikle karşı çıkmasıdır.

Bu makale, Aspose.Cells API kullanarak birkaç basit kod satırıyla hücrelere koşullu biçimlendirme eklemeyi göstermektedir.

{{% /alert %}}

## **Koşullu Biçimlendirme İle Çalışmak**

Bu makale aşağıdaki görevleri ele alır:

1. Hücre Değerine Bağlı Koşullu Biçimlendirme Uygulamak İçin Aspose.Cells Kullanma
1. Formül Temelli Koşullu Biçimlendirme Uygulamak İçin Aspose.Cells Kullanma

### **Görev 1: Hücre Değerine Bağlı Koşullu Biçimlendirme Uygulamak İçin Aspose.Cells Kullanma**

1. **Aspose.Cells.zip**'i indirin ve kurun:
   1. [İndir](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Geliştirme bilgisayarınızda zip dosyasını açın.
      Tüm Aspose bileşenleri, yüklendiklerinde değerlendirme modunda çalışır. Değerlendirme modunun süresi sınırlı değildir ve üretilen belgelere filigran enjekte eder.
1. **Bir proje oluşturun.**
   Eclipse gibi bir Java Düzenleyici kullanarak bir proje oluşturun veya bir metin düzenleyici kullanarak basit bir program oluşturun.
1. **Sınıf yolunu ekleyin.**
   Eclipse'te Class Path ayarlamak için lütfen aşağıdaki adımları izleyin:
   1. Aspose.Cells.jar ve dom4j_1.6.1.jar dosyalarını Aspose.Cells.zip'ten çıkartın.
   1. Eclipse'te proje classpath'ini ayarlayın:
      1. Eclipse'te projenizi seçin ve **Proje** menüsünden **Özellikler**'i seçin.
      1. Diyalog kutusunun sol tarafındaki "Java Build Path"'i seçin.
      1. **Kütüphaneler** sekmesinde, Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçmek için **JAR Dosyaları Ekle** veya **Harici JAR Dosyaları Ekle**'yi seçin ve onları derleme yollarına ekleyin.
   1. Aspose'un bileşenlerinin API'lerini çağırmak için uygulama yazın.
      Veya Windows'ta bir DOS komut isteminde çalışma zamanında yolu ayarlayabilirsiniz.

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Hücre değerine dayalı koşullu biçimlendirme uygula**.
   Aşağıda, bileşenin görevi yerine getirmek için kullandığı kod bulunmaktadır. Bir hücreye koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Yukarıdaki kod çalıştırıldığında, koşullu biçimlendirme çıktı dosyasının ilk çalışma sayfasındaki A1 hücresine uygulanır (çıkış.xls). A1'in hücre değerine bağlı olarak koşullu biçimlendirme uygulanır. A1'in hücre değeri 50 ile 100 arasında ise, koşullu biçimlendirme uygulandığı için arka plan rengi kırmızı olur. Oluşturulan XLS dosyasının aşağıdaki ekran görüntülerine bakınız.

**A1 değeri 50'den küçük olan çıkış Excel dosyası**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**A1'in 50 ile 100 arasında olduğu çıkış Excel dosyası**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **Görev 2: Koşullu biçimlendirme Uygulamak için Aspose.Cells Kullanımı**

1. **Formülüne bağlı olarak koşullu biçimlendirme uygula**.
   Aşağıda, görevi yerine getirmek için bileşenin kullandığı gerçek kod bulunmaktadır. “B3” üzerinde koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Yukarıdaki kod çalıştırıldığında, koşullu biçimlendirme çıktı dosyasının ilk çalışma sayfasındaki “B3” hücresine uygulanır (çıkış.xls). Uygulanan koşullu biçimlendirme, “B3” değerine bağlıdır ve “B3” değerini B1 ve B2'nin toplamı olarak hesaplayan formüle bağlıdır. Oluşturulan XLS dosyasının aşağıdaki ekran görüntülerine bakınız.

**B3 değeri 100'den küçük olan çıkış Excel dosyası**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**B3'ün 100'den büyük olduğu çıkış Excel dosyası**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **Sonuç**

{{% alert color="primary" %}}

Bu makale, Aspose.Cells API'si ile bir çalışma sayfasındaki hücrelere koşullu biçimlendirme uygulamanın nasıl yapıldığını göstermektedir. Umarım, kendi senaryolarınızda bu seçenekleri kullanabilirsiniz.

Aspose.Cells, belirli iş uygulama gereksinimlerini karşılamak için olağanüstü hız, verimlilik ve güvenilirlik sunar. Yılların araştırma, tasarım ve dikkatli ayarlamasından faydalanır.

Sorularınızı, yorumlarınızı ve önerilerinizi [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9) 'da bekliyoruz. Hızlı bir yanıt garantisi veriyoruz.

{{% /alert %}}
