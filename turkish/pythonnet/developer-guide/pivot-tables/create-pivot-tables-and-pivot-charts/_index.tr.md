---
title: Pivot Tablolar ve Pivot Grafikler Oluşturun
type: docs
weight: 20
url: /tr/python-net/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Python via .NET ile Pivot Tablolar ve Pivot Grafikler nasıl eklenir?
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

Pivot tablo, kayıtların etkileşimli bir özetidir. Örneğin, bir çalışma sayfasındaki listede yüzlerce fatura girişiniz olabilir. Bir pivot tablo, faturaları müşteriye, ürüne veya tarihe göre toplayabilir. Microsoft Excel ile, düğmeleri yeni bir konuma sürükleyerek pivot tablodaki bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.

Pivot grafiği, pivot tablodaki verilerin etkileşimli grafiksel temsilidir. Pivot grafikler Excel 2000'de kullanılmaya başlandı. Pivot tablo, alt toplamları ve toplamları otomatik olarak oluşturduğundan, pivot grafiği kullanmak verileri anlamayı daha da kolaylaştırır.

 Aspose.Cells for Python via .NET destekler[pivot tablolar](/cells/tr/python-net/create-pivot-tables-and-pivot-charts/) Ve[pivot çizelgeleri](/cells/tr/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **Pivot Tablolar ve Grafikler Ekleme**

Aspose.Cells for Python via .NET, pivot tablolar oluşturmak için kullanılan özel bir sınıf seti sağlar. Bu sınıflar, PivotTable nesnesinin temel yapı taşları olarak görev yapan PivotTable nesnelerini oluşturmak ve ayarlamak için kullanılır:

- PivotField, pivot tablo raporundaki bir alan.
- PivotFields, bir pivot tablodaki tüm PivotField nesnelerinin koleksiyonudur.
- PivotTable, bir çalışma sayfasındaki PivotTable raporu.
- PivotTable'lar, çalışma sayfasındaki tüm PivotTable nesnelerinin bir koleksiyonudur.

###  **Kullanıma hazırlama Aspose.Cells for Python via .NET**
1.  Aspose.Cells for Python via .NET'i şuradan yükleyin:[pypi](https://pypi.org/project/aspose-cells-python/)komutu şu şekilde kullanın: $ pip install aspose-cells-python.
1. Ayrıca geliştirici ortamınıza “Aspose.Cells for Python via .NET” kurulumunun nasıl yapılacağına dair adım adım talimatları takip edebilirsiniz.


###  **Pivot Tablo Ekleme**

Aspose.Cells for Python via .NET'i kullanarak pivot tablo oluşturmak için:

1. Cell nesnesinin put_value yöntemini kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin. Ayrıca halihazırda verilerle doldurulmuş bir şablon dosyası da kullanırsınız. Veriler pivot tablonun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun ekleme yöntemini (Çalışma Sayfası nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablo ekleyin.
1. PivotTable koleksiyonundan yeni PivotTable nesnesine dizinini ileterek erişin. # Tabloyu yönetmek için PivotTable nesnesinde kapsüllenmiş pivot tablo nesnelerinden herhangi birini kullanın.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **Pivot Grafik Ekleme**

Aspose.Cells for Python via .NET'i kullanarak PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafiğin PivotSource'unu e-tablodaki mevcut bir pivot tabloya başvuracak şekilde ayarlayın.
1. Diğer nitelikleri ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

