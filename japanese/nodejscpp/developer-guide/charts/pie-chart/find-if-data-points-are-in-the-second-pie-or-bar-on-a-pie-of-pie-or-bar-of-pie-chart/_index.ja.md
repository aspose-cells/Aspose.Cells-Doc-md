---  
title: Node.jsとC++を使って、Data Pointsが円の第二の円または棒の中にあるかどうかを調べる方法  
linktitle: パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける  
description: Aspose.Cells for Node.js via C++を使って、データポイントが円の第二の円または棒の中にあるかを見つける方法を学びましょう。このガイドでは、複合チャートのセカンダリー円または棒にアクセスし識別する方法を示し、データを効果的に分析・操作できるようにします。  
keywords: Aspose.Cells for Node.js via C++、円の円、棒の円、セカンダリ円、セカンダリ棒、データ分析、データ操作。  
type: docs  
weight: 180  
url: /ja/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **可能な使用シナリオ**  
シリーズのデータポイントが*Pie of Pie*チャートの第二の円にあるか、または*Bar of Pie*チャートの棒にあるかを、Aspose.Cells for Node.js via C++を使って確認できます。 [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) プロパティを使用して判定してください。  

以下のサンプルコードと[サンプルExcelファイル](5115193.xlsx)をダウンロードし、そのコンソール出力を確認してください。Excelファイルを開くと、すべての値が10未満のデータポイントが*Bar of Pie*チャートの棒内にあることがわかります。  
## **パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける**  
次のサンプルコードは、*Pie of Pie*または*Bar of Pie*チャートの第二の円または棒内にデータポイントがあるかどうかを確認する方法を示しています。  

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
## **コンソール出力**  
上記のサンプルコードと[サンプルExcelファイル](5115193.xlsx)の実行後に生成されるコンソール出力を確認してください。 [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) が**false**の場合、そのデータポイントは円の中にあります。**true**の場合、そのデータポイントは棒の中にあります。  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
