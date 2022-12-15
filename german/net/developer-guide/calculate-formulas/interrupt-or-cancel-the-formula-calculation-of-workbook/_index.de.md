---
title: Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab
type: docs
weight: 50
url: /de/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells bietet einen Mechanismus zum Unterbrechen oder Abbrechen der Formelberechnung der Arbeitsmappe mithilfe von[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)Methode. Dies ist nützlich, wenn die Formelberechnung der Arbeitsmappe zu viel Zeit in Anspruch nimmt und Sie ihre Verarbeitung abbrechen möchten.

## **Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab**

Der folgende Beispielcode implementiert die[**VorBerechnen()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)Methode von[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) Klasse. Innerhalb dieser Methode findet es den Zellennamen mithilfe von Zeilen- und Spaltenindexparametern. Wenn der Zellenname B8 ist, unterbricht es den Berechnungsprozess, indem es die aufruft[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)Methode. Einmal die konkrete Klasse von[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)Klasse implementiert ist, wird ihre Instanz zugewiesen[**Berechnungsoptionen.Berechnungsmonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)Eigentum. Endlich,[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)wird durch Vorbeigehen aufgerufen[**Berechnungsoptionen**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) als Parameter. Bitte sehen Sie sich ... an[Beispiel-Excel-Datei](51740731.xlsx)innerhalb des Codes sowie der Konsolenausgabe des unten angegebenen Codes als Referenz verwendet.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
