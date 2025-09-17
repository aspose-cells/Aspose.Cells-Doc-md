##Shapes in Charts with Node.js via C++
Learn how to use Aspose.Cells for Node.js via C++ to add controls and customize charts in Microsoft Excel. This guide demonstrates how to manipulate chart elements, adjust formatting, and enhance the overall appearance and usability of your charts.
Sometimes you need to insert drawing objects like labels, text boxes, pictures and so on into a chart. Aspose.Cells can add the controls to a chart at runtime.
## **Adding Label Control to the Chart**
Labels provide a means for giving information to users about a spreadsheet's content. Aspose.Cells allows you to add and manipulate labels even into charts.
The [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) class provides a method named [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-), used to add a label control to a chart. Below is a list of the parameters used for the method:
- **top** – the vertical offset of the label from the upper left corner in units of 1/4000 of the chart area.
- **left** – the vertical offset of the label from the upper left corner in units of 1/4000 of the chart area.
- **height** – the height of the label, in units of 1/4000 of the chart area.
- **width** – the width of label, in units of 1/4000 of the chart area.
The method returns [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) object. The [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) class represents a label in the chart. It has some important members:
- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (property) – specifies a label's caption string.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (property) – specifies the fill color attributes.
The following example shows how to add a label to the chart. The example uses a designer file (**exp_piechart.xls**) which has a chart in it. We use this file to insert a label into the chart. Below is the original code for adding a label to the chart. The following output is generated when executing the code.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));
// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);
// Add a new label to the chart.
const label = chart.getShapes().addLabelInChart(100, 100, 350, 900);
// Set the caption of the label.
label.setText("A Label In Chart");
// Set the Placement Type, the way the Label is attached to the cells.
label.setPlacement(AsposeCells.PlacementType.FreeFloating);
// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```
## **Adding TextBox Control to the Chart**
One way to highlight important information in a report is to use a text box. For example, enter text to highlight the company name or to indicate the geographic region with the highest sales. The [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) class provides a method named [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), which is used to add a text box control to a chart. Following is the parameters list used for the method:
- **top** – the vertical offset of the text box from the upper left corner in units of 1/4000 of the chart area.
- **left** – the vertical offset of text box from the upper left corner in units of 1/4000 of the chart area.
- **height** – the height of text box, in units of 1/4000 of the chart area.
- **width** – the width of the text box, in units of 1/4000 of the chart area.
The method returns [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) object. The [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) class represents a text box in the chart.
The following example shows how to add a text box to a chart. The example uses the previous designer file (**exp_piechart.xls**) which has a chart in it. We use this file to insert a text box into the chart to show the chart title. Below is the original code for adding text box to the chart.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));
// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);
// Add a new textbox to the chart.
const textbox0 = chart.getShapes().addTextBoxInChart(100, 1100, 350, 2550);
// Fill the text.
textbox0.setText("Sales By Region");
// Get the textbox text frame.
// const textframe0 = textbox0.getTextFrame();
// Set the textbox to adjust it according to its contents.
// textframe0.setAutoSize(true);
// Set the font color.
textbox0.getFont().setColor(AsposeCells.Color.Maroon);
// Set the font to bold.
textbox0.getFont().setIsBold(true);
// Set the font size.
textbox0.getFont().setSize(14);
// Set font attribute to italic.
textbox0.getFont().setIsItalic(true);
// Get the fill format of the textbox.
const fillformat = textbox0.getFill();
// Get the line format type of the textbox.
const lineformat = textbox0.getLine();
// Set the line weight.
lineformat.setWeight(2);
// Set the dash style to solid.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);
// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```
## **Adding Picture to the Chart**
Aspose.Cells allows you to insert images into a chart. For example, add a picture to emphasize or give more meaning to a chart or its contents, or insert a brand image file.
The [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) class provides a method named [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), which is used to add a picture object to the chart. Following is the parameters list used for the method:
- **top** – the vertical offset of the picture from the upper left corner in units of 1/4000 of the chart area.
- **left** – the vertical offset of the picture from the upper left corner in units of 1/4000 of the chart area.
- **stream** – a stream object which contains the image data.
- **widthScale** – the scale of image width, a percentage value.
- **heightScale** – the scale of image height, a percentage value.
The method returns an [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) object. The [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) class represents a picture object in the chart.
The following example shows how to add a picture to the chart. The example utilizes the previous designer file (**exp_piechart.xls**) which has a chart in it. We use this file to insert an image into the chart. Below is the original code for adding picture to the chart.
```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart_shapes.xls"));
// Get an image file to the stream.
const stream = fs.readFileSync(path.join(dataDir, "logo.jpg"));
// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(0);
const chart = sheet.getCharts().get(0);
// Add a new picture to the chart.
const pic0 = chart.getShapes().addPictureInChart(50, 50, stream, 40, 40);
// Get the lineformat type of the picture.
const lineformat = pic0.getLine();
// Set the dash style.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);
// Set the line weight.
lineformat.setWeight(4);
// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```
## **Adding Checkbox in the Chart**
Aspose.Cells allows you to insert checkboxes into a chart sheet by using [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/) enumeration. The following example demonstrates adding a checkbox to a chart sheet.
The following image shows the chart sheet with the checkbox in the output file.
![todo:image_alt_text](controls-in-charts_1.jpg)
The [output file](101089316.xlsx) generated by the following code snippet is attached for your reference.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a chart to the worksheet
const index = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet = workbook.getWorksheets().get(index);
sheet.getCharts().addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);
sheet.getCharts().get(0).getNSeries().add("{1,2,3}", false);
// Add checkbox to the chart.
sheet.getCharts().get(0).getShapes().addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);
sheet.getCharts().get(0).getShapes().get(0).setText("CheckBox 1");
// Save the excel file.
workbook.save(outputDir +"InsertCheckboxInChartSheet_out.xlsx");
```
## **Advance topics**
- [Add WordArt Watermark to Chart](https://docs.aspose.com/cells/nodejs-cpp/add-wordart-watermark-to-chart/)
