---
title: Datenverwaltung von Excel-Dateien.
linktitle: Cells Daten
type: docs
weight: 110
url: /de/net/view-and-edit-excel-data/
description: Dieser Artikel beschreibt, wie Sie Daten von Excel-Dateien mit der Bibliothek Aspose.Cells anzeigen und bearbeiten.
---
{{% alert color="primary" %}}

 Im[Zugriff auf Cells eines Arbeitsblatts](/cells/de/net/accessing-cells-of-a-worksheet/)haben wir grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt besprochen. Dieser Artikel verwendet einen dieser Ansätze, um Zellen verschiedene Datentypen hinzuzufügen.

{{% /alert %}}

## **Hinzufügen von Daten zu Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jeder Artikel in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung stellt ein Objekt der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells ermöglicht Entwicklern das Hinzufügen von Daten zu den Zellen in Arbeitsblättern durch Aufrufen von[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) Methode. Aspose.Cells bietet überladene Versionen der[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) Methode, mit der Entwickler Zellen verschiedene Arten von Daten hinzufügen können. Die Verwendung dieser überladenen Versionen der[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)-Methode ist es möglich, der Zelle einen Boolean-, String-, Double-, Integer- oder Datums-/Zeitwert usw. hinzuzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Effizienz verbessern**

 Wenn du benutzt[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Um eine große Datenmenge in ein Arbeitsblatt einzufügen, sollten Sie den Zellen Werte hinzufügen, zuerst nach Zeilen und dann nach Spalten. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

## **Abrufen von Daten von Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jeder Artikel in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung stellt ein Objekt der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Das[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Die Klasse stellt mehrere Eigenschaften bereit, die es Entwicklern ermöglichen, Werte aus den Zellen gemäß ihren Datentypen abzurufen. Zu diesen Eigenschaften gehören:

- [**Zeichenfolgenwert**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): gibt den Zeichenfolgenwert der Zelle zurück.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): gibt den doppelten Wert der Zelle zurück.
- [**BoolWert**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): gibt den booleschen Wert der Zelle zurück.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): gibt den Datums-/Uhrzeitwert der Zelle zurück.
- [**Gleitkommawert**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): gibt den Gleitkommawert der Zelle zurück.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)gibt den ganzzahligen Wert der Zelle zurück.

 Wenn ein Feld nicht ausgefüllt ist, werden Zellen mit[**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) oder[**Gleitkommawert**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)wirft eine Ausnahme.

Die Art der in einer Zelle enthaltenen Daten kann auch mit überprüft werden[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**Typ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) Eigentum. Tatsächlich ist die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**Typ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) Eigentum basiert auf der[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)Enumeration, deren vordefinierte Werte unten aufgeführt sind:

|**Cell Werttypen**|**Beschreibung**|
|:- |:- |
|IsBool|Gibt an, dass der Zellenwert boolesch ist.|
|IsDateTime|Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|Ist Null|Stellt eine leere Zelle dar.|
|IstNumerisch|Gibt an, dass der Zellenwert numerisch ist.|
|IstString|Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|Ist unbekannt|Gibt an, dass der Zellenwert unbekannt ist.|

Sie können auch die oben vordefinierten Zellenwerttypen verwenden, um sie mit dem in jeder Zelle vorhandenen Datentyp zu vergleichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Während der Arbeit an Arbeitsblättern können Benutzer verschiedene Arten von Daten in die Zellen einfügen. Diese Datentypen können boolesche, ganzzahlige, Fließkomma-, Text- oder Datums-/Zeitwerte umfassen. Mit Aspose.Cells können Sie die entsprechenden Werte aus den Zellen entsprechend ihrer Datentypen abrufen.

{{% /alert %}}

## **Themen vorantreiben**
- [Zugriff auf Cells eines Arbeitsblatts](/cells/de/net/accessing-cells-of-a-worksheet/)
- [Konvertieren Sie numerische Textdaten in Zahlen](/cells/de/net/convert-text-numeric-data-to-number/)
- [Erstellen von Zwischensummen](/cells/de/net/creating-subtotals/)
- [Datenfilterung](/cells/de/net/data-filtering/)
- [Datensortierung](/cells/de/net/sort-data-of-excel/)
- [Datenvalidierung](/cells/de/net/data-validation/)
- [Daten aus Arbeitsblatt exportieren](/cells/de/net/export-data-from-worksheet/)
- [Daten finden oder suchen](/cells/de/net/find-or-search-data/)
- [Holen Sie sich Cell Zeichenfolgenwert mit und ohne Formatierung](/cells/de/net/get-cell-string-value-with-and-without-formatting/)
- [Hinzufügen von HTML-Rich-Text in Cell](/cells/de/net/adding-html-rich-text-inside-the-cell/)
- [Fügen Sie Hyperlinks in Excel oder OpenOffice ein](/cells/de/net/insert-hyperlinks-to-excel/)
- [Daten in Arbeitsblatt importieren](/cells/de/net/import-data-into-worksheet/)
- [Wie und wo Enumeratoren verwendet werden](/cells/de/net/how-and-where-to-use-enumerators/)
- [Messen Sie die Breite und Höhe des Werts Cell in Pixeleinheiten](/cells/de/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Gleichzeitiges Lesen von Cell-Werten in mehreren Threads](/cells/de/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Konvertierung zwischen Zellenname und Zeilen-/Spaltenindex](/cells/de/net/names-and-indices/)
- [Füllen Sie die Daten zuerst nach Zeile und dann nach Spalte aus](/cells/de/net/populate-data-first-by-row-then-by-column/)
- [Präfix für einfache Anführungszeichen von Cell Wert oder Bereich beibehalten](/cells/de/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Greifen Sie auf die Rich-Text-Teile von Cell zu und aktualisieren Sie sie](/cells/de/net/access-and-update-the-portions-of-rich-text-of-cell/)



