---
title: Erkennen leerer Arbeitsblätter
type: docs
weight: 410
url: /de/python-net/detecting-empty-worksheets/
description: Dieser Artikel zeigt Code, wie man programmatisch überprüft, ob Excel Arbeitsmappen leere Arbeitsblätter enthalten, unter Verwendung der Aspose.Cells für Python via .NET Bibliothek.
keywords: Python Excel Bibliothek, leeres Arbeitsblatt erkennen mit Python, leeres Excel Arbeitsblatt finden in Python.
---

## **Überprüfung auf belegte Zellen**

Arbeitsblätter können eine oder mehrere Zellen enthalten, die Werte enthalten, wobei ein Wert einfach (Text, numerisch, Datum/Uhrzeit) oder eine Formel oder ein formelbasierter Wert sein kann. In einem solchen Fall ist es einfach zu erkennen, ob ein gegebenes Arbeitsblatt leer ist oder nicht. Alles, was wir überprüfen müssen, sind die [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) oder [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) Eigenschaften. Wenn die oben genannten Eigenschaften Null oder positive Werte zurückgeben, bedeutet dies, dass eine oder mehr Zellen gefüllt wurden. Wenn jedoch eine dieser Eigenschaften -1 zurückgibt, bedeutet dies, dass keine der Zellen im angegebenen Arbeitsblatt gefüllt wurde.

{{% alert color="primary" %}}

Die Sammlungen von Zeilen und Spalten haben einen Null-basierten Index. Daher bedeutet eine Zelle in Zeile 0 und Spalte 0 die erste Zelle im Arbeitsblatt, welche A1 ist.

{{% /alert %}}

## **Überprüfung auf leere initialisierte Zellen**

Alle Zellen, die Werte enthalten, werden automatisch initialisiert, allerdings besteht die Möglichkeit, dass ein Arbeitsblatt Zellen nur mit Formatierungen enthält. In einem solchen Szenario geben die [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) oder [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/)-Eigenschaften -1 zurück, was auf das Fehlen von gefüllten Werten hinweist. Inititalisierte Zellen aufgrund der Zellformatierung können jedoch mit diesem Ansatz nicht erkannt werden. Um zu überprüfen, ob ein Arbeitsblatt leere initialisierte Zellen enthält, empfiehlt es sich, die IEnumerator.MoveNext-Methode auf dem Enumerator zu verwenden, der aus der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung gewonnen wurde. Wenn die IEnumerator.MoveNext-Methode **true** zurückgibt, bedeutet dies, dass sich in dem Arbeitsblatt eine oder mehrere initialisierte Zellen befinden.

## **Überprüfung auf Formen**

Es ist möglich, dass ein bestimmtes Arbeitsblatt keine gefüllten Zellen enthält, es kann jedoch Formen & Objekte wie Steuerelemente, Diagramme, Bilder usw. enthalten. Wenn wir überprüfen möchten, ob ein Arbeitsblatt irgendwelche Formen enthält, können wir dies durch Inspektion der [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)-Elemente tun. Jede positive Zahl zeigt das Vorhandensein von Formen im Arbeitsblatt an.

## **Programmierbeispiel**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
