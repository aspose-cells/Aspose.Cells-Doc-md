---  
title: Определить, находятся ли точки данных на втором секторе или баре на круговой или секторной диаграмме с помощью Node.js через C++  
linktitle: Определите, находятся ли данные во второй круговой или столбчатой диаграмме на круговой диаграмме с обрывным или столбчатой диаграмме  
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для определения, находятся ли точки данных во втором секторе или баре на круговой диаграмме с секторами. Это руководство покажет, как идентифицировать и получить доступ к второму сектору или бару на сложной диаграмме, чтобы эффективно анализировать и управлять данными.  
keywords: Aspose.Cells for Node.js via C++, Круговая диаграмма с несколькими секторами, Баровая диаграмма с несколькими секторами, Второй сектор, Второй бар, Анализ данных, Манипуляция данными.  
type: docs  
weight: 180  
url: /ru/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Возможные сценарии использования**  
Вы можете определить, находятся ли точки данных серии во втором секторе на *Круговой диаграмме с несколькими секторами* или в баре на *Баровой диаграмме с несколькими секторами*, используя Aspose.Cells for Node.js via C++. Пожалуйста, используйте свойство [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) для определения этого.  

Пожалуйста, скачайте [пример файла Excel](5115193.xlsx), используемый в следующем примере кода, и ознакомьтесь с его выводом в консоль. Если откроете [пример файла Excel](5115193.xlsx), найдете все точки данных, которые меньше 10, внутри баров *Баровой диаграммы*, как показывает вывод в консоль.  
## **Определение того, находятся ли точки данных во втором сегменте или в столбце на круговой из кругов или столбчатой из кругов диаграмме**  
Следующий пример кода показывает, как определить, находятся ли точки данных во втором секторе или баре на *Круговой диаграмме с секторами* или *Баровой диаграмме*.  

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
## **Вывод в консоль**  
Пожалуйста, ознакомьтесь с выводом в консоль, сгенерированным после выполнения этого кода с [примером файла Excel](5115193.xlsx). Если [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) возвращает **false**, то точка находится внутри круга, а если **true**, то внутри баров.  

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

