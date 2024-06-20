---
title: Einstellen des Formelberechnungsmodus der Arbeitsmappe
type: docs
weight: 130
url: /de/java/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells ermöglicht es Ihnen auch, den **Formelberechnungsmodus** mit der [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) Eigenschaft festzulegen. Sie können ihr die [**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) Enumeration zuweisen, die einen der folgenden Werte hat:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

Der folgende Beispielcode erstellt zunächst eine Arbeitsmappe, setzt dann den Formelberechnungsmodus auf **Manuell** und speichert die Arbeitsmappe als Ausgabedatei auf der Festplatte.

**Die Ausgabedatei. Beachten Sie den Formelberechnungsmodus.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
