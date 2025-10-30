---
title: Verwalten von Daten von Excel Dateien
linktitle: Zellendaten
type: docs
weight: 110
url: /de/nodejs-cpp/view-and-edit-excel-data/
description: Dieser Artikel beschreibt, wie man mit Aspose.Cells für Node.js via C++ Daten von Excel Dateien anzeigen und bearbeiten kann.
keywords: Aspose.Cells Node.js via C++, Verwalten von Excel Dateidaten, Daten zu Excel hinzufügen, Daten aus Excel lesen, Effizienz beim Hinzufügen von Daten verbessern, Zellen verwalten, Zellen aktualisieren, Zellen Daten abrufen, Zellen Daten einfügen
---

{{% alert color="primary" %}}

In [Zugreifen auf Zellen eines Arbeitsblatts](/cells/de/nodejs-cpp/accessing-cells-of-a-worksheet/) haben wir grundlegende Ansätze zum Zugriff auf Zellen in einem Arbeitsblatt besprochen. Dieser Artikel nutzt einen dieser Ansätze, um verschiedene Datentypen in Zellen hinzuzufügen.

{{% /alert %}}

## **Wie man Daten zu Zellen hinzufügt**

Aspose.Cells for Node.js via C++ bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse stellt eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung bereit. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse dar.

Aspose.Cells erlaubt es Entwicklern, Daten durch Aufruf der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse-Methode [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) zu Zellen in Arbeitsblättern hinzuzufügen. Aspose.Cells bietet überladene Versionen der [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-Methode, die Entwicklern erlauben, unterschiedliche Datentypen zu Zellen hinzuzufügen. Mit diesen überladenen Versionen der [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-Methode können Boolean-, String-, Double-, Integer- oder Date-/Uhrzeitwerte in die Zelle eingefügt werden.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **Wie man die Effizienz verbessert**

Wenn Sie die [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-Methode verwenden, um eine große Datenmenge in ein Arbeitsblatt einzufügen, sollten Sie zuerst Werte zeilenweise und dann spaltenweise hinzufügen. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

## **Wie man Daten von Zellen abruft**

Aspose.Cells for Node.js via C++ bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse stellt eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung bereit. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung ist ein Objekt der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse.

Die [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse bietet mehrere Eigenschaften, mit denen Entwickler Werte aus Zellen entsprechend ihrem Datentyp abrufen können. Diese Eigenschaften umfassen:

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): gibt den String-Wert der Zelle zurück.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): Gibt den doppelten Wert der Zelle zurück.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): Gibt den booleschen Wert der Zelle zurück.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): Gibt den Datum/Uhrzeit-Wert der Zelle zurück.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): Gibt den Fließkomma-Wert der Zelle zurück.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): Gibt den Ganzzahlwert der Zelle zurück.

Wenn ein Feld nicht ausgefüllt ist, löst die Verwendung von [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) oder [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) eine Ausnahme aus.

Der Typ der in einer Zelle enthaltenen Daten kann auch durch Verwendung der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse' [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--)-Methode überprüft werden. Tatsächlich basiert die [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse' [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--)-Methode auf der [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype)-Aufzählung, deren vordefinierte Werte unten aufgelistet sind:

|**Zellwerttypen**|**Beschreibung**|
| :- | :- |
|IsBool| Gibt an, dass der Zellenwert Boolean ist.|
|IsDateTime| Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|IsNull| Stellt eine leere Zelle dar.|
|IsNumeric| Gibt an, dass der Zellenwert numerisch ist.|
|IsString| Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|IsUnknown| Gibt an, dass der Zellenwert unbekannt ist.|

Sie können auch die oben vordefinierten Zellwerttypen verwenden, um sie mit dem Datentyp in jeder Zelle zu vergleichen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

Beim Arbeiten an Tabellenblättern können Benutzer verschiedene Datentypen in den Zellen hinzufügen. Diese Datentypen können Boolean, Ganzzahlen, Fließkommazahlen, Text oder Datum/Uhrzeit-Werte einschließen. Mit Aspose.Cells können Sie die entsprechenden Werte aus den Zellen entsprechend ihrer Datentypen abrufen.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen eines Arbeitsblatts zugreifen](/cells/de/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [Text numerische Daten in Nummer konvertieren](/cells/de/nodejs-cpp/convert-text-numeric-data-to-number/)
- [Teilergebnisse erstellen](/cells/de/nodejs-cpp/creating-subtotals/)
- [Daten filtern](/cells/de/nodejs-cpp/data-filtering/)
- [Daten sortieren](/cells/de/nodejs-cpp/sort-data-of-excel/)
- [Datenüberprüfung](/cells/de/nodejs-cpp/data-validation/)
- [Daten suchen oder suchen](/cells/de/nodejs-cpp/find-or-search-data/)
- [Zellzeichenfolgenwert mit und ohne Formatierung abrufen](/cells/de/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [Hinzufügen von HTML-Rich-Text in die Zelle](/cells/de/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [Hyperlinks in Excel oder OpenOffice einfügen](/cells/de/nodejs-cpp/insert-hyperlinks-to-excel/)
- [Verwendung und Platzierung von Enumeratoren](/cells/de/nodejs-cpp/how-and-where-to-use-enumerators/)
- [Breite und Höhe des Zellenwerts in Pixeln messen](/cells/de/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lesen von Zellenwerten in mehreren Threads gleichzeitig](/cells/de/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Umwandlung zwischen Zellnamen und Zeilen-/Spaltenindex](/cells/de/nodejs-cpp/names-and-indices/)
- [Daten erst nach Zeile und dann nach Spalte ausfüllen](/cells/de/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten](/cells/de/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Teile des Rich-Texts der Zelle zugreifen und aktualisieren](/cells/de/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="nodejs-cpp" >}}
