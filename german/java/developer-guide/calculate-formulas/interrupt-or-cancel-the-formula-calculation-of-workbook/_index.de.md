---
title: Unterbrechen oder Abbrechen der Formelberechnung des Arbeitsblatts
type: docs
weight: 30
url: /de/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet eine Möglichkeit, die Formelberechnung der Arbeitsmappe mithilfe der Methode „interrupt()“ der Klasse [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) zu unterbrechen oder abzubrechen. Dies ist nützlich, wenn die Formelberechnung der Arbeitsmappe zu viel Zeit in Anspruch nimmt und Sie deren Verarbeitung abbrechen möchten.

## **Unterbrechen oder Abbrechen der Formelberechnung des Arbeitsbuchs**

Der folgende Beispielcode implementiert die Methode [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) der Klasse [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). Innerhalb dieser Methode wird der Zellenname mithilfe der Parameter Zeilen- und Spaltenindex ermittelt. Wenn der Zellenname B8 ist, unterbricht er den Berechnungsprozess, indem die Methode AbstractCalculationMonitor.interrupt() aufgerufen wird. Sobald die konkrete Klasse der Klasse [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) implementiert ist, wird deren Instanz der Eigenschaft [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor) zugewiesen. Schließlich wird [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) aufgerufen, indem [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) als Parameter übergeben wird. Bitte sehen Sie sich auch die verwendete [Beispiel Exceldatei](51740744.xlsx) im Code sowie die Konsolenausgabe des folgenden Codes als Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
