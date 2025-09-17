##Extract Text from the Gear Type SmartArt Shape
## **Possible Usage Scenarios**
Aspose.Cells can extract text from the Gear Type Smart Art Shape. In order to do so, you should first convert Smart Art Shape to Group Shape using the [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art) method. Then you should get the array of all the Individual Shapes forming the Group Shape using the [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes) method. Finally, you can iterate all of the Individual Shapes one by one in a loop and extract their text using the [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) property.
## **Extract Text from the Gear Type SmartArt Shape**
The following sample code loads the [sample Excel file](67338483.xlsx) that contains Gear Type Smart Art Shape. It then extracts the text from its individual shapes as discussed above. Please see the console output of the code given below for a reference.
## **Sample Code**
## **Console Output**
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
