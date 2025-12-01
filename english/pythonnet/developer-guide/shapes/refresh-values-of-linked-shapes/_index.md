---
title: Refresh Values of Linked Shapes
type: docs
weight: 3200
url: /python-net/refresh-values-of-linked-shapes/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you have a linked shape in your Excel file which is linked to some cell. In Microsoft Excel, changing the value of the linked cell also changes the value of the linked shape. This also works fine with Aspose.Cells for Python via .NET if you want to save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, then you will have to call [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) method to refresh the value of the linked shape.

{{% /alert %}}

## Example

The following screenshot shows the source Excel file used in the sample code below. It has a linked picture linked to cells A1 to E4. We will change the value of cell B4 with Aspose.Cells for Python via .NET and then call [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) method to refresh the value of the picture and save it in PDF format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

You can download the [source Excel file](95584291.xlsx) and the [output PDF](95584292.pdf) from the given links.

### C# code to refresh the values of linked shapes

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
