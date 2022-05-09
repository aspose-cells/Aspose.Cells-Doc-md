---
title: Setting Formula Calculation Mode of Workbook
type: docs
weight: 110
url: /net/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells also allows you to set the **Formula Calculation Mode** using [**FormulaSettings.CalculationMode**](https://apireference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) mode property. You can assign it the [**CalcModeType**](https://apireference.aspose.com/cells/net/aspose.cells/calcmodetype) enumeration which has one of the following values:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
