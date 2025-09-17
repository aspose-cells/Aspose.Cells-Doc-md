##Get Worksheet of the Chart with Node.js via C++
Learn how to retrieve the worksheet associated with an Excel chart using Aspose.Cells for Node.js via C++. Access and manipulate the underlying data of the chart efficiently.
Sometimes, you want to access a worksheet from a chart's reference. Aspose.Cells provides the [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) property which returns the reference of the worksheet that contains the chart.
The following example shows how to use the [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) property. The code first prints the name of the worksheet, then accesses the first chart on the worksheet. It then prints the worksheet name again, using the [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) property.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));
// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);
// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());
// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);
// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```
Below is the console output that the sample code results in. As you can see, it prints the same worksheet name both times.
Sheet Name: Portfolio
Chart's Sheet Name: Portfolio
