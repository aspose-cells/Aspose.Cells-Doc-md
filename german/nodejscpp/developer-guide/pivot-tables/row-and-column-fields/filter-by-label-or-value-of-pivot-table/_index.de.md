---
title: Filtern von Pivot-Tabellen nach Beschriftung oder Wert
linktitle: Filtern von Pivot-Tabellen nach Beschriftung oder Wert
description: Aspose.Cells for Node.js via C++ unterstützt umfassende Filterfunktionen für Pivot-Tabellen. Dieser Artikel erläutert, wie Sie Pivot-Tabellen-Daten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Aus- oder Einblenden von Pivot-Elementen filtern.
keywords: Aspose.Cells, Node.js via C++ Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells bietet fünf praxisnahe Strategien zum Filtern der in einer Pivot-Tabelle angezeigten Daten. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld ausschließlich Datums-/Uhrzeit-Zellen oder leere Zellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter einsetzen, um nach einem Wertfeld zu sortieren, oder einzelne Pivot-Elemente mithilfe der `IsHidden`-Eigenschaft manuell aus- und einblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}
## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, enthalten in ihren Rohzusammenfassungen jedoch oft weit mehr Informationen, als Sie darstellen möchten. Das Filtern ist der primäre Mechanismus, um eine Pivot-Tabelle auf die Zeilen, Spalten oder Werte einzugrenzen, die für einen bestimmten Bericht relevant sind. Aspose.Cells for Node.js via C++ spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt sie programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Elemente von Zeilen- oder Spaltenfeldern basierend auf deren Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die ausschließlich Datums-/Uhrzeit-Werte (oder leere Werte) enthalten.
3. **Wertfilter** — filtert Elemente basierend auf den aggregierten Werten eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente, sortiert nach einem Wertfeld.
5. **Pivot-Elemente aus-/einblenden** — steuert manuell die Sichtbarkeit jedes einzelnen Elements in einem Feld.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nach Anwendung eines Filters müssen Sie `refreshData()` und `calculateData()` für die Pivot-Tabelle aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.
## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es Ihnen, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem deren Textbeschriftungen mit einem Muster verglichen werden. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder einem anderen beschriftungsbasierten Kriterium entsprechen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.filterByLabel(PivotFilterType, string)` bereit. Die Enumeration `PivotFilterType` enthält Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und weitere. Das zweite Argument liefert die Beschriftungszeichenfolge für den Vergleich.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen Pivot-Tabelle, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die Pivot-Tabelle und speichert das Ergebnis.
```javascript
fileName = "sample.xlsx";
let prefix = "B";

// Lädt die vorhandene Arbeitsmappe mit einer Pivot-Tabelle
let workbook = new AsposeCells.Workbook(fileName);

// Zugriff auf das Arbeitsblatt über den Index (erstes Arbeitsblatt)
let worksheet = workbook.getWorksheets().get(0);

// Zugriff auf die Pivot-Tabelle über den Index
let pivotTable = worksheet.getPivotTables().get(0);

// Ruft das PivotField der ersten Zeile ab
let rowField = pivotTable.getRowFields().get(0);

// Wendet den Beschriftungsfilter an — zeigt nur Zeilenelemente, deren Beschriftungen mit dem angegebenen Präfix beginnen
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Aktualisiert und berechnet die Pivot-Tabellendaten neu, damit der Filter wirksam wird
pivotTable.getPivotCache().refresh();

// Speichert die Arbeitsmappe wieder auf der Festplatte
workbook.save(fileName);
```
## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine Pivot-Tabelle nach datumsbasierten Kriterien wie heute, letzte Woche, diesem Monat, nächstem Quartal oder einem bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezialisierte Filter, die ausschließlich für Felder funktionieren, die Datums-/Uhrzeit-Informationen speichern.
{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datums-/Uhrzeit-Zellen oder leere Werte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
{{% /alert %}}
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Abhängig vom gewählten Filtertyp übergeben Sie ein oder zwei `DateTime`-Werte (für `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}

// Lade die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
const workbook = new AsposeCells.Workbook(inputPath);

// Greife auf das Arbeitsblatt zu, das die Pivot-Tabelle enthält (nach Index)
const worksheet = workbook.getWorksheets().get(0);

// Greife auf die Pivot-Tabelle nach Index zu
const pivotTable = worksheet.getPivotTables().get(0);

// Rufe das Datums-PivotField aus dem Zeilenbereich ab
// (Der Datumsfilter funktioniert nur, wenn der Zeilen-/Spaltenbereich nur Datums-/Uhrzeit-Zellen oder Leerzeichen enthält)
const dateField = pivotTable.getRowFields().get(0);

// Definiere das Datumskriterium für den Zwischen-Filter
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// Wende den Datumsfilter auf das Pivot-Feld an
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Aktualisiere und berechne die Pivot-Tabelle neu, damit der Filter wirksam wird
pivotTable.getPivotCache().refresh();

// Speichere die Arbeitsmappe
workbook.save(outputPath);
```
## **Wertfilter**
Wertfilter arbeiten mit den aggregierten Werten, die eine Pivot-Tabelle in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle sind das Anzeigen nur der Produkte, deren Umsatzsumme einen Zielwert übersteigt, oder nur der Regionen, deren Transaktionsanzahl in einem bestimmten Bereich liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` bereit. Der Parameter `filterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `valueField` gibt an, welches Datenfeld ausgewertet werden soll, und das/die letzte(n) Argument(e) liefert/liefern den/die Schwellenwert(e).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```javascript
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```
## **Top-10-Filter**
Der Top-10-Filter ist eine spezialisierte Form des Wertfilters, der nur die obersten oder untersten N Elemente basierend auf einem ausgewählten Wertfeld beibehält. Er wird häufig für Ranking-Berichte verwendet, etwa für "Top-10-Produkte nach Umsatz" oder "Untere 5 Regionen nach Verkaufsanzahl".
{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die Pivot-Tabelle ein oder mehrere Wert-Pivot-Felder im Datenbereich enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kennzahl, gegen die die Elemente sortiert werden können, und der Filter kann nicht angewendet werden.
{{% /alert %}}
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` bereit. Der Parameter `itemCount` definiert, wie viele Elemente beibehalten werden, `isTop` gibt an, ob die obersten Elemente (true) oder die untersten Elemente (false) beibehalten werden sollen, `valueField` verweist auf das für die Rangfolge verwendete Datenfeld, und `filterType` steuert, wie der Wert berechnet wird (typischerweise `Sum`, aber auch `Count` und `Percent`).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die obersten 10 Elemente nach der Umsatzsumme beizubehalten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```javascript
const AsposeCells = require("aspose.cells");

// Lade die bestehende Arbeitsmappe, die die Pivot-Tabelle enthält
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// Greife auf das Arbeitsblatt zu, das die Pivot-Tabelle enthält (Index 0)
const worksheet = workbook.getWorksheets().get(0);

// Greife über den Index auf die Pivot-Tabelle zu
const pivotTable = worksheet.getPivotTables().get(0);

// Stelle sicher, dass mindestens ein Wert-PivotField im Datenbereich vorhanden ist
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Die Pivot-Tabelle enthält kein Wert-PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);

// Rufe das Ziel-Zeilen-PivotField ab (das Feld, auf das wir Top 10 anwenden möchten)
const rowField = pivotTable.getRowFields().get(0);

// Das erste (und einzige) Datenfeld befindet sich am Index 0; Top 10 ordnet danach.
const valueFieldIndex = 0;

// Wende den Top-10-Filter auf das Zeilenfeld an:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (Top N; false würde Bottom N bedeuten)
//   - valueFieldIndex = der Index des Datenfelds, das zum Rangordnen der Elemente verwendet wird
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Aktualisiere die Daten der Pivot-Tabelle und berechne sie neu, damit der Filter wirksam wird
pivotTable.getPivotTableCache().refresh();

// Speichere die Arbeitsmappe
workbook.save(outputPath);
```
## **Filtern durch Aus- oder Einblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht Aspose.Cells die direkte Steuerung der Sichtbarkeit jedes einzelnen Pivot-Elements. Durch Iteration über die Sammlung `PivotItems` eines `PivotField` und Umschalten der Eigenschaft `IsHidden` können Sie bestimmte Elemente selektiv unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `IsHidden = true` blendet das Element aus der Pivot-Tabelle aus; das Setzen von `IsHidden = false` blendet es wieder ein und macht es erneut sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, etwa beim Ausblenden einer kleinen Anzahl benannter Kategorien, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine Pivot-Tabelle, blendet ein bestimmtes Element namentlich aus, zeigt, wie es wieder eingeblendet wird, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```javascript
const AsposeCells = require("aspose.cells");

// Vorhandene Arbeitsmappe laden, die eine Pivot-Tabelle enthält
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Auf das erste Arbeitsblatt zugreifen, das die Pivot-Tabelle enthält
const sheet = workbook.getWorksheets().get(0);

// Auf die Pivot-Tabelle über den Index zugreifen (die erste Pivot-Tabelle auf dem Blatt)
const pivotTable = sheet.getPivotTables().get(0);

// Das Ziel-PivotField abrufen (das erste Zeilenbeschriftungsfeld, in dem wir Elemente aus-/einblenden)
const pivotField = pivotTable.getRowFields().get(0);

// Durch die PivotItems-Sammlung des ausgewählten PivotField iterieren
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // Pivot-Elemente ausblenden, die einem bestimmten Namen/Kriterium entsprechen
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // Einblenden demonstrieren: ein zuvor ausgeblendetes Pivot-Element wieder anzeigen
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// Die Pivot-Tabelle aktualisieren und neu berechnen, damit die Änderungen wirksam werden
pivotTable.getPivotCache().refreshData();

// Die Arbeitsmappe speichern – ausgeblendete Elemente bleiben in den zugrunde liegenden Daten erhalten,
// werden jedoch in der angezeigten Pivot-Tabelle ausgeschlossen
workbook.save("output_pivot_filtered.xlsx");
```
## **Zusammenfassung**
Aspose.Cells for Node.js via C++ bietet einen vollständigen Satz an Filterfunktionen für Pivot-Tabellen, die denen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertfilter decken die gängigsten Analyseszenarien ab, während der Top-10-Filter Ranking-Berichte abdeckt. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.IsHidden` einen flexiblen Fallback auf Elementebene. Die Kombination dieser Strategien — beispielsweise das Anwenden eines Beschriftungsfilters und anschließendes Ausblenden bestimmter Elemente — ermöglicht es Ihnen, vollständig aus Code heraus präzise zugeschnittene Pivot-Tabellen-Berichte zu erstellen.
{{< app/cells/assistant language="nodejs-cpp" >}}