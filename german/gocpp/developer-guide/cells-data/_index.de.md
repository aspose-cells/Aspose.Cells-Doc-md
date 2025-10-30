---
title: Datenverwaltung von Excel Dateien mit Golang über C++
linktitle: Zellendaten
type: docs
weight: 110
url: /de/go-cpp/view-and-edit-excel-data/
description: Dieser Artikel beschreibt, wie man mit der Aspose.Cells Bibliothek in C++ Daten von Excel Dateien anzeigt und bearbeitet.
keywords: Aspose.Cells C++ Daten in Excel Dateien verwalten, Daten zu Excel hinzufügen, Daten aus Excel auslesen, Effizienz beim Hinzufügen von Daten verbessern, Zellen verwalten, Zellen aktualisieren, Zellen Daten abrufen, Zellen Daten einfügen
---

{{% alert color="primary" %}}

In [Zugriff auf Zellen eines Arbeitsblatts](/cells/de/cpp/accessing-cells-of-a-worksheet/) haben wir grundlegende Ansätze zum Zugriff auf Zellen in einem Arbeitsblatt besprochen. In diesem Artikel wird einer dieser Ansätze verwendet, um verschiedene Arten von Daten zu Zellen hinzuzufügen.

{{% /alert %}}

## **Wie man Daten zu Zellen hinzufügt**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse dar.

Mit Aspose.Cells können Entwickler Daten in Zellen von Arbeitsmappen hinzufügen, indem sie die [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)-Methode der [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/)-Klasse aufrufen. Aspose.Cells bietet überladene Versionen der [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/)-Methode, mit denen Entwickler verschiedene Arten von Daten zu Zellen hinzufügen können. Unter Verwendung dieser überladenen Versionen der [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/)-Methode ist es möglich, Boolesche, Zeichenfolgen, Dezimalzahlen, Ganzzahlen oder Datum/Zeit usw. Werte der Zelle hinzuzufügen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData.go" >}}
## **Wie man die Effizienz verbessert**

Wenn Sie die Methode [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue_bool/) verwenden, um eine große Menge an Daten in ein Arbeitsblatt einzufügen, sollten Sie zuerst Werte in die Zellen nach Zeilen und dann nach Spalten einfügen. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

## **Wie man Daten von Zellen abruft**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse dar.

Die Klasse [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) bietet mehrere Eigenschaften, die es Entwicklern ermöglichen, Werte aus den Zellen gemäß ihren Datentypen abzurufen. Diese Eigenschaften umfassen:

- [**StringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/): gibt den String-Wert der Zelle zurück.
- [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/): gibt den Double-Wert der Zelle zurück.
- [**BoolValue**](https://reference.aspose.com/cells/go-cpp/cell/getboolvalue/): gibt den Boolean-Wert der Zelle zurück.
- [**DateTimeValue**](https://reference.aspose.com/cells/go-cpp/cell/getdatetimevalue/): gibt den Datum/Uhrzeit-Wert der Zelle zurück.
- [**FloatValue**](https://reference.aspose.com/cells/go-cpp/cell/getfloatvalue/): gibt den Float-Wert der Zelle zurück.
- [**IntValue**](https://reference.aspose.com/cells/go-cpp/cell/getintvalue/): gibt den Integer-Wert der Zelle zurück.

Wenn ein Feld nicht ausgefüllt ist, wirft die Zelle mit [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/) oder [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) eine Ausnahme.

Der Typ der in einer Zelle enthaltenen Daten kann auch über die Eigenschaft [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) der Klasse [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) überprüft werden. Tatsächlich basiert die Eigenschaft [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) der Klasse [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) auf der Enumeration [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/), deren vordefinierte Werte unten aufgeführt sind:

|**Zellwerttypen**|**Beschreibung**|
| :- | :- |
|IsBool| Gibt an, dass der Zellenwert Boolean ist.|
|IsDateTime| Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|IsNull| Stellt eine leere Zelle dar.|
|IsNumeric| Gibt an, dass der Zellenwert numerisch ist.|
|IsString| Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|IsUnknown| Gibt an, dass der Zellenwert unbekannt ist.|

Sie können auch die oben vordefinierten Zellwerttypen verwenden, um sie mit dem Datentyp in jeder Zelle zu vergleichen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData-1.go" >}}
{{% alert color="primary" %}}

Beim Arbeiten mit Arbeitsblättern können Benutzer verschiedene Arten von Daten in den Zellen hinzufügen. Diese Datentypen können Boolesche, Ganzzahlen, Gleitkommazahlen, Text- oder Datum-/Uhrzeitwerte umfassen. Mit Aspose.Cells können Sie die entsprechenden Werte basierend auf ihren Datentypen aus den Zellen abrufen.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen eines Arbeitsblatts zugreifen](/cells/de/cpp/accessing-cells-of-a-worksheet/)
- [Text numerische Daten in Nummer konvertieren](/cells/de/cpp/convert-text-numeric-data-to-number/)
- [Teilergebnisse erstellen](/cells/de/cpp/creating-subtotals/)
- [Daten filtern](/cells/de/cpp/data-filtering/)
- [Daten sortieren](/cells/de/cpp/sort-data-of-excel/)
- [Datenüberprüfung](/cells/de/cpp/data-validation/)
- [Daten suchen oder suchen](/cells/de/cpp/find-or-search-data/)
- [Zellzeichenfolgenwert mit und ohne Formatierung abrufen](/cells/de/cpp/get-cell-string-value-with-and-without-formatting/)
- [Hinzufügen von HTML-Rich-Text in die Zelle](/cells/de/cpp/adding-html-rich-text-inside-the-cell/)
- [Hyperlinks in Excel oder OpenOffice einfügen](/cells/de/cpp/insert-hyperlinks-to-excel/)
- [Verwendung und Platzierung von Enumeratoren](/cells/de/cpp/how-and-where-to-use-enumerators/)
- [Breite und Höhe des Zellenwerts in Pixeln messen](/cells/de/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lesen von Zellenwerten in mehreren Threads gleichzeitig](/cells/de/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Umwandlung zwischen Zellnamen und Zeilen-/Spaltenindex](/cells/de/cpp/names-and-indices/)
- [Daten erst nach Zeile und dann nach Spalte ausfüllen](/cells/de/cpp/populate-data-first-by-row-then-by-column/)
- [Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten](/cells/de/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Teile des Rich-Texts der Zelle zugreifen und aktualisieren](/cells/de/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
