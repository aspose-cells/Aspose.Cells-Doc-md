---
title: Verwalten von Daten von Excel Dateien
linktitle: Zellendaten
type: docs
weight: 110
url: /de/python-net/view-and-edit-excel-data/
description: Dieser Artikel beschreibt, wie Daten von Excel Dateien mit der Aspose.Cells für Python via .NET Bibliothek angezeigt und bearbeitet werden können.
keywords: Python Excel Bibliothek, Aspose.Cells für Python Daten in Excel Datei verwalten, Python Daten zu Excel Datei hinzufügen, Python Daten aus Excel Datei abrufen, Python Wie man die Effizienz beim Hinzufügen von Daten verbessert, Python Zellen Daten verwalten, Python Zellen Daten aktualisieren, Python Zellen Daten abrufen, Python Zellen Daten einfügen.
---

{{% alert color="primary" %}}

In [Zugriff auf Zellen eines Arbeitsblatts](/cells/de/python-net/zugriff-auf-zellen-eines-arbeitsblatts/), haben wir grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt diskutiert. In diesem Artikel verwenden wir einen dieser Ansätze, um verschiedene Arten von Daten zu Zellen hinzuzufügen.

{{% /alert %}}

## **Wie man Daten zu Zellen hinzufügt**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells für Python via .NET ermöglicht Entwicklern, Daten zu den Zellen in Arbeitsblättern zu addieren, indem sie die Methode [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) der Klasse [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) aufrufen. Aspose.Cells für Python via .NET bietet überladene Versionen der Methode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int), mit denen Entwickler verschiedene Arten von Daten zu Zellen hinzufügen können. Unter Verwendung dieser überladenen Versionen der Methode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) ist es möglich, einen Boolean, String, Double, Integer oder Datum/Uhrzeit usw. Werte der Zelle hinzuzufügen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **Wie man die Effizienz verbessert**

Wenn Sie die Methode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) verwenden, um eine große Menge an Daten in ein Arbeitsblatt einzufügen, sollten Sie zuerst Werte in die Zellen nach Zeilen und dann nach Spalten einfügen. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

## **Wie man Daten von Zellen abruft**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Die Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) bietet mehrere Eigenschaften, die es Entwicklern ermöglichen, Werte aus den Zellen gemäß ihren Datentypen abzurufen. Diese Eigenschaften umfassen:

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): gibt den String-Wert der Zelle zurück.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): gibt den Double-Wert der Zelle zurück.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): gibt den Boolean-Wert der Zelle zurück.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): gibt den Datum/Uhrzeit-Wert der Zelle zurück.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): gibt den Float-Wert der Zelle zurück.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): gibt den Integer-Wert der Zelle zurück.

Wenn ein Feld nicht ausgefüllt ist, wirft die Zelle mit [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) oder [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) eine Ausnahme.

Der Typ der in einer Zelle enthaltenen Daten kann auch über die Eigenschaft [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) der Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) überprüft werden. Tatsächlich basiert die Eigenschaft [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) der Klasse [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) auf der Enumeration [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype), deren vordefinierte Werte unten aufgeführt sind:

|**Zellwerttypen**|**Beschreibung**|
| :- | :- |
|IS_BOOL| Beschreibt, dass der Zellenwert ein Boolean ist.|
|IS_DATE_TIME| Beschreibt, dass der Zellenwert ein Datum/Uhrzeit ist.|
|IS_NULL|Stellt eine leere Zelle dar.
|IS_NUMERIC|Gibt an, dass der Zellenwert numerisch ist.
|IS_STRING|Gibt an, dass der Zellenwert eine Zeichenfolge ist.
|IS_ERROR|Gibt an, dass der Zellenwert ein Fehlerwert ist.
|IS_UNKNOWN|Gibt an, dass der Zellenwert unbekannt ist.

Sie können auch die oben vordefinierten Zellwerttypen verwenden, um sie mit dem Datentyp in jeder Zelle zu vergleichen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

Bei der Arbeit mit Tabellenblättern können Benutzer verschiedene Arten von Daten in den Zellen hinzufügen. Diese Datentypen können boolesche, ganze, Gleitkommazahlen, Text- oder Datum/Zeit-Werte enthalten. Mit Aspose.Cells für Python via .NET können Sie die entsprechenden Werte aus den Zellen gemäß ihren Datentypen abrufen.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen eines Arbeitsblatts zugreifen](/cells/de/python-net/accessing-cells-of-a-worksheet/)
- [Text numerische Daten in Nummer konvertieren](/cells/de/python-net/convert-text-numeric-data-to-number/)
- [Teilergebnisse erstellen](/cells/de/python-net/creating-subtotals/)
- [Daten filtern](/cells/de/python-net/data-filtering/)
- [Daten sortieren](/cells/de/python-net/sort-data-of-excel/)
- [Datenüberprüfung](/cells/de/python-net/data-validation/)
- [Zellzeichenfolgenwert mit und ohne Formatierung abrufen](/cells/de/python-net/get-cell-string-value-with-format-strategy/)
- [Hinzufügen von HTML-Rich-Text in die Zelle](/cells/de/python-net/adding-html-rich-text-inside-the-cell/)
- [Daten suchen oder suchen](/cells/de/python-net/find-or-search-data/)
- [Hyperlinks in Excel oder OpenOffice einfügen](/cells/de/python-net/insert-hyperlinks-to-excel/)
- [Breite und Höhe des Zellenwerts in Pixeln messen](/cells/de/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Umwandlung zwischen Zellnamen und Zeilen-/Spaltenindex](/cells/de/python-net/names-and-indices/)
- [Daten erst nach Zeile und dann nach Spalte ausfüllen](/cells/de/python-net/populate-data-first-by-row-then-by-column/)
- [Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten](/cells/de/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Teile des Rich-Texts der Zelle zugreifen und aktualisieren](/cells/de/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="python-net" >}}
