---
title: Format and Modify Named Ranges
type: docs
weight: 85
url: /net/format-and-modify-named-ranges/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Format Ranges**

### **Setting Background Color and Font Attributes to a Named Range**

To apply formatting, define a [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object to specify the style settings and apply it to the [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) object.

The following example shows how to set the solid fill color (shading color) with font settings to a range.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Adding Borders to a Named Range**

It is possible to add borders to a range of cells instead of just a single cell. The [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) object provides a [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) method that takes the following parameters to add a border to the range of cells:

- Border type, selected from the [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) enumeration.  
- Line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) enumeration.  
- Color, the line color, selected from the Color enumeration.

The following example shows how to set an outline border to a range.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

The following example shows how to set borders around each cell in the range.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Rename a Named Range**

Aspose.Cells allows you to rename a named range as needed. You can retrieve the named range and rename it using the [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text) property. The following example shows how to rename a named range.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Union of Ranges**

Aspose.Cells provides the [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) method to compute the union of ranges; the method returns an [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8) object. The following example shows how to take the union of ranges.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Intersection of Ranges**

Aspose.Cells provides the [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) method to intersect two ranges. The method returns a [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) object. To check whether a range intersects another range, use the [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) method that returns a Boolean value. The following example shows how to intersect the ranges.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Merge Cells in the Named Range**

Aspose.Cells provides the [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) method to merge the cells in the range. The following example shows how to merge the individual cells of a named range.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Remove a Named Range**

Aspose.Cells provides the [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) method to erase the name of the range. To clear the contents of the range, use the [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index) method. The following example shows how to remove a named range with its contents.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
