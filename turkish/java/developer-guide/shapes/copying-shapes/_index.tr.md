---
title: Çalışma Sayfaları Arasında Şekilleri Kopyalama
type: docs
weight: 250
url: /tr/java/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

Bazen, ihtiyacınıza göre farklı resimleri, çizelgeleri ve diğer çizim nesnelerini farklı çalışma sayfalarına kopyalamanız gerekir. Aspose.Cells, çalışma sayfaları arasında şekillerin kopyalanmasını destekler. Grafikler, resimler ve diğer nesneler en yüksek hassasiyetle kopyalanır.

Office Otomasyonu'nu deneyebilirsiniz, ancak bunun kendi dezavantajları vardır. İlgili birkaç neden ve sorun vardır: örneğin güvenlik, kararlılık, ölçeklenebilirlik, hız, fiyat ve özellikler. Kısacası, pek çok neden var ve bunlardan en önemlisi Microsoft'in yazılım çözümlerinden Office otomasyonuna karşı şiddetle tavsiye etmesi.

Bu yazımızda Aspose.Cells kullanarak birkaç ve en basit kod satırı ile bir konsol uygulaması oluşturuyoruz, bir çalışma kitabının çalışma sayfaları arasında resim, çizelge ve diğer çizim nesnelerinin kopyalanmasını gerçekleştiriyoruz.

Bu belge, geliştiricilere şekillerin (resimler, grafikler, kontroller ve diğer çizim nesneleri) çalışma sayfaları arasında nasıl kopyalanacağı konusunda ayrıntılı bir anlayış sağlamak için tasarlanmıştır.

{{% /alert %}}

## **Şekilleri Kopyalama**

Bu makalede, aşağıdakilerin nasıl yapılacağı açıklanmaktadır:

- [Resmi bir çalışma sayfasından diğerine kopyalama](/cells/tr/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Grafiği bir çalışma sayfasından diğerine kopyalama](/cells/tr/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Denetimleri ve diğer çizim nesnelerini bir çalışma sayfasından diğerine kopyalama](/cells/tr/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Bir Çalışma Sayfasından Bir Resmi Diğerine Kopyalama**

#### **1. Adım: Microsoft Excel'de resim ve grafik içeren bir çalışma kitabı oluşturma**

1. Microsoft Excel'de yeni bir çalışma kitabı oluşturuldu.
1. İlk çalışma sayfasına bir resim ve ikinci çalışma sayfasına bir grafik ekleyin.

 Aşağıdaki ekran görüntüleri, Microsoft Excel'de oluşturulan iki şablon çalışma sayfasını göstermektedir.

   **Grafik içeren çalışma sayfası “Grafik”**

![yapılacaklar:resim_alternatif_metin](copy-shapes-between-worksheets_1.png)

**Resimli “Resim” çalışma sayfası**

![yapılacaklar:resim_alternatif_metin](copy-shapes-between-worksheets_2.png)

Şimdi, “Resim” adlı çalışma sayfasındaki resmi, son çalışma sayfası olan “Sonuç” a kopyalayın.

#### **2. Adım: Aspose.Cells.Zip dosyasını indirin**

1. [İndir Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Geliştirme bilgisayarınızda açın.

 Herşey[Aspose](http://www.aspose.com/) bileşenler kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.

#### **3. Adım: Bir Proje Oluşturun**

Eclipse gibi bir Java düzenleyici kullanarak bir proje oluşturabilir veya bir NotePad kullanarak basit bir program oluşturabilirsiniz.

#### **4. Adım: Sınıf Yolu Ekleyin**

Eclipse kullanarak bir Sınıf Yolu ayarlamak için lütfen aşağıdaki adımları gerçekleştirin:

1. Aspose.Cells.jar ve dom4j_1.6.1.jar'ı Aspose.Cells.zip'ten çıkarın.
1. Eclipse'de projenin sınıf yolunu ayarlayın:
1. Eclipse'de projenizi seçin ve ardından Proje-Özellikler menülerine tıklayın.
1. Açılır pencerenin sol tarafındaki "Java Derleme Yolu"nu seçin, ardından "Kütüphaneler" sekmesini seçin, "JAR'ları Ekle" veya "Harici JAR'ları Ekle"ye tıklayarak Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçin ve bunları derlemeye ekleyin yollar.
1. Aspose'in bileşenlerinin API'lerini çağırmak için uygulama yazın.

Veya Windows'deki DOS isteminde çalışma zamanında ayarlayabilirsiniz. Örneğin:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; Sınıf adı

#### **Adım 5: Bir resmi bir çalışma sayfasından diğerine kopyalama**

Görevi gerçekleştirmek için kod aşağıdadır. “Resim” adlı çalışma sayfasındaki bir resmi “Sonuç” çalışma sayfasına kopyalar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Sonuç Görev 1:**

Yukarıdaki kodu çalıştırdıktan sonra, “Resim” çalışma sayfasındaki resim artık son çalışma sayfası olan “Sonuç”a kopyalanmıştır.

**Kopyalanan resim ile çalışma sayfası “Sonuç”**

![yapılacaklar:resim_alternatif_metin](copy-shapes-between-worksheets_3.png)

### **Görev 2: Grafiği Bir Çalışma Sayfasından Diğerine Kopyalama**

#### **1. Adım: Grafiği bir çalışma sayfasından diğerine kopyalama**

Görevi gerçekleştirmek için bileşen tarafından kullanılan gerçek kod aşağıdadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Sonuç Görev 2**

Yukarıdaki kodu çalıştırdıktan sonra, "Grafik" çalışma sayfasındaki grafik "Sonuç" çalışma sayfasına kopyalanır. Lütfen ortaya çıkan çalışma sayfasının aşağıdaki anlık görüntüsüne bakın.

**Kopyalanan resim ve çizelge ile “Sonuç” çalışma sayfası**

![yapılacaklar:resim_alternatif_metin](copy-shapes-between-worksheets_4.png)

### **Görev 3: Kontrolleri ve Diğer Çizim Nesnelerini Bir Çalışma Sayfasından Diğerine Kopyalama**

**Metin kutusu ve oval içeren çalışma sayfası “Kontrol”**

![yapılacaklar:resim_alternatif_metin](copy-shapes-between-worksheets_5.png)

Lütfen istediğiniz sonuçları elde etmek için gerçekleştirmeniz gereken aşağıdaki basit adımlara bakın.

#### **1. Adım: Bir çalışma sayfasını çalışma kitapları arasında kopyalama**

Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıdadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Sonuç Görev 3**

Yukarıdaki kodu çalıştırdıktan sonra, "Kontrol" çalışma sayfasındaki kontroller şimdi "Sonuç" çalışma sayfasına kopyalanır. Lütfen aşağıdaki "Sonuç" anlık görüntüsüne bakın.

**Kopyalanan metin kutusu ve oval ile çalışma sayfası "Sonuç"**

![yapılacaklar:resim_alternatif_metin](copy-shapes-between-worksheets_6.png)

## **Çözüm**

Bu makale, Aspose.Cells'i kullanarak resimler, çizelgeler ve diğer çizim nesneleri gibi farklı şekillerin nasıl kopyalanacağını göstermiştir. Umarız size biraz fikir verir ve bu seçenekleri farklı senaryolarınıza göre kullanabilirsiniz.

Aspose.Cells, çözümler için diğerlerinden daha fazla esneklik sunabilir ve belirli iş uygulaması gereksinimlerini karşılamak için olağanüstü hız, verimlilik ve güvenilirlik sağlar. Sonuçlar, Aspose.Cells'in yıllarca süren araştırma, tasarım ve dikkatli ayarlamadan yararlandığını gösteriyor.

 Soru, görüş ve önerilerinizi içtenlikle karşılıyoruz.[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9).
