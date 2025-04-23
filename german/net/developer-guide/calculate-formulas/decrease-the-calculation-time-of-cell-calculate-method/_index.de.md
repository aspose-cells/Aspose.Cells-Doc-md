---
title: Verringerung der Berechnungszeit der Cell.Calculate Methode
description: In diesem Artikel wird erläutert, wie die Aspose.Cells Bibliothek verwendet werden kann, um die Berechnungszeit der Zellberechnungsmethoden in Microsoft Excel zu reduzieren. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen können wir die von Aspose.Cells bereitgestellten Methoden nutzen, um die Zellberechnungsmethode zu optimieren und die Leistung zu verbessern. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Methoden zur Zellberechnung, Optimierung, Leistung, Verkürzung der Berechnungszeit
type: docs
weight: 100
url: /de/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Mögliche Verwendungsszenarien**

Normalerweise empfehlen wir Benutzern, die Methode [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) einmal aufzurufen und dann die berechneten Werte der einzelnen Zellen zu erhalten. Manchmal möchten Benutzer jedoch nicht das gesamte Arbeitsblatt berechnen. Sie möchten nur eine einzelne Zelle berechnen. Aspose.Cells bietet die Eigenschaft [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive), die Sie auf **false** setzen können, um die Berechnungszeit der einzelnen Zelle erheblich zu verringern. Denn wenn die rekursive Eigenschaft auf **true** gesetzt ist, werden alle Abhängigen von Zellen bei jedem Aufruf neu berechnet. Wenn die rekursive Eigenschaft jedoch auf **false** gesetzt ist, werden abhängige Zellen nur einmal berechnet und bei nachfolgenden Aufrufen nicht erneut berechnet.

## **Verringerung der Berechnungszeit der Cell.Calculate() Methode**

Der folgende Beispielcode veranschaulicht die Verwendung der [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)-Eigenschaft. Bitte führen Sie diesen Code mit der angegebenen [Beispiel-Excel-Datei] (5113710.xlsx) aus und überprüfen Sie die Konsolenausgabe. Sie werden feststellen, dass die Einstellung der rekursiven Eigenschaft auf **false** die Berechnungszeit erheblich verringert hat. Lesen Sie bitte auch die Kommentare für ein besseres Verständnis dieser Eigenschaft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der gegebenen [Beispiel-Excel-Datei] (5113710.xlsx) auf unserer Maschine ausgeführt wird. Bitte beachten Sie, dass Ihr Output abweichen kann, aber die verstrichene Zeit nach Einstellen der rekursiven Eigenschaft auf **false** wird immer kürzer sein als bei Einstellung auf **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
