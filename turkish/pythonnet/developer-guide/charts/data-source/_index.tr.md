---
title: Grafiğin Veri Kaynağını Ayarlama
description: Aspose.Cells for Python via .NET tarafından desteklenen çeşitli veri kaynakları hakkında bilgi edinin. Kılavuzumuz, mevcut farklı veri kaynağı türlerini gösterecek ve bunlara bağlanıp, verileri nasıl alacağınızı ve çalışma sayfalarını nasıl dolduracağınızı gösterecek.
keywords: Aspose.Cells for Python via .NET, grafikler, veri biçimlendirme, etiketler, renkler, yazı tipleri, görünüm, kullanılabilirlik.
linktitle: Veri Kaynağı
type: docs
weight: 10
url: /tr/python-net/data-formatting-in-charts/
---

Önceki konularımızda, grafikleriniz için bir veri kaynağı nasıl belirleneceğini zaten birçok örnek vermiştik, ancak bu konuda, bir grafik için belirlenebilecek veri türleri hakkında daha fazla ayrıntı sağlayacağız.

## **Grafik Verisi Ayarlama**

Aspose.Cells for Python via .NET ile grafiklerde çalışırken iki tür veriyle ilgilenirsiniz:

- Grafik verisi.
- Kategori verisi.

### **Grafik Verisi**

Grafik verisi, grafiklerimizi oluşturmak için veri kaynağı olarak kullandığımız veridir. Hücrelerin bir rangını (grafik verisi içeren) [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) nesnesinin [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add) yöntemi çağrılarak ekleyebiliriz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **Kategori Verisi**

Kategori verisi, grafik verisinin etiketlenmesi için kullanılır ve [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)'nin [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data) özelliği kullanılarak eklenir. Aşağıda, grafik ve kategori verisinin kullanımını gösteren tam bir örnek verilmiştir. Yukarıdaki örnek kodu çalıştırdıktan sonra, çalışma sayfasına sütun grafiği aşağıdaki gibi eklenecektir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **Gelişmiş Konular**
- [Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme](/cells/tr/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dinamik Grafikler Oluşturma](/cells/tr/python-net/create-dynamic-charts/)
- [Chart.SetChartDataRange Yöntemini Kullanarak Grafik Kurulumu için Kolay Yol](/cells/tr/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Grafik Serisindeki X ve Y Değerleri Türünü Bul](/cells/tr/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
