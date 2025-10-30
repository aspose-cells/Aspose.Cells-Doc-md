---
title: Pasta Grafiklerinde veya Barlı Pasta veya Pasta Grafiğindeki İkinci Pastada veya Bar da Veri Noktalarını Bulma
description: Aspose.Cells for Python via .NET kullanarak, veri noktalarının ikinci pasta veya bar üzerinde olup olmadığını nasıl bulacağınızı gösteririz. Kılavuzumuz, bir kombinasyon grafiğinde ikinci pastanın veya çubuğun nasıl tanımlanıp erişileceğini anlatır, böylece verileri etkin şekilde analiz edebilirsiniz.
keywords: Aspose.Cells for Python via .NET, Pastadan Pasta Grafiği, Çubuklu Pasta Grafiği, İkinci Pasta, İkinci Çubuk, Veri Analizi, Veri Manipülasyonu.
type: docs
weight: 180
url: /tr/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for Python via .NET kullanarak, *Pastadan Pasta* grafiğinde veya *Çubuklu Pasta* grafiğinde veri noktalarının ikinci pastada olup olmadığını nasıl belirleyeceğinizi gösteririz. Bunu [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot) özelliği ile yapabilirsiniz.

Lütfen aşağıdaki örnek kodda kullanılan [örnek excel dosyasını](5115193.xlsx) indirin ve konsol çıktısını görün. [Örnek excel dosyasını](5115193.xlsx) açarsanız, tüm veri noktalarının 10'dan az olduğunu, *Barlı Pasta* grafik içinde olduğunu, aynı zamanda konsol çıktısı tarafından da gösterildiğini bulacaksınız.

## **Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma**
Aşağıdaki örnek kod, veri noktalarının *Pasta Grafiği* veya *Barlı Pasta* grafiklerinde ikinci pastada veya bar'da olup olmadığını nasıl bulacağınızı gösterir.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun çalıştırılmasından sonra üretilen aşağıdaki konsol çıktısını inceleyebilirsiniz. Ayrıca [sample excel file](5115193.xlsx) kullanılmıştır. Eğer [is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/) yanlışsa, veri noktası Pastanın içindedir, doğruysa Çubuğun içindedir.



{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
