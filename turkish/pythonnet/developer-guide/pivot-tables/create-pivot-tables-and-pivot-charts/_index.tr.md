---
title: Özet Tabloları ve Özet Grafikler Oluşturma
type: docs
weight: 20
url: /tr/python-net/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Python via .NET ile Pivot Tabloları ve Pivot Grafikleri Nasıl Eklenir.
keywords: Aspose.Cells for Python Excel, Excel Python kütüphanesi, Aspose.Cells for Python Excel Kütüphanesi Kullanılarak Pivot Tabloları ve Pivot Grafikleri Ekleme.
---

{{% alert color="primary" %}}

Bir özet tablo, kayıtların etkileşimli bir özeti. Örneğin, bir çalışma sayfasındaki bir listede yüzlerce fatura girişiniz olabilir. Bir özet tablo, faturaları müşteri, ürün veya tarihe göre toplayabilir. Microsoft Excel ile özet tablonun düğmeleri sürüklenerek bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.

Bir özet grafik, bir özet tablonun verilerinin etkileşimli grafiksel bir temsilidir. Özet grafikler Excel 2000'de tanıtılmıştır. Özet grafik kullanmak, özet tablonun alt toplamlarını ve toplamlarını otomatik olarak oluşturduğu için verileri anlamak daha da kolaylaştırır.

Aspose.Cells for Python via .NET [pivot tablolarını](/cells/tr/python-net/create-pivot-tables-and-pivot-charts/) ve [pivot grafiklerini](/cells/tr/python-net/create-pivot-tables-and-pivot-charts/) destekler.

{{% /alert %}}

## **Aspose.Cells for Python Excel Kütüphanesi Kullanılarak Pivot Tabloları ve Grafikleri Ekleme**

Aspose.Cells for Python via .NET, pivot tabloları oluşturmak için kullanılan özel bir sınıf setini sağlar. Bu sınıflar, bir PivotTablosu nesnesinin temel yapı taşları olan PivotTablosu nesnelerini oluşturmak ve ayarlamak için kullanılır:

- PivotField, bir özet tablo raporundaki bir alan.
- PivotFields, bir özet tablodaki tüm PivotField nesnelerinin koleksiyonu.
- PivotTable, bir çalışma sayfasındaki bir PivotTable raporu.
- PivotTables, çalışma sayfasındaki tüm PivotTable nesnelerinin koleksiyonu.

### **Aspose.Cells for Python via .NET'yı kullanmaya hazırlanın**
1. [pypi](https://pypi.org/project/aspose-cells-python/) üzerinden Aspose.Cells for Python via .NET'yi yükleyin, komutu şu şekilde kullanabilirsiniz: $ pip install aspose-cells-python.
1. “Aspose.Cells for Python via .NET”'yi geliştirici ortamınıza nasıl kuracağınıza dair adım adım talimatları da takip edebilirsiniz.


### **Aspose.Cells for Python Excel Kütüphanesi Kullanılarak Pivot Tablosu Nasıl Eklenir**

Aspose.Cells for Python via .NET kullanarak bir pivot tablosu oluşturmak için:

1. Hücre nesnesinin put_value methodunu kullanarak bir çalışma sayfasına veri ekleyin. Ayrıca veri ile doldurulmuş bir şablon dosyası da kullanabilirsiniz. Veri, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun add yöntemini (Worksheet nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablosu ekleyin.
1. Yeni PivotTable nesnesine PivotTables koleksiyonundan endeksini geçerek erişin. # PivotTable nesnesinde kapsanan herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **Aspose.Cells for Python Excel Kütüphanesi Kullanarak Bir Pivot Chart Nasıl Eklenir**

Aspose.Cells for Python via .NET Kullanarak Bir PivotChart Oluşturmak için:

1. Bir grafik ekleyin.
1. Grafik PivotSource'unu elektronik tabloda zaten mevcut bir pivot çizelgesine atıf yapacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

