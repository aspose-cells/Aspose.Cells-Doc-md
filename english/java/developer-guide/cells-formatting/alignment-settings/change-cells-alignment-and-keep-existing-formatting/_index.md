---
title: Change Cells Alignment and Keep Existing Formatting
type: docs
weight: 260
url: /java/change-cells-alignment-and-keep-existing-formatting/
---

## **Possible Usage Scenarios**

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells allows you to do it using the [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) property. If you will set it **true**, changes in alignment will take place otherwise not. Please note, [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) object is passed as a parameter to [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) method which actually applies the formatting to the range of cells.

## **Change Cells Alignment and Keep Existing Formatting**

The following sample code loads the [sample Excel file](67338592.xlsx), creates the range and center aligns it horizontally and vertically and keeps the existing formatting intact. The following screenshot compares the sample Excel file and [output Excel file](67338591.xlsx) and shows that all existing formatting of the cells is the same except that cells are now center aligned horizontally and vertically.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
{{< app/cells/assistant language="java" >}}