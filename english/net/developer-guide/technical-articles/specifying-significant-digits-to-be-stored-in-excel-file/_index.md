---
title: Specifying Significant Digits to be Stored in Excel File
type: docs
weight: 30
url: /net/specifying-significant-digits-to-be-stored-in-excel-file/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

By default, Aspose.Cells stores 17 significant digits of double values inside the Excel file, unlike Microsoft Excel which stores only 15 significant digits. You can change the default behavior of Aspose.Cells from 17 significant digits to 15 significant digits using the [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) property.

## **Specifying Significant Digits to be Stored in Excel File**

The following sample code enforces Aspose.Cells to use 15 significant digits while storing double values inside the Excel file. Please check the [output Excel file](22774105.xlsx). Change its extension to .zip and unzip it, and you will see that only 15 significant digits are stored inside the Excel file. The following screenshot explains the effect of [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) property on the output Excel file.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
{{< app/cells/assistant language="csharp" >}}
