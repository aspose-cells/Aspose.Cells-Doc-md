---
title: Çalışma Sayfalarını Çalışma Kitapları İçinde ve Çalışma Kitapları Arasında Kopyalama ve Taşıma
type: docs
weight: 20
url: /tr/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişi içeren bir dizi çalışma sayfasına ihtiyacınız olur. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalardan oluşan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu var: bir sayfa oluşturup ardından onu üç kez kopyalayarak.

Aspose.Cells, çalışma kitaplarının içinde veya arasında çalışma sayfalarının kopyalanmasını veya taşınmasını destekler. Veriler, biçimlendirme, tablolar, matrisler, çizelgeler, resimler ve diğer nesneleri içeren çalışma sayfaları en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

Bu makalede, Aspose.Cells'in aşağıdaki amaçlarla nasıl kullanılacağı açıklanmaktadır:

- [Çalışma kitabı içindeki çalışma sayfasını kopyalama](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Çalışma sayfasını çalışma kitabı içinde taşıma](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Çalışma kitapları arasında çalışma sayfası kopyalama](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Bir çalışma sayfasını çalışma kitapları arasında taşıma](/cells/tr/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Çalışma Kitabındaki Çalışma Sayfasını Kopyalama**

İlk adımlar tüm örnekler için aynıdır.

1. Microsoft Excel'de bazı verilerle iki çalışma kitabı oluşturun. Bu örneğin amaçları doğrultusunda, Microsoft Excel'de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik.

- FirstWorkbook.xls (3 çalışma sayfası)
- SecondWorkbook.xls (1 çalışma sayfası).

  **FirstWorkbook.xls**

![yapılacaklar:resim_alternatif_Metin](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![yapılacaklar:resim_alternatif_Metin](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Aspose.Cells'i indirin ve yükleyin:
   1. [İndir Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Geliştirme bilgisayarınızda sıkıştırılmış dosyayı açın.
 Herşey[Aspose](http://www.aspose.com/) bileşenler kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.
1. Bir proje oluşturun:
 1. Eclipse gibi bir Java düzenleyici kullanarak bir proje oluşturun veya bir metin düzenleyici kullanarak basit bir program oluşturun.
1. Bir sınıf yolu ekleyin:
1. Aspose.Cells.jar ve dom4j_1.6.1.jar'ı Aspose.Cells.zip'ten çıkarın.
 1. Eclipse'de projenin sınıf yolunu ayarlayın:
 1. Eclipse'de projenizi seçin ve menülere tıklayın**proje** , sonra**Özellikleri**.
 1. Seçin**Java Derleme Yolu** iletişim kutusunun sol tarafında, ardından Kitaplıklar sekmesini seçin,
 1. tıklayın**JAR ekle** veya**Harici JAR'lar Ekle** Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçip derleme yollarına eklemek için.

{{% alert color="primary" %}}

Veya sınıf yolunu çalışma zamanında Windows'de bir DOS isteminde ayarlayabilirsiniz.
Örneğin:

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Çalışma sayfasını bir çalışma kitabı içinde kopyalama:
 Görevi gerçekleştirmek için tarafından kullanılan kod aşağıdadır. FirstWorkbook.xls içindeki Copy çalışma sayfasını kopyalar.

Kodun çalıştırılması, FirstWorkbook.xls içindeki Copy adlı çalışma sayfasını Last Sheet yeni adıyla taşır.

**Çıktı dosyası**

![yapılacaklar:resim_alternatif_Metin](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Çalışma Kitabında Çalışma Sayfasını Taşıma**

Görevi gerçekleştirmek için kullanılan kod aşağıdadır.

Kodun yürütülmesi, çalışma sayfasını FirstWorkbook.xls'de dizin 1'den dizin 2'ye taşır.

**Çıktı dosyası**

![yapılacaklar:resim_alternatif_Metin](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Çalışma Kitapları Arasında Çalışma Sayfası Kopyalama**

Kodun çalıştırılması, Copy to SecondWorkbook.xls çalışma sayfasını Sheet2 yeni adıyla kopyalar.

**Çıktı dosyası**

![yapılacaklar:resim_alternatif_Metin](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Çalışma Sayfasını Çalışma Kitapları Arasında Taşıma**

Kodun çalıştırılması, taşıma çalışma sayfasını FirstWorkbook.xls'den Sheet3 yeni adıyla SecondWorkbook.xls'ye taşır.

**Çıktı FirstWorkbook.xls**

![yapılacaklar:resim_alternatif_Metin](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**SecondWorkbook.xls çıktısı**

![yapılacaklar:resim_alternatif_Metin](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Çözüm**

{{% alert color="primary" %}}

Bu makalede, Aspose.Cells kullanılarak çalışma sayfalarının çalışma kitaplarının içinde ve arasında nasıl kopyalanacağı ve taşınacağı açıklanmaktadır.

 Aspose.Cells, yıllarca süren araştırma, tasarım ve dikkatli ayarlamadan yararlanmıştır. Soru, görüş ve önerilerinizi şu adrese bekliyoruz:[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Hızlı yanıt garantisi veriyoruz.

{{% /alert %}}
