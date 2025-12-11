---
title: Refresh Values of Linked Shapes
type: docs
weight: 3000
url: /java/refresh-values-of-linked-shapes/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you have a linked shape in your Excel file that is linked to a cell. In Microsoft Excel, changing the value of the linked cell also changes the value of the linked shape. This also works fine with Aspose.Cells when you save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, you will have to call [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) method to refresh the value of the linked shape.

{{% /alert %}}

## Example

The following screenshot shows the source Excel file used in the sample code below. It contains a linked **Picture 1** that is linked to cell A1. We will change the value of cell A1 with Aspose.Cells and then call [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) method to refresh the value of **Picture 1** and save it in PDF format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

You can download the [source Excel file](5472956.xlsx) and the [output PDF](5472955.pdf) from the given links.

### Java code to refresh the values of linked shapes

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
{{< app/cells/assistant language="java" >}}
