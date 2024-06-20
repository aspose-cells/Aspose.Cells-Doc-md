---
title: Pasta Grafiklerinde veya Barlı Pasta veya Pasta Grafiğindeki İkinci Pastada veya Bar da Veri Noktalarını Bulma
type: docs
weight: 910
url: /tr/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells kullanarak *Pasta of Pasta* grafiğindeki veri serilerinin veri noktalarının ikinci pasta içinde veya *Pasta of Bar* grafikteki çubuk içinde olduğunu bulabilirsiniz. Lütfen [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) özelliğini belirlemek için kullanın.

Lütfen aşağıdaki örnek kodunda kullanılan [örnek excel dosyasını](5473373.xlsx) indirin ve konsol çıktısını görün. Eğer [örnek excel dosyasını](5473373.xlsx) açarsanız, tüm 10'dan küçük olan veri noktalarını çubuk içinde *Pasta of Bar* grafik olarak da konsol çıktısı tarafından gösterildiği gibi bulacaksınız.
## **Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma**
Aşağıdaki örnek kod, veri noktalarının *Pasta Grafiği* veya *Barlı Pasta* grafiklerinde ikinci pastada veya bar'da olup olmadığını nasıl bulacağınızı gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Konsol Çıktısı**
Lütfen yukarıdaki örnek kodun yürütülmesinden sonra oluşturulan konsol çıktısını aşağıda bulunan [örnek excel dosyası](5473373.xlsx) ile kontrol edin. Eğer [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) **false** ise, veri noktası Pasta'nın içindedir, eğer **true** ise, o zaman veri noktası Bar'ın içindedir.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
