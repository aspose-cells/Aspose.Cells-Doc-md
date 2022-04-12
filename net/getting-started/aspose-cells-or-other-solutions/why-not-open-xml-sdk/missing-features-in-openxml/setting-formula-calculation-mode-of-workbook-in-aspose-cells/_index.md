---
title: Setting Formula Calculation Mode of Workbook in Aspose.Cells
type: docs
weight: 100
url: /net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel allows you to set the formula calculation mode, that is, the way formulas are calculated. There are three possible values:

- Automatic - recalculate whenever something is changed, and every time a workbook is opened.
- Automatic except for data tables - recalculate whenever something is changed, but leaving out data tables.
- Manual - recalculate only when the user explicitly requests it by pressing F9 or CTRL+ALT+F9, or when the workbook is saved.

{{% /alert %}} 

To set the formula calculation mode in Microsoft Excel:

1. Select **Formulas** and then **Calculation Options**.
1. Select one of the options.

Aspose.Cells also allows you to set the **Formula Calculation Mode** using Workbook.Settings.CalcMode mode property. You can assign it the CalcModeType enumeration which has one of the following values:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

The following sample code first creates a workbook, then it sets the formula calculation mode to **Manual** and saves the workbook as output Excel file on disk.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.CalcMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Download Sample Code**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Download Running Example**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
