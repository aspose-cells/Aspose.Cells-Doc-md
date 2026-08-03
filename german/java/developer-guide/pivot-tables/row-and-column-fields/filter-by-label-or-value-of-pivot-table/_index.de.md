---
title: Filtern von Pivot-Tabellen nach Beschriftung oder Wert
linktitle: Filtern von Pivot-Tabellen nach Beschriftung oder Wert
description: Aspose.Cells for Java unterstützt umfassende Filterfunktionen für Pivot-Tabellen. Dieser Artikel erklärt, wie Pivot-Tabellen-Daten mit Beschriftungsfiltern, Datumsfiltern, Wertfiltern, Top-10-Filtern sowie durch Ein- oder Ausblenden von Pivot-Elementen gefiltert werden.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Filter, Beschriftungsfilter, Wertfilter, Datumsfilter, Top-10-Filter, Pivot-Element, Pivot-Element ausblenden
type: docs
weight: 10
url: /de/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells bietet fünf praktische Strategien zum Filtern der in einer Pivot-Tabelle angezeigten Daten. Sie können Beschriftungsfilter auf textbasierte Zeilen- oder Spaltenfelder anwenden, Datumsfilter verwenden, wenn das Feld nur Datums-/Uhrzeit-Zellen oder leere Zellen enthält, Wertfilter auf aggregierte Zahlen anwenden, Top-10-Filter verwenden, um nach einem Wertfeld zu sortieren, oder einzelne Pivot-Elemente mithilfe der Eigenschaft `IsHidden` manuell ein- und ausblenden. Jede Strategie wird über dedizierte APIs der Klassen `PivotField` und `PivotItem` bereitgestellt.
{{% /alert %}}
## **Einführung**
Pivot-Tabellen sind leistungsstarke Analysewerkzeuge, aber rohe Zusammenfassungen enthalten oft weit mehr Informationen, als Sie darstellen möchten. Filtern ist der primäre Mechanismus, um eine Pivot-Tabelle auf die Zeilen, Spalten oder Werte einzugrenzen, die für einen bestimmten Bericht relevant sind. Aspose.Cells for Java spiegelt die in Microsoft Excel verfügbaren Filterfunktionen wider und stellt diese programmatisch bereit, sodass die Berichterstellung vollständig automatisiert werden kann.
Die folgenden Filterstrategien werden in diesem Artikel behandelt:
1. **Beschriftungsfilter** — filtert Zeilen- oder Spaltenfeldelemente basierend auf ihren Textbeschriftungen.
2. **Datumsfilter** — filtert Zeilen- oder Spaltenfelder, die nur Datums-/Uhrzeit-Werte (oder leere Werte) enthalten.
3. **Wertfilter** — filtert Elemente basierend auf den aggregierten Werten eines Datenfelds.
4. **Top-10-Filter** — zeigt nur die obersten oder untersten N Elemente an, sortiert nach einem Wertfeld.
5. **Pivot-Elemente ein-/ausblenden** — steuert die Sichtbarkeit jedes einzelnen Elements in einem Feld manuell.
Jeder Ansatz verwendet eine andere Methode der Klasse `PivotField` oder eine Eigenschaft der Klasse `PivotItem`. Nachdem Sie einen Filter angewendet haben, müssen Sie `refreshData()` und `calculateData()` auf der Pivot-Tabelle aufrufen, damit die zwischengespeicherten Daten und berechneten Werte den neuen Filterzustand widerspiegeln.
## **Beschriftungsfilter**
Ein Beschriftungsfilter ermöglicht es Ihnen, die Elemente eines Zeilen- oder Spaltenfelds zu filtern, indem Sie deren Textbeschriftungen mit einem Muster vergleichen. Dies ist nützlich, wenn Sie nur Produkte anzeigen möchten, deren Namen mit einem bestimmten Buchstaben beginnen, ein bestimmtes Wort enthalten oder ein anderes beschriftungsbasiertes Kriterium erfüllen.
Aspose.Cells stellt die Beschriftungsfilterung über die Methode `PivotField.filterByLabel(PivotFilterType, String)` bereit. Die Enumeration `PivotFilterType` enthält Werte wie `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` und so weiter. Das zweite Argument liefert die Beschriftungszeichenfolge, die für den Vergleich verwendet wird.
Das folgende Beispiel lädt eine Arbeitsmappe mit einer vorhandenen Pivot-Tabelle, wendet einen Beschriftungsfilter an, sodass nur Elemente sichtbar bleiben, deren Beschriftungen mit einem angegebenen Präfix beginnen, aktualisiert die Pivot-Tabelle und speichert das Ergebnis.
```java
import com.aspose.cells.*;

String fileName = "sample.xlsx";
String prefix = "B";

// Laden Sie die vorhandene Arbeitsmappe mit einer Pivot-Tabelle
Workbook workbook = new Workbook(fileName);

// Auf das Arbeitsblatt über den Index zugreifen (erstes Arbeitsblatt)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Auf die Pivot-Tabelle über den Index zugreifen
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Das erste Zeilen-PivotField abrufen
PivotField rowField = pivotTable.getRowFields().get(0);

// Den Beschriftungsfilter anwenden - nur Zeilenelemente anzeigen, deren Beschriftungen mit dem angegebenen Präfix beginnen
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");

// Die Pivot-Tabellen-Daten aktualisieren und neu berechnen, damit der Filter wirksam wird
pivotTable.refreshData();

// Die Arbeitsmappe wieder auf der Festplatte speichern
workbook.save(fileName);
```
## **Datumsfilter**
Datumsfilter ermöglichen es Ihnen, eine Pivot-Tabelle nach datumsbasierten Kriterien wie heute, letzte Woche, diesem Monat, nächstes Quartal oder einem bestimmten Datumsbereich einzugrenzen. Es handelt sich um spezielle Filter, die nur bei Feldern funktionieren, die Datums-/Uhrzeit-Informationen speichern.
{{% alert color="primary" %}}
Der Datumsfilter funktioniert nur, wenn der Zeilen- oder Spaltenbereich ausschließlich Datums-/Uhrzeit-Zellen oder leere Werte enthält. Wenn das zugrunde liegende Feld andere Datentypen wie Zahlen oder Text enthält, liefert der Datumsfilter nicht das erwartete Ergebnis. Stellen Sie sicher, dass das Feld als Datum formatiert ist und alle Werte gültige `DateTime`-Instanzen oder leere Zellen sind, bevor Sie diesen Filter anwenden.
{{% /alert %}}
Aspose.Cells stellt die Datumsfilterung über die Methode `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` bereit. Die Enumeration `PivotFilterType` enthält dedizierte Datumswerte wie `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` und `Between`. Abhängig vom gewählten Filtertyp übergeben Sie einen oder zwei `DateTime`-Werte (für `Between` übergeben Sie das Start- und Enddatum).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, deren Zeilenbereich ein Datumsfeld enthält, wendet einen Datumsfilter an, der die sichtbaren Elemente auf einen bestimmten Datumsbereich beschränkt, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```java
import java.io.File;
import java.io.FileNotFoundException;

String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";

if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}

// Laden Sie die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
Workbook workbook = new Workbook(inputPath);

// Greifen Sie auf das Arbeitsblatt zu, das die Pivot-Tabelle enthält (nach Index)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Greifen Sie nach Index auf die Pivot-Tabelle zu
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Rufen Sie das Datums-PivotField aus dem Zeilenbereich ab
// (Datumsfilter funktioniert nur, wenn der Zeilen-/Spaltenbereich nur Datums-/Uhrzeit-Zellen oder leere Zellen enthält)
PivotField dateField = pivotTable.getRowFields().get(0);

// Definieren Sie das Datumskriterium für den Zwischen-Filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Wenden Sie den Datumsfilter auf das Pivot-Feld an
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);

// Aktualisieren und berechnen Sie die Pivot-Tabelle neu, damit der Filter wirksam wird
pivotTable.refreshData();

// Speichern Sie die Arbeitsmappe
workbook.save(outputPath);
```
## **Wertfilter**
Wertfilter arbeiten mit den aggregierten Werten, die eine Pivot-Tabelle in ihrem Datenbereich berechnet. Anstatt Textbeschriftungen abzugleichen, vergleichen sie numerische Summen mit einem Schwellenwert. Typische Anwendungsfälle umfassen das Anzeigen nur von Produkten, deren Umsatzsumme einen Zielbetrag überschreitet, oder nur von Regionen, deren Transaktionsanzahl innerhalb eines Bereichs liegt.
Aspose.Cells stellt die Wertfilterung über die Methode `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` bereit. Der Parameter `filterType` verwendet Werte wie `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` und `ValueLessThanOrEqual`. Der Parameter `valueField` gibt an, welches Datenfeld ausgewertet werden soll, und das/die letzte(n) Argument(e) liefert/liefern den/die Schwellenwert(e).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, wendet einen Wertfilter an, der nur Elemente beibehält, deren aggregierter Umsatz einen numerischen Schwellenwert überschreitet, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);

PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);

// Den Datenfeldindex manuell suchen, da PivotFieldCollection keine IndexOf-Methode besitzt
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}

pivotTable.refreshData();

workbook.save("output.xlsx");
```
## **Top-10-Filter**
Der Top-10-Filter ist eine spezielle Form des Wertfilters, der nur die höchsten oder niedrigsten N Elemente basierend auf einem ausgewählten Wertfeld beibehält. Er wird häufig für Ranking-Berichte verwendet, wie etwa „Top 10 Produkte nach Umsatz" oder „Untere 5 Regionen nach Verkaufsanzahl".
{{% alert color="primary" %}}
Der Top-10-Filter ist nur wirksam, wenn die Pivot-Tabelle ein oder mehrere Wert-Pivot-Felder im Datenbereich enthält. Ohne mindestens ein Wertfeld gibt es keine aggregierte Kennzahl, gegen die die Elemente eingestuft werden können, und der Filter kann nicht angewendet werden.
{{% /alert %}}
Aspose.Cells stellt die Top-10-Filterung über die Methode `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)` bereit. Der Parameter `itemCount` definiert, wie viele Elemente beibehalten werden sollen, `isTop` gibt an, ob die obersten Elemente (true) oder die untersten Elemente (false) beibehalten werden sollen, `valueField` verweist auf das für die Rangfolge verwendete Datenfeld, und `filterType` steuert, wie der Wert berechnet wird (typischerweise `Sum`, aber auch `Count` und `Percent`).
Das folgende Beispiel lädt eine Arbeitsmappe mit einer Pivot-Tabelle, die ein Wertfeld enthält, wendet einen Top-10-Filter an, um nur die obersten 10 Elemente nach der Umsatzsumme beizubehalten, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```java
ells.*;

// Laden Sie die vorhandene Arbeitsmappe, die die Pivot-Tabelle enthält
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Zugriff auf das Arbeitsblatt, das die Pivot-Tabelle enthält (Index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Zugriff auf die Pivot-Tabelle nach Index
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Bestätigen, dass mindestens ein Wert-PivotField im Datenbereich vorhanden ist
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);

// Abrufen des Ziel-Zeilen-PivotField (das Feld, auf das wir Top 10 anwenden möchten)
PivotField rowField = pivotTable.getRowFields().get(0);

// Das erste (und einzige) Datenfeld befindet sich bei Index 0; Top 10 sortiert danach.
int valueFieldIndex = 0;

// Anwenden des Top-10-Filters auf das Zeilenfeld:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (Top N; false würde Bottom N bedeuten)
//   - valueFieldIndex = der Index des Datenfelds, das zum Sortieren der Elemente verwendet wird
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);

// Aktualisieren der Pivot-Tabellendaten und Neuberechnung, damit der Filter wirksam wird
pivotTable.refreshData();

// Speichern der Arbeitsmappe
workbook.save(outputPath);
```
## **Filtern durch Ein- oder Ausblenden von Pivot-Elementen**
Zusätzlich zu den strukturierten Filter-APIs ermöglicht es Ihnen Aspose.Cells, die Sichtbarkeit jedes einzelnen Pivot-Elements direkt zu steuern. Durch Iteration durch die `PivotItems`-Sammlung eines `PivotField` und Umschalten der Eigenschaft `IsHidden` können Sie bestimmte Elemente selektiv unterdrücken, ohne einen formelbasierten Filter anzuwenden. Das Setzen von `IsHidden = true` blendet das Element aus der Pivot-Tabelle aus; das Setzen von `IsHidden = false` macht es wieder sichtbar.
Dieser Ansatz ist nützlich, wenn die Filterregel unregelmäßig oder elementspezifisch ist, beispielsweise wenn eine kleine Anzahl benannter Kategorien ausgeblendet werden soll, die in einem bestimmten Bericht nicht erscheinen sollen. Das folgende Beispiel lädt eine Pivot-Tabelle, blendet ein bestimmtes Element nach Namen aus, zeigt, wie es wieder eingeblendet wird, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.
```java
import com.aspose.cells.*;

// Eine vorhandene Arbeitsmappe laden, die eine Pivot-Tabelle enthält
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Auf das erste Arbeitsblatt zugreifen, das die Pivot-Tabelle enthält
Worksheet sheet = workbook.getWorksheets().get(0);

// Auf die Pivot-Tabelle nach Index zugreifen (die erste Pivot-Tabelle auf dem Blatt)
PivotTable pivotTable = sheet.getPivotTables().get(0);

// Das Ziel-PivotField abrufen (das erste Zeilenbeschriftungsfeld, in dem wir Elemente ausblenden/einblenden werden)
PivotField pivotField = pivotTable.getRowFields().get(0);

// Durch die PivotItems-Sammlung des ausgewählten PivotField iterieren
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);

    // Pivot-Elemente ausblenden, die einem bestimmten Namen/Kriterium entsprechen
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }

    // Einblenden demonstrieren: ein zuvor ausgeblendetes Pivot-Element wieder anzeigen
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}

// Die Pivot-Tabelle aktualisieren und neu berechnen, damit die Änderungen wirksam werden
pivotTable.refreshData();

// Die Arbeitsmappe speichern - ausgeblendete Elemente bleiben in den zugrunde liegenden Daten
// werden aber aus der angezeigten Pivot-Tabellen-Ausgabe ausgeschlossen
workbook.save("output_pivot_filtered.xlsx");
```
## **Zusammenfassung**
Aspose.Cells for Java bietet einen vollständigen Satz von Filterfunktionen für Pivot-Tabellen, die denen in Microsoft Excel entsprechen. Beschriftungs-, Datums- und Wertfilter decken die häufigsten Analyseszenarien ab, während der Top-10-Filter Ranking-Berichte verarbeitet. Wenn die Filterregel unregelmäßig ist, bietet die Eigenschaft `PivotItem.IsHidden` einen flexiblen Fallback auf Elementebene. Die Kombination dieser Strategien — beispielsweise das Anwenden eines Beschriftungsfilters und anschließendes Ausblenden bestimmter Elemente — ermöglicht es Ihnen, präzise zielgerichtete Pivot-Tabellen-Berichte vollständig aus Code zu erstellen.
{{< app/cells/assistant language="java" >}}