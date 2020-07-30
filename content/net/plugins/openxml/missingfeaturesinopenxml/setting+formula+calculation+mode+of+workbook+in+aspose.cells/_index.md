---
title : "Setting Formula Calculation Mode of Workbook in Aspose.Cells" 
description : "" 
weight : 16888 
toc : false
type: docs
url: /net/plugins/openxml/missingfeaturesinopenxml/setting+formula+calculation+mode+of+workbook+in+aspose.cells/
---

# Aspose.Cells for .NET : Setting Formula Calculation Mode of Workbook in Aspose.Cells


Microsoft Excel allows you to set the formula calculation mode, that is, the way formulas are calculated. There are three possible values:

*   Automatic - recalculate whenever something is changed, and every time a workbook is opened.
*   Automatic except for data tables - recalculate whenever something is changed, but leaving out data tables.
*   Manual - recalculate only when the user explicitly requests it by pressing F9 or CTRL+ALT+F9, or when the workbook is saved.

To set the formula calculation mode in Microsoft Excel:

1.  Select **Formulas** and then **Calculation Options**.
2.  Select one of the options.

Aspose.Cells also allows you to set the **Formula Calculation Mode** using `Workbook.Settings.CalcMode` mode property. You can assign it the `CalcModeType` enumeration which has one of the following values:

*   `CalcModeType.Automatic`
*   `CalcModeType.AutomaticExceptTable`
*   `CalcModeType.Manual`

The following sample code first creates a workbook, then it sets the formula calculation mode to **Manual** and saves the workbook as output Excel file on disk.

**C#**

string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";//Create a workbookWorkbook workbook = new Workbook();//Set the Formula Calculation Mode to Manualworkbook.Settings.CalcMode = CalcModeType.Manual;//Save the workbookworkbook.Save(FileName, SaveFormat.Xlsx);

### Download Sample Code

*   [Codeplex](https://asposeopenxml.codeplex.com/SourceControl/latest#Aspose.Cells Features missing in OpenXML/Setting Formula Calculation Mode/)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c/view/SourceCode#content)

### Download Running Example

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)

