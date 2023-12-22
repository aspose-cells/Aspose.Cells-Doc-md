---
title: Veri Noktalarının Pasta Pastası veya Pasta Çubuğu Grafiğindeki İkinci Pasta veya Çubukta olup olmadığını bulma
description: Veri noktalarının bir pasta pastası veya pasta çubuğu grafiğindeki ikinci pasta veya çubukta olup olmadığını bulmak için Aspose.Cells for .NET'i nasıl kullanacağınızı öğrenin. Kılavuzumuz, verileri etkili bir şekilde analiz etmenize ve değiştirmenize olanak tanıyacak şekilde, bileşik bir grafikte ikincil pasta veya çubuğun nasıl tanımlanacağını ve erişileceğini gösterecektir.
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /tr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **Olası Kullanım Senaryoları**
 Serinin veri noktalarının ikinci pastada olup olmadığını şu adreste bulabilirsiniz:*Turta Turtası* grafikte veya çubuğunda*Pasta Barı* Aspose.Cells numaralı tabloyu kullanın. Lütfen[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)bunu belirleyecek özellik.

 Lütfen indirin[örnek excel dosyası](5115193.xlsx)aşağıdaki örnek kodda kullanıldı ve konsol çıktısına bakın. Eğer açarsan[örnek excel dosyası](5115193.xlsx) 10'dan küçük tüm veri noktalarının çubuğun içinde olduğunu göreceksiniz.*Pasta Barı*grafik konsol çıktısında da gösterildiği gibi.
##  **Veri Noktalarının Pasta Pastası veya Pasta Çubuğu Grafiğindeki İkinci Pasta veya Çubukta olup olmadığını bulma**
 Aşağıdaki örnek kod, veri noktalarının bir veri kümesindeki ikinci pastada mı yoksa çubukta mı bulunduğunun nasıl bulunacağını gösterir.*Turta Turtası* veya*Pasta Barı*çizelge.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **Konsol Çıkışı**
 Lütfen yukarıdaki örnek kodun çalıştırılmasından sonra oluşturulan aşağıdaki konsol çıktısına bakın.[örnek excel dosyası](5115193.xlsx) . Eğer[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)*yanlış** ise veri noktası Pastanın içindedir veya *doğru** ise veri noktası Çubuğun içindedir.



{{< highlight "java" >}}

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
