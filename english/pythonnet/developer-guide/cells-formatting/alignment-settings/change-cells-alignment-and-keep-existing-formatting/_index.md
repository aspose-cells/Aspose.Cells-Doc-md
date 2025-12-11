---
title: Change Cells Alignment and Keep Existing Formatting
description: Use the Aspose.Cells for Python via .NET library to change cell alignment and preserve existing formatting
keywords: Aspose.Cells for Python via .NET, Python Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /python-net/change-cells-alignment-and-keep-existing-formatting/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells for Python via .NET allows you to do it using the [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments) property. If you set it to **true**, changes in alignment will take place; otherwise, they will not. Please note that the [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) object is passed as a parameter to the [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style) method, which actually applies the formatting to a range of cells.

## **Change Cells Alignment and Keep Existing Formatting**

The following sample code loads the [sample Excel file](67338585.xlsx), creates the range, and center‑aligns it horizontally and vertically while keeping the existing formatting intact. The screenshot below compares the sample Excel file with the [output Excel file](67338586.xlsx) and shows that all existing formatting of the cells remains the same, except that the cells are now center‑aligned horizontally and vertically.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}
