---
title: Grafiklerde Veri Biçimlendirme
linktitle: Veri kaynağı
type: docs
weight: 50
url: /tr/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

Önceki konularımızda, grafiğiniz için bir veri kaynağını nasıl ayarlayabileceğinizi göstermek için birçok örnek vermiştik ancak bu konuda, bir grafik için ayarlanabilecek veri türleri hakkında daha fazla ayrıntı sağlayacağız.

{{% /alert %}}

## **Grafik Verilerini Ayarlama**

Aspose.Cells'i kullanarak grafikler üzerinde çalışırken ele alınması gereken iki tür veri vardır:

- [Grafik verileri](/cells/tr/java/data-formatting-in-charts/#chart-data).
- [Kategori verileri](/cells/tr/java/data-formatting-in-charts/#category-data).

### **Grafik Verileri**

 Grafik verileri, grafiklerimizi oluşturmak için veri kaynağı olarak kullandığımız verilerdir. Çağırarak bir hücre aralığı (grafik verileri içeren) ekleyebiliriz.[**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) nesnenin[**Eklemek**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Kategori Verileri**

 Kategori verileri, grafik verilerinin etiketlenmesi için kullanılır ve aşağıdakilere eklenebilir:[**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) kullanarak[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Grafik ve kategori verileri içeren sütun grafiği** 

![yapılacaklar:resim_alternatif_metin](data-formatting-in-charts_1.png)

## **ileri konular**
- [Dinamik Grafikler Oluşturun](/cells/tr/java/create-dynamic-charts/)
- [Chart.setChartDataRange yöntemini kullanarak Grafik Kurulumu için kolay yol](/cells/tr/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Grafik Serisindeki Noktaların X ve Y Değerlerinin Türünü Bulma](/cells/tr/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/java/set-the-values-format-code-of-chart-series/)
