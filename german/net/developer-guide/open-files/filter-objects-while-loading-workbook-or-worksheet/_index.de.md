---
title: Filtern Sie Objekte beim Laden der Arbeitsmappe oder des Arbeitsblatts
type: docs
weight: 330
url: /de/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **Mögliche Nutzungsszenarien**
Bitte verwende[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)-Eigenschaft beim Filtern von Daten aus der Arbeitsmappe. Wenn Sie jedoch Daten aus einzelnen Arbeitsblättern filtern möchten, müssen Sie die überschreiben[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)Methode. Bitte geben Sie den entsprechenden Wert von an[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)Aufzählung beim Erstellen oder Arbeiten mit[Ladefilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

 Das[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)Enumeration hat die folgenden möglichen Werte.

- Alle
- Bucheinstellungen
- ZelleLeer
- CellBool
- CellData
- Zellenfehler
- ZelleNumerisch
- CellString
- Zellwert
- Diagramm
- Bedingte Formatierung
- Datenvalidierung
- DefinierteNamen
- Dokumenteigenschaften
- Formel
- Hyperlinks
- MergedArea
- PivotTable
- Einstellungen
- Form
- Blattdaten
- Tabelleneinstellungen
- Struktur
- Stil
- Tisch
- VBA
- XmlMap
## **Filtern Sie Objekte beim Laden der Arbeitsmappe**
 Der folgende Beispielcode veranschaulicht, wie Diagramme aus der Arbeitsmappe gefiltert werden. Bitte überprüfen Sie die[Excel-Beispieldatei](5115258.xlsx) in diesem Code verwendet und die[PDF ausgeben](5115257.pdf)dadurch erzeugt. Wie Sie im Ausgabe-PDF sehen können, wurden alle Diagramme aus der Arbeitsmappe herausgefiltert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Filtern Sie Objekte beim Laden des Arbeitsblatts**
 Der folgende Beispielcode lädt die[Excel-Quelldatei](5115255.xlsx) und filtert die folgenden Daten aus seinen Arbeitsblättern mit einem benutzerdefinierten Filter.

- Es filtert Diagramme aus dem Arbeitsblatt mit dem Namen NoCharts.
- Es filtert Formen aus dem Arbeitsblatt mit dem Namen NoShapes.
- Es filtert die bedingte Formatierung aus dem Arbeitsblatt mit dem Namen NoConditionalFormatting.

 Einmal lädt es die[Excel-Quelldatei](5115255.xlsx) Mit einem benutzerdefinierten Filter werden die Bilder aller Arbeitsblätter einzeln aufgenommen. Hier sind die Ausgabebilder für Ihre Referenz. Wie Sie sehen, hat das erste Bild keine Diagramme, das zweite Bild keine Formen und das dritte Bild keine bedingte Formatierung.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


So verwenden Sie die CustomLoadFilter-Klasse gemäß den Arbeitsblattnamen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
