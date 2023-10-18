---
title: Find or Search Data
type: docs
weight: 50
url: /net/find-or-search-data/
description: Learn how to find or search cells in a worksheet that contains specified data through the Aspose.Cells for .NET API.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---

{{% alert color="primary" %}}

Microsoft Excel allows users to find cells in a worksheet that contains specified data.

{{% /alert %}}

## **Finding Cells Containing Specified Data**

### **Using Microsoft Excel**

Microsoft Excel allows users to find cells in a worksheet that contains specified data. If you select **Edit** from the **Find** menu in Microsoft Excel, you will see a dialog where you can specify the search value.

Here, we are looking for the value "Oranges". Aspose.Cells also allows developers to find cells in the worksheet containing specified values.

### **Using Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The  [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection provides several methods for finding cells in a worksheet containing user-specified data. A few of these methods are discussed below in more detail.

{{% alert color="primary" %}}

All Find methods return the references of the cells containing the specified data to search.

{{% /alert %}}

## **Finding Cells Containing a Formula**

Developers can find a specified formula in the worksheet by calling the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection's [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) method. Typically, the [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) method accepts three parameters:

- **Object:** The object to search for. The type should be int,double,DateTime,string,bool.
- **Previous cell:** Previous cell with the same object. This parameter can be set to null if searching from the start.
- FindOptions: Options for finding the required object.

The examples below use worksheet data for practicing find methods:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Finding Data or Formulas using FindOptions**

It is possible to find specified values using the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection's [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) method with various [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions). Typically, the [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) method accepts the following parameters:

- **Search value**, the data or value to be searched for.
- **Previous cell**, the last cell that contained the same value. This parameter can be set to null when searching from the start.
- **Find options**, the find options.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Finding Cells Containing Specified String Value or Number**

It is possible to find specified string values by calling the same [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) method found in the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection with various [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

Specify the [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) and [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) properties. The following example code illustrates how to use these properties to find cells with various number of strings at the **beginning** or at the **center** or at the **end** of the cell's string.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Advance topics**
- [Find Cells with Specific Style](/cells/net/find-cells-with-specific-style/)
- [Find if the cell value starts with single quote mark](/cells/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Search Data using Original Values](/cells/net/search-data-using-original-values/)
