---
title: Find or Search Data
type: docs
weight: 50
url: /python-net/find-or-search-data/
description: Learn how to find or search cells in a worksheet that contains specified data through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Find data, Python Search data, Python Find Cells Containing a Formula, Python Search Cells Containing a Formula, Python Find Data or Formulas using FindOptions, Python Search Data or Formulas using FindOptions, Python Find or Search Cells Containing Specified String Value or Number, Python Find or Search cells contains specified data
---

{{% alert color="primary" %}}

Microsoft Excel allows users to find cells in a worksheet that contains specified data.

{{% /alert %}}

## **Finding Cells Containing Specified Data**

### **Using Microsoft Excel**

Microsoft Excel allows users to find cells in a worksheet that contains specified data. If you select **Edit** from the **Find** menu in Microsoft Excel, you will see a dialog where you can specify the search value.

Here, we are looking for the value "Oranges". Aspose.Cells also allows developers to find cells in the worksheet containing specified values.

### **Using Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The  [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection that represents all cells in the worksheet. The [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection provides several methods for finding cells in a worksheet containing user-specified data. A few of these methods are discussed below in more detail.

{{% alert color="primary" %}}

All Find methods return the references of the cells containing the specified data to search.

{{% /alert %}}

## **Finding Cells Containing a Formula**

Developers can find a specified formula in the worksheet by calling the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection's [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) method. Typically, the [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) method accepts three parameters:

- **what:** The object to search for. The type should be int,double,DateTime,string,bool.
- **previous_cell:** Previous cell with the same object. This parameter can be set to null if searching from the start.
- **find_options:** Options for finding the required object.

The examples below use worksheet data for practicing find methods:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **Finding Data or Formulas using FindOptions**

It is possible to find specified values using the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection's [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) method with various [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions). Typically, the [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) method accepts the following parameters:

- **what:**, the data or value to be searched for.
- **previous_cell**, the last cell that contained the same value. This parameter can be set to null when searching from the start.
- **find_options**, the find options.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **Finding Cells Containing Specified String Value or Number**

It is possible to find specified string values by calling the same [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) method found in the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection with various [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions).

Specify the [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) and [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/) properties. The following example code illustrates how to use these properties to find cells with various number of strings at the **beginning** or at the **center** or at the **end** of the cell's string.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **Advance topics**
- [Find Cells with Specific Style](/cells/python-net/find-cells-with-specific-style/)
- [Find if the cell value starts with single quote mark](/cells/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Search Data using Original Values](/cells/python-net/search-data-using-original-values/)
{{< app/cells/assistant language="python-net" >}}