---
title: Specifying Significant Digits to be Stored in Excel file
type: docs
weight: 20
url: /java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Possible Usage Scenarios**
By default, Aspose.Cells stores 17 significant digits of double values in spreadsheets unlike Excel application which stores only 15 significant digits. You can change the default behavior of Aspose.Cells for this case, that is; you can change the number of significant digits from 17 to 15 while using the [CellsHelper.SignificantDigits](https://apireference.aspose.com/java/cells/com.aspose.cells/cellshelper#SignificantDigits) property.
## **Specifying Significant Digits to be Stored in Excel file**
The following sample code enforces Aspose.Cells to use 15 significant digits while storing double values inside the excel file. Please check the [output excel file](attachments/22970436/23166982.xlsx). Change its extension to .zip and unzip it and you will see, only 15 significant digits are stored inside the excel file. The following screenshot explains the effect of [CellsHelper.SignificantDigits](https://apireference.aspose.com/java/cells/com.aspose.cells/cellshelper#SignificantDigits) property on the output excel file.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
