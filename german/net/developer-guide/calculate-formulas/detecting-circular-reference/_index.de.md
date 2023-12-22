---
title: Erkennen von Zirkelverweisen
description: In diesem Artikel wird erläutert, wie Sie die Bibliothek Aspose.Cells verwenden, um Zirkelverweise in Microsoft Excel zu erkennen. Indem wir eine vorhandene Excel-Datei laden oder eine neue erstellen, können wir die von Aspose.Cells bereitgestellte Methode verwenden, um Zirkelverweise zu erkennen und die Ergebnisse zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /de/net/detecting-circular-reference/
---
##  **Einführung**

Arbeitsmappen können Zirkelverweise enthalten und manchmal muss festgestellt werden, ob Zirkelverweise vorhanden sind oder nicht.

##  **Konzept hinter der Erkennung des Zirkelverweises**

Zirkelbezüge können nur bei der Berechnung der Formel erkannt werden, da die Bezüge einer Formel üblicherweise vom berechneten Ergebnis anderer Teile oder anderer Formeln abhängen. Deshalb stellen wir für diese Anforderung (zum Sammeln von Zellen mit Zirkelbezügen) im Prozess der Formelberechnung neue APIs bereit:

[**Berechnungszelle**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Stellt die Berechnung relevanter Daten zu einer berechneten Zelle dar

[**AbstractCalculationMonitor.OnCircular(IEnumerator CircularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): wird von der Formelberechnungs-Engine aufgerufen, wenn Zirkelverweise auf das Element im Enumerator stoßen[**Berechnungszelle**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) Objekte, die alle Zellen in einem Kreis darstellen. Der zurückgegebene Wert gibt an, ob die Formel-Engine diese Zellen nach diesem Aufruf kreisförmig berechnen muss.

 Der Benutzer kann diese Zirkelverweise bei der Implementierung von sammeln[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) Methode.

Die Quellbeispieldatei kann über den folgenden Link heruntergeladen werden:

[Kreisformeln.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definition von*CircularMonitor* Klasse, von der abgeleitet ist[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) Klasse ist wie folgt:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
