---
title: Golang kullanarak C++ ile Grafik İçin Veri Kaynağı Ayarlama
linktitle: Veri Kaynağı
type: docs
weight: 10
url: /tr/go-cpp/data-formatting-in-charts/
description: Aspose.Cells for C++ tarafından desteklenen çeşitli veri kaynakları hakkında bilgi edinin. Rehberimiz, mevcut farklı veri kaynağı türlerini anlatacak ve bunlara nasıl bağlanıp verileri alarak çalışma sayfalarınızı dolduracağınızı gösterecektir.
keywords: Aspose.Cells for C++, çizelgeleme, veri biçimlendirme, etiketler, renkler, yazı tipleri, görünüm, kullanılabilirlik.
---

Önceki konularımızda, grafikleriniz için veri kaynağı nasıl ayarlanır gösteren birçok örnek sunduk. Bu konuda, bir grafik için ayarlanabilecek veri türleri hakkında daha fazla detay vereceğiz.

## **Grafik Verisi Ayarlama**

Aspose.Cells kullanarak grafikler üzerinde çalışırken ele almanız gereken iki tür veri şunlardır:

- Grafik verisi.
- Kategori verisi.

### **Grafik Verisi**

Grafik verisi, grafiklerimizi oluşturmak için veri kaynağı olarak kullandığımız veridir. Hücrelerin bir rangını (grafik verisi içeren) [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) nesnesinin [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) yöntemi çağrılarak ekleyebiliriz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **Kategori Verisi**

Kategori verisi, grafik verisinin etiketlenmesi için kullanılır ve [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/)'nin [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/) özelliği kullanılarak eklenir. Aşağıda, grafik ve kategori verisinin kullanımını gösteren tam bir örnek verilmiştir. Yukarıdaki örnek kodu çalıştırdıktan sonra, çalışma sayfasına sütun grafiği aşağıdaki gibi eklenecektir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **Gelişmiş Konular**
- [Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme](/cells/tr/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dinamik Grafikler Oluşturma](/cells/tr/cpp/create-dynamic-charts/)
- [Chart.SetChartDataRange Yöntemini Kullanarak Grafik Kurulumu için Kolay Yol](/cells/tr/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Grafik Serisindeki X ve Y Değerleri Türünü Bul](/cells/tr/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
