---
title: Grafik Serisindeki X ve Y Değerleri Türünü Bul
description: Aspose.Cells for .NET ile ChartPoint.XValueType ve ChartPoint.YValueType özelliklerini kullanarak grafik serisi noktalarındaki X ve Y değerlerinin türünü belirlemenin nasıl yapıldığını öğrenin. Rehberimiz, farklı veri değerlerini açıklayacak ve bunlarla nasıl erişileceğinizi ve çalıştıracağınızı gösterecektir.
keywords: Aspose.Cells for .NET, grafik, X değerleri, Y değerleri, veri türleri, erişim, işlem, grafik serisi.
type: docs
weight: 150
url: /tr/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Olası Kullanım Senaryoları**
Bazı durumlarda, bir serideki grafik noktalarının X ve Y değerlerinin türünü bilmek isteyebilirsiniz. Aspose.Cells, bu amaçla kullanılabilecek ChartPoint.XValueType ve ChartPoint.YValueType özelliklerini sağlar. Lütfen unutmayın, bu özellikleri etkili bir şekilde kullanmadan önce Chart.Calculate() yöntemini çağırmanız gerekecektir.
## **Grafik Serisindeki X ve Y Değerleri Türünü Bul**
Aşağıdaki örnek kod, [örnek Excel dosyasını](64716905.xlsx) yükler ve ilk çalışma sayfasındaki ilk grafik erişir. Daha sonra Chart.Calculate() yöntemini çağırır ve ilk grafik noktasının X ve Y değerlerinin türünü bulur ve bunları konsola yazdırır. Referans için aşağıda gösterilen konsol çıktısına bakınız.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
