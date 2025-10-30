---
title: Data Noktalarının Pie of Pie veya Pie of Pie grafikte İkinci Piyada veya Bar da olup olmadığını Golang ile C++ kullanarak bulun
linktitle: Pasta Grafiklerinde veya Barlı Pasta veya Pasta Grafiğindeki İkinci Pastada veya Bar da Veri Noktalarını Bulma
description: Pasta ve pasta grafiklerinde veri noktalarının ikinci pasta veya çubuğa ait olup olmadığını bulmak için Aspose.Cells for C++ nasıl kullanılır öğrenin. Kılavuzumuz, ikincil pasta veya çubuğu tanımlama ve erişim yöntemlerini gösterecek, veriyi etkili biçimde analiz etmenize ve manipüle etmenize olanak tanıyacaktır.
keywords: Aspose.Cells for C++, Pasta ve Pasta Grafiği, Çubuğa Sahip Pasta Grafiği, İkincil Pasta, İkincil Çubuk, Veri Analizi, Veri Manipülasyonu.
type: docs
weight: 180
url: /tr/go-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells kullanarak serinin data noktalarının *Pie of Pie* grafiğinde ikinci pie'da veya *Bar of Pie* grafikteki çubuğunda olup olmadığını bulabilirsiniz. Lütfen bunu belirlemek için [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/go-cpp/chartpoint/isinsecondaryplot/) özelliğini kullanın.

Lütfen aşağıdaki örnek kodda kullanılan [örnek excel dosyasını](5115193.xlsx) indirin ve konsol çıktısını görün. [Örnek excel dosyasını](5115193.xlsx) açarsanız, tüm veri noktalarının 10'dan az olduğunu, *Barlı Pasta* grafik içinde olduğunu, aynı zamanda konsol çıktısı tarafından da gösterildiğini bulacaksınız.

## **Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma**
Aşağıdaki örnek kod, veri noktalarının *Pasta Grafiği* veya *Barlı Pasta* grafiklerinde ikinci pastada veya bar'da olup olmadığını nasıl bulacağınızı gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfDataPointsAreInTheSecondPieOrBarOnAPieOfPieOrBarOfPieChart.go" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun çalıştırılmasından sonra üretilen konsol çıktısını [örnek excel dosyası](5115193.xlsx) ile inceleyin. Eğer [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) **false** ise, veri noktası Pasta içindedir; eğer **true** ise, Veri noktası Çubuk içindedir.

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
