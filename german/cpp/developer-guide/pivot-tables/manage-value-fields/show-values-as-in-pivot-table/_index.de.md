---
title: „Werte anzeigen als“ in einer PivotTable mit Aspose.Cells for C++
linktitle: „Werte anzeigen als“ in einer PivotTable mit Aspose.Cells for C++
description: Mit Aspose.Cells for C++ Werte von Datenfeldern in einer PivotTable als Prozentsatz des Gesamtwerts, als Differenz zu einem Basiselement, als laufende Summe, als Rang und in weiteren Formaten anzeigen.
keywords: Aspose.Cells, C++, PivotTable, Werte anzeigen als, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /de/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable aggregiert normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `Sum` oder `Count`. Die Excel-Funktion **„Werte anzeigen als“** ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus diesem Aggregat abgeleitet wird – beispielsweise als Prozentsatz des Gesamtwerts, als laufende Summe, als Differenz zu einem ausgewählten Basiselement oder als Rang –, sodass Sie Vergleichsanalysen ohne Hilfsformeln oder berechnete Spalten durchführen können.
Typische Anwendungen umfassen die Analyse der Anteile am Gesamtwert, einschließlich der Prozentsätze einer Zeile, einer Spalte oder des Gesamtwerts; kumulatives Reporting mithilfe einer laufenden Summe in einem Periodenfeld; die Varianzanalyse gegen ein Vergleichselement anhand einer Differenz zu oder prozentualen Differenz zu einem Basiselement; sowie die Rangfolge der Werte vom kleinsten zum größten oder vom größten zum kleinsten.
In Aspose.Cells for C++ wählt die Aufzählung `PivotShowValuesAsType` die sekundäre Berechnung aus. Der Getter `PivotField.GetShowValuesSetting()` gibt ein `PivotShowValuesSetting`-Objekt zurück, dessen Methoden `SetShowValuesAs`, `SetBaseFieldIndex` und `SetBaseItemIndex` das Verhalten konfigurieren. Die zusätzliche Methode `PivotField.ShowValuesAs(...)` wendet dieselben Einstellungen in einem einzigen Aufruf an. Wenden Sie diese Einstellungen auf ein Daten- oder Wertfeld an, das über `PivotTable.GetDataFields()` abgerufen wurde.

## **Mitglieder der Aufzählung `PivotShowValuesAsType`**
Das Datenfeld behält seine Aggregatfunktion, etwa `Sum` oder `Count`, während „Werte anzeigen als“ nur die Anzeige des aggregierten Werts verändert.
Zusätzlich zum direkten Schreiben der `PivotShowValuesSetting`-Werte (siehe letzter Abschnitt) bietet eine Methode mit einem einzigen Aufruf dieselbe Konfiguration an. Sie ist in zwei Varianten verfügbar: Eine adressiert Basisfeld und Basiselement über den Index, die andere über den Namen:

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| Parameter | Bedeutung | Erforderlich, wenn |
| --- | --- | --- |
| `showValuesAsType` | Die anzuwendende sekundäre Berechnung vom Typ `PivotShowValuesAsType`. | Immer. |
| `baseField` | Nullbasierter Index des Basisfelds in den Basisfeldern der PivotTable (beispielsweise der Index des Zeilenfelds, zu dem das Basiselement gehört) oder – in der Namensvariante – der Name des Basisfelds. | Bei den acht auf das Basisfeld bezogenen Formaten unten (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); für alle anderen Formate ist `0` (oder in der Namensvariante eine leere `U16String`) zu übergeben. |
| `baseItem` | Nullbasierter Index des Basiselements mit zwei Sentinel-Werten: -1 wählt das vorhergehende Element und -2 das nachfolgende Element aus (die C++-API definiert keine benannten Konstanten für diese Sentinel-Werte – übergeben Sie die Literalwerte). Die Namensvariante verwendet stattdessen die Beschriftung des Basiselements und für Formate, die kein Basiselement benötigen, eine leere `U16String`. | Nur die drei Formate mit Basiselement (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) berücksichtigen das Basiselement; die fünf feldbezogenen Formate (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn` sowie beide Rangformate) ignorieren es – übergeben Sie `0` oder eine leere `U16String`. |

| Berechnungstyp | Verhalten | Basiselementparameter |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt die Differenz zwischen dem Wert und dem Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung bzw. der Sentinel-Wert für das vorherige/nächste Element) |
| `PercentageOf` | Zeigt den Wert als Prozentsatz des Werts eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung bzw. der Sentinel-Wert für das vorherige/nächste Element) |
| `PercentageDifferenceFrom` | Zeigt die prozentuale Differenz zwischen dem Wert und dem Wert eines Basiselements in einem Basisfeld an. | `baseField` + `baseItem` (ein Index oder eine Beschriftung bzw. der Sentinel-Wert für das vorherige/nächste Element) |
| `RunningTotalIn` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Elemente eines Basisfelds an. | `baseField` (das Feld, dessen Elementreihenfolge die laufende Summe bestimmt) |
| `PercentageOfRow` | Zeigt den Wert als Prozentsatz des Zeilengesamtwerts an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozentsatz des Spaltengesamtwerts an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozentsatz des Gesamtwerts an. | — |
| `Index` | Zeigt den Wert mithilfe der Excel-Indexformel ((Wert * Gesamtwert) / (Zeilengesamtwert * Spaltengesamtwert)) an. | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozentsatz des Gesamtwerts der übergeordneten Zeile (für verschachtelte Zeilenfelder) an. | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozentsatz des Gesamtwerts der übergeordneten Spalte (für verschachtelte Spaltenfelder) an. | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozentsatz des übergeordneten Gesamtwerts an. | `baseField` (das übergeordnete Feld, dessen Gesamtwert als Referenz dient) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Ordnet den Wert vom kleinsten (1) bis zum größten ein. | `baseField` (das Feld, dessen Elemente den Umfang der Rangfolge bestimmen) |
| `RankLargestToSmallest` | Ordnet den Wert vom größten (1) bis zum kleinsten ein. | `baseField` (das Feld, dessen Elemente den Umfang der Rangfolge bestimmen) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` legt die Werte `ShowValuesAs`, `BaseFieldIndex` und `BaseItemIndex` im `PivotShowValuesSetting`-Objekt fest. Die Methode und das Einstellungsobjekt bieten zwei Möglichkeiten, denselben Zustand zu konfigurieren, und entsprechen den Feldern zur Auswahl von Basisfeld und Basiselement im Dialog „Werte anzeigen als“ von Excel.
{{% /alert %}}

## **Werte als Prozentsatz des Gesamtwerts anzeigen**
Rufen Sie die Methode `PivotField.ShowValuesAs` mit `PivotShowValuesAsType::PercentageOfTotal` auf, um jede Datenfeldzelle, einschließlich der Gesamtwertzelle, als ihren Anteil am Gesamtwert anzuzeigen. Die angezeigten Zahlen werden daher als Anteile an der gesamten Ergebnismenge dargestellt. Dieses Format bezieht jeden Wert ausschließlich auf den Gesamtwert und benötigt daher weder ein Basisfeld noch ein Basiselement – die abschließenden Argumente (`0`, `0`) sind Platzhalter, die dieses Format ignoriert, wie in der Parametertabelle oben erläutert.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **PivotField.ShowValuesSetting abrufen und konfigurieren**
Lesen Sie die aktuelle Konfiguration über `PivotField.GetShowValuesSetting()`: Der Getter gibt das `PivotShowValuesSetting`-Objekt des Felds zurück, dessen Getter-Methoden die aktive Berechnung für „Werte anzeigen als“ beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.ShowValuesAs` auf – sie schreibt alle Einstellungen in einem einzigen Aufruf, sodass Sie die Werte nie einzeln festlegen müssen.
Das `PivotShowValuesSetting`-Objekt enthält den Zustand, der durch `ShowValuesAs` festgelegt wird:
- `GetShowValuesAs()` / `SetShowValuesAs()` wählen die sekundäre Berechnung vom Typ `PivotShowValuesAsType` aus.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` geben den nullbasierten Index des Basisfelds innerhalb der Felder der PivotTable an bzw. legen ihn fest. Er wird von den auf das Basisfeld bezogenen Formaten verwendet.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` geben das Basiselement an bzw. legen es fest: einen nullbasierten Index eines bestimmten Elements der PivotTable oder einen der beiden Sentinel-Werte – -1 für das vorhergehende Element, -2 für das nachfolgende Element (die C++-API definiert keine benannten Konstanten für diese Sentinel-Werte). Er wird von den Formaten mit Basiselement verwendet.
- `GetBaseFieldName()` und `GetBaseItemCaption()` sind schreibgeschützte Getter, die den aufgelösten Namen des Basisfelds und die Beschriftung des Basiselements wiedergeben; nach Auswahl des Sentinel-Werts für das vorherige Element gibt `GetBaseItemCaption()` beispielsweise `(previous)` zurück.
Rufen Sie nach `ShowValuesAs` erneut `PivotTable.CalculateData()` auf, damit der Inhalt der PivotTable mit der aktualisierten Konfiguration neu berechnet und neu gerendert wird.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Verwandte Artikel**
- [Wertfelder in PivotTable verwalten](/cells/de/cpp/manage-value-fields/)
- [PivotTable aktualisieren](/cells/de/cpp/refresh-pivot-table/)
- [Formatierung auf PivotTable anwenden](/cells/de/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}