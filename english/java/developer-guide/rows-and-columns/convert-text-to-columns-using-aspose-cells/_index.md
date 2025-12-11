---
title: Convert Text to Columns using Aspose.Cells
type: docs
weight: 70
url: /java/convert-text-to-columns-using-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
You can convert text to columns using Microsoft Excel. This feature is available from *Data Tools* under the *Data* tab. In order to split the contents of a column into multiple columns, the data should contain a specific delimiter such as a comma (or any other character) based on which Microsoft Excel splits the contents of a cell into multiple cells. Aspose.Cells also provides this feature via the [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) method.

## **Convert Text to Columns using Aspose.Cells**
The following sample code explains the usage of the [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) method. The code first adds some people’s names in column A of the first worksheet. The first and last names are separated by a space character. Then it applies the [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) method on column A and saves it as an output Excel file. If you open the [output Excel file](25395230.xlsx), you will see that first names are in column A while last names are in column B as shown in this screenshot.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}
