---
title: Erkennung von zirkulären Verweisen
type: docs
weight: 70
url: /de/java/detecting-circular-reference/
---

## **Einführung**

Arbeitsmappen können zirkuläre Verweise enthalten, und manchmal besteht die Notwendigkeit festzustellen, ob zirkuläre Verweise vorliegen oder nicht.

## **Konzept zur Erkennung des zirkulären Verweises**

Zirkuläre Verweise können nur erkannt werden, wenn die Formel berechnet wird, da die Verweise einer Formel in der Regel vom berechneten Ergebnis anderer Teile oder anderer Formeln abhängen. Daher stellen wir neue APIs für diese Anforderung bereit (zum Sammeln von Zellen mit zirkulären Verweisen) im Prozess der Formelberechnung:

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Stellt die Berechnung relevanter Daten über eine berechnete Zelle dar

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-): wird vom Formelberechnungsmotor aufgerufen, wenn zirkuläre Verweise auftreten, das Element im Enumerator ist [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) Objekte, die alle Zellen in einem Kreis darstellen. Der zurückgegebene Wert gibt an, ob der Formelmotor diese Zellen nach diesem Aufruf in der Kreisberechnung berechnen muss.

Benutzer können diese zirkulären Verweise bei der Implementierung der Methode [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-) sammeln.

Die Quellbeispieldatei kann unter folgendem Link heruntergeladen werden:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Definition der *CircularMonitor* Klasse, die von der [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)-Klasse abgeleitet ist, lautet wie folgt:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
{{< app/cells/assistant language="java" >}}
