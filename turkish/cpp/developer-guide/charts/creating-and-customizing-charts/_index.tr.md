---
title: Grafikler Oluşturma ve Özelleştirme
type: docs
weight: 10
url: /tr/cpp/creating-and-customizing-charts/
---
## **Olası Kullanım Senaryoları**

Grafik, bilgilerin görsel bir gösterimidir. Aspose.Cells, geliştiricilerin tıpkı Microsoft Excel'in yaptığı gibi grafiklerdeki bilgileri görselleştirmesine olanak tanır. Bilgileri grafikler halinde sunmak, karar vericilerin hızlı ve zamanında kararlar almaları için her zaman yardımcı olur. Verilerdeki karşılaştırmaları, kalıpları ve eğilimleri, ham sayılar yerine grafiklerle hızlı bir şekilde görmek daha kolaydır. Bir elektronik tablodaki verilere dayalı olarak çalışma zamanında grafikler oluşturmak, Aspose.Cells'in kullanışlı özelliklerinden biridir. Aspose.Cells, hem Standart hem de Özelleştirilmiş grafikler oluşturmayı destekler. Aşağıda, Aspose.Cells API kullanarak bazı yaygın MS-Excel grafik türlerinin nasıl oluşturulacağına ilişkin örnek dosyalarla birlikte birkaç örnek göstereceğiz.

## **Piramit Grafiği**

 Örnek kod yürütüldüğünde, çalışma sayfasına bir piramit grafiği eklenir. Lütfen bkz[çıktı excel dosyası](66519068.xlsx) aşağıdaki örnek koddan.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart.cpp" >}}

## **Çizgi grafik**

Yukarıdaki örnekte, basitçe değiştirmek[**Grafik tipi**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)ile[**ChartType_Line**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70ad12ff1561ab1424a0c3095b6dc07ac25)bir çizgi grafiği oluşturur. Tam kaynak aşağıda verilmiştir. kod yürütüldüğünde, çalışma sayfasına bir çizgi grafik eklenir. Lütfen bkz[çıktı excel dosyası](66519069.xlsx) aşağıdaki örnek koddan.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart.cpp" >}}

## **Kabarcık Grafiği**

Balon grafiği oluşturmak için,[**Grafik tipi**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70) olarak ayarlanması gerekir[**ChartType_Bubble**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70a5efa533b454f9415e4497dbb2ab28b3d) ve birkaç ekstra özellik gibi[**Balon Boyutlarını Ayarla**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a00cf890ba7ab419d31a522ab52b02e9d) & [**SetXValues**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a788ff4aa51dbf9bed5327298af93a6db) buna göre ayarlanması gerekir. Aşağıdaki kodu çalıştırdıktan sonra, çalışma sayfasına bir balon grafiği eklenir. Lütfen bkz[çıktı excel dosyası](66519070.xlsx) aşağıdaki örnek koddan.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart.cpp" >}}

## **Özel Grafikler Oluşturma**

Şimdiye kadar grafikleri tartıştığımızda, kendi standart biçimlendirme ayarlarına sahip standart grafiklere baktık. Yalnızca veri kaynağını tanımlarız, birkaç özellik ayarlarız ve grafik, varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells API'leri, geliştiricilerin kendi biçim ayarlarıyla grafikler oluşturmasına olanak tanıyan özel grafikler oluşturmayı da destekler. Geliştiriciler, çalışma zamanında Aspose.Cells'i kullanarak özel grafikler oluşturabilir.

Grafik, bir veri serisinden oluşur. Geliştiriciler, özel bir grafik oluştururken, farklı veri serileri için farklı türde grafikler kullanma özgürlüğüne sahiptir.

 Aşağıdaki örnek kod, özel grafiklerin nasıl oluşturulacağını gösterir. Bu örnekte, birinci veri serisi için bir sütun grafiği ve ikinci seri için bir çizgi grafiği kullanacağız. Sonuç olarak, çalışma sayfasına bir çizgi grafiğiyle birlikte bir sütun grafiği ekliyoruz. Lütfen bkz[çıktı excel dosyası](66519071.xlsx) aşağıdaki örnek koddan.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart.cpp" >}}
