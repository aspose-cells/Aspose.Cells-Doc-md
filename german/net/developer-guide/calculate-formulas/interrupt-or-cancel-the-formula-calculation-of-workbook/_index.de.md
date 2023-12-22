---
title: Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab
description: In diesem Artikel wird erläutert, wie Sie die Bibliothek Aspose.Cells verwenden, um Formelberechnungen von Arbeitsmappen in Microsoft Excel zu unterbrechen oder abzubrechen. Indem wir eine vorhandene Excel-Datei laden oder eine neue erstellen, können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um die Formelberechnung zu unterbrechen oder abzubrechen und das Ergebnis zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /de/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
##  **Mögliche Nutzungsszenarien**

Aspose.Cells bietet einen Mechanismus zum Unterbrechen oder Abbrechen der Formelberechnung der Arbeitsmappe mithilfe von[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)Methode. Dies ist nützlich, wenn die Formelberechnung der Arbeitsmappe zu viel Zeit in Anspruch nimmt und Sie die Verarbeitung abbrechen möchten.

##  **Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab**

Der folgende Beispielcode implementiert die[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)Methode von[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) Klasse. Innerhalb dieser Methode wird der Zellenname mithilfe von Zeilen- und Spaltenindexparametern ermittelt. Wenn der Zellenname B8 lautet, wird der Berechnungsvorgang durch den Aufruf von unterbrochen[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)Methode. Einmal, die konkrete Klasse von[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)Klasse implementiert ist, wird ihre Instanz zugewiesen[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)Eigentum. Endlich,[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)wird im Vorbeigehen aufgerufen[**Berechnungsoptionen**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) als Parameter. Bitte sehen Sie sich ... an[Beispiel-Excel-Datei](51740731.xlsx) wird im Code sowie in der Konsolenausgabe des unten angegebenen Codes als Referenz verwendet.

##  **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

##  **Konsolenausgabe**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
