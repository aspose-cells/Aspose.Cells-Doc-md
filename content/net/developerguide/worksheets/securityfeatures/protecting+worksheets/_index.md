---
title : "Protecting Worksheets" 
description : "" 
weight : 16163 
toc : false
type: docs
url: /net/developerguide/worksheets/securityfeatures/protecting+worksheets/
---

# Aspose.Cells for .NET : Protecting Worksheets


When a worksheet is protected, the actions a user can take are restricted. For example, they cannot input data, insert or delete rows or columns etc.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Protect Worksheets](#protect-worksheets)
    *   1.1 [Introduction](#introduction)
    *   1.2 [Protect a Worksheet](#protect-a-worksheet)
    *   1.3 [Protect a few Cells in the Worksheet Using Microsoft Excel](#protect-a-few-cells-in-the-worksheet-using-microsoft-excel)
    *   1.4 [Protect a few Cells in the Worksheet Using Aspose Cells](#protect-a-few-cells-in-the-worksheet-using-aspose-cells)
    *   1.5 [Protect a Row in the Worksheet](#protect-a-row-in-the-worksheet)
    *   1.6 [Protect a Column in the Worksheet](#protect-a-column-in-the-worksheet)
    *   1.7 [Allow Users to Edit Ranges](#allow-users-to-edit-ranges)
{{< /panel >}}
 

## Protect Worksheets

### Introduction

The general protection options in Microsoft Excel are:

*   Contents
*   Objects
*   Scenarios

Protected worksheets don't hide or protect sensitive data, so it's different from file encryption. Generally, worksheet protection is suitable for presentation purposes. It prevents the end user from modifying data, content, and formatting in the worksheet.

### Protect a Worksheet

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class.

The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides the [Protect](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/methods/protect/index) method that is used to apply protection on the worksheet. [Protect](https://apireference.aspose.com/net/cells/aspose.cells.worksheet/protect/methods/1) method accepts the following parameters:

*   Protection Type, the type of protection to apply on the worksheet. Protection type is applied with the help of the [ProtectionType](https://apireference.aspose.com/net/cells/aspose.cells/protectiontype) enumeration.
*   New Password, the new password used to protect the worksheet.
*   Old Password, the old password, if the worksheet is already password protected. If the worksheet is not already protected then just pass null.

The [ProtectionType](https://apireference.aspose.com/net/cells/aspose.cells/protectiontype) enumeration contains the following pre-defined protections types:

{{< table style="table-striped" >}}
|Protection Types|Description|
|:----|:----|
|All|The user cannot modify anything on this worksheet|
|Contents|The user cannot enter data in this worksheet|
|Objects|The user cannot modify drawing objects|
|Scenarios|The user cannot modify saved scenarios|
|Structure|The user cannot modify the structure|
|Windows|Protection is applied to windows|
|None|No protection is applied|
{{< /table >}}

The example below shows how to protect a worksheet with a password.

  
After the above code is used to protect the worksheet, you can check the protection on the worksheet by opening it. Once you open the file and try to add some data to the worksheet, you will see the following dialog:

{{< table style="table-striped" >}}
|A dialog warning that a user can't modify the worksheet|
|:----|
|![image](5115175.png)|
{{< /table >}}

To work on the worksheet, unprotect the worksheet by selecting the **Protection**, then **Unprotect Sheet** from the **Tools** menu item.

After you select Unprotect Sheet menu item, a dialog will open that would prompt you to enter the password so that you may work on the worksheet as shown below:

![image](5115174.png)

### Protect a few Cells in the Worksheet Using Microsoft Excel

There might be certain scenarios where you need to lock a few cells only in the worksheet. If you want to lock some specific cells in the worksheet, you have to unlock all the other cells in the worksheet. All the cells in a worksheet are already initialized for locking, you may check this opening any excel file into MS Excel and click the **Format | Cells...** to show **Format Cells** dialog box and then click the **Protection** tab and see a checkbox labeled "Locked" is checked by default.

The following points describe how to lock a few cells using MS Excel. This method applies to Microsoft Office Excel 97, 2000, 2002, 2003 and greater versions.

1.  Select the entire worksheet by clicking the **Select All** button (the gray rectangle directly above the row number for row 1 and to the left of column letter A).
2.  Click **Cells** on the **Format** menu, click the **Protection** tab, and then clear the **Locked** checkbox.  
    This unlocks all the cells on the worksheet  
    If the **Cells** command is not available, parts of the worksheet may already be locked. On the **Tools** menu, point to **Protection**, and then click **Unprotect Sheet**.
3.  Select just the cells you want to lock and repeat step 2, but this time select the **Locked** checkbox.
4.  On the **Tools** menu, point to **Protection**, click **Protect Sheet** and then click **OK**.
5.  In the **Protect Sheet** dialog box, you have the option to specify a password and select the elements that you want users to be able to change.

### Protect a few Cells in the Worksheet Using Aspose Cells

In this method, we use Aspose.Cells API only to do the task.

Example: The following example exhibits how to protect a few cells in the worksheet. It unlocks all the cells in the worksheet first and then locks 3 cells (A1, B1, C1) in it. Finally, it protects the worksheet. The [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object contains a boolean property, [IsLocked](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/islocked). You can set [IsLocked](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/islocked) property to true or false and apply Column/Row.ApplyStyle() method to lock or unlock the row/column with your desired attributes.

### Protect a Row in the Worksheet

Aspose.Cells allows you to easily lock any row in the worksheet. Here, we can make use of [ApplyStyle()](https://apireference.aspose.com/net/cells/aspose.cells/row/methods/applystyle) method of [Aspose.Cells.Row](https://apireference.aspose.com/net/cells/aspose.cells/row) class to apply [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) to a particular row in the worksheet. This method takes two arguments: a [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object and [StyleFlag](https://apireference.aspose.com/net/cells/aspose.cells/styleflag) object which has all the members related to applied formatting.

The following example shows how to protect a row in the worksheet. It unlocks all the cells in the worksheet first and then locks the first row in it. Finally, it protects the worksheet. The [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object contains a boolean property, [IsLocked](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/islocked). You can set [IsLocked](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/islocked) property to true or false to lock or unlock the row/column using the [StyleFlag](https://apireference.aspose.com/net/cells/aspose.cells/styleflag) object.

### Protect a Column in the Worksheet

Aspose.Cells allows you to easily lock any column in the worksheet. Here, we can make use of [ApplyStyle()](https://apireference.aspose.com/net/cells/aspose.cells/column/methods/applystyle) method of [Aspose.Cells.Column](https://apireference.aspose.com/net/cells/aspose.cells/column) class to apply [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) to a particular column in the worksheet. This method takes two arguments: a [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object and [StyleFlag](https://apireference.aspose.com/net/cells/aspose.cells/styleflag) object which has all the members related to applied formatting.

The following example shows how to protect a column in the worksheet. It unlocks all the cells in the worksheet first and then locks the first column in it. Finally, it protects the worksheet. The [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object contains a boolean property, [IsLocked](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/islocked). You can set [IsLocked](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/islocked) property to true or false to lock or unlock the row/column using the [StyleFlag](https://apireference.aspose.com/net/cells/aspose.cells/styleflag) object.

### Allow Users to Edit Ranges

The following example shows how to allow users to edit a range in a protected worksheet.

