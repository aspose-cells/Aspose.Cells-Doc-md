---
title: Change Cells Alignment and Keep Existing Formatting
linktitle: Change Cells Alignment and Keep Existing Formatting
description: Use the Aspose.Cells library to change cell alignment and preserve existing formatting in Node.js via C++
keywords: Aspose.Cells, Node.js via C++, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells for Node.js via C++ allows you to do it using the [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-) method. If you will set it **true**, changes in alignment will take place otherwise not. Please note, [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) object is passed as a parameter to the [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-) method which actually applies the formatting to a range of cells.

## **Change Cells Alignment and Keep Existing Formatting**

The following sample code loads the [sample Excel file](67338585.xlsx), creates the range and center aligns it horizontally and vertically and keeps the existing formatting intact. The following screenshot compares the sample Excel file and [output Excel file](67338586.xlsx) and shows that all existing formatting of the cells is the same except that cells are now center aligned horizontally and vertically.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
