##Find Type of X and Y Values of Points in Chart Series with Node.js via C++
Learn how to determine the type of X and Y values in chart series points using Aspose.Cells for Node.js via C++. This guide explains the types of data values and how to access and work with them in your charts.
## **Possible Usage Scenarios**
Sometimes, you want to know the type of X and Y values of chart points in a series. Aspose.Cells for Node.js via C++ provides `ChartPoint.XValueType` and `ChartPoint.YValueType` properties that can be used for this purpose. Please note, you will have to call `Chart.calculate()` method before you can use these properties effectively.
## **Find Type of X and Y Values of Points in Chart Series**
The following sample code loads the [sample Excel file](64716905.xlsx) and accesses the first chart inside the first worksheet. It then calls the `Chart.calculate()` method and finds the type of X and Y values of the first chart point and prints them in the console. Please see the console output shown below for a reference.
## **Sample Code**
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
## **Console Output**
X Value Type: IsString
Y Value Type: IsNumeric
