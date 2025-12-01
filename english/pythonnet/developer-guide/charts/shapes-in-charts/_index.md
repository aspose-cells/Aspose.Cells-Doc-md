---
title: Shapes in Charts
description: Learn how to use Aspose.Cells for Python via .NET to add controls and customize charts in Microsoft Excel. Our guide will demonstrate how to manipulate chart elements, adjust formatting, and enhance the overall appearance and usability of your charts.
keywords: Aspose.Cells for Python via .NET, Chart Controls, Chart Customization, Microsoft Excel, Chart Elements, Formatting.
type: docs
weight: 70
url: /python-net/controls-in-charts/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you need to insert drawing objects like labels, text boxes, pictures and so on into a chart. Aspose.Cells for Python via .NET can add the controls to a chart at runtime.

{{% /alert %}}

## **Adding Label Control to the Chart**

Labels provide a means for giving information to users about a spreadsheet's content.
Aspose.Cells for Python via .NET allows you to add and manipulate labels even into charts.

The [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) class provides a method named [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart), used to add a label control to a chart. Below is a list of the parameters used for the method:

- **top** – the vertical offset of the label from the upper left corner in units of 1/4000 of the chart area.
- **left** – the vertical offset of the label from the upper left corner in units of 1/4000 of the chart area.
- **height** – the height of the label, in units of 1/4000 of the chart area.
- **width** – the width of label, in units of 1/4000 of the chart area.

The method returns [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) object. The [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) class represents a label in the chart. It has some important members:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (property) – specifies a label's caption string.
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (property) – specifies the fill color attributes.

The following example shows how to add a label to the chart. The example uses a designer file (**exp_piechart.xls**) which has a chart in it. We use this file to insert a label into the chart. Below is the original code for adding a label to the chart. The following output is generated when executing the code.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **Adding TextBox Control to the Chart**

One way to highlight important information in a report is to use a text box. For example, enter text to highlight the company name or to indicate the geographic region with the highest sales. The [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) class provides a method named [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart), which is used to add a text box control to a chart. Following is the parameters list used for the method:

- **top** – the vertical offset of the text box from the upper left corner in units of 1/4000 of the chart area.
- **left** – the vertical offset of text box from the upper left corner in units of 1/4000 of the chart area.
- **height** – the height of text box, in units of 1/4000 of the chart area.
- **width** – the width of the text box, in units of 1/4000 of the chart area.

The method returns [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) object. The [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) class represents a text box in the chart.

The following example shows how to add a text box to a chart. The example uses the previous designer file (**exp_piechart.xls**) which has a chart in it. We use this file to insert a text box into the chart to show the chart title. Below is the original code for adding text box to the chart.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **Adding Picture to the Chart**

Aspose.Cells for Python via .NET allows you to insert images into a chart. For example, add a picture to emphasize or give more meaning to a chart or its contents, or insert a brand image file.

The [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) class provides a method named [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart), which is used to add a picture object to the chart. Following is the parameters list used for the method:

- **top** – the vertical offset of the picture from the upper left corner in units of 1/4000 of the chart area.
- **left** – the vertical offset of the picture from the upper left corner in units of 1/4000 of the chart area.
- **stream** – a stream object which contains the image data.
- **widthScale** – the scale of image width, a percentage value.
- **heightScale** – the scale of image height, a percentage value.

The method returns an [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) object. The [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) class represents a picture object in the chart.

The following example shows how to add a picture to the chart. The example utilizes the previous designer file (**exp_piechart.xls**) which has a chart in it. We use this file to insert an image into the chart. Below is the original code for adding picture to the chart.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **Adding Checkbox in the Chart**

Aspose.Cells for Python via .NET allows you to insert checkboxes into a chart sheet by using [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype) enumeration. The following example demonstrates adding a checkbox to a chart sheet.

The following image shows the chart sheet with the checkbox in the output file.

![todo:image_alt_text](controls-in-charts_1.jpg)

The [output file](101089316.xlsx) generated by the following code snippet is attached for your reference.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **Advance topics**
- [Add WordArt Watermark to Chart](/cells/python-net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="python-net" >}}
