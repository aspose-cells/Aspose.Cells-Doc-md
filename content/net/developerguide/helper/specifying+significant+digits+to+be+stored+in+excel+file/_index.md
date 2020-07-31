---
title : "Specifying Significant Digits to be Stored in Excel File" 
description : "" 
weight : 12301 
toc : false
type: docs
url: /net/developerguide/helper/specifying+significant+digits+to+be+stored+in+excel+file/
---

# Aspose.Cells for .NET : Specifying Significant Digits to be Stored in Excel File


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Specifying Significant Digits to be stored in Excel file](#specifying-significant-digits-to-be-stored-in-excel-file)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

 

## Possible Usage Scenarios

By default, Aspose.Cells stores 17 significant digits of double values inside the excel file, unlike MS-Excel which stores only 15 significant digits. You can change the default behavior of Aspose.Cells from 17 significant digits to 15 significant digits using the [CellsHelper.SignificantDigits](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/properties/significantdigits) property.

## Specifying Significant Digits to be stored in Excel file

The following sample code enforces Aspose.Cells to use 15 significant digits while storing double values inside the excel file. Please check the [output excel file](https://docs2.aspose.com/cells/net/attachments/22546710/22774105.xlsx). Change its extension to `.zip` and unzip it and you will see, only 15 significant digits are stored inside the excel file. The following screenshot explains the effect of [CellsHelper.SignificantDigits](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/properties/significantdigits) property on the output excel file.

![](https://docs2.aspose.com/cells/net/attachments/22546710/22774106.png)

## Sample Code

