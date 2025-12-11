---
title: Change Cells Alignment and Keep Existing Formatting
description: Use the Aspose.Cells library to change cell alignment and preserve existing formatting
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /net/change-cells-alignment-and-keep-existing-formatting/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells allows you to do it using the [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) property. If you set it **true**, changes in alignment will take place; otherwise, they will not. Please note that the [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) object is passed as a parameter to the [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle) method, which actually applies the formatting to a range of cells.

## **Change Cells Alignment and Keep Existing Formatting**

The following sample code loads the [sample Excel file](67338585.xlsx), creates the range, and center‑aligns it horizontally and vertically while keeping the existing formatting intact. The following screenshot compares the sample Excel file and the [output Excel file](67338586.xlsx) and shows that all existing formatting of the cells is the same, except that the cells are now center‑aligned horizontally and vertically.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
