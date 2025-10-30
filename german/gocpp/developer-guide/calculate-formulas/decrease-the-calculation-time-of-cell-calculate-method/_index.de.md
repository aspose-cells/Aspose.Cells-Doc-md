---
title: Reduzieren Sie die Berechnungszeit der Cell.Calculate Methode mit Golang über C++
linktitle: Verringerung der Berechnungszeit der Cell.Calculate
description: In diesem Artikel wird erläutert, wie die Aspose.Cells Bibliothek verwendet werden kann, um die Berechnungszeit der Zellberechnungsmethoden in Microsoft Excel zu reduzieren. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen können wir die von Aspose.Cells bereitgestellten Methoden nutzen, um die Zellberechnungsmethode zu optimieren und die Leistung zu verbessern. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Methoden zur Zellberechnung, Optimierung, Leistung, Verkürzung der Berechnungszeit
type: docs
weight: 100
url: /de/go-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Mögliche Verwendungsszenarien**

 Normalerweise empfehlen wir den Benutzern, die Methode [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) einmal aufzurufen und dann die berechneten Werte der einzelnen Zellen zu erhalten. Manchmal möchten die Benutzer jedoch nicht die gesamte Arbeitsmappe berechnen. Sie möchten nur eine einzelne Zelle berechnen. Aspose.Cells bietet die Eigenschaft [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/), die Sie auf **false** setzen können, was die Berechnungszeit der einzelnen Zellen erheblich verringert. Wenn die rekursive Eigenschaft auf **true** gesetzt ist, werden alle Abhängigkeiten der Zellen bei jedem Aufruf neu berechnet. Wenn die rekursive Eigenschaft jedoch **false** ist, werden abhängige Zellen nur einmal berechnet und nicht erneut bei nachfolgenden Aufrufen.

## **Verringerung der Berechnungszeit der Cell.Calculate() Methode**

 Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getrecursive/). Führen Sie diesen Code mit der bereitgestellten [Beispiel-Excel-Datei](5113710.xlsx) aus und prüfen Sie die Konsolenausgabe. Sie werden feststellen, dass das Setzen der rekursiven Eigenschaft auf **false** die Berechnungszeit erheblich verkürzt hat. Lesen Sie auch die Kommentare für ein besseres Verständnis dieser Eigenschaft.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod-1.go" >}}
## **Konsolenausgabe**

 Dies ist die Konsolenausgabe des oben genannten Beispielcodes, wenn er mit der bereitgestellten [Beispiel-Excel-Datei](5113710.xlsx) auf unserer Maschine ausgeführt wird. Beachten Sie, dass Ihre Ausgabe unterschiedlich sein kann, aber die nach der Einstellung der rekursiven Eigenschaft auf **false** verstrichene Zeit immer kürzer ist als bei **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
