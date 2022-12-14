---
title: Festlegen des Formelberechnungsmodus der Arbeitsmappe
type: docs
weight: 130
url: /de/java/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Mit Excel können Sie den Formelberechnungsmodus festlegen, d. h. die Art und Weise, wie Formeln berechnet werden. Es gibt drei mögliche Werte:

- Automatisch - neu berechnen, wenn etwas geändert wird und jedes Mal, wenn eine Arbeitsmappe geöffnet wird.
- Automatisch außer für Datentabellen - neu berechnen, wenn etwas geändert wird, aber Datentabellen weglassen.
- Manuell – nur neu berechnen, wenn der Benutzer dies explizit anfordert, indem er F9 oder STRG+ALT+F9 drückt, oder wenn die Arbeitsmappe gespeichert wird.

{{% /alert %}}

So stellen Sie den Formelberechnungsmodus in Microsoft Excel ein:

1.  Auswählen**Formeln** und dann**Berechnungsoptionen**.
1. Wählen Sie eine der Optionen aus.

 Aspose.Cells können Sie auch die einstellen**Formelberechnungsmodus** Verwendung der[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) Eigentum. Sie können ihm die zuweisen[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)Enumeration, die einen der folgenden Werte hat:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

 Der folgende Beispielcode erstellt zuerst eine Arbeitsmappe und setzt dann den Formelberechnungsmodus auf**Handbuch** und speichert die Arbeitsmappe als Excel-Ausgabedatei auf der Festplatte.

**Die Ausgabedatei. Beachten Sie den Formelberechnungsmodus.**

![todo: Bild_alt_Text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
