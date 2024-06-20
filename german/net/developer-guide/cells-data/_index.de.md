---
title: Verwalten von Daten von Excel Dateien
linktitle: Zellendaten
type: docs
weight: 110
url: /de/net/view-and-edit-excel-data/
description: Dieser Artikel beschreibt, wie Daten von Excel Dateien mit der Aspose.Cells Bibliothek angezeigt und bearbeitet werden können.
keywords: Aspose.Cells C# Verwaltung von Excel Dateidaten, Daten zu Excel Datei hinzufügen, Daten aus Excel Datei abrufen, Optimierung der Effizienz bei der Datenablage, Verwalten von Zellendaten, Aktualisieren von Zellendaten, Abrufen von Zellendaten, Einfügen von Zellendaten
---

{{% alert color="primary" %}}

In [Zugriff auf Zellen eines Arbeitsblatts](/cells/de/net/accessing-cells-of-a-worksheet/) haben wir grundlegende Ansätze zur Zugriff auf Zellen in einem Arbeitsblatt besprochen. In diesem Artikel wird einer dieser Ansätze verwendet, um verschiedene Arten von Daten in Zellen hinzuzufügen.

{{% /alert %}}

## **Wie man Daten zu Zellen hinzufügt**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Klasse dar.

Mit Aspose.Cells können Entwickler Daten in Zellen von Arbeitsmappen hinzufügen, indem sie die [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Methode der [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)-Klasse aufrufen. Aspose.Cells bietet überladene Versionen der [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)-Methode, mit denen Entwickler verschiedene Arten von Daten zu Zellen hinzufügen können. Unter Verwendung dieser überladenen Versionen der [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)-Methode ist es möglich, Boolesche, Zeichenfolgen, Dezimalzahlen, Ganzzahlen oder Datum/Zeit usw. Werte der Zelle hinzuzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Wie man die Effizienz verbessert**

Wenn Sie die Methode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) verwenden, um eine große Menge an Daten in ein Arbeitsblatt einzufügen, sollten Sie zuerst Werte in die Zellen nach Zeilen und dann nach Spalten einfügen. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

## **Wie man Daten von Zellen abruft**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Klasse dar.

Die Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) bietet mehrere Eigenschaften, die es Entwicklern ermöglichen, Werte aus den Zellen gemäß ihren Datentypen abzurufen. Diese Eigenschaften umfassen:

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): gibt den String-Wert der Zelle zurück.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): gibt den Double-Wert der Zelle zurück.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): gibt den Boolean-Wert der Zelle zurück.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): gibt den Datum/Uhrzeit-Wert der Zelle zurück.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): gibt den Float-Wert der Zelle zurück.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): gibt den Integer-Wert der Zelle zurück.

Wenn ein Feld nicht ausgefüllt ist, wirft die Zelle mit [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) oder [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) eine Ausnahme.

Der Typ der in einer Zelle enthaltenen Daten kann auch über die Eigenschaft [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) überprüft werden. Tatsächlich basiert die Eigenschaft [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) der Klasse [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) auf der Enumeration [**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype), deren vordefinierte Werte unten aufgeführt sind:

|**Zellwerttypen**|**Beschreibung**|
| :- | :- |
|IsBool| Gibt an, dass der Zellenwert Boolean ist.|
|IsDateTime| Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|IsNull| Stellt eine leere Zelle dar.|
|IsNumeric| Gibt an, dass der Zellenwert numerisch ist.|
|IsString| Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|IsUnknown| Gibt an, dass der Zellenwert unbekannt ist.|

Sie können auch die oben vordefinierten Zellwerttypen verwenden, um sie mit dem Datentyp in jeder Zelle zu vergleichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Beim Arbeiten mit Arbeitsblättern können Benutzer verschiedene Arten von Daten in den Zellen hinzufügen. Diese Datentypen können Boolesche, Ganzzahlen, Gleitkommazahlen, Text- oder Datum-/Uhrzeitwerte umfassen. Mit Aspose.Cells können Sie die entsprechenden Werte basierend auf ihren Datentypen aus den Zellen abrufen.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen eines Arbeitsblatts zugreifen](/cells/de/net/accessing-cells-of-a-worksheet/)
- [Text numerische Daten in Nummer konvertieren](/cells/de/net/convert-text-numeric-data-to-number/)
- [Teilergebnisse erstellen](/cells/de/net/creating-subtotals/)
- [Daten filtern](/cells/de/net/data-filtering/)
- [Daten sortieren](/cells/de/net/sort-data-of-excel/)
- [Datenüberprüfung](/cells/de/net/data-validation/)
- [Daten aus dem Arbeitsblatt exportieren](/cells/de/net/export-data-from-worksheet/)
- [Daten suchen oder suchen](/cells/de/net/find-or-search-data/)
- [Zellzeichenfolgenwert mit und ohne Formatierung abrufen](/cells/de/net/get-cell-string-value-with-and-without-formatting/)
- [Hinzufügen von HTML-Rich-Text in die Zelle](/cells/de/net/adding-html-rich-text-inside-the-cell/)
- [Hyperlinks in Excel oder OpenOffice einfügen](/cells/de/net/insert-hyperlinks-to-excel/)
- [Daten in Arbeitsblatt importieren](/cells/de/net/import-data-into-worksheet/)
- [Verwendung und Platzierung von Enumeratoren](/cells/de/net/how-and-where-to-use-enumerators/)
- [Breite und Höhe des Zellenwerts in Pixeln messen](/cells/de/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lesen von Zellenwerten in mehreren Threads gleichzeitig](/cells/de/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Umwandlung zwischen Zellnamen und Zeilen-/Spaltenindex](/cells/de/net/names-and-indices/)
- [Daten erst nach Zeile und dann nach Spalte ausfüllen](/cells/de/net/populate-data-first-by-row-then-by-column/)
- [Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten](/cells/de/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Teile des Rich-Texts der Zelle zugreifen und aktualisieren](/cells/de/net/access-and-update-the-portions-of-rich-text-of-cell/)



