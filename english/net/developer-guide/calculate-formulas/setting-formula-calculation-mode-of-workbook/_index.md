---
title: Setting Formula Calculation Mode of Workbook
description: This article introduces how to set the formula calculation mode of a workbook in Microsoft Excel with the Aspose.Cells library. By loading an existing Excel file or creating a new Excel file, we can use the method provided by Aspose.Cells to set the formula calculation mode and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /net/setting-formula-calculation-mode-of-workbook/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel allows you to set the formula calculation mode, that is, the way formulas are calculated. There are three possible values:

- Automatic – recalculate whenever something changes, and every time a workbook is opened.  
- Automatic except for data tables – recalculate whenever something changes, but excluding data tables.  
- Manual – recalculate only when the user explicitly requests it by pressing F9 or CTRL+ALT+F9, or when the workbook is saved.

{{% /alert %}}

To set the formula calculation mode in Microsoft Excel:

1. Select **Formulas** and then **Calculation Options**.  
2. Select one of the options.

Aspose.Cells also allows you to set the **Formula Calculation Mode** using the [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) property. You can assign it the [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype) enumeration, which has one of the following values:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
