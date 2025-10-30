---
title: Grafik Oluşturma ve Özelleştirme
type: docs
weight: 10
url: /tr/cpp/creating-and-customizing-charts/
---

## **Olası Kullanım Senaryoları**

Bir grafik, bilgilerin görsel bir şekilde gösterimidir. Aspose.Cells geliştiricilere, Microsoft Excel'in yaptığı gibi bilgileri grafiklerde görselleştirmeyi sağlar. Bilgilerin grafiklerde sunulması, karar vericilerin hızlı ve zamanında kararlar almasına yardımcı olur. Grafikler aracılığıyla verilerdeki karşılaştırmalar, desenler ve trendler hızlı bir şekilde görülebilir. Aspose.Cells'ın faydalı bir özelliği, elektronik tablodaki verilere dayalı olarak çalışma zamanında grafikler oluşturmaktır. Aspose.Cells, Hem Standart Hem de Özelleştirilmiş grafikler oluşturmayı destekler. Aşağıda, Aspose.Cells API'sini kullanarak yaygın MS-Excel grafik tiplerini oluşturmak için birkaç örnek dosya ile bazı örnekleri göstereceğiz.

## **Piramit Grafiği**

Örnek kod çalıştırıldığında, bir piramit grafik çalışma sayfasına eklenir. Lütfen aşağıdaki örnek kodun [çıktı Excel dosyasını](66519068.xlsx) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **Çizgi Grafiği**

Yukarıdaki örnekte, sadece [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)'yu **`ChartType::Line`**'a değiştirerek bir çizgi grafiği oluşturulur. Tam kaynak aşağıda sağlanmıştır. Kod çalıştırıldığında, bir çizgi grafiği çalışma sayfasına eklenir. Lütfen aşağıdaki örnek kodun [çıktı Excel dosyasını](66519069.xlsx) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **Kabarcık Grafiği**

Baloncuk grafik oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) **`ChartType_Bubble`** olarak ayarlanmalı ve [**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) gibi ekstra özellikler uygun şekilde ayarlanmalıdır. Aşağıdaki kodu çalıştırdığınızda, bir baloncuk grafik çalışma sayfasına eklenir. Lütfen aşağıdaki örnek kodun [çıktı Excel dosyasını](66519070.xlsx) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **Özel Grafikler Oluşturma**

Şimdiye kadar, grafikleri tartışırken, kendi standart biçim ayarlarına sahip standart grafiklere bakmıştık. Yalnızca veri kaynağını tanımlarız, birkaç özellik ayarları yaparız ve grafik, varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells API'leri, geliştiricilere kendi biçim ayarları ile grafik oluşturmayı destekler. Geliştiriciler, Aspose.Cells'ı kullanarak çalışma zamanında özel grafikler oluşturabilir.

Bir grafik, bir veri serisinden oluşur. Özel bir grafik oluştururken, geliştiriciler farklı veri serileri için farklı grafik türlerini kullanmada özgürlüğe sahiptir.

Aşağıdaki örnek kod, özel grafikler oluşturmayı nasıl gösterir. Bu örnekte, ilk veri serisi için bir sütun grafiği ve ikinci serisi için bir çizgi grafiği kullanacağız. Sonuç olarak, bir çalışma sayfasına sütun grafiği ve çizgi grafiği eklenir. Lütfen aşağıdaki örnek kodun [çıktı Excel dosyasını](66519071.xlsx) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
