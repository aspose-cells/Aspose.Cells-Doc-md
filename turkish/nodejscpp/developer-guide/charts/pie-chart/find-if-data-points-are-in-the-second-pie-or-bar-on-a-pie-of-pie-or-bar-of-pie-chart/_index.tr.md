---  
title: Bir Pasta veya Pasta Üzerinde İkinci Pasta veya Bar bulunan Veri Noktalarını Bulmak için Node.js ve C++ kullanma  
linktitle: Pasta Grafiklerinde veya Barlı Pasta veya Pasta Grafiğindeki İkinci Pastada veya Bar da Veri Noktalarını Bulma  
description: Aspose.Cells for Node.js via C++ kullanarak, pasta veya pasta üzerindeki bar grafiklerinde veri noktalarının ikinci pasta veya bar içinde olup olmadığını nasıl bulacağınızı öğrenin. Bu kılavuz, çoklu grafiklerde ikinci pasta veya barı tanımlama ve erişme yöntemlerini gösterecek ve veriyi etkin bir şekilde analiz etmenize olanak tanıyacaktır.  
keywords: Aspose.Cells for Node.js via C++, Pasta Puanı, Bar Pastası, İkinci Pasta, İkinci Bar, Veri Analizi, Veri İşleme.  
type: docs  
weight: 180  
url: /tr/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Olası Kullanım Senaryoları**  
Seri için veri noktalarının *Pasta Puanı* veya *Bar Puanı* grafiklerinde ikinci pasta veya bar içinde olup olmadığını bulmak için Aspose.Cells for Node.js via C++ kullanabilirsiniz. Lütfen [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) özelliğini kullanarak bunu belirleyin.  

Aşağıdaki örnek kodu indirerek ve kullanılan [örnek Excel dosyasını](5115193.xlsx) deneyerek, verilerin 10’dan az olan tüm noktalarının *Bar of Pie* grafiğinde olduğunu görebilirsiniz. Ayrıca bu bilgiler konsol çıktısında da gösterilir.  
## **Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma**  
Aşağıdaki örnek kod, *Pie of Pie* veya *Bar of Pie* grafiklerindeki verilerin ikinci pasta veya bar içinde olup olmadığını nasıl kontrol edeceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load source excel file containing Bar of Pie chart
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieBars.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart which is Bar of Pie chart and calculate it
const chart = worksheet.getCharts().get(0);
chart.calculate();

// Access the chart series
const series = chart.getNSeries().get(0);

/* 
* Print the data points of the chart series and 
* check its IsInSecondaryPlot property to determine 
* if data point is inside the bar or pie 
*/
for (let i = 0; i < series.getPoints().getCount(); i++) {
// Access chart point
const chartPoint = series.getPoints().get(i);

// Skip null values
if (chartPoint.get_YValue() === null) continue;

/* 
* Print the chart point value and see if it is inside bar or pie.
* If the IsInSecondaryPlot is true, then the data point is inside bar 
* otherwise it is inside the pie. 
*/
console.log("Value: " + chartPoint.get_YValue());
console.log("IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot());
console.log();
}
```  
## **Konsol Çıktısı**  
Yukarıdaki örnek kod ve [örnek Excel dosyası](5115193.xlsx) çalıştırıldıktan sonra üretilen konsol çıktısını görebilirsiniz. Eğer [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) **false** ise, veri noktası Pasta’nın içindedir; **true** ise, Veri Noktası Bar’ın içindedir.  

{{< highlight javascript >}}  
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

