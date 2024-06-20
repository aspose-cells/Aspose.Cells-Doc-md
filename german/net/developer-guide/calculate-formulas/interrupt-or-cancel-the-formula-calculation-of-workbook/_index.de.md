---
title: Unterbrechen oder Abbrechen der Formelberechnung des Arbeitsblatts
description: In diesem Artikel wird erläutert, wie die Aspose.Cells Bibliothek verwendet werden kann, um Formelberechnungen von Arbeitsmappen in Microsoft Excel zu unterbrechen oder abzubrechen. Indem wir eine vorhandene Excel Datei laden oder eine neue erstellen, können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um die Formelberechnung zu unterbrechen oder abzubrechen und das Ergebnis zu erhalten. Abschließend speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Arbeitsmappen, Formelberechnungen, Unterbrechungen, Stornierungen
type: docs
weight: 50
url: /de/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet einen Mechanismus, um die Formelberechnung der Arbeitsmappe mit der Methode [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) zu unterbrechen oder abzubrechen. Dies ist nützlich, wenn die Formelberechnung der Arbeitsmappe zu viel Zeit in Anspruch nimmt und Sie deren Verarbeitung abbrechen möchten.

## **Unterbrechen oder Abbrechen der Formelberechnung des Arbeitsbuchs**

Der folgende Beispielcode implementiert die Methode [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) der Klasse [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor). In dieser Methode findet sie den Zellnamen unter Verwendung der Zeilen- und Spaltenindexparameter. Wenn der Zellname B8 ist, unterbricht sie den Berechnungsprozess durch Aufrufen der Methode [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). Sobald die konkrete Klasse der Klasse [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) implementiert ist, wird ihre Instanz der Eigenschaft [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor) zugewiesen. Schließlich wird [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) aufgerufen, indem [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) als Parameter übergeben wird. Bitte beachten Sie die [Beispiel-Excel-Datei](51740731.xlsx), die innerhalb des Codes verwendet wird, sowie die Konsolenausgabe des folgenden Codes zur Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
