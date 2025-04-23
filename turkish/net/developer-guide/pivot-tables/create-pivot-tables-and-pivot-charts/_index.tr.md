---
title: Özet Tabloları ve Özet Grafikler Oluşturma
type: docs
weight: 20
url: /tr/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

Bir özet tablo, kayıtların etkileşimli bir özeti. Örneğin, bir çalışma sayfasındaki bir listede yüzlerce fatura girişiniz olabilir. Bir özet tablo, faturaları müşteri, ürün veya tarihe göre toplayabilir. Microsoft Excel ile özet tablonun düğmeleri sürüklenerek bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.

Bir özet grafik, bir özet tablonun verilerinin etkileşimli grafiksel bir temsilidir. Özet grafikler Excel 2000'de tanıtılmıştır. Özet grafik kullanmak, özet tablonun alt toplamlarını ve toplamlarını otomatik olarak oluşturduğu için verileri anlamak daha da kolaylaştırır.

Aspose.Cells, [pivot tablolarını](/cells/tr/net/create-pivot-tables-and-pivot-charts/) ve [pivot grafiklerini](/cells/tr/net/create-pivot-tables-and-pivot-charts/) destekler.

{{% /alert %}}

## **Özet Tabloları ve Grafikler Eklemek**

Aspose.Cells, özet tabloları oluşturmak için kullanılan özel bir sınıf kümesi sağlar. Bu sınıflar, PivotTable nesnelerini oluşturmak ve ayarlamak için kullanılır ve temel PivotTable nesnesinin yapı taşları olarak hareket ederler:

- PivotField, bir özet tablo raporundaki bir alan.
- PivotFields, bir özet tablodaki tüm PivotField nesnelerinin koleksiyonu.
- PivotTable, bir çalışma sayfasındaki bir PivotTable raporu.
- PivotTables, çalışma sayfasındaki tüm PivotTable nesnelerinin koleksiyonu.

### **Aspose.Cells'i kullanmaya hazırlık**

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells'i İndirin](https://downloads.aspose.com/cells/net).
   1. Geliştirme bilgisayarınıza kurun.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun bir süre sınırı yoktur ve üretilen belgelere sadece filigranlar ekler. Bileşenle tam kapasitede çalışmak için geçerli bir lisansa sahip olmanız gerekir.
1. Bir proje oluşturun:
   1. Visual Studio.Net'i başlatın.
   1. Yeni bir konsol uygulaması oluşturun.
1. Referanslar ekleyin:
   Projenize Aspose.Cells bileşenine referans ekleyin, örneğin...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Pivot Tablo Ekleme**

Aspose.Cells kullanarak bir pivot tablosu oluşturmak için:

1. Bir Hücre nesnesi'nin PutValue/setValue yöntemini kullanarak bir çalışma sayfasındaki hücrelere bazı veriler ekleyin. Ayrıca zaten verilerle doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun add yöntemini (Worksheet nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablosu ekleyin.
1. Yeni PivotTable nesnesine PivotTables koleksiyonundan endeksini geçerek erişin. # PivotTable nesnesinde kapsanan herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Pivot Grafik Ekleme**

Aspose.Cells kullanarak bir PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafik PivotSource'unu elektronik tabloda zaten mevcut bir pivot çizelgesine atıf yapacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
