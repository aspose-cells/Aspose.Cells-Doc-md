---
title: Extract Text from the Gear Type SmartArt Shape
type: docs
weight: 500
url: /net/extract-text-from-the-gear-type-smartart-shape/
---

## **Possible Usage Scenarios**

Aspose.Cells can extract text from the Gear Type Smart Art Shape. In order to do so, you should first convert Smart Art Shape to Group Shape using the [**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) method. Then you should get the array of all the Individual Shapes forming the Group Shape using the [**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) method. Finally, you can iterate all of the Individual Shapes one by one in a loop and extract their text using the [**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) property.

## **Extract Text from the Gear Type SmartArt Shape**

The following sample code loads the [sample Excel file](67338483.xlsx) that contains Gear Type Smart Art Shape. It then extracts the text from its individual shapes as discussed above. Please see the console output of the code given below for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Console Output**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
