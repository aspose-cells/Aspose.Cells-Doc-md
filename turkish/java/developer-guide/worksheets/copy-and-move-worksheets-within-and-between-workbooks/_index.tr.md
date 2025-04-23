---
title: Çalışma Kitapları Arasında ve İçinde Çalışma Sayfalarını Kopyalayın ve Taşıyın
type: docs
weight: 20
url: /tr/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişi gerektiren sayısız çalışma sayfasına ihtiyacınız olabilir. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfaları olan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu vardır: bir sayfa oluşturarak ve ardından bunu üç kez kopyalayarak.

Aspose.Cells, çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama veya taşımayı destekler. Veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerin yanı sıra sayfalar en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

Bu makale, Aspose.Cells'ı kullanarak şunları nasıl yapılacağını açıklar:

- [Çalışma kitabı içinde bir çalışma sayfasını kopyalama](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Çalışma kitabı içinde bir çalışma sayfasını taşıma](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Çalışma kitapları arasında bir çalışma sayfasını kopyalama](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Çalışma kitapları arasında bir çalışma sayfasını taşıma](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Bir Çalışma Sayfasını Bir Çalışma Kitabı İçinde Kopyalama**

Tüm örnekler için ilk adımlar aynıdır.

1. Microsoft Excel'de bazı veriler içeren iki çalış kitabı oluşturun. Bu örneğin amaçları için, Microsoft Excel'de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik.

- FirstWorkbook.xls (3 çalışma sayfası)
- SecondWorkbook.xls (1 çalışma sayfası)

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells for Java'yi indirin](https://downloads.aspose.com/cells/java).
   1. Geliştirme bilgisayarınızda zip dosyasını açın.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun bir zaman limiti yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun:
   1. Eclipse gibi bir Java düzenleyici kullanarak bir proje oluşturun veya metin düzenleyici kullanarak basit bir program oluşturun.
1. Bir sınıf yolunu ekleyin:
   1. Aspose.Cells.jar ve dom4j_1.6.1.jar dosyalarını Aspose.Cells.zip'ten çıkartın.
   1. Eclipse'te proje classpath'ini ayarlayın:
      Eclipse'de projenizi seçin ve ardından **Proje**, sonra **Özellikler** düğmelerine tıklayın.
      Açılan iletişim kutusunun sol tarafında **Java Yapı Yolu**'nu seçin, ardından Kütüphaneler sekmesini seçin.
      **JAR Ekle** veya **Harici JAR'ları Ekle**'ye tıklayarak Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçin ve yapı yollarına ekleyin.

{{% alert color="primary" %}}

Veya Windows'ta bir DOS komut isteminden çalışma zamanında sınıf yolunu ayarlayabilirsiniz.
Örneğin:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Çalış kitabı içinde ki çalışma sayfasını kopyalayın:
   Aşağıda görevi tamamlamak için kullanılan kod. Bu, FirstWorkbook.xls içindeki Kopyala çalışma sayfasını kopyalar.

Kodun çalıştırılması, Kopyala olarak adlandırılan çalışma sayfasını FirstWorkbook.xls içinde yeni adı Son Sayfa ile taşır.

**Çıkış dosyası**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Çalışma Kitabı İçinde Bir Çalışma Sayfası Taşıma**

Aşağıdaki kod, görevi tamamlamak için kullanılan kod.

Kodun çalıştırılması, Move olarak adlandırılan çalışma sayfasını FirstWorkbook.xls içindeki 1. indexten 2. indexe taşır.

**Çıkış dosyası**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Kopylama**

Kodun çalıştırılması, Kopya olarak adlandırılan çalışma sayfasını SecondWorkbook.xls içine Sheet2 olarak kopyalar.

**Çıkış dosyası**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Taşıma**

Kodu çalıştırmak, FirstWorkbook.xls'den Sheet3 adıyla ikinci çalışma kitabı olan SecondWorkbook.xls'ye çalışma sayfasını taşır.

**FirstWorkbook.xls Çıktısı**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**SecondWorkbook.xls Çıktısı**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Sonuç**

{{% alert color="primary" %}}

Bu makale, Aspose.Cells kullanarak çalışma kitapları arasında ve içinde çalışma sayfalarını kopyalama ve taşıma işlemlerini açıklar.

Aspose.Cells yılların araştırmasından, tasarımından ve dikkatli ayarlama süreçlerinden yararlanmıştır. [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9) adresinden soru, yorum ve önerilerinizi bekliyoruz. Hızlı bir yanıt garantisi veriyoruz.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
