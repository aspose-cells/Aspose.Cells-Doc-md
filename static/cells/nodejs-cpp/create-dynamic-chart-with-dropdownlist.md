##How to create Dynamic Chart with Dropdownlist using Node.js via C++
Learn how to create a dynamic chart that updates based on a drop-down list selection using Aspose.Cells for Node.js via C++. Our step-by-step guide will demonstrate how to integrate a drop-down list into your chart for flexible data visualization.
## **Possible Usage Scenarios**
A Dynamic Chart with Dropdownlist in Excel is a powerful tool that allows users to create interactive charts that can dynamically update based on the selected data. This feature is particularly useful in situations where there is a need to analyze multiple datasets or compare various scenarios.
One common application of a Dynamic Chart with Dropdownlist is in financial analysis. For example, a company may have multiple sets of financial data for different years or departments. By using a dropdown list, users can select the specific dataset they want to analyze, and the chart will automatically update to display the corresponding information. This allows for easy comparison and identification of trends or patterns.
Another application is in sales and marketing. A company may have sales data for different products or regions. With a Dynamic Chart with Dropdownlist, users can choose a specific product or region from the dropdown list, and the chart will dynamically update to show the sales performance for the selected option. This helps in identifying the top-performing areas or products and making data-driven decisions.
In summary, a Dynamic Chart with Dropdownlist in Excel provides a flexible and interactive way to visualize and analyze data. It is valuable in situations where there is a need to compare multiple datasets or explore different scenarios, making it a versatile tool for financial analysis, sales and marketing, and many other applications.
## **Use Aspose Cells to create Dynamic Chart with Dropdownlist**
In the next paragraphs, we will show you how to create Dynamic Chart with Dropdownlist using Aspose.Cells for Node.js via C++. We'll show you the code for the example, as well as the Excel file created with this code.
## **Sample Code**
The following sample code will generate the [Dynamic Chart with Dropdownlist File](DynamicChartWithDropdownlist.xlsx).
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// Your local test path
const localPath = "";
// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);
// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");
// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1;
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}
// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);
// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");
// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");
// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");
// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```
## **Notes**
In the generated file, the chart will dynamically count the data for the selected month. This is done using the "OFFSET" formula in the sample code:
```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```
You can try changing the dropdown list value in cell "Sheet1!$A$10", and you will see the dynamic change of the chart. Now we have created a dynamic chart with dropdownlist using Aspose.Cells successfully.
