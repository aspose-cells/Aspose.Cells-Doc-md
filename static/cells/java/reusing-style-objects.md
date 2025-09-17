##Reusing Style Objects
Reusing style objects can save memory and make the program execute faster.
To apply some formatting to a large range of cells in a worksheet:
1. Create a style object.
1. Specify the attributes.
1. Apply the style to the cells in the range.
The same process as discussed above could also be accomplished as follow.
Because the [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) and [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) methods use a lot less memory and are efficient, the older *Cell.getStyle()* property which consumed a lot of unnecessary memory, was removed with the release of *Aspose.Cells 7.1.0*.
