---
title: Pivot Tablolar ve Pivot Grafikler Oluşturun
type: docs
weight: 20
url: /tr/net/create-pivot-tables-and-pivot-charts/
---
{{% alert color="primary" %}}

Pivot tablo, kayıtların etkileşimli bir özetidir. Örneğin, bir çalışma sayfasındaki bir listede yüzlerce fatura girişiniz olabilir. Bir pivot tablo, faturaları müşteriye, ürüne veya tarihe göre toplayabilir. Microsoft Excel ile, düğmeleri yeni bir konuma sürükleyerek pivot tablodaki bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.

Pivot grafik, pivot tablodaki verilerin etkileşimli bir grafik temsilidir. Pivot grafikler Excel 2000'de kullanılmaya başlandı. Pivot tablo otomatik olarak ara toplamlar ve toplamlar oluşturduğundan, pivot grafik kullanmak verilerin anlaşılmasını daha da kolaylaştırır.

 Aspose.Cells destekler[pivot tablolar](/cells/tr/net/create-pivot-tables-and-pivot-charts/) ve[pivot grafikler](/cells/tr/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Pivot Tablolar ve Grafikler Ekleme**

Aspose.Cells, pivot tablolar oluşturmak için kullanılan özel bir sınıf seti sağlar. Bu sınıflar, PivotTable nesnesinin temel yapı taşları olarak hareket eden PivotTable nesneleri oluşturmak ve ayarlamak için kullanılır:

- PivotField, pivot tablo raporundaki bir alan.
- PivotFields, bir pivot tablodaki tüm PivotField nesnelerinin bir koleksiyonu.
- PivotTable, bir çalışma sayfasındaki PivotTable raporu.
- PivotTable'lar, çalışma sayfasındaki tüm PivotTable nesnelerinin bir koleksiyonudur.

### **Kullanıma hazırlanıyor Aspose.Cells**

1. Aspose.Cells'i indirin ve yükleyin:
   1. [İndir Aspose.Cells](https://downloads.aspose.com/cells/net).
 1. Geliştirme bilgisayarınıza kurun.
 Herşey[Aspose](http://www.aspose.com/) bileşenler kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler. Bileşenle tam kapasitede çalışmak için geçerli bir lisansa sahip olmanız gerekir.
1. Bir proje oluşturun:
 1. Visual Studio.Net'i başlatın.
 1. Yeni bir konsol uygulaması oluşturun.
1. Referans ekle:
 Projenize Aspose.Cells bileşenine referans ekleyin, örneğin ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Pivot Tablo Ekleme**

Aspose.Cells'i kullanarak bir pivot tablo oluşturmak için:

1. Cell nesnesinin PutValue/setValue yöntemini kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin. Ayrıca önceden verilerle doldurulmuş bir şablon dosyası da kullanırsınız. Veriler, pivot tablonun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun ekleme yöntemini (Çalışma Sayfası nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir özet tablo ekleyin.
1. Dizinini geçirerek PivotTables koleksiyonundan yeni PivotTable nesnesine erişin. # Tabloyu yönetmek için PivotTable nesnesinde kapsüllenmiş herhangi bir pivot tablo nesnesini kullanın.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Pivot Grafik Ekleme**

Aspose.Cells kullanarak PivotChart oluşturmak için:

1. Grafik ekleyin.
1. Grafiğin PivotSource'unu e-tablodaki mevcut bir pivot tabloya atıfta bulunacak şekilde ayarlayın.
1. Diğer nitelikleri ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

