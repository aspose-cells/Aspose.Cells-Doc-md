---
title: Erkennen leerer Arbeitsblätter
type: docs
weight: 710
url: /de/java/detecting-empty-worksheets/
---

## **Überprüfung auf belegte Zellen**
Arbeitsblätter können eine oder mehrere Zellen enthalten, die mit Werten gefüllt sind, wobei ein Wert einfach (Text, numerisch, Datum/Uhrzeit) oder eine Formel oder ein auf einer Formel basierender Wert sein kann. In einem solchen Fall ist es einfach zu erkennen, ob ein bestimmtes Arbeitsblatt leer ist oder nicht. Alles, was wir überprüfen müssen, sind die Eigenschaften [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) oder [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn). Wenn die genannten Eigenschaften Null- oder positive Werte zurückgeben, bedeutet dies, dass eine oder mehrere Zellen gefüllt wurden. Wenn jedoch eine dieser Eigenschaften -1 zurückgibt, bedeutet dies, dass keine der Zellen im angegebenen Arbeitsblatt gefüllt wurden.

{{% alert color="primary" %}} 

Die Zeilen- und Spaltensammlungen haben einen nullbasierten Index, daher bedeutet eine Zelle in Zeile 0 & Spalte 0 die erste Zelle im Arbeitsblatt, nämlich A1.

{{% /alert %}} 
## **Überprüfung auf leere initialisierte Zellen**
Alle Zellen, die Werte enthalten, werden automatisch initialisiert. Es besteht jedoch die Möglichkeit, dass ein Arbeitsblatt Zellen nur mit Formatierungen enthält. In einem solchen Szenario geben die Eigenschaften [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) oder [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) -1 zurück, was auf das Fehlen von gefüllten Werten, aber initialisierten Zellen aufgrund der Zellformatierung hinweist. Um festzustellen, ob ein Arbeitsblatt leere initialisierte Zellen hat, wird empfohlen, die *Iterator.hasNext*-Methode auf dem aus der Zellsammlung erhaltenen Iterator zu verwenden. Wenn die Methode *iterator.hasNext* true zurückgibt, bedeutet dies, dass es im angegebenen Arbeitsblatt eine oder mehrere initialisierte Zellen gibt.

{{% alert color="primary" %}} 

Es gibt eine Reihe von Möglichkeiten, den Zellenenumerator zu erhalten, wie in [Wie und wo Iteratoren verwendet werden](/cells/de/java/how-and-where-to-use-iterators/) ausführlich erläutert.

{{% /alert %}} 
## **Überprüfung auf Formen**
Es ist möglich, dass ein bestimmtes Arbeitsblatt keine gefüllten Zellen enthält, jedoch Formen und Objekte wie Steuerelemente, Diagramme, Bilder usw. enthält. Wenn wir überprüfen müssen, ob ein Arbeitsblatt eine Form enthält, können wir dies tun, indem wir die Eigenschaft [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count) überprüfen. Ein positiver Wert deutet auf das Vorhandensein von Form(en) im Arbeitsblatt hin.
## **Programmierbeispiel**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}
