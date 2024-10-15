---
title: Formatting Smart Markers
type: docs
weight: 20
url: /java/formatting-smart-markers/
---

## **Copy Style Attribute**
Sometimes, when using smart markers, you want to copy the style of the cell that contains the smart marker tags. You can use the CopyStyle attribute of the smart marker's tags for this purpose.
### **Copying Styles from Cells with Smart Markers**
This example uses a simple template Microsoft Excel file with two markers in the A2 and B2 cells. The marker pasted in cell B2 uses the CopyStyle attribute, whereas the marker in cell A2 does not. Apply simple formatting (for example, set the font color to **red** and set the cell fill color to **yellow**).

This example uses a [template file](template1.xlsx) with a few markers in the cells.When executing the code, Aspose.Cells copies the formatting to all the records in column B but does not keep the formatting in column A.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **Adding Custom Labels**
### **Introduction**
While working with Smart Markers' grouping data feature, sometimes you need to add your own custom labels to the summary row. You also want to concatenate the Column's name with that Label, e.g "Sub Total of Orders". Aspose.Cells provides you Label and LabelPosition attributes, so you may place your custom labels in the Smart Markers while concatenating with the Subtotal rows in grouping data.
### **Adding custom Labels to concatenate with the Subtotal rows in Smart Markers**
This example uses a [template file](template.xlsx) with a few markers in the cells. When executing the code, Aspose.Cells adds some custom labels to the summary rows for the grouped data.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
{{< app/cells/assistant language="java" >}}