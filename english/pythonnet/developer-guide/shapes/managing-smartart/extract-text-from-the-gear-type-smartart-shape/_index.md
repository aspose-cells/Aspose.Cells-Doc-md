---
title: Extract Text from the Gear Type SmartArt Shape
type: docs
weight: 500
url: /python-net/extract-text-from-the-gear-type-smartart-shape/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells can extract text from the Gear Type SmartArt shape. In order to do so, you should first convert the SmartArt shape to a Group shape using the [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art) method. Then you should get the array of all the individual shapes forming the Group shape using the [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes) method. Finally, you can iterate over all the individual shapes one by one in a loop and extract their text using the [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) property.

## **Extract Text from the Gear Type SmartArt Shape**

The following sample code loads the [sample Excel file](67338483.xlsx) that contains a Gear Type SmartArt shape. It then extracts the text from its individual shapes as discussed above. Please see the console output of the code given below for reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **Console Output**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
