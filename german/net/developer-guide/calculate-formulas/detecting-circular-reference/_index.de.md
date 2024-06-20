---
title: Erkennung von zirkulären Verweisen
description: Dieser Artikel erläutert, wie die Aspose.Cells Bibliothek verwendet werden kann, um zirkuläre Verweise in Microsoft Excel zu erkennen. Durch Laden einer vorhandenen Excel Datei oder das Erstellen einer neuen können wir die von Aspose.Cells bereitgestellte Methode verwenden, um zirkuläre Verweise zu erkennen und die Ergebnisse zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, zirkuläre Verweise, Erkennung
type: docs
weight: 70
url: /de/net/detecting-circular-reference/
---

## **Einführung**

Arbeitsmappen können zirkuläre Verweise enthalten, und manchmal besteht die Notwendigkeit festzustellen, ob zirkuläre Verweise vorliegen oder nicht.

## **Konzept zur Erkennung des zirkulären Verweises**

Zirkuläre Verweise können nur erkannt werden, wenn die Formel berechnet wird, da die Verweise einer Formel in der Regel vom berechneten Ergebnis anderer Teile oder anderer Formeln abhängen. Daher stellen wir neue APIs für diese Anforderung bereit (zum Sammeln von Zellen mit zirkulären Verweisen) im Prozess der Formelberechnung:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Stellt die Berechnung relevanter Daten über eine berechnete Zelle dar

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): wird vom Formelberechnungsmotor aufgerufen, wenn zirkuläre Verweise auftreten, das Element im Enumerator ist [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) Objekte, die alle Zellen in einem Kreis darstellen. Der zurückgegebene Wert gibt an, ob der Formelmotor diese Zellen nach diesem Aufruf in der Kreisberechnung berechnen muss.

Benutzer können diese zirkulären Verweise bei der Implementierung der Methode [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) sammeln.

Die Quellbeispieldatei kann unter folgendem Link heruntergeladen werden:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definition der *CircularMonitor* Klasse, die von der [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)-Klasse abgeleitet ist, lautet wie folgt:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
