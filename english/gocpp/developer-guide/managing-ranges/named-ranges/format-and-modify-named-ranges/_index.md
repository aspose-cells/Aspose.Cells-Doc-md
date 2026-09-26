---
title: Format and Modify Named Ranges with Golang via C++
linktitle: Format and Modify Named Ranges
type: docs
weight: 85
url: /go-cpp/format-and-modify-named-ranges/
description: Learn how to format, rename, merge, and remove named ranges in Excel files using Aspose.Cells with Golang via C++.
---

## **Format Ranges**

### **Setting Background Color and Font Attributes to a Named Range**

To apply formatting, define a [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object to specify the style settings and apply it to the [**Range**](https://reference.aspose.com/cells/go-cpp/range/) object.

The following example shows how to set the solid fill color (shading color) with font settings to a range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatAndModifyNamedRanges.go" >}}

### **Adding Borders to a Named Range**

It is possible to add borders to a range of cells instead of just a single cell. The [**Range**](https://reference.aspose.com/cells/go-cpp/range/) object provides a [**SetOutlineBorder**](https://reference.aspose.com/cells/go-cpp/range/setoutlineborder_bordertype_cellbordertype_cellscolor/) method that takes the following parameters to add a border to the range of cells:

- Border type, the type of border, selected from the [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/) enumeration.
- Line style, the line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/) enumeration.
- Color, the line color, selected from the Color enumeration.

The following example shows how to set an outline border to a range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatAndModifyNamedRanges-1.go" >}}

The following example shows how to set borders around each cell in the range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatAndModifyNamedRanges-2.go" >}}

## **Rename a Named Range**

Aspose.Cells allows you to rename a named range to suit your needs. You may get the named range and rename it by using the **Name.SetText()** method. The following example shows how to rename a named range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatAndModifyNamedRanges-3.go" >}}

## **Union of Ranges**

Aspose.Cells provides the **Range.UnionRange** method to take the union of ranges; the method returns a *std::vector* object. The following example shows how to take the union of ranges.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatAndModifyNamedRanges-4.go" >}}

## **Intersection of Ranges**

Aspose.Cells provides the **Range.Intersect** method to intersect two ranges. The method returns a **Range** object. To check whether a range intersects another range, use the **Range.IsIntersect** method, which returns a Boolean value. The following example shows how to intersect the ranges.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatAndModifyNamedRanges-5.go" >}}

## **Merge Cells in the Named Range**

Aspose.Cells provides the **Range.Merge()** method to merge the cells in the range. The following example shows how to merge the individual cells of a named range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatAndModifyNamedRanges-6.go" >}}

## **Remove a Named Range**

Aspose.Cells provides the **NameCollection.RemoveAt()** method to erase the name of the range. To clear the contents of the range, use the **Cells.ClearRange()** method. The following example shows how to remove a named range along with its contents.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatAndModifyNamedRanges-7.go" >}}
