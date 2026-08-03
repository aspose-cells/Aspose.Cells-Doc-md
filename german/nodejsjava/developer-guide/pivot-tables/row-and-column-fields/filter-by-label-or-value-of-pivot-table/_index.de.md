---
title: Pivot-Tabellen nach Beschriftung oder Wert filtern
linktitle: Pivot-Tabellen nach Beschriftung oder Wert filtern
description: Aspose.Cells for Node.js via Java unterstützt umfassende Pivot-Tabellen-Filterfunktionen. Dieser Artikel erklärt, wie Pivot-Tabellen-Daten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern und durch Aus- oder Einblenden von Pivot-Elementen gefiltert werden.
keywords: Aspose.Cells, Node.js via Java Bibliothek, Tabellenkalkulation, PivotTable, Filter, Beschriftungsfilter, Wertefilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/nodejs-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells bietet fünf praxisorientierte Strategien zum Filtern der in einer PivotTable angezeigten Daten. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Datums-/Uhrzeit-Zellen oder leere Zellen enthält, Wertefilter auf aggregierte Zahlen anwenden, Top-10-Filter zum Rangordnen nach einem Wertefeld einsetzen oder einzelne Pivot-Elemente über die Eigenschaft `IsHidden` manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}
## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, aber rohe Zusammenfassungen enthalten häufig weitaus mehr Informationen, als Sie darstellen müssen. Filtern ist der primäre Mechanismus, um eine PivotTable auf die Zeilen, Spalten oder Werte einzugrenzen, die für einen bestimmten Bericht relevant sind. Aspose.Cells for Node.js via Java spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt sie programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** – filtert Elemente von Zeilen- oder Spaltenfeldern anhand ihrer Textbeschriftungen.
2. **Datumsfilter** – filtert Zeilen- oder Spaltenfelder, die ausschließlich Datums-/Uhrzeit-Werte (oder leere Werte) enthalten.
3. **Wertefilter** – filtert Elemente basierend auf den aggregierten Werten eines Datenfelds.
4. **Top-10-Filter** – zeigt nur die obersten oder untersten N Elemente, geordnet nach einem Wertefeld.
5. **Pivot-Elemente aus- / einblenden** – steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nachdem ein beliebiger Filter angewendet wurde, müssen Sie `refreshData()` und `calculateData()` auf der PivotTable aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.
## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es Ihnen, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem deren Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder einem anderen beschriftungsbasierten Kriterium entsprechen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.filterByLabel(PivotFilterType, string)` bereit. Die Enumeration `PivotFilterType` enthält Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und weitere. Das zweite Argument liefert die Beschriftungszeichenfolge für den Vergleich.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen PivotTable, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die PivotTable und speichert das Ergebnis.
```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Lade die vorhandene Arbeitsmappe, die eine Pivot-Tabelle enthält
let workbook = new AsposeCells.Workbook(fileName);

// Greife per Index auf das Arbeitsblatt zu (erstes Arbeitsblatt)
let worksheet = workbook.getWorksheets().get(0);

// Greife per Index auf die Pivot-Tabelle zu
let pivotTable = worksheet.getPivotTables().get(0);

// Hole das erste Zeilen-PivotField
let rowField = pivotTable.getRowFields().get(0);

// Wende den Beschriftungsfilter an — zeige nur Zeilenelemente, deren Beschriftungen mit dem angegebenen Präfix beginnen
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Aktualisiere und berechne die Daten der Pivot-Tabelle neu, damit der Filter wirksam wird
pivotTable.getPivotCache().refresh();

// Speichere die Arbeitsmappe zurück auf die Festplatte
workbook.save(fileName);
```
## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine PivotTable anhand datumsbezogener Kriterien wie heute, letzte Woche, diesen Monat, nächstes Quartal oder einen bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezialisierte Filter, die nur für Felder funktionieren, die Datums-/Uhrzeit-Informationen speichern.
{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datums-/Uhrzeit-Zellen oder leere Werte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und dass alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
{{% /alert %}}
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Abhängig vom gewählten Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (für `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die PivotTable und speichert die Arbeitsmappe.
```javascript
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}

// Lade die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
var workbook = new AsposeCells.Workbook(inputPath);

// Greife auf das Arbeitsblatt zu, das die Pivot-Tabelle enthält (nach Index)
var worksheet = workbook.getWorksheets().get(0);

// Greife auf die Pivot-Tabelle nach Index zu
var pivotTable = worksheet.getPivotTables().get(0);

// Rufe das Datums-PivotField aus dem Zeilenbereich ab
// (Datumsfilter funktionieren nur, wenn der Zeilen-/Spaltenbereich nur Datums-/Uhrzeitzellen oder Leerzeichen enthält)
let dateField = pivotTable.getRowFields().get(0);

// Definiere das Datumskriterium für den Zwischen-Filter
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);

// Wende den Datumsfilter auf das Pivot-Feld an
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Aktualisiere und berechne die Pivot-Tabelle neu, damit der Filter wirksam wird
pivotTable.getPivotCache().refresh();

// Speichere die Arbeitsmappe
workbook.save(outputPath);
```
## **Wertefilter**
Wertefilter arbeiten mit den aggregierten Werten, die eine PivotTable in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Gesamtsummen mit einem Schwellenwert. Typische Anwendungsfälle sind das Anzeigen nur von Produkten, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur von Regionen, deren Anzahl an Transaktionen innerhalb eines Bereichs liegt.
Aspose.Cells stellt die Wertefilterung über die Methode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` bereit. Der Parameter `filterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `valueField` legt fest, welches Datenfeld ausgewertet werden soll, und das bzw. die letzten Argumente liefern den bzw. die Schwellenwerte.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, wendet einen Wertefilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die PivotTable und speichert die Arbeitsmappe.
```javascript
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);

var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);

// Den Datenfeldindex manuell finden, da PivotFieldCollection kein IndexOf hat
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.Pivot.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```
## **Top-10-Filter**
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, der nur die höchsten oder niedrigsten N Elemente basierend auf einem ausgewählten Wertefeld beibehält. Er wird häufig für Rangordnungsberichte wie „Top 10 Produkte nach Umsatz" oder „Untere 5 Regionen nach Verkaufsanzahl" verwendet.
{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die PivotTable ein oder mehrere Wert-Pivot-Felder im Datenbereich enthält. Ohne mindestens ein Wertefeld gibt es keine aggregierte Messgröße, gegen die die Elemente geordnet werden können, und der Filter kann nicht angewendet werden.
{{% /alert %}}
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` bereit. Der Parameter `itemCount` definiert, wie viele Elemente beibehalten werden sollen, `isTop` gibt an, ob die obersten Elemente (true) oder die untersten Elemente (false) beibehalten werden sollen, `valueField` verweist auf das für die Rangordnung verwendete Datenfeld, und `filterType` steuert, wie der Wert berechnet wird (typischerweise `Sum`, aber auch `Count` und `Percent`).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer PivotTable, die ein Wertefeld enthält, wendet einen Top-10-Filter an, um nur die 10 höchsten Elemente nach der Summe der Verkäufe beizubehalten, aktualisiert die PivotTable und speichert die Arbeitsmappe.
```javascript
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);

// Zugriff auf das Arbeitsblatt, das die Pivot-Tabelle enthält (Index 0)
let worksheet = workbook.getWorksheets().get(0);

// Zugriff auf die Pivot-Tabelle nach Index
let pivotTable = worksheet.getPivotTables().get(0);

// Bestätigen, dass mindestens ein Wert-PivotField im Datenbereich vorhanden ist
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);

// Das Ziel-Zeilen-PivotField abrufen (das Feld, auf das wir Top 10 anwenden möchten)
let rowField = pivotTable.getRowFields().get(0);

// Das erste (und einzige) Datenfeld befindet sich bei Index 0; Top 10 ordnet danach.
let valueFieldIndex = 0;

// Den Top-10-Filter auf das Zeilenfeld anwenden:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (obere N; false würde untere N bedeuten)
//   - valueFieldIndex = der Index des Datenfelds, das zum Sortieren der Elemente verwendet wird
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Die Pivot-Tabellendaten aktualisieren und neu berechnen, damit der Filter wirksam wird
pivotTable.getPivotCache().refresh();

// Die Arbeitsmappe speichern
workbook.save(outputPath);
```
## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Durch Iteration über die Sammlung `PivotItems` eines `PivotField` und Umschalten der Eigenschaft `IsHidden` können Sie bestimmte Elemente selektiv unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `IsHidden = true` blendet das Element aus der PivotTable aus; das Setzen von `IsHidden = false` blendet es wieder ein und macht es sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, etwa beim Ausblenden einer kleinen Anzahl benannter Kategorien, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine PivotTable, blendet ein bestimmtes Element anhand seines Namens aus, zeigt, wie es wieder eingeblendet wird, aktualisiert die PivotTable und speichert die Arbeitsmappe.
```javascript
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Zugriff auf das erste Arbeitsblatt, das die Pivot-Tabelle enthält
let sheet = workbook.getWorksheets().get(0);

// Zugriff auf die Pivot-Tabelle über den Index (die erste Pivot-Tabelle auf dem Blatt)
let pivotTable = sheet.getPivotTables().get(0);

// Abrufen des Ziel-PivotFields (das erste Zeilenbeschriftungsfeld, in dem wir Elemente ausblenden/einblenden werden)
let pivotField = pivotTable.getRowFields().get(0);

// Durchlaufen der PivotItems-Sammlung des ausgewählten PivotFields
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);

    // Pivot-Elemente ausblenden, die einem bestimmten Namen/Kriterium entsprechen
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setIsHidden(true);
    }

    // Einblenden demonstrieren: Ein zuvor ausgeblendetes Pivot-Element wieder anzeigen
    if (item.getName() == "Item3") {
        item.setIsHidden(false);
    }
}

// Pivot-Tabelle aktualisieren und neu berechnen, damit die Änderungen wirksam werden
pivotTable.getPivotCache().refreshData();

// Arbeitsmappe speichern – ausgeblendete Elemente bleiben in den zugrunde liegenden Daten erhalten,
// werden jedoch aus der angezeigten Pivot-Tabellen-Ausgabe ausgeschlossen
workbook.save("output_pivot_filtered.xlsx");
```
## **Zusammenfassung**
Aspose.Cells for Node.js via Java stellt einen vollständigen Satz an Pivot-Tabellen-Filterfunktionen bereit, die denen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertefilter decken die gängigsten Analyseszenarien ab, während der Top-10-Filter Rangordnungsberichte verarbeitet. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.IsHidden` eine flexible, elementbezogene Rückfalloption. Die Kombination dieser Strategien – beispielsweise das Anwenden eines Beschriftungsfilters und das anschließende Ausblenden bestimmter Elemente – ermöglicht es Ihnen, vollständig aus Code heraus präzise zugeschnittene Pivot-Tabellen-Berichte zu erstellen.
{{< app/cells/assistant language="nodejs-java" >}}