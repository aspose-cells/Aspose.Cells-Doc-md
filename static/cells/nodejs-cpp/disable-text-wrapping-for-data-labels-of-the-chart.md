##Disable Text Wrapping for Data Labels of the Chart with Node.js via C++
Learn how to disable text wrapping for data labels in charts using Aspose.Cells for Node.js via C++. Our guide will show you how to prevent long labels from overlapping and provide more readable and clear chart displays.
Microsoft Excel 2013 allows users to wrap or unwrap text inside the Data Labels of the Chart. By default, the text inside the Data Labels of the Chart is in the wrapped state.
Aspose.Cells provides a [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--) property which you can set true or false to enable or disable text wrapping of data labels respectively.
The below code sample shows how to disable text wrapping for the data labels of the chart.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);
// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);
// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
