---
title: Werte anzeigen als in Pivot-Tabelle in Aspose.Cells für C++
linktitle: Werte anzeigen als in Pivot-Tabelle
description: Pivot-Tabellendatenfeldwerte als Prozentsatz des Gesamtergebnisses, als Unterschied zu einem Basis‑Element, als laufende Summe, als Rangliste und mehr mit Aspose.Cells für C++ anzeigen.
keywords: Aspose.Cells, C++, Pivot-Tabelle, Werte anzeigen als, Datenanzeigeformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /de/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Eine Pivot‑Tabelle fasst normalerweise jedes Datenfeld mit einer Aggregatfunktion wie `Sum` oder `Count` zusammen. Die **Show Values As**‑Funktion von Excel ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus diesem Aggregat abgeleitet wird – zum Beispiel ein Prozentsatz der Gesamtsumme, eine laufende Summe, eine Differenz zu einem ausgewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen durchführen können, ohne Hilfsformeln oder berechnete Spalten zu verwenden.  
Typische Anwendungsfälle umfassen die Analyse des Anteils am Gesamtwert, einschließlich Prozentsätzen einer Zeile, Spalte oder der Gesamtsumme; kumulatives Reporting mittels einer laufenden Summe in einem Periodenfeld; Varianzanalyse gegenüber einem Benchmark‑Element unter Verwendung von Differenz zu oder prozentualer Differenz zu einem Basiselement; sowie das Rangieren von Werten vom Kleinsten zum Größten oder vom Größten zum Kleinsten.  
In Aspose.Cells für C++ wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Der Accessor `PivotField.GetShowValuesSetting()` gibt ein `PivotShowValuesSetting`‑Objekt zurück, dessen Methoden `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` und `SetBaseItemIndex` das Verhalten konfigurieren; die Komfortmethode `PivotField.ShowValuesAs(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Wertefeld an, das über `PivotTable.GetDataFields()` erhalten wird.

## **PivotFieldDataDisplayFormat Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregatfunktion, wie Sum oder Count, bei, während Show Values As nur die Anzeige des aggregierten Werts transformiert.  
Neben dem direkten Schreiben der `PivotShowValuesSetting`‑Werte (siehe den letzten Abschnitt) wendet eine Komfortmethode mit einem Aufruf dieselbe Konfiguration an:

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| Parameter | Bedeutung | Wenn erforderlich |
| --- | --- | --- |
| `displayFormat` | Die anzuwendende sekundäre Berechnung `PivotFieldDataDisplayFormat`. | Immer. |
| `baseField` | Nullbasierter Index des Basisfeldes unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfelds, zu dem das Basiselement gehört). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); von allen anderen Formaten wird es ignoriert. |
| `baseItemPositionType` | Wie das Basiselement relativ zum aktuellen Element ausgewählt wird: `PivotItemPositionType::Previous`, `::Next` oder `::Custom`. | Nur für die drei Basis-Element-Formate (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); von allen anderen Formaten wird es ignoriert. |
| `baseItem` | Nullbasierter Index des Basiselements. | Nur wenn `baseItemPositionType` `Custom` ist (der Index wählt das genaue Basiselement); für `Previous`/`Next` und alle Nicht‑Basis‑Formate ignoriert — übergeben Sie `0`. |

| Berechnungstyp | Verhalten | Parameter des Basiselements |
| --- | --- | --- |
| `Normal` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DifferenceFrom` | Zeigt den Wert als Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur mit `Custom`) |
| `PercentageOf` | Zeigt den Wert als Prozentsatz des Wertes eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur mit `Custom`) |
| `PercentageDifferenceFrom` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basiselements in einem Basisfeld an. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` nur mit `Custom`) |
| `RunningTotalIn` | Zeigt den Wert als laufende Summe für aufeinander folgende Elemente eines Basisfeldes an. | `baseField` (das Feld, dessen Elementreihenfolge die Akkumulation steuert) |
| `PercentageOfRow` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PercentageOfColumn` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PercentageOfTotal` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `Index` | Zeigt den Wert mit der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PercentageOfParentRowTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme an (für verschachtelte Zeilenfelder). | — |
| `PercentageOfParentColumnTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme an (für verschachtelte Spaltenfelder). | — |
| `PercentageOfParentTotal` | Zeigt den Wert als Prozentsatz der übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Referenzfeld) |
| `PercentageOfRunningTotalIn` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basisfeld an. | `baseField` (das Akkumulationsfeld) |
| `RankSmallestToLargest` | Rangiert den Wert vom Kleinsten (1) zum Größten. | — |
| `RankLargestToSmallest` | Rangiert den Wert vom Größten (1) zum Kleinsten. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` schreibt die `PivotShowValuesSetting`‑Werte (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — die Methode und das Einstellungsobjekt sind zwei Wege, denselben Zustand zu konfigurieren, analog zu den Basisfeld‑ und Basiselement‑Auswahloptionen im Show Values As‑Dialog von Excel.
{{% /alert %}}

## **Werte als Prozentsatz des Gesamttotals anzeigen**
Rufen Sie die Methode `PivotField.ShowValuesAs` mit `PivotFieldDataDisplayFormat::PercentageOfTotal` auf, um jede Datenfeldzelle, einschließlich der Gesamtsumme, in ihren Anteil an der Gesamtsumme umzuwandeln. Die angezeigten Zahlen stellen daher Anteile des vollständigen Ergebnissets dar. Dieses Format misst jeden Wert nur gegenüber der Gesamtsumme, sodass kein Basisfeld oder Basiselement erforderlich ist – die nachfolgenden Argumente (`0`, `PivotItemPositionType::Previous`, `0`) sind Platzhalter, die das Format ignoriert, wie die obige Parametertabelle zeigt.

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
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **PivotField.ShowValuesSetting abrufen und konfigurieren**
Lesen Sie die aktuelle Konfiguration über `PivotField.GetShowValuesSetting()`: Der Accessor gibt das `PivotShowValuesSetting`‑Objekt des Feldes zurück, dessen vier Getter‑Methoden die aktive Show‑Values‑As‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.ShowValuesAs` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie die Werte nicht einzeln zuweisen müssen.  
Das `PivotShowValuesSetting`‑Objekt stellt die vier Werte bereit, die `ShowValuesAs` schreibt:
- `GetCalculationType()` / `SetCalculationType()` wählen die sekundäre Berechnung `PivotFieldDataDisplayFormat` aus.  
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` geben den nullbasierten Index des Basisfeldes innerhalb der Pivot‑Felder an. Er wird von den basisbezogenen Formaten verwendet.  
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` bestimmen, wie das Basiselement relativ zum aktuellen Element positioniert wird, und akzeptieren `PivotItemPositionType::Next`, `PivotItemPositionType::Previous` oder `PivotItemPositionType::Custom`.  
- `GetBaseItemIndex()` / `SetBaseItemIndex()` geben den nullbasierten Index des Basiselements an und werden verwendet, wenn der Positionstyp `Custom` ist.  
Rufen Sie nach dem Aufruf von `ShowValuesAs` erneut `PivotTable.CalculateData()` auf, damit der Pivot‑Körper mit der aktualisierten Konfiguration neu berechnet und neu gerendert wird.

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
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Verwandte Artikel**
- [Verwalten von Wertefeldern in Pivot‑Tabelle](/cells/de/cpp/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/cpp/refresh-pivot-table/)
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}