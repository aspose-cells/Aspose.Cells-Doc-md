---
title: Erkennen leerer Arbeitsblätter
type: docs
weight: 410
url: /de/net/detecting-empty-worksheets/
description: Dieser Artikel zeigt Ihnen den Code, der erklärt, wie Sie leere Arbeitsblätter von Excel Arbeitsmappen programmgesteuert mithilfe der C# API und .NET Bibliothek erkennen können.
keywords: Leeres Arbeitsblatt in c# erkennen, leeres Excel Arbeitsblatt in c# finden
---

## **Überprüfung auf belegte Zellen**

Arbeitsblätter können eine oder mehrere Zellen enthalten, die Werte enthalten, wobei ein Wert einfach (Text, numerisch, Datum/Uhrzeit) oder eine Formel oder ein formelbasierter Wert sein kann. In einem solchen Fall ist es einfach zu erkennen, ob ein gegebenes Arbeitsblatt leer ist oder nicht. Alles, was wir überprüfen müssen, sind die [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) oder [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) Eigenschaften. Wenn die oben genannten Eigenschaften Null oder positive Werte zurückgeben, bedeutet dies, dass eine oder mehr Zellen gefüllt wurden. Wenn jedoch eine dieser Eigenschaften -1 zurückgibt, bedeutet dies, dass keine der Zellen im angegebenen Arbeitsblatt gefüllt wurde.

{{% alert color="primary" %}}

Die Sammlungen von Zeilen und Spalten haben einen Null-basierten Index. Daher bedeutet eine Zelle in Zeile 0 und Spalte 0 die erste Zelle im Arbeitsblatt, welche A1 ist.

{{% /alert %}}

## **Überprüfung auf leere initialisierte Zellen**

Alle Zellen, die Werte enthalten, werden automatisch initialisiert. Es besteht jedoch die Möglichkeit, dass ein Arbeitsblatt Zellen nur mit Formatierung enthält. In einem solchen Szenario geben die [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) oder [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) Eigenschaften -1 zurück, was auf das Fehlen von gefüllten Werten, aber initialisierten Zellen aufgrund der Zellformatierung hinweist. Um zu überprüfen, ob ein Arbeitsblatt leere initialisierte Zellen enthält, wird empfohlen, die IEnumerator.MoveNext-Methode auf dem Enumerator, der aus der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung erhalten wurde, zu verwenden. Wenn die IEnumerator.MoveNext-Methode **true** zurückgibt, bedeutet dies, dass es eine oder mehrere initialisierte Zellen im angegebenen Arbeitsblatt gibt.

## **Überprüfung auf Formen**

Es ist möglich, dass ein bestimmtes Arbeitsblatt keine gefüllten Zellen enthält, aber Formen und Objekte wie Steuerelemente, Diagramme, Bilder usw. enthalten kann. Wenn wir überprüfen müssen, ob ein Arbeitsblatt eine Form enthält, können wir dies tun, indem wir die [**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)-Eigenschaft untersuchen. Jeder positive Wert weist auf das Vorhandensein von Formen im Arbeitsblatt hin.

## **Programmierbeispiel**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
