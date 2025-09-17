##Set the Values Format Code of Chart Series with Node.js via C++
Learn how to set the values format code of chart series in Aspose.Cells for Node.js via C++. This guide will help you understand how to format your chart series data using the appropriate format code, allowing you to present your data accurately and professionally.
## **Possible Usage Scenarios**
You can set the values format code of chart series using the [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) property. This property is not only useful for the series which is based on the range inside the worksheet but also works well for the series created with an array of values.
## **Set the Values Format Code of Chart Series**
The following sample code adds a series in the empty chart which has no series before. It adds the series using the array of values. Once it adds the series, it formats it with the code $#,##0 using the [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) property and the number 10000 becomes $10,000. The screenshot shows the effect of code on the [sample Excel file](51740712.xlsx) and [output Excel file](51740713.xlsx) after execution.
![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Sample Code**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");
// Load the source Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Access first chart
const chart = worksheet.getCharts().get(0);
// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);
// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");
// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
