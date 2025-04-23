---
title: Çalışsayfalar Arasında Şekiller Kopyalama
type: docs
weight: 250
url: /tr/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Bazen, farklı resimleri, grafikleri ve diğer çizim nesnelerini gereksiniminize göre farklı çalışma sayfalarına kopyalamanız gerekebilir. Aspose.Cells, çalışma sayfaları arasında şekil kopyalamayı destekler. Grafikler, resimler ve diğer nesneler en yüksek hassasiyetle kopyalanır.

Ofis Otomasyonunu deneyebilirsiniz ancak bunun kendi dezavantajları vardır. Güvenlik, istikrar, ölçeklenebilirlik, hız, fiyat ve özellikler gibi birçok neden ve sorun bulunmaktadır. Kısacası, Microsoft kendisi, ofis otomasyonuna karşı yazılım çözümlerinden şiddetle kaçınmanızı önerir.

Bu makalede, Aspose.Cells kullanarak bir çalışma kitabının çalışma sayfaları arasında resimler, grafikler ve diğer çizim nesnelerinin kopyalanmasını yapmak için birkaç ve en basit kod satırı kullanarak bir konsol uygulaması oluşturuyoruz.

Bu belge, geliştiricilere, çalışma sayfaları arasında şekillerin (resimler, grafikler, denetimler ve diğer çizim nesneleri) nasıl kopyalanacağı hakkında detaylı bir anlayış sağlamak için tasarlanmıştır.

{{% /alert %}}

## **Şekillerin Kopyalanması**

Bu makalede şunları açıklar:

- [Bir çalışma sayfasından diğerine bir resmi kopyalama](/cells/tr/java/copy-shapes-between-worksheets/#bir-çalışma-sayfasından-diğerine-bir-resmin-kopyalanması).
- [Bir çalışma sayfasından diğerine bir grafik kopyalama](/cells/tr/java/copy-shapes-between-worksheets/#görev-2-bir-çalışma-sayfasından-diğerine-bir-grafik-kopyalanması).
- [Bir çalışma sayfasından diğerine denetimler ve diğer çizim nesnelerini kopyalama](/cells/tr/java/copy-shapes-between-worksheets/#görev-3-denetimler-ve-diğer-çizim-nesnelerini-bir-çalışma-sayfasından-diğerine-kopyalama).

### **Bir Resmi Bir Çalışsayfasından Başka Birine Kopyalama**

#### **Adım 1: Resim ve Grafik ile Microsoft Excel'de bir çalışma kitabı oluşturma**

1. Microsoft Excel'de yeni bir çalışma kitabı oluşturuldu.
1. Birinci çalışma sayfasına bir resim ve ikinci çalışma sayfasına bir grafik eklendi.

   Aşağıdaki ekran görüntüleri, Microsoft Excel'de oluşturulan iki şablon çalışma sayfasını göstermektedir.

   **Grafik** adlı çalışma sayfası ile

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**Resim** adlı çalışma sayfası ile

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

Şimdi, “Resim” adlı çalışma sayfasındaki resmi son çalışma sayfası olan “Sonuç”a kopyalayın.

#### **Adım 2: Aspose.Cells.Zip'i İndirme**

1. [Aspose.Cells for Java'yi indirin](https://downloads.aspose.com/cells/java).
1. Geliştirme bilgisayarınızda zip dosyasını açın.

   Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun bir zaman limiti yoktur ve yalnızca üretilen belgelere filigran enjekte eder.

#### **Adım 3: Bir Proje Oluşturma**

Bir Java düzenleyici kullanarak bir proje oluşturabilirsiniz, örneğin Eclipse veya bir Not Defteri kullanarak basit bir program oluşturabilirsiniz.

#### **Adım 4: Sınıf Yolu Eklemek**

Eclipse'te Class Path ayarlamak için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.jar ve dom4j_1.6.1.jar dosyalarını Aspose.Cells.zip'ten çıkartın.
1. Eclipse'te proje classpath'ini ayarlayın:
1. Eclipse'te projeyi seçin ve ardından menülerden Proje-Özellikler'e tıklayın.
1. Açılan pencerenin sol tarafında "Java Build Path"'i seçin, ardından "Libraries" sekmesini seçin, "Add JARs" veya "Add External JARs"'ı tıklayarak Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçin ve build yoluna ekleyin.
1. Aspose'un bileşenlerinin API'lerini çağırmak için uygulama yazın.

Veya Windows'ta DOS komut isteminde çalışma zamanında ayarlayabilirsiniz. Örneğin:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **Adım 5: Bir çalışma sayfasından diğerine resim kopyalama**

Aşağıdaki kod, görevi başarmak için kullanılır. Bu, "Picture" adlı çalışma sayfasından resmi çalışma sayfasına "Sonuç" kopyalar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Sonuç Görev 1:**

Yukarıdaki kodu çalıştırdıktan sonra, resim "Picture" çalışma sayfasından artık en son çalışma sayfasına "Sonuç" kopyalanmıştır.

**Kopyalanan resimli "Sonuç" çalışma sayfası**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **Görev 2: Bir çalışma sayfasından diğerine grafik kopyalama**

#### **Adım 1: Bir çalışma sayfasından diğerine bir grafik kopyalayın**

Aşağıdaki kod, görevi başarmak için kullanılır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Sonuç Görev 2**

Yukarıdaki kodu çalıştırdıktan sonra, "Chart" çalışma sayfasından grafik "Sonuç" çalışma sayfasına kopyalanmıştır. Lütfen oluşan çalışma sayfasının aşağıdaki ekran görüntüsüne bakın.

**Kopyalanan resimli ve grafikli "Sonuç" çalışma sayfası**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **Görev 3: Bir çalışma sayfasından diğerine denetimler ve diğer çizim nesnelerini kopyalama**

**Metin kutusu ve oval bulunan "Control" çalışma sayfası**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

İstenen sonuçları elde etmek için yapmanız gereken basit adımları aşağıda bulabilirsiniz.

#### **Adım 1: Çalışma kitapları arasında bir çalışma sayfası kopyalama**

Görevi başarmak için bileşen tarafından kullanılan kod aşağıdaki gibidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Sonuç Görev 3**

Yukarıdaki kodu çalıştırdıktan sonra, "Control" çalışma sayfasındaki kontroller artık "Sonuç" çalışma sayfasına kopyalanmıştır. Lütfen "Sonuç" çalışma sayfasının aşağıdaki ekran görüntüsüne bakın.

**Kopyalanan metin kutusu ve oval olan "Sonuç" çalışma sayfası**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **Sonuç**

Bu makale, Aspose.Cells kullanarak resimler, grafikler ve diğer çizim nesneleri gibi farklı şekillerin kopyalanacağını göstermiştir. Umarım size bir bakış açısı kazandırır ve farklı senaryolarınıza göre bu seçenekleri kullanabilirsiniz.

Aspose.Cells, özel iş uygulama gereksinimlerini karşılamak için olağanüstü hız, verimlilik ve güvenilirlik sunar. Sonuçlar, Aspose.Cells'ın yıllar süren araştırma, tasarım ve dikkatli ayarlardan yararlandığını göstermektedir.

Sorularınızı, yorumlarınızı ve önerilerinizi [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9)'da bekliyoruz.
{{< app/cells/assistant language="java" >}}
