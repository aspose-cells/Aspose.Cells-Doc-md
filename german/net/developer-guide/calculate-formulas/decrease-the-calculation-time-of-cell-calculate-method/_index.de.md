---
title: Verringern Sie die Berechnungszeit von Cell. Berechnen Sie die Methode
description: In diesem Artikel wird erläutert, wie Sie die Bibliothek Aspose.Cells verwenden, um die Berechnungszeit von Zellberechnungsmethoden in Microsoft Excel zu verkürzen. Durch das Laden einer vorhandenen Excel-Datei oder das Erstellen einer neuen können wir die von Aspose.Cells bereitgestellten Methoden nutzen, um die Zellberechnungsmethode zu optimieren und ihre Leistung zu verbessern. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /de/net/decrease-the-calculation-time-of-cell-calculate-method/
---
##  **Mögliche Nutzungsszenarien**

Normalerweise empfehlen wir Benutzern, anzurufen[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)Methode einmal ausführen und dann die berechneten Werte der einzelnen Zellen erhalten. Manchmal möchten Benutzer jedoch nicht die gesamte Arbeitsmappe berechnen. Sie wollen nur eine einzelne Zelle berechnen. Aspose.Cells bietet[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) Eigenschaft, die Sie festlegen können**FALSCH**und es wird die Berechnungszeit einzelner Zellen erheblich verkürzen. Denn wenn die rekursive Eigenschaft auf *true** gesetzt ist, werden alle abhängigen Zellen bei jedem Aufruf neu berechnet. Wenn die rekursive Eigenschaft jedoch *false** ist, werden abhängige Zellen nur einmal berechnet und bei nachfolgenden Aufrufen nicht erneut berechnet.

##  **Verringern Sie die Berechnungszeit der Methode Cell.Calculate()**

 Der folgende Beispielcode veranschaulicht die Verwendung von[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) Eigentum. Bitte führen Sie diesen Code mit den angegebenen aus[Beispiel-Excel-Datei](5113710.xlsx) und überprüfen Sie die Konsolenausgabe. Sie werden feststellen, dass die rekursive Eigenschaft auf eingestellt ist**FALSCH**hat die Berechnungszeit erheblich verkürzt. Bitte lesen Sie auch die Kommentare, um diese Immobilie besser zu verstehen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

##  **Konsolenausgabe**

 Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem angegebenen ausgeführt wird[Beispiel-Excel-Datei](5113710.xlsx) auf unserer Maschine. Bitte beachten Sie, dass Ihre Ausgabe abweichen kann, jedoch die verstrichene Zeit nach dem Festlegen der rekursiven Eigenschaft auf**FALSCH**wird immer kleiner sein, als es auf *true** zu setzen.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
