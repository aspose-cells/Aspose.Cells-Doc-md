---
title: Werte in einer PivotTable anzeigen als
linktitle: Werte in einer PivotTable anzeigen als
description: Datenfeldwerte in einer PivotTable mit Aspose.Cells for Java als Prozentsatz des Gesamtergebnisses, als Differenz zu einem Basiselement, als laufende Summe, als Rang und vielem mehr anzeigen.
keywords: Aspose.Cells, PivotTable, Werte anzeigen als, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /de/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable aggregiert jedes Datenfeld normalerweise mit einer Aggregatfunktion wie `Sum` oder `Count`. Die Excel-Funktion **„Werte anzeigen als“** ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – etwa einen Prozentsatz des Gesamtergebnisses, eine laufende Summe, eine Differenz zu einem ausgewählten Basiselement oder einen Rang –, sodass Sie Vergleichsanalysen ohne Hilfsformeln oder berechnete Spalten durchführen können.
Typische Anwendungen sind Anteilsanalysen, einschließlich der Prozentwerte für eine Zeile, eine Spalte oder das Gesamtergebnis; kumulative Berichte mit einer laufenden Summe in einem Periodenfeld; Varianzanalysen im Vergleich zu einem Referenzelement mithilfe der Differenz oder der prozentualen Differenz zu einem Basiselement; sowie die Rangfolgebildung von Werten vom kleinsten zum größten oder vom größten zum kleinsten.
In Aspose.Cells for Java wählt die Enumeration `PivotShowValuesAsType` die sekundäre Berechnung aus. Der schreibgeschützte Getter `PivotField.getShowValuesSetting()` gibt ein `PivotShowValuesSetting`-Objekt zurück, dessen Methoden `setShowValuesAs(...)`, `setBaseFieldIndex(...)` und `setBaseItemIndex(...)` das Verhalten konfigurieren; die Komfortmethode `PivotField.showValuesAs(...)` wendet dieselben Einstellungen in einem einzigen Aufruf an. Wenden Sie diese Einstellungen auf ein Daten- oder Wertfeld an, das Sie über `PivotTable.getDataFields()` erhalten.

## **Mitglieder der Enumeration `PivotShowValuesAsType`**
Das Datenfeld behält seine Aggregatfunktion, etwa Sum oder Count, während „Werte anzeigen als“ ausschließlich die Darstellung des aggregierten Werts verändert.
Neben der direkten Verwendung der Set-Methoden von `PivotShowValuesSetting` (siehe letzter Abschnitt) bietet eine Komfortmethode dieselbe Konfiguration mit nur einem Aufruf an. Sie ist in zwei Überladungen verfügbar – eine legt Basisfeld und Basiselement anhand des Index fest, die andere anhand des Namens:

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| Parameter | Bedeutung | Wann er erforderlich ist |
| --- | --- | --- |
| `showValuesAsType` | Die anzuwendende sekundäre Berechnung vom Typ `PivotShowValuesAsType`. | Immer. |
| `baseField` | Nullbasierter Index des Basisfelds unter den Basisfeldern der PivotTable (beispielsweise der Index des Zeilenfelds, zu dem das Basiselement gehört) oder – in der Überladung mit `String` – der Name des Basisfelds. | Für die acht Formate mit Basisbezug unten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); für alle anderen Formate ist `0` (oder `null` in der Überladung mit `String`) zu übergeben. |
| `baseItem` | Nullbasierter Index des Basiselements. Zwei reservierte Kennwerte dienen als Sonderwerte: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) wählt das vorherige Element und `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) das nachfolgende aus. Die Überladung mit `String` übernimmt stattdessen die Beschriftung des Basiselements bzw. `null`, wenn das ausgewählte Format kein Basiselement benötigt. | Nur die drei Formate mit Basiselementbezug (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) werten das Basiselement aus; die fünf feldbezogenen Formate (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, beide Rangformate) ignorieren es – übergeben Sie `0` oder `null`. |

| Berechnungstyp | Verhalten | Parameter für Basiselement und Basisfeld |
| --- | --- | --- |
| `NORMAL` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DIFFERENCE_FROM` | Zeigt den Wert als Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung oder der reservierte Kennwert für das vorherige bzw. nachfolgende Element) |
| `PERCENTAGE_OF` | Zeigt den Wert als Prozentsatz des Werts eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung oder der reservierte Kennwert für das vorherige bzw. nachfolgende Element) |
| `PERCENTAGE_DIFFERENCE_FROM` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung oder der reservierte Kennwert für das vorherige bzw. nachfolgende Element) |
| `RUNNING_TOTAL_IN` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basisfelds an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation bestimmt) |
| `PERCENTAGE_OF_ROW` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PERCENTAGE_OF_COLUMN` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PERCENTAGE_OF_TOTAL` | Zeigt den Wert als Prozentsatz des Gesamtergebnisses an. | — |
| `INDEX` | Zeigt den Wert mithilfe der Excel-Indexformel ((Wert * Gesamtergebnis) / (Zeilensumme * Spaltensumme)) an. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme an (für verschachtelte Zeilenfelder). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme an (für verschachtelte Spaltenfelder). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Zeigt den Wert als Prozentsatz des übergeordneten Gesamtergebnisses an. | `baseField` (das übergeordnete Feld, dessen Gesamtergebnis als Referenz dient) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `baseField` (das Feld, in dem die Werte akkumuliert werden) |
| `RANK_SMALLEST_TO_LARGEST` | Ordnet den Wert einer Rangfolge vom kleinsten (1) bis zum größten zu. | `baseField` (das Feld, dessen Elemente den Bereich der Rangfolge bestimmen) |
| `RANK_LARGEST_TO_SMALLEST` | Ordnet den Wert einer Rangfolge vom größten (1) bis zum kleinsten zu. | `baseField` (das Feld, dessen Elemente den Bereich der Rangfolge bestimmen) |

{{% alert color="primary" %}}
`showValuesAs(...)` setzt genau den Zustand des Objekts `PivotShowValuesSetting` über `setShowValuesAs(...)`, `setBaseFieldIndex(...)` und `setBaseItemIndex(...)` – die Methode und das Eigenschaftsobjekt bieten zwei Möglichkeiten, denselben Zustand zu konfigurieren, und spiegeln die Auswahlfelder für Basisfeld und Basiselement im Excel-Dialog „Werte anzeigen als“.
{{% /alert %}}

## **Werte als Prozentsatz des Gesamtergebnisses anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs(...)` mit `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` auf, um jede Zelle des Datenfelds, einschließlich der Zelle für das Gesamtergebnis, in ihren Anteil am Gesamtergebnis umzuwandeln. Die angezeigten Zahlen geben somit die Anteile der vollständigen Ergebnismenge wieder. Dieses Format bezieht jeden Wert ausschließlich auf das Gesamtergebnis und benötigt daher weder ein Basisfeld noch ein Basiselement – die abschließenden Argumente (`0`, `0`) sind Platzhalter, die vom Format ignoriert werden, wie in der Parametertabelle oben erläutert.

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting abrufen und konfigurieren**
Lesen Sie die aktuelle Konfiguration über `PivotField.getShowValuesSetting()`: Der schreibgeschützte Getter gibt das `PivotShowValuesSetting`-Objekt des Feldes zurück, dessen Eigenschaften die aktive Berechnung „Werte anzeigen als“ beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs(...)` auf – sie schreibt alle Einstellungen mit einem einzigen Aufruf, sodass Sie die Eigenschaften nicht einzeln festlegen müssen.
Das Objekt `PivotShowValuesSetting` enthält den durch `showValuesAs(...)` festgelegten Zustand:
- `getShowValuesAs()` / `setShowValuesAs(...)` ruft die sekundäre Berechnung vom Typ `PivotShowValuesAsType` ab bzw. legt sie fest.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` ruft den nullbasierten Index des Basisfelds innerhalb der Felder der PivotTable ab bzw. legt ihn fest. Er wird von den Formaten mit Basisbezug verwendet.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` ruft das Basiselement ab bzw. legt es fest: einen nullbasierten Index eines bestimmten PivotTable-Elements oder einen der beiden reservierten Kennwerte – `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) für das vorherige Element, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) für das nachfolgende. Es wird von den Formaten mit Basiselementbezug verwendet.
- `getBaseFieldName()` und `getBaseItemCaption()` sind schreibgeschützte Getter, die den ermittelten Basisfeldnamen und die Beschriftung des Basiselements zurückgeben; nach Auswahl des reservierten Kennwerts für das vorherige Element gibt `getBaseItemCaption()` beispielsweise `(previous)` zurück.
Rufen Sie nach dem Aufruf von `showValuesAs(...)` erneut `PivotTable.calculateData()` auf, damit der Datenbereich der PivotTable neu berechnet und mit der aktualisierten Konfiguration neu gerendert wird.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Verwandte Artikel**
- [Wertfelder in einer PivotTable verwalten](/cells/de/java/manage-value-fields/)
- [PivotTable aktualisieren](/cells/de/java/refresh-pivot-table/)
- [Formatvorlage auf eine PivotTable anwenden](/cells/de/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}