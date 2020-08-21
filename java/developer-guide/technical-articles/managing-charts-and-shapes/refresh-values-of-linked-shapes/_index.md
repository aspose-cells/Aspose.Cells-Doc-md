---
title: Refresh Values of Linked Shapes
type: docs
weight: 100
url: /java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}} 

Sometimes, you have a linked shape in your Excel file which is linked to some cell. In Microsoft Excel, changing the value of the linked cell also changes the value of linked shape. This also works fine with Aspose.Cells if you want to save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, then you will have to call [Worksheet.getShapes().updateSelectedValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/shapecollection#updateSelectedValue\(\)) method to refresh the value of the linked shape.

{{% /alert %}} 
#### **Example**
The following screenshot shows the source Excel file used in the sample code below. It has a linked **Picture 1** linked to cell A1. We will change the value of cell A1 with Aspose.Cells and then call [Worksheet.getShapes().updateSelectedValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/shapecollection#updateSelectedValue\(\)) method to refresh the value of **Picture 1** and save it in PDF format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

You can download the [source Excel file](5472956.xlsx) and the [output PDF](5472955.pdf) from the given links.
#### **Code**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
