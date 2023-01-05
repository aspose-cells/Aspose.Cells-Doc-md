---
title: Verringern Sie die Berechnungszeit von Cell. Berechnungsmethode
type: docs
weight: 100
url: /de/net/decrease-the-calculation-time-of-cell-calculate-method/
---
## **Mögliche Nutzungsszenarien**

Normalerweise empfehlen wir Benutzern anzurufen[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)Methode einmal und erhalte dann die berechneten Werte der einzelnen Zellen. Aber manchmal möchten Benutzer nicht die gesamte Arbeitsmappe berechnen. Sie wollen nur eine einzelne Zelle berechnen. Aspose.Cells bietet[**Berechnungsoptionen.Rekursiv**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) Eigenschaft, die Sie festlegen können**FALSCH** und es wird die Berechnungszeit der einzelnen Zelle erheblich verkürzen. Denn wenn die rekursive Eigenschaft auf gesetzt ist**wahr** , dann werden alle abhängigen Zellen bei jedem Aufruf neu berechnet. Aber wenn die rekursive Eigenschaft ist**FALSCH**, dann werden abhängige Zellen nur einmal berechnet und bei nachfolgenden Aufrufen nicht erneut berechnet.

## **Verringern Sie die Berechnungszeit der Methode Cell.Calculate()**

 Der folgende Beispielcode veranschaulicht die Verwendung von[**Berechnungsoptionen.Rekursiv**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) Eigentum. Bitte führen Sie diesen Code mit dem angegebenen aus[Excel-Beispieldatei](5113710.xlsx) und überprüfen Sie die Konsolenausgabe. Sie werden feststellen, dass die rekursive Eigenschaft auf eingestellt wird**FALSCH**hat die Berechnungszeit erheblich verkürzt. Bitte lesen Sie auch die Kommentare für ein besseres Verständnis dieser Eigenschaft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Konsolenausgabe**

 Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem angegebenen ausgeführt wird[Excel-Beispieldatei](5113710.xlsx) auf unserer Maschine. Bitte beachten Sie, dass Ihre Ausgabe abweichen kann, aber die verstrichene Zeit nach dem Setzen der rekursiven Eigenschaft auf**FALSCH** wird immer kleiner sein als eingestellt**wahr**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
