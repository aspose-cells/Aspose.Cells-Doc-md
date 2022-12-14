---
title: Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab
type: docs
weight: 30
url: /de/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells bietet einen Mechanismus zum Unterbrechen oder Abbrechen der Formelberechnung der Arbeitsmappe mithilfe der Methode interrupt() der[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) Klasse. Dies ist nützlich, wenn die Formelberechnung der Arbeitsmappe zu viel Zeit in Anspruch nimmt und Sie ihre Verarbeitung abbrechen möchten.

## **Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab**

Der folgende Beispielcode implementiert die[**vorherBerechnen()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) Methode der[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)Klasse. Innerhalb dieser Methode findet es den Zellennamen mithilfe von Zeilen- und Spaltenindexparametern. Wenn der Zellenname B8 ist, unterbricht es den Berechnungsprozess, indem es die Methode AbstractCalculationMonitor.interrupt() aufruft. Einmal die konkrete Klasse von[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)Klasse implementiert ist, wird ihre Instanz zugewiesen[**Berechnungsoptionen.Berechnungsmonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)Eigentum. Endlich,[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) wird durch Vorbeigehen aufgerufen[**Berechnungsoptionen**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)als Parameter. Bitte sehen Sie sich ... an[Beispiel-Excel-Datei](51740744.xlsx)innerhalb des Codes sowie der Konsolenausgabe des unten angegebenen Codes als Referenz verwendet.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
