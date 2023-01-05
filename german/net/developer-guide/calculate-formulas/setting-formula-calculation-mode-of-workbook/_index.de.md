---
title: Festlegen des Formelberechnungsmodus der Arbeitsmappe
type: docs
weight: 110
url: /de/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Mit Excel können Sie den Formelberechnungsmodus festlegen, d. h. die Art und Weise, wie Formeln berechnet werden. Es gibt drei mögliche Werte:

- Automatisch - neu berechnen, wenn etwas geändert wird und jedes Mal, wenn eine Arbeitsmappe geöffnet wird.
- Automatisch außer für Datentabellen - neu berechnen, wenn etwas geändert wird, aber Datentabellen weglassen.
- Manuell – nur neu berechnen, wenn der Benutzer dies explizit anfordert, indem er F9 oder STRG+ALT+F9 drückt, oder wenn die Arbeitsmappe gespeichert wird.

{{% /alert %}}

So stellen Sie den Formelberechnungsmodus in Microsoft Excel ein:

1.  Wählen**Formeln** und dann**Berechnungsoptionen**.
1. Wählen Sie eine der Optionen aus.

 Aspose.Cells können Sie auch die einstellen**Formelberechnungsmodus** verwenden[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) Modus-Eigenschaft. Sie können ihm die zuweisen[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)Enumeration, die einen der folgenden Werte hat:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
