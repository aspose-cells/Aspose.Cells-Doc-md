##Showing Cell Range as the Data Labels with Node.js via C++
Learn how to show a range of cells as data labels in charts using Aspose.Cells for Node.js via C++. Our guide will demonstrate how to link the labels to your data source and format them to provide accurate and meaningful information in your charts.
In Microsoft Excel 2013, you can display a cell range for data labels. Aspose.Cells for Node.js supports this feature.
## **Check-box to Show Cell Range as Data Labels**
To show the cell range as data labels in Microsoft Excel:
1. Select the series data labels and right-click to open the context menu.
1. Select **Format Data Labels**. Label options are displayed.
1. Select or clear the option **Label Contains - Value From Cells**.
The sample code below accesses a chart series data labels and sets the [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) property to **true** to select the **Label Contains - Value From Cells** option.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");
// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);
// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);
// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
