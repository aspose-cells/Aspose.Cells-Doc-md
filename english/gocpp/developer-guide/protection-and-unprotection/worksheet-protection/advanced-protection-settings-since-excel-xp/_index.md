---
title: Advanced Protection Settings since Excel XP with Golang via C++
linktitle: Advanced Protection Settings since Excel XP
type: docs
weight: 30
url: /go-cpp/advanced-protection-settings-since-excel-xp/
description: Learn how to apply advanced protection settings in Excel files using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Since the release of Excel 2002 (XP), Microsoft has added many advanced protection settings.

{{% /alert %}}

## **Introduction**

These protection settings restrict or allow users to:

- Delete rows or columns.  
- Edit contents, objects, or scenarios.  
- Format cells, rows, or columns.  
- Insert rows, columns, or hyperlinks.  
- Select locked or unlocked cells.  
- Use pivot tables and much more.

Aspose.Cells supports all the advanced protection settings offered by Excel XP or later versions.

### **Advanced Protection Settings Using Excel XP and Later Versions**

To view the protection settings available in Excel XP:

1. From the **Tools** menu, select **Protection** followed by **Protect Sheet**. A dialog will be displayed.

To view the protection settings available in Excel 2016:

1. From the **File** menu, select **Protect Workbook** followed by **Protect Current Sheet**.  
2. Select **Protect Sheet** on the **Review** tab.

Following the steps mentioned above will show a dialog where you can allow or restrict worksheet features or apply a password to the worksheet.

### **Advanced Protection Settings Using Aspose.Cells**

Aspose.Cells supports all of the advanced protection settings.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class.

The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides the [**GetProtection()**](https://reference.aspose.com/cells/go-cpp/worksheet/getprotection/) property that is used to apply these advanced protection settings. The [**GetProtection()**](https://reference.aspose.com/cells/go-cpp/worksheet/getprotection/) property is, in fact, an object of the [**Protection**](https://reference.aspose.com/cells/go-cpp/protection/) class that encapsulates several Boolean properties for disabling or enabling restrictions.

Below is a small example application. It opens an Excel file and uses most of the advanced protection settings supported by Excel XP and later versions.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdvancedProtectionSettingsSinceExcelXp.go" >}}

{{% alert color="primary" %}}

Please do not call the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class's [**Protect**](https://reference.aspose.com/cells/go-cpp/worksheet/protect_protectiontype/) method when using the [**GetProtection()**](https://reference.aspose.com/cells/go-cpp/worksheet/getprotection/) property. Also, save the file in **Excel97To2003** or **Xlsx** format because the advanced protection settings are only supported by Excel XP and later versions.

{{% /alert %}}

### **Cell Locking Issue**

If you want to restrict users from editing cells, the cells must be locked before any protection settings are applied. Otherwise, the cells can be edited even if the worksheet is protected. In Microsoft Excel XP, cells can be locked through the following dialog:

| **Dialog to lock cells in Excel XP** |
| :- |
| ![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png) |

It is possible to lock cells using the Aspose.Cells API as well. Each cell can obtain a [**Style**](https://reference.aspose.com/cells/go-cpp/style/) that contains a Boolean property, [**IsLocked**](https://reference.aspose.com/cells/go-cpp/style/islocked/). Set the [**IsLocked**](https://reference.aspose.com/cells/go-cpp/style/islocked/) property to **true** or **false** to lock or unlock the cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdvancedProtectionSettingsSinceExcelXp-1.go" >}}
{{< app/cells/assistant language="go" >}}
