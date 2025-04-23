---
title: Pasta Grafiklerinde veya Barlı Pasta veya Pasta Grafiğindeki İkinci Pastada veya Bar da Veri Noktalarını Bulma
description: Veri noktalarının pasta grafiğindeki veya barlı pasta grafiğindeki ikinci pastada veya bar da olup olmadığını bulmayı öğrenin Aspose.Cells for .NET kullanın. Kılavuzumuz, bileşik bir grafikte ikincil pastayı veya barı tanımlamanın ve erişmenin nasıl olduğunu gösterecektir, böylece verileri etkin bir şekilde analiz edip manipüle edebilirsiniz.
keywords: Aspose.Cells for .NET, Pasta Grafiği, Barlı Pasta Grafiği, İkincil Pasta, İkincil Bar, Veri Analizi, Veri Manipülasyonu.
type: docs
weight: 180
url: /tr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells kullanarak *Pasta Grafiği* veya *Barlı Pasta* grafiklerinde serilerin veri noktalarının ikinci pastada veya ikinci barda olup olmadığını bulabilirsiniz. Lütfen [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) özelliğini kullanarak bunu belirleyin.

Lütfen aşağıdaki örnek kodda kullanılan [örnek excel dosyasını](5115193.xlsx) indirin ve konsol çıktısını görün. [Örnek excel dosyasını](5115193.xlsx) açarsanız, tüm veri noktalarının 10'dan az olduğunu, *Barlı Pasta* grafik içinde olduğunu, aynı zamanda konsol çıktısı tarafından da gösterildiğini bulacaksınız.
## **Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma**
Aşağıdaki örnek kod, veri noktalarının *Pasta Grafiği* veya *Barlı Pasta* grafiklerinde ikinci pastada veya bar'da olup olmadığını nasıl bulacağınızı gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun çalıştırılmasından sonra oluşturulan aşağıdaki konsol çıktısını inceleyin. [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) **false** ise, veri noktası pastanın içindedir; **true** ise, veri noktası bardadır.



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
{{< app/cells/assistant language="csharp" >}}
