---
title: Grafik Serisindeki X ve Y Değerleri Türünü Bul
description: Aspose.Cells for Python via .NET kullanarak grafik serisi noktalarında X ve Y değerlerinin türünü nasıl belirleyeceğinizi öğrenin. Rehberimiz, farklı veri değerleri türlerini açıklayacak ve grafiklerinizde bunlara nasıl erişip çalışacağınızı gösterecek.
keywords: Aspose.Cells for Python via .NET, grafikleme, X değerleri, Y değerleri, veri türleri, erişim, çalışma, grafik serisi.
type: docs
weight: 150
url: /tr/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Olası Kullanım Senaryoları**
Bazen, bir serideki grafik noktalarının X ve Y değerlerinin türünü bilmek istersiniz. Aspose.Cells for Python via .NET, bu amaçla kullanılabilecek [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) ve [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/) özelliklerini sağlar. Lütfen dikkate alın, bu özellikleri etkili bir şekilde kullanmadan önce [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) yöntemini çağırmanız gerekir.

## **Grafik Serisindeki X ve Y Değerleri Türünü Bul**
Aşağıdaki örnek kod, [örnek Excel dosyasını](64716905.xlsx) yükler ve ilk çalışma sayfasındaki ilk grafiğe erişir. Ardından [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) metodunu çağırır ve ilk grafik noktasının X ve Y değerlerinin türünü bulur ve bunları konsolda yazdırır. Lütfen aşağıdaki konsol çıktısını referans olarak görün.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
