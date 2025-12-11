---
title: Specify how to cross string in output HTML using HtmlCrossType
type: docs
weight: 140
url: /java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When the cell contains text or a string but it is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file into HTML, you can control this overflow by specifying the cross type using the **[HtmlCrossType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)** enumeration. It has the following values:

- **[HtmlCrossType.DEFAULT](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT)**: Display like MS Excel, which depends on the next cell. If the next cell is null, the string will cross, or it will be truncated.

- **[HtmlCrossType.MS_EXPORT](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS-EXPORT)**: Display the string as MS Excel does when exporting to HTML.

- **[HtmlCrossType.CROSS](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS)**: Display HTML cross string; the performance of creating large HTML files will be more than ten times faster than setting the value to **DEFAULT** or **FIT_TO_CELL**.

- **[HtmlCrossType.CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT)**: Display HTML cross string and hide the right string when the texts overlap.

- **[HtmlCrossType.FIT_TO_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL)**: Displays only the string within the width of the cell.

## **Specify how to cross string in output HTML using HtmlCrossType**

The following sample code loads the **sample Excel file** and saves it to HTML format by specifying different **HtmlCrossType** values. Please download the **output HTML** files generated with this code. The sample Excel file contains an image bordered in red, as shown in this screenshot, which demonstrates the effect of the **HtmlCrossType** values on the output HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
{{< app/cells/assistant language="java" >}}
