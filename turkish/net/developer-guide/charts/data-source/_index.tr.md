---
title: Grafiğin Veri kaynağını ayarlayın
description: Aspose.Cells for .NET tarafından desteklenen çeşitli veri kaynakları hakkında bilgi edinin. Kılavuzumuz, mevcut farklı veri kaynakları türleri arasında size yol gösterecek ve çalışma sayfalarınızı doldurmak için bunlara nasıl bağlanacağınızı ve onlardan nasıl veri alacağınızı gösterecektir.
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: Veri kaynağı
type: docs
weight: 10
url: /tr/net/data-formatting-in-charts/
---
Grafiğiniz için veri kaynağını nasıl ayarlayabileceğinizi göstermek amacıyla önceki konularımızda zaten birçok örnek sunmuştuk ancak bu konuda, bir grafik için ayarlanabilecek veri türleri hakkında daha fazla ayrıntı vereceğiz.

##  **Grafik Verilerini Ayarlama**

Aspose.Cells'i kullanarak grafikler üzerinde çalışırken aşağıdaki şekilde ele alınması gereken iki tür veri vardır:

- Grafik verileri.
- Kategori verileri.

###  **Grafik Verileri**

 Grafik verileri, grafiklerimizi oluşturmak için veri kaynağı olarak kullandığımız verilerdir. Çağrı yaparak bir dizi hücre (grafik verilerini içeren) ekleyebiliriz.[**SeriKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) nesnenin[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

###  **Kategori Verileri**

 Kategori verileri, grafik verilerinin etiketlenmesi için kullanılır ve eklenebilir.[**SeriKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) onu kullanarak[**KategoriVeri**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)mülk. Grafik ve kategori verilerinin kullanımını göstermek için aşağıda tam bir örnek verilmiştir. Yukarıdaki örnek kodu çalıştırdıktan sonra çalışma sayfasına aşağıda gösterildiği gibi bir sütun grafiği eklenecektir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

##  **İleri konular**
- [Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme](/cells/tr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dinamik Grafikler Oluşturun](/cells/tr/net/create-dynamic-charts/)
- [Chart.SetChartDataRange yöntemini kullanarak Grafik Kurulumunun kolay yolu](/cells/tr/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Grafik Serisinde Noktaların X ve Y Değerlerinin Türünü Bulma](/cells/tr/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
