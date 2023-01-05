---
title: Zirkuläre Referenz erkennen
type: docs
weight: 70
url: /de/net/detecting-circular-reference/
---
## **Einführung**

Arbeitsmappen können Zirkelverweise enthalten, und manchmal muss festgestellt werden, ob Zirkelverweise vorhanden sind oder nicht.

## **Konzept hinter der Erkennung des Zirkelbezugs**

Zirkelbezüge können nur bei der Berechnung der Formel erkannt werden, da die Bezüge einer Formel häufig vom berechneten Ergebnis anderer Teile oder anderer Formeln abhängen. Daher bieten wir neue APIs für diese Anforderung (um Zellen mit Zirkelbezügen zu sammeln) im Prozess der Formelberechnung:

[**Berechnungszelle**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Stellt die Berechnung relevanter Daten über eine zu berechnende Zelle dar

[**AbstractCalculationMonitor.OnCircular(IEnumerator circleCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): wird von der Formelberechnungs-Engine aufgerufen, wenn auf Zirkelverweise gestoßen wird, das Element im Enumerator ist[**Berechnungszelle**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) Objekte, die alle Zellen in einem Kreis darstellen. Der zurückgegebene Wert gibt an, ob die Formel-Engine diese Zellen nach diesem Aufruf kreisförmig berechnen muss.

 Der Benutzer kann diese Zirkelverweise bei der Implementierung von sammeln[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) Methode.

Die Quellbeispieldatei kann unter folgendem Link heruntergeladen werden:

[Kreisformeln.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definition von*CircularMonitor* Klasse, von der abgeleitet wird[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) Klasse ist wie folgt:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
