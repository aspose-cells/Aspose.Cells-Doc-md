---
title: Update references in other worksheets while deleting blank columns and rows in a worksheet with Golang via C++
linktitle: Update references in other worksheets
type: docs
weight: 5000
url: /go-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Learn how to update references in other worksheets while deleting blank columns and rows in a worksheet using Aspose.Cells for Go via C++.
---

{{% alert color="primary" %}}

When you delete blank columns and rows in a worksheet, **their** references in other worksheets become invalid. If you want to avoid this behavior and ensure that references to the current worksheet in other worksheets are also updated, use the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/go-cpp/deleteoptions/getupdatereference/) property and set it to **true**.

{{% /alert %}}

## **Update references in other worksheets while deleting blank columns and rows in a worksheet**

Please see the following sample code and its console output. The cell E3 in the second worksheet has a formula `=Sheet1!C3`, which refers to cell C3 in the first worksheet. If you set the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/go-cpp/deleteoptions/getupdatereference/) property to **true**, this formula will be updated to `=Sheet1!A1` after deleting blank columns and rows in the first worksheet. However, if you set the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/go-cpp/deleteoptions/getupdatereference/) property to **false**, the formula in cell E3 of the second worksheet will remain `=Sheet1!C3` and become invalid.

### **Programming Sample**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateReferencesInOtherWorksheetsWhileDeletingBlankColumnsAndRowsInAWorksheet.go" >}}

### **Console Output**

This is the console output of the above sample code when the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/go-cpp/deleteoptions/getupdatereference/) property is set to **true**.

{{< highlight java >}}
Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!A1
Cell Value: 4
{{< /highlight >}}

This is the console output of the above sample code when the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/go-cpp/deleteoptions/getupdatereference/) property is set to **false**. As you can see, the formula in cell E3 of the second worksheet is not updated, and its cell value is now 0 instead of 4, which is invalid.

{{< highlight java >}}
Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 0
{{< /highlight >}}
{{< app/cells/assistant language="go" >}}

