---
title: Output Blank Page when there is Nothing to Print
type: docs
weight: 80
url: /java/output-blank-page-when-there-is-nothing-to-print/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If the sheet is empty, then Aspose.Cells will not print anything when you export worksheet to image. You can change this behavior by using [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#setOutputBlankPageWhenNothingToPrint-boolean-) property. When you will set it to **true**, it will print the blank page.

## **Output Blank Page when there is Nothing to Print**

The following sample code creates the empty workbook which has an empty worksheet and renders the empty worksheet to an image after setting the [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#setOutputBlankPageWhenNothingToPrint-boolean-) property as **true**. Consequently, it generates the blank page as there is nothing to print which you can see as below.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
{{< app/cells/assistant language="java" >}}
