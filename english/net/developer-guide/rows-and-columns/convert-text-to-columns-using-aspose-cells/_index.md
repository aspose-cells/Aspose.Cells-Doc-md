---
title: Convert Text to Columns using Aspose.Cells
type: docs
weight: 30
url: /net/convert-text-to-columns-using-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

You can convert your text to columns using Microsoft Excel. This feature is available under *Data Tools* on the *Data* tab. In order to split the contents of a column into multiple columns, the data must contain a specific delimiter, such as a comma (or any other character), based on which Microsoft Excel splits the contents of a cell into separate cells. Aspose.Cells also provides this feature via the [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) method.

## **Convert Text to Columns using Aspose.Cells**

The following sample code explains the usage of the [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) method. The code first adds some people's names in column A of the first worksheet. The first and last names are separated by a space character. Then it applies the [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) method on column A and saves the result as an output Excel file. If you open the [output Excel file](25395213.xlsx), you will see that first names are in column A while last names are in column B, as shown in this screenshot.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
{{< app/cells/assistant language="csharp" >}}
