---
title: Leere Arbeitsblätter erkennen
type: docs
weight: 410
url: /de/net/detecting-empty-worksheets/
---
## **Suchen Sie nach besetzt Cells**

Arbeitsblätter können eine oder mehrere Zellen haben, die mit Werten gefüllt sind, wobei ein Wert einfach (Text, numerisch, Datum/Uhrzeit) oder eine Formel oder ein formelbasierter Wert sein kann. In einem solchen Fall ist leicht zu erkennen, ob ein bestimmtes Arbeitsblatt leer ist oder nicht. Alles, was wir überprüfen müssen, ist die[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) oder[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)Eigenschaften. Wenn die oben genannten Eigenschaften Null oder positive Werte zurückgeben, bedeutet dies, dass eine oder mehrere Zellen ausgefüllt wurden. Wenn jedoch eine dieser Eigenschaften -1 zurückgibt, bedeutet dies, dass keine der Zellen im angegebenen Arbeitsblatt ausgefüllt wurde.

{{% alert color="primary" %}}

Die Zeilen- und Spaltensammlungen haben einen nullbasierten Index, daher bedeutet eine Zelle in Zeile 0 und Spalte 0 die erste Zelle im Arbeitsblatt, die A1 ist.

{{% /alert %}}

## **Prüfen Sie, ob Cells leer initialisiert ist**

 Alle Zellen mit Werten werden automatisch initialisiert, es besteht jedoch die Möglichkeit, dass ein Arbeitsblatt Zellen enthält, auf die nur eine Formatierung angewendet wurde. In einem solchen Szenario ist die[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)oder[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) properties gibt -1 zurück, was das Fehlen ausgefüllter Werte anzeigt, aber initialisierte Zellen aufgrund der Zellenformatierung können mit diesem Ansatz nicht erkannt werden. Um zu überprüfen, ob ein Arbeitsblatt leere initialisierte Zellen hat, wird empfohlen, die Methode IEnumerator.MoveNext für den Enumerator zu verwenden, von dem es abgerufen wurde[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Wenn die IEnumerator.MoveNext-Methode zurückkehrt**Stimmt** Das bedeutet, dass das angegebene Arbeitsblatt eine oder mehrere initialisierte Zellen enthält.

## **Suchen Sie nach Formen**

 Es ist möglich, dass ein bestimmtes Arbeitsblatt keine gefüllten Zellen hat, es kann jedoch Formen und Objekte wie Steuerelemente, Diagramme, Bilder usw. enthalten. Wenn wir überprüfen müssen, ob ein Arbeitsblatt eine Form enthält, können wir dies tun, indem wir die untersuchen[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)Eigentum. Jeder positive Wert zeigt das Vorhandensein von Formen im Arbeitsblatt an.

## **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
