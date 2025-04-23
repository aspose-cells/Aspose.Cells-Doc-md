---
title: Filterobjekte beim Laden der Arbeitsmappe oder des Arbeitsblatts
type: docs
weight: 330
url: /de/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Mögliche Verwendungsszenarien**
Bitte verwenden Sie die [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) Eigenschaft beim Filtern von Daten aus dem Arbeitsbuch. Wenn Sie Daten aus einzelnen Arbeitsblättern filtern möchten, müssen Sie die [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet) Methode überschreiben. Geben Sie während der Erstellung oder Arbeit mit [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) einen geeigneten Wert aus der [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) Aufzählung an.

Die Aufzählung [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) hat die folgenden möglichen Werte.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

