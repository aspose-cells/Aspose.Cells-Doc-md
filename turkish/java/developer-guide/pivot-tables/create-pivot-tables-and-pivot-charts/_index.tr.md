---
title: Özet Tabloları ve Özet Grafikler Oluşturma
type: docs
weight: 10
url: /tr/java/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Java API ile Özet Tabloları ve Özet Grafikler Oluşturma.
keywords: excel özet tablo oluştur java, excel özet grafik oluştur java, excel özet tablo ve özet grafik oluştur java, excel özet tablo oluştur ve özet grafik java, excel özet grafik oluştur ve özet tablo java, excel özet tablo ve özet grafik oluştur java, java excel özet tablo ve özet grafik oluştur, java ile excel özet tablo ve özet grafik nasıl oluşturulur
---

{{% alert color="primary" %}}

Bir özet tablo, kayıtların etkileşimli bir özeti. Örneğin, bir çalışma sayfasındaki bir listede yüzlerce fatura girişiniz olabilir. Bir özet tablo, faturaları müşteri, ürün veya tarihe göre toplayabilir. Microsoft Excel ile özet tablonun düğmeleri sürüklenerek bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.

Bir özet grafik, bir özet tablonun verilerinin etkileşimli grafiksel bir temsilidir. Özet grafikler Excel 2000'de tanıtılmıştır. Özet grafik kullanmak, özet tablonun alt toplamlarını ve toplamlarını otomatik olarak oluşturduğu için verileri anlamak daha da kolaylaştırır.

Aspose.Cells, [özet tabloları](/cells/tr/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) ve [özet grafikleri](/cells/tr/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table) destekler.

{{% /alert %}}

## **Özet Tabloları ve Grafikler Eklemek**

Aspose.Cells, özet tabloları oluşturmak için kullanılan özel bir sınıf kümesi sağlar. Bu sınıflar, PivotTable nesnelerini oluşturmak ve ayarlamak için kullanılır ve temel PivotTable nesnesinin yapı taşları olarak hareket ederler:

- PivotField, bir özet tablo raporundaki bir alan.
- PivotFields, bir özet tablodaki tüm PivotField nesnelerinin koleksiyonu.
- PivotTable, bir çalışma sayfasındaki bir PivotTable raporu.
- PivotTables, çalışma sayfasındaki tüm PivotTable nesnelerinin koleksiyonu.

### **Aspose.Cells'i kullanmaya hazırlık**

1. Aspose.Cells.Zip'i indirip kurun:
   1. [Aspose.Cells for Java'yi indirin](https://downloads.aspose.com/cells/java).
   1. Geliştirme bilgisayarınızda zip dosyasını açın.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun bir zaman limiti yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun
   1. Ya bir Eclipse gibi Java Düzenleyici kullanarak bir proje oluşturun ya da NotePad kullanarak basit bir program oluşturun.
1. Sınıf yolunu ekleyin:
   Eclipse kullanarak bir sınıf yolu ayarlamak için:
   1. Aspose.Cells.jar ve dom4j_1.6.1.jar dosyalarını Aspose.Cells.zip'ten çıkartın.
   1. Eclipse'te proje classpath'ini ayarlayın:
   1. Eclipse'te projenizi seçin ve ardından menus Proje-Özellikler'e tıklayın.
   1. Açılan pencerenin sol tarafında "Java Build Path"'i seçin, ardından "Libraries" sekmesini seçin, "Add JARs" veya "Add External JARs"'ı tıklayarak Aspose.Cells.jar ve dom4j_1.6.1.jar'ı seçin ve build yoluna ekleyin.
   1. Aspose'un bileşenlerinin API'lerini çağırmak için uygulama yazın.
      Veya Windows'ta dos komut istemine çalışma zamanında ayarlayabilirsiniz.

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Pivot Tablosu Oluşturma**

Aspose.Cells kullanarak bir pivot tablosu oluşturmak için:

1. Bir Hücre nesnesi'nin PutValue/setValue yöntemini kullanarak bir çalışma sayfasındaki hücrelere bazı veriler ekleyin. Ayrıca zaten verilerle doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun add yöntemini (Worksheet nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablosu ekleyin.
1. PivotTables koleksiyonundan yeni PivotTable nesnesine geçerek indeksini iletebilirsiniz.
1. Tabloyu yönetmek için PivotTable nesnesinde kapsüllenmiş herhangi bir pivot tablo nesnesini kullanın.

Aşağıda bileşen tarafından görevin tamamlanması için kullanılan kod örneği bulunmaktadır. Kodu çalıştırmak yeni bir dosya oluşturur: pivotTable_test.xls.

**Giriş verisi** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Çıktı pivot tablosu**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Pivot Tablosuna Dayalı Pivot Çizelgesi Oluşturma**

Aspose.Cells kullanarak bir pivot çizelgesi oluşturmak için:

1. Bir grafik ekleyin.
1. Grafik PivotSource'unu elektronik tabloda zaten mevcut bir pivot çizelgesine atıf yapacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıda verilmiştir. Kodu çalıştırmak yeni bir dosya oluşturur: pivotChart_test.xls.

**Pivot çizelgesi sayfası**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Bu makale Aspose.Cells kullanarak pivot tabloları ve pivot çizelgeleri oluşturmayı göstermektedir. Umarız kendi senaryolarınızda bu özellikleri kullanmanıza yardımcı olur.

Aspose.Cells yılların araştırması, tasarımı ve dikkatli ayarlamasından faydalanmıştır.

[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9) adresindeki sorularınızı, yorumlarınızı ve önerilerinizi bekliyoruz. Hızlı bir yanıt garantisi veriyoruz.

{{% /alert %}}

## İlgili Makaleler

- [Pivot Tablosunda Özel Sıralama](/cells/tr/java/custom-sorting-in-pivot-table/)
- [Pivot Tablosu Biçimlendirme](/cells/tr/java/formatting-pivot-table/)
- [Hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama](/cells/tr/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Pivot Tablo Şeritlerini Devre Dışı Bırak](/cells/tr/java/disable-pivot-table-ribbons/)

