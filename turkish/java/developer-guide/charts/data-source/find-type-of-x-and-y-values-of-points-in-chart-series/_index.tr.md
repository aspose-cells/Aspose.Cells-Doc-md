---
title: Grafik Serisindeki Noktaların X ve Y Değerlerinin Türünü Bulma
type: docs
weight: 110
url: /tr/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Olası Kullanım Senaryoları**

Bazen bir dizideki grafik noktalarının X ve Y değerlerinin türünü bilmek istersiniz. Aspose.Cells sağlar[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)ve[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)Bu amaçla kullanılabilecek özellikler. Lütfen dikkat, aramanız gerekecek[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) yöntemi, bu özellikleri etkin bir şekilde kullanabilmeniz için.

## **Grafik Serisindeki Noktaların X ve Y Değerlerinin Türünü Bulma**

Aşağıdaki örnek kod,[örnek excel dosyası](64716920.xlsx)ve ilk çalışma sayfasındaki ilk grafiğe erişir. Daha sonra çağırır[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()yöntemini kullanır ve ilk grafik noktasının X ve Y değerlerinin türünü bulur ve bunları konsolda yazdırır. Lütfen referans için aşağıda gösterilen konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
