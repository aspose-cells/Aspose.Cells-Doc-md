---
title: Grafik için Veri kaynağını ayarla
linktitle: Veri kaynağı
type: docs
weight: 10
url: /tr/net/data-formatting-in-charts/
---
Önceki konularımızda, grafiğiniz için bir veri kaynağını nasıl ayarlayabileceğinizi göstermek için birçok örnek vermiştik ancak bu konuda, bir grafik için ayarlanabilecek veri türleri hakkında daha fazla ayrıntı sağlayacağız.

## **Grafik Verilerini Ayarlama**

Aspose.Cells'i kullanarak grafikler üzerinde çalışırken ele alınması gereken iki tür veri vardır:

- Grafik verileri.
- Kategori verileri.

### **Grafik Verileri**

Grafik verileri, grafiklerimizi oluşturmak için veri kaynağı olarak kullandığımız verilerdir. Çağırarak bir hücre aralığı (grafik verileri içeren) ekleyebiliriz.[**Seri Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) nesnenin[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Kategori Verileri**

 Kategori verileri, grafik verilerinin etiketlenmesi için kullanılır ve aşağıdakilere eklenebilir:[**Seri Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) kullanarak[**KategoriVerileri**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)Emlak. Grafik ve kategori verilerinin kullanımını göstermek için aşağıda eksiksiz bir örnek verilmiştir. Yukarıdaki örnek kodu çalıştırdıktan sonra, çalışma sayfasına aşağıda gösterildiği gibi bir sütun grafiği eklenecektir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **ileri konular**
- [Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirin](/cells/tr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dinamik Grafikler Oluşturun](/cells/tr/net/create-dynamic-charts/)
- [Chart.SetChartDataRange yöntemini kullanarak Grafik Kurulumu için kolay yol](/cells/tr/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Grafik Serisindeki Noktaların X ve Y Değerlerinin Türünü Bulma](/cells/tr/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
