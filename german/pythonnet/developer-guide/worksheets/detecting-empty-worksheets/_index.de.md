---
title: Erkennen leerer Arbeitsblätter
type: docs
weight: 410
url: /de/python-net/detecting-empty-worksheets/
description: In diesem Artikel wird Ihnen der Code gezeigt, wie Sie mit der Aspose.Cells für die Python via .NET Bibliothek programmgesteuert leere Arbeitsblätter von Excel Arbeitsmappen erkennen.
keywords: Python Excel Bibliothek, leeres Arbeitsblatt mit Python erkennen, leeres Excel Arbeitsblatt in Python finden.
---

## **Überprüfung auf belegte Zellen**

Arbeitsblätter können eine oder mehrere Zellen enthalten, die Werte enthalten, wobei ein Wert einfach (Text, numerisch, Datum/Uhrzeit) oder eine Formel oder ein formelbasierter Wert sein kann. In einem solchen Fall ist es einfach zu erkennen, ob ein gegebenes Arbeitsblatt leer ist oder nicht. Alles, was wir überprüfen müssen, sind die [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) oder [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) Eigenschaften. Wenn die oben genannten Eigenschaften Null oder positive Werte zurückgeben, bedeutet dies, dass eine oder mehr Zellen gefüllt wurden. Wenn jedoch eine dieser Eigenschaften -1 zurückgibt, bedeutet dies, dass keine der Zellen im angegebenen Arbeitsblatt gefüllt wurde.

{{% alert color="primary" %}}

Die Sammlungen von Zeilen und Spalten haben einen Null-basierten Index. Daher bedeutet eine Zelle in Zeile 0 und Spalte 0 die erste Zelle im Arbeitsblatt, welche A1 ist.

{{% /alert %}}

## **Überprüfung auf leere initialisierte Zellen**

Alle Zellen, die Werte enthalten, werden automatisch initialisiert, jedoch ist es möglich, dass ein Arbeitsblatt Zellen enthält, auf die nur Formatierungen angewendet wurden. In einem solchen Szenario geben die Eigenschaften [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) oder [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) -1 zurück, was auf die Abwesenheit von bevölkerten Werten hinweist, aber initialisierte Zellen aufgrund der Zellformatierung mit diesem Ansatz nicht erkannt werden können. Um zu überprüfen, ob ein Arbeitsblatt leere initialisierte Zellen enthält, wird empfohlen, die IEnumerator.MoveNext-Methode auf dem Enumerator aus der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung zu verwenden. Wenn die IEnumerator.MoveNext-Methode **true** zurückgibt, bedeutet dies, dass es eine oder mehrere initialisierte Zellen im angegebenen Arbeitsblatt gibt.

## **Überprüfung auf Formen**

Es ist möglich, dass ein bestimmtes Arbeitsblatt keine bevölkerten Zellen enthält, jedoch Formen und Objekte wie Steuerelemente, Diagramme, Bilder usw. enthält. Wenn wir überprüfen müssen, ob ein Arbeitsblatt eine Form enthält, können wir dies tun, indem wir die [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)-Elemente inspizieren. Ein positiver Wert zeigt das Vorhandensein von Formen im Arbeitsblatt an.

## **Programmierbeispiel**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
