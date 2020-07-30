---
title : "Find or Search Data" 
description : "" 
weight : 12204 
toc : false
type: docs
url: /net/developerguide/data/find+or+search+data/
---

# Aspose.Cells for .NET : Find or Search Data


Microsoft Excel allows users to find cells in a worksheet that contains specified data.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Finding Cells Containing Specified Data](#finding-cells-containing-specified-data)
    *   1.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   1.2 [Using Aspose.Cells](#using-aspose.cells)
*   2 [Finding Cells Containing a Formula](#finding-cells-containing-a-formula)
*   3 [Finding Data or Formulas using FindOptions](#finding-data-or-formulas-using-findoptions)
*   4 [Finding Cells Containing Specified String Value or Number](#finding-cells-containing-specified-string-value-or-number)
{{< /panel >}}
 

## Finding Cells Containing Specified Data

### Using Microsoft Excel

Microsoft Excel allows users to find cells in a worksheet that contains specified data. If you select **Edit** from the **Find** menu in Microsoft Excel, you will see a dialog where you can specify the search value.

Here, we are looking for the value "Oranges". Aspose.Cells also allows developers to find cells in the worksheet containing specified values.

### Using Aspose.Cells

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection that represents all cells in the worksheet. The [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection provides several methods for finding cells in a worksheet containing user-specified data. A few of these methods are discussed below in more detail.

All `Find` methods return the references of the cells containing the specified data to search.

## Finding Cells Containing a Formula

Developers can find a specified formula in the worksheet by calling the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection's [Find](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/find/index) method. Typically, the [Find](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/find/index) method accepts three parameters:

*   **Object: **The object to search for. The type should be int,double,DateTime,string,bool.
*   **Previous cell:** Previous cell with the same object. This parameter can be set to null if searching from the start.
*   FindOptions: Options for finding the required object.

The examples below use worksheet data for practicing find methods:

## Finding Data or Formulas using FindOptions

It is possible to find specified values using the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection's [Find](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/find/index) method with various [FindOptions](https://apireference.aspose.com/net/cells/aspose.cells/findoptions). Typically, the [Find](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/find/index) method accepts the following parameters:

*   **Search value**, the data or value to be searched for.
*   **Previous cell**, the last cell that contained the same value. This parameter can be set to null when searching from the start.
*   **Find options**, the find options.

## Finding Cells Containing Specified String Value or Number

It is possible to find specified string values by calling the same [Find](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/find/index) method found in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection with various [FindOptions](https://apireference.aspose.com/net/cells/aspose.cells/findoptions).

Specify the [FindOptions.LookInType](https://apireference.aspose.com/net/cells/aspose.cells/findoptions/properties/lookintype) and [FindOptions.LookAtType](https://apireference.aspose.com/net/cells/aspose.cells/findoptions/properties/lookattype) properties. The following example code illustrates how to use these properties to find cells with various number or strings at the **beginning** or at the **center** or at the **end** of the cell's string.

