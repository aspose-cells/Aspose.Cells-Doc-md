---
title: Grafiğin Veri Kaynağını Ayarlama
description: Aspose.Cells for .NET tarafından desteklenen çeşitli veri kaynakları hakkında bilgi edinin. Rehberimiz, mevcut farklı veri kaynakları üzerinden bağlantı kurmayı ve veri almayı gösterecek ve çalışma sayfalarınızı doldurmak için bunlardan nasıl yararlanabileceğinizi size gösterecektir.
keywords: Aspose.Cells for .NET, grafik oluşturma, veri biçimlendirme, etiketler, renkler, yazı tipleri, görünüm, kullanılabilirlik.
linktitle: Veri Kaynağı
type: docs
weight: 10
url: /tr/net/data-formatting-in-charts/
---

Önceki konularımızda, grafikleriniz için bir veri kaynağı nasıl belirleneceğini zaten birçok örnek vermiştik, ancak bu konuda, bir grafik için belirlenebilecek veri türleri hakkında daha fazla ayrıntı sağlayacağız.

## **Grafik Verisi Ayarlama**

Aspose.Cells kullanarak grafikler üzerinde çalışırken ele almanız gereken iki tür veri şunlardır:

- Grafik verisi.
- Kategori verisi.

### **Grafik Verisi**

Grafik verisi, grafiklerimizi oluşturmak için veri kaynağı olarak kullandığımız veridir. Hücrelerin bir rangını (grafik verisi içeren) [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) nesnesinin [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) yöntemi çağrılarak ekleyebiliriz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Kategori Verisi**

Kategori verisi, grafik verisinin etiketlenmesi için kullanılır ve [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)'nin [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata) özelliği kullanılarak eklenir. Aşağıda, grafik ve kategori verisinin kullanımını gösteren tam bir örnek verilmiştir. Yukarıdaki örnek kodu çalıştırdıktan sonra, çalışma sayfasına sütun grafiği aşağıdaki gibi eklenecektir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Gelişmiş Konular**
- [Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme](/cells/tr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dinamik Grafikler Oluşturma](/cells/tr/net/create-dynamic-charts/)
- [Chart.SetChartDataRange Yöntemini Kullanarak Grafik Kurulumu için Kolay Yol](/cells/tr/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Grafik Serisindeki X ve Y Değerleri Türünü Bul](/cells/tr/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
