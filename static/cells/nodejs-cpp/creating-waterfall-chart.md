##How to create waterfall chart with Node.js via C++
Create waterfall charts in Excel with Node.js and Aspose.Cells for Node.js via C++.
A waterfall chart is a special type of chart that is normally used to demonstrate how the starting position either increases or decreases. Microsoft Excel has many predefined chart types, including column, line, pie, bar, radar, etc., but the waterfall chart is beyond the basic graphs and can be created using the existing chart types with little or more customization.
Aspose.Cells APIs allow creating a waterfall chart with the help of the line chart. The API also allows customizing the chart appearance to give it the shape of the waterfall by setting the [**Series.getUpBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getUpBars--) & [**Series.getDownBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getDownBars--) properties.
Below provided code snippet demonstrates the usage of Aspose.Cells for Node.js via C++ to create a waterfall chart from scratch.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();
// Retrieve the first Worksheet in Workbook
const worksheet = workbook.getWorksheets().get(0);
// Retrieve the Cells of the first Worksheet
const cells = worksheet.getCells();
// Input some data which chart will use as source
cells.get("A1").putValue("Previous Year");
cells.get("A2").putValue("January");
cells.get("A3").putValue("March");
cells.get("A4").putValue("August");
cells.get("A5").putValue("October");
cells.get("A6").putValue("Current Year");
cells.get("B1").putValue(8.5);
cells.get("B2").putValue(1.5);
cells.get("B3").putValue(7.5);
cells.get("B4").putValue(7.5);
cells.get("B5").putValue(8.5);
cells.get("B6").putValue(3.5);
cells.get("C1").putValue(1.5);
cells.get("C2").putValue(4.5);
cells.get("C3").putValue(3.5);
cells.get("C4").putValue(9.5);
cells.get("C5").putValue(7.5);
cells.get("C6").putValue(9.5);
// Add a Chart of type Waterfall in same worksheet as of data
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Waterfall, 4, 4, 25, 13);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(idx);
// Add Series
chart.getNSeries().add("$B$1:$C$6", true);
// Add Category Data
chart.getNSeries().setCategoryData("$A$1:$A$6");
// Series has Up Down Bars
chart.getNSeries().get(0).setHasUpDownBars(true);
// Set the colors of Up and Down Bars
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Red);
// Make both Series Lines invisible
chart.getNSeries().get(0).getBorder().setIsVisible(false);
chart.getNSeries().get(1).getBorder().setIsVisible(false);
// Set the Plot Area Formatting Automatic
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.Automatic);
// Delete the Legend
chart.getLegend().getLegendEntries().get(0).setIsDeleted(true);
chart.getLegend().getLegendEntries().get(1).setIsDeleted(true);
// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
## Related Articles
- [Creating Charts](https://docs.aspose.com/cells/nodejs-cpp/creating-charts/)
- [Customizing Charts](https://docs.aspose.com/cells/nodejs-cpp/customizing-charts/)
