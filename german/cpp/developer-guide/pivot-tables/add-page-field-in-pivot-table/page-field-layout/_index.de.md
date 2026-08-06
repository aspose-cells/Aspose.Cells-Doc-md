---
title: Seitenfeldlayout in Pivot-Tabelle ändern
linktitle: Seitenfeldlayout in Pivot-Tabelle ändern
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ das Layout des Seitenfeldbereichs in einer Pivot-Tabelle steuern, einschließlich der Anzeigereihenfolge, der Umbruchanzahl und der Feldreihenfolge der Seitenfelder am oberen Rand der Pivot-Tabelle.
keywords: Aspose.Cells, C++ Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Seitenfeld, Seitenfeldreihenfolge, Seitenfeldumbruchanzahl, Seitenfeld verschieben
type: docs
weight: 191
url: /de/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Dieser Artikel ist eine Fortsetzung des Themas **Seitenfeld in Pivot-Tabelle hinzufügen**. Er zeigt, wie Sie das Layout des Seitenfeldbereichs — den Streifen mit Filtersteuerelementen am oberen Rand einer Pivot-Tabelle — steuern, einschließlich Anzeigereihenfolge, Umbruchanzahl und Neuanordnung der Felder.
{{% /alert %}}
## **Einführung**
Eine Pivot-Tabelle in Microsoft Excel verfügt über einen dedizierten **Seitenfeldbereich**, der oberhalb des Zeilen-/Spalten-/Datenkörpers der Tabelle liegt. Dieser Bereich wird als Streifen mit Dropdown-Filtersteuerelementen gerendert (eines pro Seitenfeld) und ist das, was Endbenutzer anklicken, um die Pivot-Tabelle nach Kriterien wie Jahr oder Region zu filtern. Aspose.Cells for C++ modelliert diesen Bereich über die Sammlung `PivotTable.PageFields` und stellt drei Eigenschaften bereit, die steuern, wie der Streifen visuell angeordnet wird:
- `PivotTable.PageFieldOrder` (ein Wert vom Typ `Aspose.Cells.PrintOrderType`) legt fest, ob zusätzliche Seitenfelder *neben* den vorhandenen oder *unterhalb* dieser platziert werden.
- `PivotTable.PageFieldWrapCount` legt fest, wie viele Seitenfelder pro Zeile oder Spalte platziert werden, bevor ein Umbruch erfolgt.
- `PivotTable.PageFields.Move(currIndex, destIndex)` ordnet die Seitenfelder neu an, ohne den Reihenfolgemodus zu ändern.
Dieser Artikel führt durch drei Codebeispiele, die jede dieser Operationen an einem gemeinsamen Datensatz demonstrieren, sodass Sie die resultierenden Layouts nebeneinander vergleichen können.
## **Quelldaten**
Alle drei folgenden Beispiele laden diese acht Zeilen Verkaufsdaten in ein Arbeitsblatt namens `PivotData`. Die Daten enthalten zwei Seitenfeldkandidaten (`Year`, `Region`), einen Zeilenfeldkandidaten (`Fruit`) und eine Kennzahl (`Amount`), wodurch der Seitenfeldstreifen sinnvoll untersucht werden kann.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alle acht Zeilen werden in jedem Codebeispiel in identischer Reihenfolge befüllt, sodass sich die Quelldaten zwischen den Szenarien nie unterscheiden — nur die Layout-Eigenschaften der Seitenfelder tun dies.
## **Beispiel 1: Über dann abwärts**
Im ersten Szenario konfigurieren wir die beiden Seitenfelder (`Year`, `Region`) so, dass sie **nebeneinander in einer einzelnen Zeile** am oberen Rand der Pivot-Tabelle erscheinen. Wir weisen `Fruit` der Zeilenachse zu, platzieren `Year` zuerst und `Region` an zweiter Stelle auf der Seitenachse (die Reihenfolge der `AddFieldToArea`-Aufrufe bestimmt den Startindex), fügen `Amount` (Summe) als Datenfeld hinzu und setzen dann `PageFieldOrder` auf `PrintOrderType.OverThenDown` mit `PageFieldWrapCount = 2`. Mit `OverThenDown` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder horizontal nebeneinander in einer einzelnen Zeile am oberen Rand der Pivot-Tabelle angeordnet, sodass der Streifen eine Zeile mit der Breite zwei einnimmt.
```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // Kopfzeilen (Zeile 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // Zeile 1: Apfel, 2022, Nord, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // Zeile 2: Apfel, 2023, Nord, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // Zeile 3: Banane, 2022, Süd, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // Zeile 4: Banane, 2023, Süd, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // Zeile 5: Kirsche, 2022, Ost, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // Zeile 6: Kirsche, 2023, Ost, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // Zeile 7: Traube, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // Zeile 8: Traube, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // PivotTableReport-Blatt hinzufügen
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // Pivot-Tabelle erstellen, die aus PivotData!A1:D9 stammt und auf A1 in PivotTableReport platziert wird
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Felder hinzufügen
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Frucht
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Jahr
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Region
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Betrag
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // Layout des Seitenfeldbereichs konfigurieren: Seitenfelder zuerst horizontal anordnen, nach jeweils 2 umbrechen
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // Aktualisieren und berechnen
    pivotTable.CalculateData();

    // Speichern
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Beispiel 2: Abwärts dann über**
In diesem Beispiel platzieren wir `Fruit` auf der Zeilenachse, `Year` und `Region` auf der Seitenachse (mit `Year` zuerst) und `Amount` (Summe) als Datenfeld — genau wie in Beispiel 1. Anschließend setzen wir `PageFieldOrder` auf `PrintOrderType.DownThenOver` und `PageFieldWrapCount` auf `2`. Mit `DownThenOver` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder vertikal gestapelt — `Year` oben, `Region` direkt darunter — und bilden eine einzelne Spalte am oberen Rand der Pivot-Tabelle. Der Streifen nimmt daher zwei Zeilen mit der Breite eins ein, im Gegensatz zu Beispiel 1.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Beispiel 3: Ein Seitenfeld verschieben**
Im dritten Szenario behalten wir diesen Datensatz und diese Feldzuordnung bei, legen ein neutrales Layout fest (`OverThenDown` mit Umbruchanzahl `2`) und demonstrieren dann die Operation `PageFields.Move`. Der Aufruf `Move(0, 1)` verschiebt das Seitenfeld an Index 0 (`Year`) an Position 1, und das Seitenfeld, das sich an Position 1 befand (`Region`), rückt auf Position 0. Nach diesem Aufruf ist `Region` das erste Seitenfeld und `Year` das zweite. Umbruch und Reihenfolgemodus bleiben unverändert, sodass der Streifen weiterhin horizontal nebeneinander gerendert wird — nur die Reihenfolge der beiden Dropdowns wurde vertauscht.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Verwandte Artikel**
- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/cpp/add-page-field-in-pivot-table/) — die übergeordnete Seite, die einführt, wie Seitenfelder zu einer Pivot-Tabelle hinzugefügt werden.
- [Zeilen- und Spaltenfelder in Pivot-Tabelle](/cells/de/cpp/row-and-column-fields/) — behandelt die Zuweisung von Feldern zu den Zeilen- und Spaltenachsen und ergänzt die hier gezeigte Arbeit an der Seitenachse.
- [Wertfelder in Pivot-Tabelle verwalten](/cells/de/cpp/manage-value-fields/) — beschreibt, wie der Daten- (Wert-) Bereich konfiguriert wird, einschließlich der in diesem Artikel verwendeten `Sum`-Aggregation.
- [Pivot-Tabelle aktualisieren](/cells/de/cpp/refresh-pivot-table/) — erläutert `RefreshData` und `CalculateData`, die nach der Neuanordnung der Seitenfelder erforderlich sind.
- [Stil auf Pivot-Tabelle anwenden](/cells/de/cpp/apply-style-to-pivot-table/) — zeigt, wie die gerenderte Pivot-Tabelle formatiert wird, nachdem der Seitenfeldstreifen angeordnet wurde.
{{< app/cells/assistant language="" >}}