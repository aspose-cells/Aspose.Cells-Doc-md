---
title: Protecting Worksheets with Golang via C++
linktitle: Protecting Worksheets
type: docs
weight: 10
url: /go-cpp/protecting-worksheets/
description: Learn how to protect worksheets, rows, columns, and specific cells in Microsoft Excel files using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

When a worksheet is protected, the actions a user can take are restricted. For example, they cannot input data, insert or delete rows or columns, etc.

{{% /alert %}}

## **Protect Worksheets**

### **Introduction**

The general protection options in Microsoft Excel are:

- Contents
- Objects
- Scenarios

Protected worksheets don't hide or protect sensitive data, so they're different from file encryption. Generally, worksheet protection is suitable for presentation purposes. It prevents the end user from modifying data, content, and formatting in the worksheet.

### **Protect a Worksheet**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class.

The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides the **Protect** method that is used to apply protection on the worksheet. The **Protect** method accepts the following parameters:

- **Protection Type** – the type of protection to apply on the worksheet. The protection type is applied with the help of the **ProtectionType** enumeration.
- **New Password** – the new password used to protect the worksheet.
- **Old Password** – the old password, if the worksheet is already password‑protected. If the worksheet is not already protected, then just pass `null`.

The **ProtectionType** enumeration contains the following pre‑defined protection types:

| **Protection Types** | **Description**                              |
| -------------------- | -------------------------------------------- |
| All                  | The user cannot modify anything on this worksheet |
| Contents             | The user cannot enter data in this worksheet |
| Objects              | The user cannot modify drawing objects       |
| Scenarios            | The user cannot modify saved scenarios       |
| Structure            | The user cannot modify the structure         |
| Windows              | Protection is applied to windows            |
| None                 | No protection is applied                    |

The example below shows how to protect a worksheet with a password.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ProtectingWorksheets.go" >}}

After using the above code to protect the worksheet, you can verify the protection by opening the file. Once you open the file and try to add data to the worksheet, you will see the following dialog:

| **A dialog warning that a user can't modify the worksheet** |
| ------------------------------------------------------------ |
| ![todo:image_alt_text](protecting-worksheets_1.png)          |

To work on the worksheet, unprotect it by selecting **Protection**, then **Unprotect Sheet** from the **Tools** menu.

After you select the **Unprotect Sheet** menu item, a dialog will open prompting you to enter the password so that you can work on the worksheet, as shown below:

| ![todo:image_alt_text](protecting-worksheets_2.png) |
| --------------------------------------------------- |

### **Protect a Few Cells in the Worksheet Using Microsoft Excel**

There are scenarios where you need to lock only a few cells in the worksheet. To lock specific cells, you must first unlock all the other cells. All cells in a worksheet are initially set to be locked; you can verify this by opening any Excel file, choosing **Format → Cells…**, and checking the **Protection** tab where the **Locked** checkbox is selected by default.

The following steps describe how to lock a few cells using Microsoft Excel. This method applies to Microsoft Office Excel 97, 2000, 2002, 2003, and later versions.

1. Select the entire worksheet by clicking the **Select All** button (the gray rectangle above row 1 and to the left of column A).  
2. Click **Cells** on the **Format** menu, then the **Protection** tab, and clear the **Locked** checkbox. This unlocks all the cells on the worksheet.  
   *If the **Cells** command is not available, parts of the worksheet may already be locked. In that case, go to **Tools → Protection → Unprotect Sheet**.*  
3. Select the cells you want to lock and repeat step 2, this time checking the **Locked** checkbox.  
4. On the **Tools** menu, point to **Protection**, click **Protect Sheet**, and then click **OK**.  
5. In the **Protect Sheet** dialog box, you can specify a password and select the elements that users are allowed to change.

### **Protect a Few Cells in the Worksheet Using Aspose.Cells**

In this method, we use only the Aspose.Cells API to perform the task.

Example: The following code shows how to protect a few cells in the worksheet. It first unlocks all cells, then locks three cells (A1, B1, C1), and finally protects the worksheet. The [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object contains a boolean property, **IsLocked**. You can set **IsLocked** to `true` or `false` and apply the style with `Column::ApplyStyle()` or `Row::ApplyStyle()`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ProtectingWorksheets-1.go" >}}

### **Protect a Row in the Worksheet**

Aspose.Cells allows you to easily lock any row in the worksheet. Use the **ApplyStyle()** method of the **Row** class to apply a [**Style**](https://reference.aspose.com/cells/go-cpp/style/) to a specific row. This method takes two arguments: a [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object and a **StyleFlag** object that contains the formatting flags.

The example below unlocks all cells, then locks the first row, and finally protects the worksheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ProtectingWorksheets-2.go" >}}

### **Protect a Column in the Worksheet**

Aspose.Cells also lets you lock any column. Use the **ApplyStyle()** method of the **Column** class to apply a [**Style**](https://reference.aspose.com/cells/go-cpp/style/) to a specific column.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ProtectingWorksheets-3.go" >}}

### **Allow Users to Edit Ranges**

The following example shows how to allow users to edit a range in a protected worksheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ProtectingWorksheets-4.go" >}}
{{< app/cells/assistant language="go" >}}
