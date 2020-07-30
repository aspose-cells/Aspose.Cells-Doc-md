---
title : "Accessing Worksheet" 
description : "" 
weight : 16605 
toc : false
type: docs
url: /net/developerguide/griddesktop/worksheet/accessing+worksheet/
---

# Aspose.Cells for .NET : Accessing Worksheet


A worksheet is an integral part of an Excel file. In fact, an Excel file is composed of one or more worksheets. Each worksheet can be composed of up tp 65,536 rows and 256 columns only. It is the worksheet that holds data in an Excel file.

Aspose.Cells.GridDesktop can create and manipulate existing and new Excel files so there is, of course, a way to access worksheets using Aspose.Cells.GridDesktop. This topic discusses how.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Using Worksheet Index](#using-worksheet-index)
*   2 [Using Worksheet Name](#using-worksheet-name)
*   3 [Accessing an Active Worksheet](#accessing-an-active-worksheet)
    *   3.1 [Using the AcriveSheetIndex Property](#using-the-acrivesheetindex-property)
    *   3.2 [Using the GetActiveWorksheet Method](#using-the-getactiveworksheet-method)
{{< /panel >}}
 

 

## Using Worksheet Index

Developers can access an instance of any Worksheet by using the worksheet index of any desired worksheet as shown below in the example. This approach is good for iterating through a number of worksheets in an Excel file.

## Using Worksheet Name

If the name of the worksheet is known, it is possible to access a worksheet using its name as shown below.

## Accessing an Active Worksheet

It is possbile that an Excel file will have more than one worksheet. The one htat a user is working on is called the active worksheet. It is possible to access the active sheet.

To access an active worksheet, Aspose.Cells.GridDesktop offers two approaches:

### Using the AcriveSheetIndex Property

One way to access an active worksheet using Aspose.Cells.GridDesktop control is to use the GridDesktop control's `ActiveSheetIndex` property. Using this property, it is possible to get the index of the active worksheet in the Aspose.Cells.GridDesktop control. Then that index can be used to access the worksheet in a traditional manner as shown below.

### Using the GetActiveWorksheet Method

The other approach is to call the GridDesktop control's `GetActiveWorksheet` method. This method provides a reference of the worksheet that is currently active in Aspose.Cells.GridDesktop control as shown below.

