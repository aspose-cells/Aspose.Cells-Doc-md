---
title: Filterobjekte beim Laden von Arbeitsmappen oder Arbeitsblättern mit Golang via C++
linktitle: Filterobjekte beim Laden der Arbeitsmappe oder des Arbeitsblatts
type: docs
weight: 330
url: /de/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Erfahren Sie, wie Sie Objekte wie Diagramme, Formen und bedingte Formatierungen beim Laden von Arbeitsmappen oder Arbeitsblättern mit Aspose.Cells for C++ filtern.
---

## **Mögliche Verwendungsszenarien**
Bitte verwenden Sie die Eigenschaft [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/), wenn Sie Daten aus der Arbeitsmappe filtern möchten. Wenn Sie Daten aus einzelnen Arbeitsblättern filtern möchten, müssen Sie die Methode [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/) überschreiben. Geben Sie beim Erstellen oder Arbeiten mit [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/) einen entsprechenden Wert aus der [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) Enumeration an.

 Die Enumeration [LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) hat die folgenden möglichen Werte.

- Alle
- Bucheinstellungen
- Zelle Leer
- Zelle Bool
- Zelldaten
- Zellenfehler
- Zellnumerisch
- Zellenzeichenfolge
- Zellwert
- Chart
- Bedingte Formatierung
- Datenvalidierung
- Definierte Namen
- Dokumenteigenschaften
- Formel
- Hyperlinks
- Zusammengeführter Bereich
- Pivot-Tabelle
- Einstellungen
- Form
- Tabellendaten
- Tabelleneinstellungen
- Struktur
- Stil
- Tabelle
- VBA
- XmlMap

## **Filterobjekte beim Laden der Arbeitsmappe**
Der folgende Beispielcode veranschaulicht, wie Diagramme aus der Arbeitsmappe gefiltert werden. Bitte überprüfen Sie die [Beispiel-Excel-Datei](5115258.xlsx), die in diesem Code verwendet wird, und das [Ausgabe-PDF](5115257.pdf), das von ihm generiert wurde. Wie Sie im Ausgabe-PDF sehen können, wurden alle Diagramme aus der Arbeitsmappe gefiltert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **Filterobjekte beim Laden des Arbeitsblatts**
Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115255.xlsx) und filtert die folgenden Daten aus ihren Arbeitsblättern mithilfe eines benutzerdefinierten Filters.

- Es filtert Diagramme aus dem Arbeitsblatt mit dem Namen NoCharts.
- Es filtert Formen aus dem Arbeitsblatt mit dem Namen NoShapes.
- Es filtert bedingte Formatierungen aus dem Arbeitsblatt mit dem Namen NoConditionalFormatting.

Sobald es die [Quell-Excel-Datei](5115255.xlsx) mit einem benutzerdefinierten Filter lädt, nimmt es die Bilder aller Arbeitsblätter nacheinander. Hier sind die Ausgabe-Bilder zur Referenz. Wie Sie sehen können, hat das erste Bild keine Diagramme, das zweite Bild hat keine Formen und das dritte Bild hat keine bedingte Formatierung.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
So verwenden Sie die Klasse CustomLoadFilter gemäß der Arbeitsblattnamen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}
