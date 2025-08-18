---
title: Change Cells Alignment and Keep Existing Formatting with Golang via C++
description: Use the Aspose.Cells library to change cell alignment and preserve existing formatting
keywords: Aspose.Cells, C++, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Possible Usage Scenarios**

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells allows you to do it using the [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/) property. If you will set it **true**, changes in alignment will take place otherwise not. Please note, [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) object is passed as a parameter to [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) method which actually applies the formatting to a range of cells.

## **Change Cells Alignment and Keep Existing Formatting**

The following sample code loads the [sample Excel file](67338585.xlsx), creates the range and center aligns it horizontally and vertically and keeps the existing formatting intact. The following screenshot compares the sample Excel file and [output Excel file](67338586.xlsx) and shows that all existing formatting of the cells is the same except that cells are now center aligned horizontally and vertically.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}