---
title : "Extract Text from the Gear Type SmartArt Shape" 
description : "" 
weight : 12230 
toc : false
type: docs
url: /java/developerguide/drawingobjects/extract+text+from+the+gear+type+smartart+shape/
---

# Aspose.Cells for Java : Extract Text from the Gear Type SmartArt Shape


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Extract Text from the Gear Type SmartArt Shape](#extract-text-from-the-gear-type-smartart-shape)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells can extract text from the `Gear Type Smart Art Shape`. In order to do so, you should first convert `Smart Art Shape` to `Group Shape` using the [Shape.getResultOfSmartArt()](https://apireference.aspose.com/java/cells/com.aspose.cells/shape#getResultOfSmartArt()) method. Then you should get the array of all the `Individual Shapes` forming the Group Shape using the [GroupShape.getGroupedShapes()](https://apireference.aspose.com/java/cells/com.aspose.cells/groupshape#getGroupedShapes()) method. Finally, you can iterate all of the Individual Shapes one by one in a loop and extract their text using the [Shape.Text](https://apireference.aspose.com/java/cells/com.aspose.cells/shape#Text) property.

## Extract Text from the Gear Type SmartArt Shape

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/66948431/67338510.xlsx) that contains `Gear Type Smart Art Shape`. It then extracts the text from its individual shapes as discussed above. Please see the console output of the code given below for a reference.

## Sample Code

## Console Output

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

