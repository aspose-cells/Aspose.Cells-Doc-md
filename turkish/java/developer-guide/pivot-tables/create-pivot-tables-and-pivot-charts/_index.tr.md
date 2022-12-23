---
title: Pivot Tablolar ve Pivot Grafikler Oluşturun
type: docs
weight: 10
url: /tr/java/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Java API ile Pivot Tablolar ve Pivot Grafikler oluşturun.
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

Pivot tablo, kayıtların etkileşimli bir özetidir. Örneğin, bir çalışma sayfasındaki bir listede yüzlerce fatura girişiniz olabilir. Bir pivot tablo, faturaları müşteriye, ürüne veya tarihe göre toplayabilir. Microsoft Excel ile, düğmeleri yeni bir konuma sürükleyerek pivot tablodaki bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.

Pivot grafik, pivot tablodaki verilerin etkileşimli bir grafik temsilidir. Pivot grafikler Excel 2000'de kullanılmaya başlandı. Pivot tablo otomatik olarak ara toplamlar ve toplamlar oluşturduğundan, pivot grafik kullanmak verilerin anlaşılmasını daha da kolaylaştırır.

 Aspose.Cells destekler[pivot tablolar](/cells/tr/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) ve[pivot grafikler](/cells/tr/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Pivot Tablolar ve Grafikler Ekleme**

Aspose.Cells, pivot tablolar oluşturmak için kullanılan özel bir sınıf seti sağlar. Bu sınıflar, PivotTable nesnesinin temel yapı taşları olarak hareket eden PivotTable nesneleri oluşturmak ve ayarlamak için kullanılır:

- PivotField, pivot tablo raporundaki bir alan.
- PivotFields, bir pivot tablodaki tüm PivotField nesnelerinin bir koleksiyonu.
- PivotTable, bir çalışma sayfasındaki PivotTable raporu.
- PivotTable'lar, çalışma sayfasındaki tüm PivotTable nesnelerinin bir koleksiyonudur.

### **Kullanıma hazırlanıyor Aspose.Cells**

1. Aspose.Cells.Zip dosyasını indirip yükleyin:
   1. [İndir Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Geliştirme bilgisayarınızda sıkıştırılmış dosyayı açın.
 Herşey[Aspose](http://www.aspose.com/) bileşenler kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.
1. proje oluştur
 1. Eclipse gibi bir Java Editor kullanarak bir proje oluşturabilir veya bir NotePad kullanarak basit bir program oluşturabilirsiniz.
1. Sınıf yolu ekle:
 Eclipse kullanarak bir sınıf yolu ayarlamak için:
1. Aspose.Cells.jar ve dom4j_1.6.1.jar'ı Aspose.Cells.zip'ten çıkarın.
 1. Eclipse'de projenin sınıf yolunu ayarlayın:
1. Eclipse'de projenizi seçin ve ardından Proje-Özellikler menülerine tıklayın.
 1. Açılır pencerenin sol tarafında "Java Derleme Yolu"nu seçin, ardından "Kütüphaneler" sekmesini seçin, "JAR'ları Ekle" veya "Harici JAR'ları Ekle"ye tıklayarak Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçin ve ekleyin oluşturma yollarına girin.
 1. Aspose'in bileşenlerinin API'lerini çağırmak için uygulama yazın.
 Veya Windows'deki dos isteminde çalışma zamanında ayarlayabilirsiniz.

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Pivot Tablo Oluşturma**

Aspose.Cells'i kullanarak bir pivot tablo oluşturmak için:

1. Cell nesnesinin PutValue/setValue yöntemini kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin. Ayrıca önceden verilerle doldurulmuş bir şablon dosyası da kullanırsınız. Veriler, pivot tablonun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun ekleme yöntemini (Çalışma Sayfası nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir özet tablo ekleyin.
1. Dizinini geçirerek PivotTables koleksiyonundan yeni PivotTable nesnesine erişin.
1. Tabloyu yönetmek için PivotTable nesnesinde kapsüllenmiş pivot tablo nesnelerinden herhangi birini kullanın.

Aşağıda bir kod örneği verilmiştir. Kodun çalıştırılması yeni bir dosya oluşturur: pivotTable_test.xls.

**Giriş verileri** 

![yapılacaklar:resim_alternatif_metin](create-pivot-tables-and-pivot-charts_1.png)

**çıkış pivot tablosu**

![yapılacaklar:resim_alternatif_metin](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Pivot Tabloya Dayalı Pivot Grafik Oluşturma**

Aspose.Cells'i kullanarak bir pivot grafik oluşturmak için:

1. Grafik ekleyin.
1. Grafiğin PivotSource'unu e-tablodaki mevcut bir pivot tabloya atıfta bulunacak şekilde ayarlayın.
1. Diğer nitelikleri ayarlayın.

Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıdadır. Kodun çalıştırılması yeni bir dosya oluşturur: pivotChart_test.xls.

**Pivot grafik sayfası**

![yapılacaklar:resim_alternatif_metin](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Bu makale, Aspose.Cells'i kullanarak pivot tabloların ve pivot grafiklerin nasıl oluşturulacağını gösterir. Umarız bu özellikleri kendi senaryolarınızda kullanmanıza yardımcı olur.

Aspose.Cells, yıllarca süren araştırma, tasarım ve dikkatli ayarlamadan yararlanmıştır.

 Soru, görüş ve önerilerinizi şu adrese bekliyoruz:[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Hızlı yanıt garantisi veriyoruz.

{{% /alert %}}

## İlgili Makaleler

- [Özet Tabloda özel sıralama](/cells/tr/java/custom-sorting-in-pivot-table/)
- [Pivot Tabloyu Biçimlendirme](/cells/tr/java/formatting-pivot-table/)
- [Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın](/cells/tr/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Pivot Tablo Şeritlerini Devre Dışı Bırak](/cells/tr/java/disable-pivot-table-ribbons/)

