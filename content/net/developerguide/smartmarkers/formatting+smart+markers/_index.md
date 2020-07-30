---
title : "Formatting Smart Markers" 
description : "" 
weight : 12306 
toc : false
type: docs
url: /net/developerguide/smartmarkers/formatting+smart+markers/
---

# Aspose.Cells for .NET : Formatting Smart Markers


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Copy Style Attribute](#copy-style-attribute)
    *   1.1 [Copying Styles from Cells with Smart Markers](#copying-styles-from-cells-with-smart-markers)
*   2 [Adding Custom Labels](#adding-custom-labels)
    *   2.1 [Introduction](#introduction)
    *   2.2 [Adding custom Labels to concatenate with the Subtotal rows in Smart Markers](#adding-custom-labels-to-concatenate-with-the-subtotal-rows-in-smart-markers)
{{< /panel >}}
 

## Copy Style Attribute

Sometimes, when using smart markers, you want to copy the style of the cell that contains the smart marker tags. You can use the `CopyStyle` attribute of the smart marker's tags for this purpose.

### Copying Styles from Cells with Smart Markers

This example uses a simple template Microsoft Excel file with two markers in the A2 and B2 cells. The marker pasted in cell B2 uses the `CopyStyle` attribute, whereas the marker in cell A2 does not. Apply simple formatting (for example, set the font color to **red** and set the cell fill color to **yellow**).

When executing the code, Aspose.Cells copies the formatting to all the records in column B but does not keep the formatting in column A.

## Adding Custom Labels

### Introduction

While working with Smart Markers' grouping data feature, sometimes you need to add your own custom labels to the summary row. You also want to concatenate the Column's name with that Label, e.g "Sub Total of Orders". Aspose.Cells provides you `Label` and `LabelPosition` attributes, so you may place your custom labels in the Smart Markers while concatenating with the Subtotal rows in grouping data.

### Adding custom Labels to concatenate with the Subtotal rows in Smart Markers

This example uses a [data file](https://docs2.aspose.com/cells/net/attachments/5017029/96927971.xlsx) and a [template file](https://docs2.aspose.com/cells/net/attachments/5017029/96927972.xlsx) with a few markers in the cells. When executing the code, Aspose.Cells adds some custom labels to the summary rows for the grouped data.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [LabelPosition-Files.zip](https://docs2.aspose.com/cells/net/attachments/5017029/50528291.zip) (application/zip)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Book1.xlsx](https://docs2.aspose.com/cells/net/attachments/5017029/96927971.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [SmartMarker\_Designer.xlsx](https://docs2.aspose.com/cells/net/attachments/5017029/96927972.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

