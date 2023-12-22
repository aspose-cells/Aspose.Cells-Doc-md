---
title: Festlegen des Formelberechnungsmodus der Arbeitsmappe
description: In diesem Artikel wird erläutert, wie Sie den Formelberechnungsmodus einer Arbeitsmappe in Microsoft Excel mit der Bibliothek Aspose.Cells festlegen. Durch das Laden einer vorhandenen Excel-Datei oder das Erstellen einer neuen Excel-Datei können wir die von Aspose.Cells bereitgestellte Methode verwenden, um den Formelberechnungsmodus festzulegen und das Ergebnis zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /de/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft In Excel können Sie den Formelberechnungsmodus festlegen, also die Art und Weise, wie Formeln berechnet werden. Es gibt drei mögliche Werte:

- Automatisch – Neuberechnung, wenn etwas geändert wird und jedes Mal, wenn eine Arbeitsmappe geöffnet wird.
- Automatisch, außer bei Datentabellen – wird bei jeder Änderung neu berechnet, Datentabellen werden jedoch weggelassen.
- Manuell – Neuberechnung nur, wenn der Benutzer dies ausdrücklich durch Drücken von F9 oder STRG+ALT+F9 anfordert oder wenn die Arbeitsmappe gespeichert wird.

{{% /alert %}}

So legen Sie den Formelberechnungsmodus in Microsoft Excel fest:

1.  Wählen**Formeln** und dann *Berechnungsoptionen**.
1. Wählen Sie eine der Optionen aus.

 Aspose.Cells ermöglicht Ihnen auch die Einstellung**Formelberechnungsmodus** verwenden[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) mode-Eigenschaft. Sie können es zuweisen[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)Aufzählung, die einen der folgenden Werte hat:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
