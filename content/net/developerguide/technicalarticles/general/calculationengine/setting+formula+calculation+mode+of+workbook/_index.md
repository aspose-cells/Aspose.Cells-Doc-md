---
title : "Setting Formula Calculation Mode of Workbook" 
description : "" 
weight : 20549 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/calculationengine/setting+formula+calculation+mode+of+workbook/
---

# Aspose.Cells for .NET : Setting Formula Calculation Mode of Workbook


Microsoft Excel allows you to set the formula calculation mode, that is, the way formulas are calculated. There are three possible values:

*   Automatic - recalculate whenever something is changed, and every time a workbook is opened.
*   Automatic except for data tables - recalculate whenever something is changed, but leaving out data tables.
*   Manual - recalculate only when the user explicitly requests it by pressing F9 or CTRL+ALT+F9, or when the workbook is saved.

To set the formula calculation mode in Microsoft Excel:

1.  Select **Formulas** and then **Calculation Options**.
2.  Select one of the options.

Aspose.Cells also allows you to set the **Formula Calculation Mode** using [Workbook.Settings.CalcMode](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/calcmode) mode property. You can assign it the [CalcModeType](https://apireference.aspose.com/net/cells/aspose.cells/calcmodetype) enumeration which has one of the following values:

*   CalcModeType.Automatic
*   CalcModeType.AutomaticExceptTable
*   CalcModeType.Manual

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Formula-Calculation-Mode.png](https://docs2.aspose.com/cells/net/attachments/5017552/5112509.png) (image/png)  

