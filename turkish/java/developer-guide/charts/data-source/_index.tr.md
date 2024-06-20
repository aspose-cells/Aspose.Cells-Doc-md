---
title: Grafiklerde Veri Biçimlendirme
linktitle: Veri Kaynağı
type: docs
weight: 50
url: /tr/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

Önceki konularımızda, grafikleriniz için bir veri kaynağı nasıl belirleneceğini zaten birçok örnek vermiştik, ancak bu konuda, bir grafik için belirlenebilecek veri türleri hakkında daha fazla ayrıntı sağlayacağız.

{{% /alert %}}

## **Grafik Verisi Ayarlama**

Aspose.Cells kullanarak grafikler üzerinde çalışırken ele almanız gereken iki tür veri şunlardır:

- [Grafik verisi](/cells/tr/java/data-formatting-in-charts/#chart-data).
- [Kategori verisi](/cells/tr/java/data-formatting-in-charts/#category-data).

### **Grafik Verisi**

Grafik verisi, grafiklerimizi oluşturmak için veri kaynağı olarak kullandığımız veridir. [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) nesnesinin [**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) yöntemini çağırarak hücrelerin bir aralığını (grafik verisi içeren) ekleyebiliriz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Kategori Verisi**

Kategori verisi, grafik verilerinin etiketlenmesi için kullanılır ve [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) kullanılarak [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData) yöntemi ile eklenir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Grafik ve Kategori Verili Sütun Grafiği** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Gelişmiş Konular**
- [Dinamik Grafikler Oluşturma](/cells/tr/java/create-dynamic-charts/)
- [Chart.setChartDataRange yöntemi kullanarak Grafik Kurulumu için Kolay Yol](/cells/tr/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Grafik Serisindeki X ve Y Değerleri Türünü Bul](/cells/tr/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/java/set-the-values-format-code-of-chart-series/)
