---
title: Grafik Serisindeki X ve Y Değerleri Türünü Bul
type: docs
weight: 110
url: /tr/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, bir serideki grafik noktalarının X ve Y değerlerinin türünü bilmek isteyebilirsiniz. Aspose.Cells, bu amaçla kullanılabilecek [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) ve [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType) özelliklerini sağlar. Lütfen unutmayın, bu özellikleri etkili bir şekilde kullanmadan önce [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) metodunu çağırmanız gerekecektir.

## **Grafik Serisindeki X ve Y Değerleri Türünü Bul**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716920.xlsx) yükler ve ilk çalışsayfadaki ilk grafiğe erişir. Ardından [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) metodunu çağırır ve ilk grafik noktasının X ve Y değerlerinin türünü bulur ve bunları konsola yazdırır. Lütfen bir referans için aşağıdaki konsol çıktısını görün.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
