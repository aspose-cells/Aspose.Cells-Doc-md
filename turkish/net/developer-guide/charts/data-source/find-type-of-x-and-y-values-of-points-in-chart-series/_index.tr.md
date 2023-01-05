---
title: Grafik Serisindeki Noktaların X ve Y Değerlerinin Türünü Bulma
type: docs
weight: 150
url: /tr/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Olası Kullanım Senaryoları**
Bazen bir dizideki grafik noktalarının X ve Y değerlerinin türünü bilmek istersiniz. Aspose.Cells, bu amaçla kullanılabilecek ChartPoint.XValueType ve ChartPoint.YValueType özelliklerini sağlar. Bu özellikleri etkili bir şekilde kullanabilmeniz için önce Chart.Calculate() yöntemini çağırmanız gerekeceğini lütfen unutmayın.
## **Grafik Serisindeki Noktaların X ve Y Değerlerinin Türünü Bulma**
 Aşağıdaki örnek kod,[örnek excel dosyası](64716905.xlsx) ve ilk çalışma sayfasındaki ilk grafiğe erişir. Daha sonra Chart.Calculate() yöntemini çağırır ve ilk grafik noktasının X ve Y değerlerinin türünü bulur ve bunları konsolda yazdırır. Lütfen referans için aşağıda gösterilen konsol çıktısına bakın.
## **Basit kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **Konsol Çıkışı**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
