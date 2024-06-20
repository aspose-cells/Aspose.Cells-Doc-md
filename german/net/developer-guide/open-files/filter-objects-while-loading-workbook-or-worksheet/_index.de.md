---
title: Filterobjekte beim Laden der Arbeitsmappe oder des Arbeitsblatts
type: docs
weight: 330
url: /de/net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Mögliche Verwendungsszenarien**
Bitte verwenden Sie die Eigenschaft [LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) zum Filtern von Daten aus der Arbeitsmappe. Wenn Sie jedoch Daten aus einzelnen Arbeitsblättern filtern möchten, müssen Sie die Methode [LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet) überschreiben. Bitte geben Sie einen geeigneten Wert aus der Enumeration [LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) an, wenn Sie einen [LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) erstellen oder damit arbeiten.

Die Enumeration [LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) hat die folgenden möglichen Werte.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Filterobjekte beim Laden des Arbeitsblatts**
Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115255.xlsx) und filtert die folgenden Daten aus ihren Arbeitsblättern mithilfe eines benutzerdefinierten Filters.

- Es filtert Diagramme aus dem Arbeitsblatt mit dem Namen NoCharts.
- Es filtert Formen aus dem Arbeitsblatt mit dem Namen NoShapes.
- Es filtert bedingte Formatierungen aus dem Arbeitsblatt mit dem Namen NoConditionalFormatting.

Sobald es die [Quell-Excel-Datei](5115255.xlsx) mit einem benutzerdefinierten Filter lädt, nimmt es die Bilder aller Arbeitsblätter nacheinander. Hier sind die Ausgabe-Bilder zur Referenz. Wie Sie sehen können, hat das erste Bild keine Diagramme, das zweite Bild hat keine Formen und das dritte Bild hat keine bedingte Formatierung.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


So verwenden Sie die Klasse CustomLoadFilter gemäß der Arbeitsblattnamen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
