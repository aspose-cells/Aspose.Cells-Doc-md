---
title: Aspose.Cells kullanarak PivotChart nasıl eklenir?
linktitle: Pivot Grafik
type: docs
weight: 100
url: /tr/net/how-to-add-pivot-chart/
description: Aspose.Cells'i kullanarak PivotChart nasıl eklenir?
keywords: PivotChart
---
##  PivotChart Nedir?

Excel'deki PivotChart, PivotTable'dan oluşturulan verilerin grafiksel temsilidir. Bilgileri grafik biçiminde özetleyip görüntüleyerek kullanıcıların verileri dinamik olarak görselleştirmelerine ve analiz etmelerine olanak tanır. PivotChart'lar etkileşimlidir ve verilerin farklı perspektiflerini gösterecek şekilde kolayca değiştirilebilir; bu da onu Excel'de veri analizi ve sunumu için güçlü bir araç haline getirir.

##  Aspose.Cells kullanarak PivotChart nasıl eklenir?

###  **Pivot Tablo Ekleme**

Aspose.Cells'i kullanarak bir pivot tablo oluşturmak için:

1. Cell nesnesinin PutValue/setValue yöntemini kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin. Ayrıca halihazırda verilerle doldurulmuş bir şablon dosyası da kullanırsınız. Veriler pivot tablonun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun ekleme yöntemini (Çalışma Sayfası nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablo ekleyin.
1. PivotTable koleksiyonundan yeni PivotTable nesnesine dizinini ileterek erişin. # Tabloyu yönetmek için PivotTable nesnesinde kapsüllenmiş pivot tablo nesnelerinden herhangi birini kullanın.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **Pivot Grafik Ekleme**

Aspose.Cells'i kullanarak PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafiğin PivotSource'unu e-tablodaki mevcut bir pivot tabloya başvuracak şekilde ayarlayın.
1. Diğer nitelikleri ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

