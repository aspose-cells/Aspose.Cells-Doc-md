---
title: Format and Modify Named Ranges
type: docs
weight: 85
url: /python-net/format-and-modify-named-ranges/
description: This article shows how to format and modify named ranges using Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Format and Modify Named Ranges, Python Set Background Color and Font Attributes to a Named Range, Python Add Borders to a Named Range, Python Rename a Named Range, Python Union of Ranges, Python Intersection of Ranges, Python Merge Cells in the Named Range.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Format Ranges**

### **How to Set Background Color and Font Attributes to a Named Range**

To apply formatting, define a [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object to specify the style settings and apply it to the [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object.

The following example shows how to set the solid fill color (shading color) with font settings to a range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **How to Add Borders to a Named Range**

It is possible to add borders to a range of cells instead of just a single cell. The [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object provides a [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor) method that takes the following parameters to add a border to the range of cells:

- Border type, the type of border, selected from the [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) enumeration.
- Line style, the line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) enumeration.
- Color, the line color, selected from the Color enumeration.

The following example shows how to set an outline border to a range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}

## **How to Rename a Named Range**

Aspose.Cells allows you to rename a named range as needed. You may get the named range and rename it by using the [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text) attribute. The following example shows how to rename a named range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **How to Take Union of Ranges**

Aspose.Cells provides the [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range) method to take the union of ranges. The following example shows how to take the union of ranges.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **How to Intersect the Ranges**

Aspose.Cells provides the [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) method to intersect two ranges. The method returns a [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object. To check whether a range intersects another range, use the [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) method that returns a Boolean value. The following example shows how to intersect the ranges.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **How to Merge Cells in the Named Range**

Aspose.Cells provides the [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) method to merge the cells in the range. The following example shows how to merge the individual cells of a named range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
