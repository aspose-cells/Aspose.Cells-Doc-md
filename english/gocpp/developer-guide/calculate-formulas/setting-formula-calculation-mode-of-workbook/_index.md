---
title: Setting Formula Calculation Mode of Workbook with Golang via C++
linktitle: Setting Formula Calculation Mode of Workbook
description: This article introduces how to set the formula calculation mode of a workbook in Microsoft Excel with Aspose.Cells library using C++. By loading an existing Excel file or creating a new Excel file, we can use the method provided by Aspose.Cells to set the formula calculation mode and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings, C++
type: docs
weight: 110
url: /go-cpp/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells also allows you to set the **Formula Calculation Mode** using [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getcalculationmode/) mode property. You can assign it the [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/) enumeration which has one of the following values:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaCalculationModeOfWorkbook.go" >}}