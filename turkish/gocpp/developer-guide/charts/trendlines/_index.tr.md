---
title: Golang ile C++ kullanarak Grafik Eğrisi Denklemi Metnini Alma
linktitle: Eğilim Çizgileri
description: Microsoft Excel da oluşturulan bir grafik içindeki eğri denklem metnini almak için Aspose.Cells for C++ kullanmayı öğrenin. Kılavuzumuz, eğri denklemine nasıl erişeceğinizi ve çıkaracağınızı gösterecek, böylece daha fazla analiz veya gösterim için kullanabilirsiniz.
keywords: Aspose.Cells for C++, Grafik Eğri Doğrusu, Denklem Metni, Microsoft Excel, Veri Analizi, Gösterim.
type: docs
weight: 110
url: /tr/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak Grafik Eğilim Çizgisinin Denklem Metnini alabilirsiniz. Aspose.Cells, eğilim çizgisinin denklem metnini döndüren [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) özelliğini sağlar. Bu özelliği kullanmak için öncelikle [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/) yöntemini çağırmanız gerekecektir.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, Trend Hattı olan ve Denklemini Kırmızı renk ile gösterilen Grafiği gösterir. Bu metni, aşağıdaki örnek kodda [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) özelliği kullanılarak alacağız.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++ ile grafik eğri doğrusunun denklem metnini alma kodu

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
Örneğin ürettiği çıktı

Yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
