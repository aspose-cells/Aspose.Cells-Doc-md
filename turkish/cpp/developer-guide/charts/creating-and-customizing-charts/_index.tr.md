---
title: Grafik Oluşturma ve Özelleştirme
type: docs
weight: 10
url: /tr/cpp/creating-and-customizing-charts/
---
##  **Olası Kullanım Senaryoları**

Grafik, bilgilerin görsel bir gösterimidir. Aspose.Cells, geliştiricilerin tıpkı Microsoft Excel'in yaptığı gibi grafiklerdeki bilgileri görselleştirmesine olanak tanır. Bilgilerin grafikler halinde sunulması karar vericilere hızlı ve zamanında karar verme konusunda her zaman yardımcı olur. Ham sayılar yerine grafiklerle verilerdeki karşılaştırmaları, kalıpları ve eğilimleri hızlı bir şekilde görmek daha kolaydır. Bir elektronik tablodaki verilere dayanarak çalışma zamanında grafikler oluşturmak, Aspose.Cells'in kullanışlı özelliklerinden biridir. Aspose.Cells, hem Standart hem de Özelleştirilmiş grafiklerin oluşturulmasını destekler. Aşağıda, Aspose.Cells API'i kullanarak bazı yaygın MS-Excel grafik türlerinin nasıl oluşturulacağına ilişkin örnek dosyalar içeren birkaç örnek göstereceğiz.

##  **Piramit Grafiği**

 Örnek kod çalıştırıldığında çalışma sayfasına bir piramit grafiği eklenir. Lütfen bkz[Excel dosyasının çıktısı](66519068.xlsx) aşağıdaki örnek koddan.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

##  **Çizgi grafik**

Yukarıdaki örnekte, yalnızca[**Grafik tipi**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)ile**'ChartType::Çizgi'**çizgi grafiği oluşturur. Kaynağın tamamı aşağıda verilmiştir. kod yürütüldüğünde çalışma sayfasına bir çizgi grafik eklenir. Lütfen bkz[Excel dosyasının çıktısı](66519069.xlsx) aşağıdaki örnek koddan.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

##  **Kabarcık Grafiği**

Kabarcık grafiği oluşturmak için[**Grafik tipi**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) olarak ayarlanması gerekiyor**'ChartType_Bubble'** ve birkaç ekstra özellik gibi[**Kabarcık Boyutlarını Ayarla**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) buna göre ayarlamak gerekiyor. Aşağıdaki kodu çalıştırdıktan sonra çalışma sayfasına bir kabarcık grafiği eklenir. Lütfen bkz[Excel dosyasının çıktısı](66519070.xlsx) aşağıdaki örnek koddan.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

##  **Özel Grafikler Oluşturma**

Şu ana kadar grafikleri tartışırken, kendi standart biçimlendirme ayarlarına sahip standart grafiklere baktık. Yalnızca veri kaynağını tanımlıyoruz, birkaç özelliği ayarlıyoruz ve grafik varsayılan format ayarlarıyla oluşturuluyor. Ancak Aspose.Cells API'leri, geliştiricilerin kendi format ayarlarıyla grafikler oluşturmasına olanak tanıyan özel grafikler oluşturmayı da destekler. Geliştiriciler çalışma zamanında Aspose.Cells'i kullanarak özel grafikler oluşturabilir.

Bir grafik bir veri serisinden oluşur. Özel bir grafik oluştururken geliştiriciler, farklı veri serileri için farklı türde grafikler kullanma özgürlüğüne sahiptir.

 Aşağıdaki örnek kod, özel grafiklerin nasıl oluşturulacağını gösterir. Bu örnekte ilk veri serisi için sütun grafiği, ikinci seri için ise çizgi grafiği kullanacağız. Sonuç olarak, çalışma sayfasına çizgi grafikle birleştirilmiş bir sütun grafiği ekliyoruz. Lütfen bkz[Excel dosyasının çıktısı](66519071.xlsx) aşağıdaki örnek koddan.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
