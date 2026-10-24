---
title: Pivot-Tabellen und Pivot-Caches in Aspose.Cells for C++ aktualisieren
linktitle: Pivot-Tabellen und Pivot-Caches
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for C++ mit der Pivot-Refresh-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, C++, Pivot-Tabelle, Aktualisieren, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet eine mehrschichtige Aktualisierungs-API, mit der Sie Pivot-Daten in vier verschiedenen Geltungsbereichen neu laden können — von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Ab **Aspose.Cells for C++ v26.7** ist die Legacy-Methode `PivotTable.RefreshData()` als veraltet markiert und sollte durch die effizienteren cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}

## Introduction
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine mehrschichtige Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Diese Kette zu verstehen, ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierschichtige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte gespeichert sind.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Zellen** — die `Cells` des Arbeitsblatts, in die die `PivotTable` ihre berechneten Werte und Stile rendert.

{{% alert color="primary" %}}
`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.Refresh()` nur die Quellentypen **`Sheet`** und **`Consolidation`** — also Daten, die in Arbeitsblattbereichen liegen. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotTable.CalculateData()`** — berechnet die Anzeige einer `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Round-Trip zurück zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblattzellen als Quelldaten, sodass der Quellentyp `Sheet` ist und die Aktualisierungsvorgänge wie beschrieben funktionieren.
{{% /alert %}}

## Quick Start
Wenn Sie nur den kürzestmöglichen Code benötigen, der jede Pivot-Tabelle in der Arbeitsmappe aktualisiert, reicht ein einziger Aufruf:

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Alles andere in diesem Artikel erklärt, wann Sie stattdessen eine spezifischere API wählen sollten.

## Required Include Directives
Alle C++-Beispiele in diesem Artikel beginnen mit den folgenden Header-Includes und Namespace-Direktiven, da die Pivot-Typen im Namespace `Aspose::Cells::Pivot` liegen:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Refresh All Pivot Tables in the Workbook
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.RefreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe — aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, dokumentweite Aktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Jahr/Betrag-Quellbereich, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `RefreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);
    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);
    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);
    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);
    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);
    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);
    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);
    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);
    pivotTable.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh All Pivot Tables on a Single Worksheet
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden — beispielsweise, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht relevant sind und nicht berührt werden sollten. Für diesen Fall bietet Aspose.Cells `Worksheet.RefreshPivotTables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);
    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);
    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);
    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);
    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);
    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);
    worksheet.RefreshPivotTables();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh a Single Pivot Table
Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder nur die Ansichts-/Layout-Einstellungen der Pivot-Tabelle selbst.

### Source Data Changed — Use `PivotCache.Refresh()`
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.GetPivotCache().Refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.

### Only View/Layout Changed — Use `CalculateData()`
Wenn sich die Quelldaten *nicht* geändert haben, aber nur die Ansichts- oder Layout-Einstellungen der Pivot-Tabelle geändert wurden (z. B. ein Feld in einen anderen Bereich verschoben oder eine Einstellung zum Aktualisieren beim Öffnen umgeschaltet wurde), ist kein Round-Trip zurück zur Datenquelle erforderlich. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.CalculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine nicht quellbezogene Eigenschaft der Pivot-Tabelle und ruft dann `CalculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Write Fruit / Year / Amount header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);
    // Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Assign fields: Fruit to Row, Year to Column, Amount to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modify a view/layout property — this is a presentation-only change,
    // so it does NOT require re-reading the source data through PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() re-renders THIS pivot table's display (data + style) from the
    // data already held in the PivotCache. Because the source data did not change,
    // no round-trip to the source is performed — only the cached values are recalculated
    // into worksheet cells.
    pivotTable.CalculateData();
    // Save the workbook to disk
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsamen Cache basieren. Um sie aufzulisten — beispielsweise vor der Durchführung einer Batch-Aktualisierung oder um die Auswirkungen des gemeinsamen Caches zu diagnostizieren — verwenden Sie `PivotCache.GetPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Vor Aspose.Cells for C++ v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.RefreshData()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der `RefreshData()`-Ansatz pro Tabelle in realen Arbeitsmappen problematisch ist:
- Er ruft die Daten bei jedem Aufruf *erneut* aus der Quelle ab, selbst wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersetzungen sind:
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzelnen Cache gemeinsam nutzen.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");
    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);
    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");
    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);
    pivotTable2.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Which Refresh API Should I Use?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und zeigt, wann welche zu wählen ist.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.RefreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.RefreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.GetPivotCache().Refresh()` | Aktualisiert ALLE Pivot-Tabellen in diesem gemeinsamen Cache. |
| Nur Ansichts-/Layout-Einstellungen geändert | `pivotTable.CalculateData()` | Überspringt unnötigen Quell-Round-Trip. |
| Alle Pivot-Tabellen in einem gemeinsamen Cache auflisten | `pivotCache.GetPivotTables()` | Zur Auflistung vor Massenaktualisierungen verwenden. |
In der Praxis sind die cache-basierten APIs dem veralteten `RefreshData()` pro Tabelle vorzuziehen. Sie kennen gemeinsame Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderung erfüllt.

## Common Pitfalls
- **Vergessen, vor dem Speichern zu aktualisieren.** Eine Pivot-Tabelle schreibt ihre gerenderten Werte nur dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wird. Wenn Sie Quellzellen ändern, rufen Sie `PivotCache.Refresh()` (oder `Workbook.RefreshAll()`) vor `Workbook.Save()` auf, da die gespeicherte Datei sonst weiterhin die alten aggregierten Werte enthält.
- **Aufruf der veralteten `RefreshData()` pro Tabelle.** In v26.7 ist `PivotTable.RefreshData()` als veraltet markiert und ruft die Quelle bei jedem Aufruf erneut ab. Bei mehreren Pivot-Tabellen, die einen Cache gemeinsam nutzen, bedeutet dies N redundante Quellabrufe. Ersetzen Sie dies durch einen einzelnen `PivotCache.Refresh()`-Aufruf, gefolgt von `CalculateData()` pro Tabelle.
- **Aktualisieren, wenn nur das Layout geändert wurde.** Wenn Sie nur die Ansicht einer Pivot-Tabelle (Spaltenreihenfolge, `ConsolidationFunction` usw.) geändert haben, ohne die Quelldaten zu berühren, ist `PivotCache.Refresh()` unnötig und langsam. Rufen Sie `pivotTable.CalculateData()` auf, um aus dem vorhandenen Cache neu zu rendern.
- **Externe Quelle wird von `PivotCache.Refresh()` nicht unterstützt.** Wenn die Quelle der Pivot-Tabelle aus einer externen Verbindung (Datenbank, OLAP-Cube usw.) stammt, kann `PivotCache.Refresh()` sie in v26.7 nicht aktualisieren — es unterstützt derzeit nur die Quellentypen `Sheet` und `Consolidation`. Für externe Quellen öffnen Sie die Arbeitsmappe erneut oder erstellen Sie den Cache aus der Quelle neu.

{{< app/cells/assistant language="cpp" >}}