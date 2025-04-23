---
title: Einstellen des Formelberechnungsmodus der Arbeitsmappe
description: Dieser Artikel zeigt, wie Sie den Formelberechnungsmodus einer Arbeitsmappe in Microsoft Excel mit der Aspose.Cells Bibliothek festlegen. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellte Methode verwenden, um den Formelberechnungsmodus festzulegen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Arbeitsmappe, Formelberechnungsmodus, Einstellungen
type: docs
weight: 110
url: /de/net/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Ihnen, den Formelberechnungsmodus festzulegen, d.h. die Art und Weise, wie Formeln berechnet werden. Es gibt drei mögliche Werte:

- Automatisch - Neu berechnen, wenn sich etwas ändert, und jedes Mal, wenn eine Arbeitsmappe geöffnet wird.
- Automatisch mit Ausnahme von Datentabellen - Neu berechnen, wenn sich etwas ändert, aber Auslassen von Datentabellen.
- Manuell - Nur neu berechnen, wenn der Benutzer dies explizit durch Drücken von F9 oder STRG+ALT+F9 anfordert oder wenn die Arbeitsmappe gespeichert wird.

{{% /alert %}}

Um den Formelberechnungsmodus in Microsoft Excel festzulegen:

1. Wählen Sie **Formeln** und dann **Berechnungsoptionen**.
1. Wählen Sie eine der Optionen aus.

Aspose.Cells ermöglicht Ihnen auch, den **Formelberechnungsmodus** mit Hilfe des [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode)-Modus-Attributs festzulegen. Sie können ihm die [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)-Enumeration zuweisen, die einen der folgenden Werte hat:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
