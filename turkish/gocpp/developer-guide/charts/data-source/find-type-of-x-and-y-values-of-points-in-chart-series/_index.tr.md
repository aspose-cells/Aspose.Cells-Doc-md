---
title: Grafik Serisinde Noktaların X ve Y Değerleri Türünü Golang ile C++ kullanarak Bulma
linktitle: Grafik Serisindeki X ve Y Değerleri Türünü Bul
description: Aspose.Cells for C++ kullanarak grafik serisi noktalarındaki X ve Y değerlerinin türünü nasıl belirleyeceğinizi öğrenin. Kılavuzumuz, farklı veri türlerini açıklayacak ve bu verilere nasıl erişip çalışacağınızı gösterecek.
keywords: Aspose.Cells for C++, grafik çizimi, X değerleri, Y değerleri, veri türleri, erişim, çalışma, grafik serisi.
type: docs
weight: 150
url: /tr/go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Olası Kullanım Senaryoları**
Bazen, bir serideki grafik noktalarının X ve Y değerlerinin türünü bilmek istersiniz. Aspose.Cells, bu amaçla `ChartPoint::get_XValueType` ve `ChartPoint::get_YValueType` metodlarını sağlar. Lütfen unutmayın, bu özellikleri etkili kullanmadan önce `Chart::Calculate()` metodunu çağırmanız gerekir.

## **Grafik Serisindeki X ve Y Değerleri Türünü Bul**
 Aşağıdaki örnek kod, [örnek Excel dosyasını](64716905.xlsx) yükler ve ilk sayfadaki ilk grafiğe erişir. Ardından `Chart::Calculate()` metodunu çağırır, ilk grafik noktasının X ve Y değerlerinin türünü bulur ve bunları konsola yazdırır. Referans için aşağıdaki konsol çıktısına bakın.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}
## **Konsol Çıktısı**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
