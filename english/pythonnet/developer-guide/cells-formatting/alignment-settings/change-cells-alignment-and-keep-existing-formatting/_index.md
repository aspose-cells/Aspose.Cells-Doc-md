---
title: Change Cells Alignment and Keep Existing Formatting
description: Use the Aspose.Cells library to change cell alignment and preserve existing formatting
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **Possible Usage Scenarios**

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells allows you to do it using the [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments) property. If you will set it **true**, changes in alignment will take place otherwise not. Please note, [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/style_flag) object is passed as a parameter to [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style) method which actually applies the formatting to a range of cells.

## **Change Cells Alignment and Keep Existing Formatting**

The following sample code loads the [sample Excel file](67338585.xlsx), creates the range and center aligns it horizontally and vertically and keeps the existing formatting intact. The following screenshot compares the sample Excel file and [output Excel file](67338586.xlsx) and shows that all existing formatting of the cells is the same except that cells are now center aligned horizontally and vertically.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
