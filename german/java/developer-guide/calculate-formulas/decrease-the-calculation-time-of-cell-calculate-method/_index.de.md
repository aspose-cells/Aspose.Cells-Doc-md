---
title: Verringern Sie die Berechnungszeit von Cell. Berechnungsmethode
type: docs
weight: 860
url: /de/java/decrease-the-calculation-time-of-cell-calculate-method/
---
Mögliche Nutzungsszenarien

 Normalerweise empfehlen wir Benutzern anzurufen[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\) ) Methode einmal und erhalte dann die errechneten Werte der einzelnen Zellen. Aber manchmal möchten Benutzer nicht die gesamte Arbeitsmappe berechnen. Sie wollen nur eine einzelne Zelle berechnen. Aspose.Cells bietet[Berechnungsoptionen.Rekursiv](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) Eigenschaft, die Sie festlegen können**FALSCH**und es wird die Berechnungszeit der einzelnen Zelle erheblich verkürzen. Denn wenn die rekursive Eigenschaft auf gesetzt ist**Stimmt**dann werden alle abhängigen Zellen bei jedem Aufruf neu berechnet. Aber wenn die rekursive Eigenschaft auf gesetzt ist**FALSCH**, dann werden abhängige Zellen nur einmal berechnet und bei nachfolgenden Aufrufen nicht erneut berechnet.
## **Verringern Sie die Berechnungszeit der Methode Cell.Calculate()**
 Der folgende Beispielcode veranschaulicht die Verwendung von[Berechnungsoptionen.Rekursiv](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) Eigentum. Bitte führen Sie diesen Code mit dem angegebenen aus[Excel-Beispieldatei](5472288.xlsx) und überprüfen Sie die Konsolenausgabe. Sie werden feststellen, dass die rekursive Eigenschaft auf eingestellt wird**FALSCH**hat die Berechnungszeit erheblich verkürzt. Bitte lesen Sie auch die Kommentare für ein besseres Verständnis dieser Eigenschaft.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Konsolenausgabe**
 Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem angegebenen ausgeführt wird[Excel-Beispieldatei](5472288.xlsx) auf unserer Maschine. Bitte beachten Sie, dass Ihre Ausgabe abweichen kann, aber die verstrichene Zeit nach dem Setzen der rekursiven Eigenschaft auf**FALSCH** wird immer kleiner sein als eingestellt**Stimmt**.



{{< highlight "java" >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
