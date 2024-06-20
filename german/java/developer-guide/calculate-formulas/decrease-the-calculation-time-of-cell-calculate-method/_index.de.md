---
title: Verringerung der Berechnungszeit der Cell.Calculate Methode
type: docs
weight: 860
url: /de/java/decrease-the-calculation-time-of-cell-calculate-method/
---


Mögliche Verwendungsszenarien

Normalerweise empfehlen wir Benutzern, die Methode [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) einmal aufzurufen und dann die berechneten Werte der einzelnen Zellen abzurufen. Manchmal möchten Benutzer jedoch nicht die gesamte Arbeitsmappe berechnen. Sie möchten nur eine einzelne Zelle berechnen. Aspose.Cells bietet die Eigenschaft [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive), die auf **false** gesetzt werden kann und die die Berechnungszeit der einzelnen Zelle erheblich verringert. Denn wenn die rekursive Eigenschaft auf **true** gesetzt ist, werden bei jedem Aufruf alle Abhängigen von Zellen neu berechnet. Wenn die rekursive Eigenschaft jedoch auf **false** gesetzt ist, werden abhängige Zellen nur einmal berechnet und bei nachfolgenden Aufrufen nicht erneut berechnet.
## **Verringerung der Berechnungszeit der Cell.Calculate() Methode**
Der folgende Beispielcode veranschaulicht die Verwendung der Eigenschaft [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive). Bitte führen Sie diesen Code mit der angegebenen [Beispiel Exceldatei](5472288.xlsx) aus und überprüfen Sie die Konsolenausgabe. Sie werden feststellen, dass durch das Einstellen der rekursiven Eigenschaft auf **false** die Berechnungszeit erheblich verringert wurde. Lesen Sie auch die Kommentare, um diese Eigenschaft besser zu verstehen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Konsolenausgabe**
Dies ist die Konsolenausgabe des oben genannten Beispielcodes, wenn er mit der angegebenen [Beispiel Exceldatei](5472288.xlsx) auf unserem Rechner ausgeführt wird. Bitte beachten Sie, dass Ihr Ergebnis möglicherweise abweicht, aber die verstrichene Zeit nach Einstellung der rekursiven Eigenschaft auf **false** ist immer geringer als bei Einstellung auf **true**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
