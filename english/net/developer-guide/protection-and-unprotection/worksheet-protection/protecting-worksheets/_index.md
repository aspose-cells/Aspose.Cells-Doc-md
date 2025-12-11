---
title: Protecting Worksheets
type: docs
weight: 10
url: /net/protecting-worksheets/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
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

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class.

The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides the [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) method that is used to apply protection to the worksheet. The [**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) method accepts the following parameters:

- **Protection Type** – the type of protection to apply on the worksheet. The protection type is applied with the help of the [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) enumeration.  
- **New Password** – the new password used to protect the worksheet.  
- **Old Password** – the old password, if the worksheet is already password‑protected. If the worksheet is not already protected, simply pass `null`.

The [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) enumeration contains the following predefined protection types:

| **Protection Types** | **Description** |
| :- | :- |
| All | The user cannot modify anything on this worksheet |
| Contents | The user cannot enter data in this worksheet |
| Objects | The user cannot modify drawing objects |
| Scenarios | The user cannot modify saved scenarios |
| Structure | The user cannot modify the structure |
| Windows | Protection is applied to windows |
| None | No protection is applied |

The example below shows how to protect a worksheet with a password.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

After the above code is used to protect the worksheet, you can verify the protection by opening the file. Once you open the file and try to add some data to the worksheet, you will see the following dialog:

| **A dialog warning that a user can't modify the worksheet** |
| :- |
| ![todo:image_alt_text](protecting-worksheets_1.png) |

To work on the worksheet, unprotect it by selecting **Protection**, then **Unprotect Sheet** from the **Tools** menu.

After you select the **Unprotect Sheet** menu item, a dialog opens prompting you to enter the password so you can work on the worksheet, as shown below:

| ![todo:image_alt_text](protecting-worksheets_2.png) |
| :- |

### **Protect a Few Cells in the Worksheet Using Microsoft Excel**

There might be certain scenarios where you need to lock only a few cells in the worksheet. If you want to lock specific cells, you must unlock all the other cells first. All cells in a worksheet are initialized for locking; you can verify this by opening any Excel file in MS Excel, clicking **Format | Cells…** to show the **Format Cells** dialog box, then the **Protection** tab, where the **Locked** checkbox is checked by default.

The following points describe how to lock a few cells using MS Excel. This method applies to Microsoft Office Excel 97, 2000, 2002, 2003, and later versions.

1. Select the entire worksheet by clicking the **Select All** button (the gray rectangle directly above the row numbers and to the left of column letters).  
2. Click **Cells** on the **Format** menu, click the **Protection** tab, and then clear the **Locked** checkbox. This unlocks all the cells on the worksheet. If the **Cells** command is not available, parts of the worksheet may already be locked. On the **Tools** menu, point to **Protection**, and then click **Unprotect Sheet**.  
3. Select just the cells you want to lock and repeat step 2, but this time check the **Locked** checkbox.  
4. On the **Tools** menu, point to **Protection**, click **Protect Sheet**, and then click **OK**.  
5. In the **Protect Sheet** dialog box, you can specify a password and select the elements that you want users to be able to change.

### **Protect a Few Cells in the Worksheet Using Aspose.Cells**

In this method, we use the Aspose.Cells API only to perform the task.

The following example demonstrates how to protect a few cells in the worksheet. It unlocks all the cells first, then locks three cells (A1, B1, C1), and finally protects the worksheet. The [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object contains a Boolean property, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). You can set the [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) property to `true` or `false` and apply the *Column/Row.ApplyStyle()* method to lock or unlock the row/column with your desired attributes.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Protect a Row in the Worksheet**

Aspose.Cells allows you to easily lock any row in the worksheet. Here, we can make use of the [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) method of the [**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) class to apply a [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) to a particular row. This method takes two arguments: a [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object and a [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) object, which contain all the members related to applied formatting.

The following example shows how to protect a row in the worksheet. It unlocks all the cells first, then locks the first row, and finally protects the worksheet. The [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object contains a Boolean property, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). You can set the [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) property to `true` or `false` to lock or unlock the row/column using the [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) object.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Protect a Column in the Worksheet**

Aspose.Cells allows you to easily lock any column in the worksheet. Here, we can make use of the [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) method of the [**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) class to apply a [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) to a particular column. This method takes two arguments: a [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object and a [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) object, which contain all the members related to applied formatting.

The following example shows how to protect a column in the worksheet. It unlocks all the cells first, then locks the first column, and finally protects the worksheet. The [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object contains a Boolean property, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). You can set the [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) property to `true` or `false` to lock or unlock the row/column using the [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) object.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Allow Users to Edit Ranges**

The following example shows how to allow users to edit a range in a protected worksheet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
