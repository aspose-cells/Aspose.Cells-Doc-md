---
title: 利用Node.js通过C++在图表中添加形状
linktitle: 图表中的形状
description: 学习如何使用Aspose.Cells for Node.js via C++在Microsoft Excel中添加控件并自定义图表。本指南演示如何操作图表元素、调整格式以及增强图表的整体外观和可用性。
keywords: Aspose.Cells for Node.js via C++，图表控件，图表自定义，Microsoft Excel，图表元素，格式化。
type: docs
weight: 70
url: /zh/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
有时需要在图表中插入标签、文本框、图片等绘图对象。Aspose.Cells 可以在运行时向图表中添加控件。
{{% /alert %}}

## **向图表添加标签控件**

标签提供了向用户提供关于电子表格内容的信息的方法。Aspose.Cells 允许您甚至在图表中添加和操作标签。

[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/)类提供了一个名为[**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-)的方法，用于向图表添加标签控件。以下是该方法使用的参数列表：

- **top** – 以图表区域的1/4000单位为垂直偏移的标签。
- **left** – 以图表区域的1/4000单位为水平偏移的标签。
- **height** – 标签的高度，以图表区域的1/4000单位为单位。
- **width** – 标签的宽度，单位为图表区域的1/4000。

该方法返回[**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/)对象。[**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/)类代表图表中的标签，具有一些重要成员：

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--)（属性）– 指定标签的标题字符串。
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--)（属性）– 指定填充颜色属性。

以下示例演示如何向图表添加标签。示例使用了一个设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用此文件向图表插入标签。以下是添加标签到图表的原始代码。执行该代码时生成以下输出。

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

## **将文本框控件添加到图表**

在报告中突出显示重要信息的一种方法是使用文本框。例如，输入文本以突出显示公司名称或指示销售额最高的地理区域。[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/)类提供了一个名为[**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-)的方法，用于向图表添加文本框控件。以下是该方法使用的参数列表：

- **top** – 文本框与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 文本框距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **height** – 文本框的高度，单位为图表区域的1/4000。
- **width** – 文本框的宽度，单位为图表区域的1/4000。

该方法返回一个 [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) 对象。[**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) 类表示图表中的文本框。

以下示例显示了如何向图表添加文本框。该示例使用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入文本框以显示图表标题。以下是添加文本框到图表的原始代码。

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

## **向图表添加图片**

Aspose.Cells 允许您将图像插入到图表中。例如，添加一张图片以强调或赋予图表或其内容更多的含义，或者插入一个品牌图片文件。

[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) 类提供了一个名为 [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-) 的方法，用于向图表添加图片对象。以下是该方法使用的参数列表。

- **top** – 图片与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 图片与图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **stream** - 一个包含图像数据的流对象。
- **widthScale** - 图像宽度的比例值，以百分比表示。
- **heightScale** - 图像高度的比例值，以百分比表示。

该方法返回一个 [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) 对象。[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) 类表示图表中的图片对象。

以下示例显示了如何向图表添加图片。该示例利用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入图片。以下是添加图片到图表的原始代码。

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

## **在图表中添加复选框**

Aspose.Cells 允许您通过使用 [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/) 枚举向图表工作表中插入复选框。以下示例演示了向图表工作表添加复选框。

以下图像显示了输出文件中带有复选框的图表工作表。

![todo:image_alt_text](controls-in-charts_1.jpg)

以下代码片段生成的[输出文件](101089316.xlsx)已附上，供您参考。

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

## **高级主题**
- [向图表添加艺术字水印](/cells/zh/nodejs-cpp/add-wordart-watermark-to-chart/)

{{< app/cells/assistant language="nodejs-cpp" >}}
