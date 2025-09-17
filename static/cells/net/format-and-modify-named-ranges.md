##Format and Modify Named Ranges
## **Format Ranges**
### **Setting Background Color and Font Attributes to a Named Range**
To apply formatting, define a [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object to specify the style settings and apply it to the [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) object.
The following example shows how to set the solid fill color (shading color) with font settings to a range.
### **Adding Borders to a Named Range**
It is possible to add borders to a range of cells instead of just a single cell. The [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) object provides a [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) method that takes the following parameters to add a border to the range of cells:
- Border type, the type of border, selected from the [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) enumeration.
- Line style, the line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) enumeration.
- Color, the line color, selected from the Color enumeration.
The following example shows how to set an outline border to a range.
The following example shows how to set borders around each cell in the range.
## **Rename a Named Range**
Aspose.Cells allows you to rename a named range for your need. You may get the named range and rename it by using [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text) attribute. The following example shows how to rename a named range.
## **Union of Ranges**
Aspose.Cells provides [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) method to take the union for ranges, the method returns an [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8) object. The following example shows how to take union for ranges.
## **Intersection of Ranges**
Aspose.Cells provides the [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) method to intersect two ranges. The method returns a [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) object. To check whether a range intersects another range, use the [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) method that returns a Boolean value. The following example shows how to intersect the ranges.
## **Merge Cells in the Named Range**
Aspose.Cells provides [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) method to merge the cells in the range. The following example shows how to merge the individual cells of a named range.
## **Remove a Named Range**
Aspose.Cells provides the [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) method to erase the name of the range. To clear the contents of the range, use [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index) method. The following example shows how to remove a named range with its contents.
