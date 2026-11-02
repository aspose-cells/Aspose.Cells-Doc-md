---
title: Top 10 in PivotTable anzeigen oder filtern
linktitle: Top 10 in PivotTable anzeigen oder filtern
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ nur die höchst- oder niedrigstplatzierten Elemente eines PivotTable-Felds anzeigen. Dieser Artikel behandelt die Methode Top10AutoShow aus Excel 97-2003, das Lesen der Optionen mit GetTop10AutoShowSettings und den Top-10-Filter aus Excel 2007-365 mithilfe von FilterTop10.
keywords: Aspose.Cells, C++, PivotTable, Top 10, AutoShow, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /de/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die jedes Element eines Zeilenfelds auflistet, kann schwer zu lesen sein, wenn das Feld Dutzende Elemente enthält. Ein Top-10-Bericht behält nur die höchst- oder niedrigstplatzierten Elemente bei und erfüllt damit genau die Anforderungen von Ranking-Berichten – etwa „die fünf umsatzstärksten Produkte“ oder „die drei Regionen mit dem niedrigsten Verkaufsvolumen“. Aspose.Cells unterstützt zwei Mechanismen, die den beiden Generationen von Microsoft Excel entsprechen.
- **AutoShow für Excel 97-2003** – die Methode `PivotField.Top10AutoShow()`. Dabei handelt es sich um die klassische Einstellung „Obere/untere N Elemente anzeigen“, die direkt im PivotTable-Feld gespeichert wird. Sie funktioniert in allen Excel-Versionen, ob alt oder neu, da sie Bestandteil des ursprünglichen PivotTable-Formats ist.
- **Top-10-Filter für Excel 2007-365** – die Methode `PivotField.FilterTop10()`. Dabei handelt es sich um den modernen Top-10-Wertfilter im Feldmenü unter „Wertfilter“. Er wird als `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und bietet eine auf Elementanzahl oder Prozentsatz basierende Rangfolge.

## **Top 10 in Excel 97-2003 anzeigen (Top10AutoShow)**
Das klassische AutoShow wird mit einem einzigen Aufruf von `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)` konfiguriert:
- `isAutoShow` – aktiviert oder deaktiviert die AutoShow-Einstellung für das Feld.
- `isTop` – `true` behält die höchstplatzierten Elemente bei, `false` behält die niedrigstplatzierten Elemente bei.
- `count` – gibt an, wie viele Elemente beibehalten werden, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `rankBy` – der nullbasierte Index des **Datenfelds**, dessen Werte die Rangfolge der Elemente bestimmen. Übergeben Sie -1, um die Elemente nach den Werten des Felds selbst zu ordnen.
Die Rangfolge kann durch ein Wertfeld oder durch das Feld selbst bestimmt werden. Im Folgenden werden zwei naheliegende Varianten gezeigt.

### **Nach einem Wertfeld ordnen**
Ordnen Sie die Elemente des Zeilenfelds anhand eines gewöhnlichen Wertfelds wie „Summe von Sales“ an. Im folgenden Beispiel wird eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) erstellt und anschließend werden die beiden Sportarten mit dem höchsten Verkaufsvolumen angezeigt. `rankBy` ist 0, weil „Summe von Sales“ dem Datenfeld mit Index 0 entspricht.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Die 2 wichtigsten Elemente anzeigen, sortiert nach "Summe von Sales" (Index des Datenfelds 0)
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Nach dem Feld selbst ordnen**
Ein Feld kann alternativ nach seinen eigenen Werten geordnet werden – übergeben Sie -1 als `rankBy`. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich liegen. Im folgenden Beispiel werden die drei untersten Sportarten in der Rangfolge nach dem Feld selbst angezeigt. Wenn diese Einstellung gespeichert wird, wird das Attribut `rankBy` aus dem XML der PivotTable weggelassen, da -1 der Standardwert des Formats ist. `GetTop10AutoShowSettings().GetRankBy()` gibt -1 zurück.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Die unteren 3 Elemente anzeigen, die nach dem Feld selbst ranken (rankBy = -1)
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Aktuelle Optionen lesen (GetTop10AutoShowSettings)**
Die Methode `PivotField.GetTop10AutoShowSettings()` gibt ein `PivotFieldTop10AutoShowSettings`-Objekt zurück, über das die aktuell im Feld gespeicherten AutoShow-Optionen verfügbar sind. Verwenden Sie es, um zu prüfen, wie eine vorhandene Arbeitsmappe beziehungsweise eine gerade konfigurierte PivotTable ihre Elemente darstellen wird – auch wenn die Arbeitsmappe aus einer Datei geladen wurde.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Die vier Mitglieder entsprechen den klassischen AutoShow-Attributen, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Die zurückgelesenen Werte entsprechen daher den Werten, die von jeder Excel-Version berücksichtigt werden.

## **Hinweis**

{{% alert color="primary" %}}
- Die direkten `PivotField`-Eigenschaften `IsAutoShow`, `IsAscendShow`, `GetAutoShowCount` und `GetAutoShowField` sind veraltet. Verwenden Sie stattdessen das `PivotFieldTop10AutoShowSettings`-Objekt: `IsAutoShow` wird durch `GetTop10AutoShowSettings().IsAutoShow()` ersetzt, `IsAscendShow` durch `GetTop10AutoShowSettings().IsTop()`, `GetAutoShowCount` durch `GetTop10AutoShowSettings().GetAutoShowCount()` und `GetAutoShowField` durch `GetTop10AutoShowSettings().GetRankBy()`. Die Methode `Top10AutoShow()` selbst ist der unterstützte Weg, um die Einstellungen zu ändern.
- `Top10AutoShow` funktioniert mit Zeilen- und Spaltenfeldern. Ein Feld, das ausschließlich im Seiten- beziehungsweise Filterbereich liegt, kann auf diese Weise nicht rangiert werden, da seine Elemente nicht im PivotTable-Bereich angeordnet sind.
{{% /alert %}}

## **Excel 2007-365: Top-10-Filter (FilterTop10)**
Moderne Excel-Versionen stellen Top 10 als Wertfilter im Feldmenü („Wertfilter“, „Top 10“) bereit. Aspose.Cells bildet dies mit der Methode `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)` ab, wobei die Methode den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` – der nullbasierte Index des Datenfelds, dessen aggregierte Werte die Rangfolge der Elemente bestimmen.
- `type` – legt fest, was `itemCount` bedeutet. `PivotFilterType::Count` behält eine feste Anzahl von Elementen bei (Option „Elemente“ des Dialogfelds). `PivotFilterType::Percent` behält einen Prozentsatz der Elemente bei, sodass `itemCount` selbst der Prozentsatz ist – 30 behält die obersten 30 Prozent. `PivotFilterType::Sum` bewertet die Elemente anhand der kumulierten Werteabdeckung.
- `isTop` – `true` für die obersten, `false` für die untersten Elemente.
- `itemCount` – der Wert N in der Formulierung „Top N“; die Einheit hängt von `type` ab.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Top-10-Filter — die beiden obersten Elemente nach „Summe von Sales“ beibehalten (Datenfeldindex 0)
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // Für einen prozentualen Filter stattdessen die obersten 30 Prozent der Elemente beibehalten:
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` und `FilterTop10` sind zwei getrennte Funktionen. AutoShow schreibt den klassischen Attributsatz (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) in das PivotTable-Feld und wird von allen Excel-Versionen seit Excel 97 berücksichtigt. `FilterTop10` schreibt einen modernen `PivotFilter`-Eintrag, für den Excel 2007 oder höher erforderlich ist. Wird eine Arbeitsmappe in einer älteren Excel-Version geöffnet, fällt eine PivotTable, die den modernen Filter verwendet, auf die Anzeige aller Elemente zurück. Für Dokumente, die mit älteren Tools verarbeitet werden müssen, ist `Top10AutoShow` vorzuziehen; für moderne Arbeitsmappen ist `FilterTop10` vorzuziehen, da es sich mit den übrigen Wertfiltern kombinieren lässt.
{{% /alert %}}

## **Verwandte Artikel**
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/cpp/filter-by-label-or-value-of-pivot-table/)
- [Zeilen- und Spaltenfelder zur PivotTable hinzufügen](/cells/de/cpp/pivot-table-add-row-and-column-fields/)
- [PivotTable-Felder in der PivotTable gruppieren](/cells/de/cpp/group-pivot-fields-in-the-pivot-table/)
- [PivotTable aktualisieren](/cells/de/cpp/refresh-pivot-table/)
- [Seitenfeld zur PivotTable hinzufügen](/cells/de/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}