---  
title: Node.js ile C++ kullanarak Grafik Serilerindeki X ve Y Değerlerinin Türünü Bulma  
linktitle: Grafik Serisindeki X ve Y Değerleri Türünü Bul  
description: Aspose.Cells for Node.js via C++ kullanarak, grafik serisi noktalarında X ve Y değerlerinin türünü nasıl belirleyeceğinizi öğrenin. Bu kılavuz, veri değerlerinin türlerini ve grafiklerinizde bunlara nasıl erişeceğinizi ve çalışacağınızı açıklar.  
keywords: Aspose.Cells for Node.js, grafik çizimi, X değerleri, Y değerleri, veri türleri, erişim, çalışma, grafik serileri.  
type: docs  
weight: 150  
url: /tr/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **Olası Kullanım Senaryoları**  
Bazen, bir serideki grafik noktalarının X ve Y değerlerinin türünü bilmek istersiniz. Aspose.Cells for Node.js via C++, bunun için `ChartPoint.XValueType` ve `ChartPoint.YValueType` özelliklerini sağlar. Lütfen, bu özellikleri etkin kullanmadan önce `Chart.calculate()` metodunu çağırmanız gerektiğini unutmayın.  

## **Grafik Serisindeki X ve Y Değerleri Türünü Bul**  
Aşağıdaki örnek kod, [örnek Excel dosyasını](64716905.xlsx) yükler ve ilk çalışma sayfasındaki ilk grafiğe erişir. Ardından, `Chart.calculate()` metodunu çağırır ve ilk grafik noktasının X ve Y değerlerinin türünü belirler ve konsola yazdırır. Referans için aşağıdaki konsol çıktısına bakın.  

## **Örnek Kod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Load sample Excel file containing chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart.
const chart = worksheet.getCharts().get(0);

// Calculate chart data.
chart.calculate();

// Access first chart point in the first series.
const point = chart.getNSeries().get(0).getPoints().get(0);

// Print the types of X and Y values of chart point.
console.log("X Value Type: " + point.getXValueType());
console.log("Y Value Type: " + point.getYValueType());
```  

## **Konsol Çıktısı**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

