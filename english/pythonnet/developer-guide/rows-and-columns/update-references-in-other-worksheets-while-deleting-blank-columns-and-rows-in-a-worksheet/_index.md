---
title: Update references in other worksheets while deleting blank columns and rows in a worksheet
type: docs
weight: 5000
url: /python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: This article shows how to Update references in other worksheets while deleting blank columns and rows in a worksheet by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Update references in other worksheets while deleting blank columns and rows in a worksheet, Update references when removing blank columns and rows in a worksheet in Python.
---

{{% alert color="primary" %}}

When you delete blank columns and rows in a worksheet, then its references in other worksheets become invalid. If you want to avoid this behavior and want those references of the current worksheet in other worksheets are also updated, then please use the [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) property and set it to **true**.

{{% /alert %}}

## **Update references in other worksheets while deleting blank columns and rows in a worksheet**

Please see the following sample code and its console output. The cell E3 in the second worksheet has a formula =Sheet1!C3 which is referring to cell C3 in the first worksheet. If you will set [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) property as **true**, this formula will be updated and become =Sheet1!A1 on deleting blank columns and rows in the first worksheet. However, if you will set [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) property as **false**, the formula in cell E3 of the second worksheet will remain =Sheet1!C3 and become invalid.

### **Programming Sample**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-UpdateReferenceInWorksheets.py" >}}

### **Console Output**

This is the console output of the above sample code when [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) property has been set as **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

This is the console output of the above sample code when [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/) property has been set as **false**. As you can see, the formula in cell E3 of the second worksheet is not updated and its cell value is now 0 instead of 4 which is invalid.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}