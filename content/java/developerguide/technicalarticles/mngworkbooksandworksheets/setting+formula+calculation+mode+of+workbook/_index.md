---
title : "Setting Formula Calculation Mode of Workbook" 
description : "" 
weight : 16427 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngworkbooksandworksheets/setting+formula+calculation+mode+of+workbook/
---

# Aspose.Cells for Java : Setting Formula Calculation Mode of Workbook


Microsoft Excel allows you to set the formula calculation mode, that is, the way formulas are calculated. There are three possible values:

*   Automatic - recalculate whenever something is changed, and every time a workbook is opened.
*   Automatic except for data tables - recalculate whenever something is changed, but leaving out data tables.
*   Manual - recalculate only when the user explicitly requests it by pressing F9 or CTRL+ALT+F9, or when the workbook is saved.

To set the formula calculation mode in Microsoft Excel:

1.  Select **Formulas** and then **Calculation Options**.
2.  Select one of the options.

Aspose.Cells also allows you to set the **Formula Calculation Mode** using the [Workbook.getSettings().setCalcMode()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#CalcMode) property. You can assign it the [CalcModeType](https://apireference.aspose.com/java/cells/com.aspose.cells/CalcModeType) enumeration which has one of the following values:

*   [CalcModeType.AUTOMATIC](https://apireference.aspose.com/java/cells/com.aspose.cells/calcmodetype#AUTOMATIC)
*   [CalcModeType.AUTOMATIC\_EXCEPT\_TABLE](https://apireference.aspose.com/java/cells/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
*   [CalcModeType.MANUAL](https://apireference.aspose.com/java/cells/com.aspose.cells/calcmodetype#MANUAL)

The following sample code first creates a workbook, then it sets the formula calculation mode to **Manual** and saves the workbook as output Excel file on disk.

**The output file. Note the formula calculation mode.**  
![](https://docs2.aspose.com/cells/java/attachments/5276656/5473046.png)


