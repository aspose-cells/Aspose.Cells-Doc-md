---
title: Teil einer Pivot-Tabelle formatieren
linktitle: Teil einer Pivot-Tabelle formatieren
description: Formatieren Sie einen Teil einer Pivot-Tabelle in Aspose.Cells for C++ durch Anwenden von Stilen auf semantische PivotArea‑Regionen oder CellArea‑Rechtecke über PivotTable.Format, wobei Formate in PivotTable.GetPivotFormats gespeichert und beim Aktualisieren der PivotTable erhalten bleiben.
keywords: Aspose.Cells, PivotTable, Format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /de/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
`PivotTable.FormatAll` wendet einen einzigen Stil auf die gesamte PivotTable an und wird auf der übergeordneten Seite behandelt. Es unterscheidet nicht zwischen Beschriftungen, Werten, Summen oder bestimmten Bereichen des Berichts.
In der Praxis muss in der Regel nur ein Teil einer PivotTable hervorgehoben werden. Häufige Ziele sind die Beschriftungen, die zu einem Zeilenfeld gehören, die Wertzellen, die von einem Feld erzeugt werden, die Gesamtsummen‑Zeile oder ein beliebiges Rechteck, beispielsweise die ersten beiden Elementzeilen.
Das direkte Anwenden eines Stils auf die Arbeitsblattzellen einer PivotTable ist nicht gleichwertig. Excel speichert die Formatierung von PivotTable als semantische `PivotArea`‑Regionen und nicht als gewöhnliche Zellstil‑Einträge. Ein PivotArea‑Format bleibt an einer Region wie den Beschriftungen eines Feldes oder den Datenwerten befestigt und wird erneut aufgelöst, wenn die PivotTable neu berechnet, aktualisiert oder erweitert wird. Ein direkt in eine Zelle geschriebenes Format hingegen ist an diese Zellposition gebunden und wird vom Pivot‑Modell nicht verfolgt.
Aspose.Cells stellt die vollständige `PivotTable.Format`‑Überladungs‑Familie bereit, sodass beide Arten von Formatierung verfügbar sind:
- `Format(const PivotArea&, const Style&)` verankert einen Stil an einer semantischen Region, die mit `PivotArea.Select` oder `PivotArea.SelectField` erstellt wird.
- `Format(const CellArea&, const Style&)` verankert einen Stil an einem Arbeitsblatt‑Rechteck innerhalb der PivotTable.
- `Format(int32_t row, int32_t column, const Style&)` richtet sich an eine einzelne Zelle.
- `FormatAll(const Style&)` formatiert die gesamte PivotTable.

## **Pivot‑Bereich formatieren**
Der semantische‑Bereich‑Workflow ist der empfohlene Ansatz, wenn eine Hervorhebung einem Feld oder einem Bereich des Berichts folgen muss.
1. Erzeugen Sie ein `PivotArea` mit `PivotArea pivotArea(pivotTable);`. Das Objekt beschreibt eine semantische Region, die zu dieser bestimmten PivotTable gehört.
2. Wählen Sie ein Feld anhand seiner nullbasierten Position auf einer angegebenen Achse mit `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)` aus.
   - `PivotTableSelectionType::DataAndLabel` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.
   - `PivotTableSelectionType::LabelOnly` wählt nur die Beschriftungen des Feldes aus.
   - `PivotTableSelectionType::DataOnly` wählt nur die Datenzellen des Feldes aus.
3. Wählen Sie ein Feld anhand des Namens mit `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)` aus. Wenn ein Zeilenfeld per Name ausgewählt wird, löst die Region zu den Wertzellen, die von den Elementen dieses Feldes erzeugt werden, auf.
4. Erzeugen Sie einen `Style` mit `Workbook.CreateStyle()`, konfigurieren Sie dessen Schriftart, Vordergrundfarbe und solide Hintergrundfüllung und übergeben Sie den Stil an `PivotTable.Format(pivotArea, style)`.
5. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `PivotTable.GetPivotFormats()` hinzu.
6. Feldverankerte Formate werden beim Berechnen der Pivot‑Daten angewendet. Rufen Sie daher nach dem Anwenden der Formate `PivotTable.CalculateData()` auf, damit die Stile sichtbar werden.
Das folgende Beispiel erstellt eine kleine Pivot‑Tabelle für Obstverkäufe, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.Select` und `PivotTableSelectionType::LabelOnly`, formatiert die von demselben Zeilenfeld erzeugten Wertzellen mit `PivotArea.SelectField` und berechnet anschließend die Pivot‑Tabelle neu, sodass beide Stile angewendet werden.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Zellbereich der PivotTable formatieren**
Verwenden Sie `PivotTable.Format(const CellArea&, const Style&)`, wenn der interessierende Bereich ein einfaches Arbeitsblatt‑Rechteck und keine semantische PivotRegion ist.
Ein `CellArea` wird durch die öffentlichen Felder `StartRow`, `StartColumn`, `EndRow` und `EndColumn` beschrieben. Die Werte sind nullbasierte Arbeitsblattkoordinaten, und die Endkoordinaten geben die letzte Zeile und Spalte an, die im Rechteck enthalten sind, sodass der Bereich die Zellen von der Start‑ bis zur Endposition (inklusive) abdeckt.
Im Gegensatz zu einem feldverankerten Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `CalculateData()` ist nicht erforderlich, damit der Stil erscheint.
Ein `CellArea`‑Rechteck kann sowohl Beschriftungs‑ als auch Wertzellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.
Das folgende Beispiel formatiert das Rechteck `E4:F5` der PivotTable mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe ohne weitere Neuberechnung.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Wie Pivot‑Bereiche und Zell‑Bereiche zugeordnet werden**
Excel speichert die Formatierung von PivotTable als `pivotArea`‑Einträge und nicht als gewöhnliche Arbeitsblatt‑Zellstil‑Einträge. Das gleiche Modell wird von Aspose.Cells verwendet, sodass eine Formatierungsanfrage beim Aufzeichnen in Pivot‑Bereiche übersetzt wird.
Die Beziehung zwischen dem vom Benutzer bereitgestellten `CellArea` und den intern gespeicherten Pivot‑Bereichen ist in beide Richtungen Many‑to‑Many.
- Ein `CellArea` kann mehrere Pivot‑Bereiche erzeugen. Wenn das Rechteck sowohl Beschriftungs‑ als auch Wertzellen umfasst, wird es in separate Beschriftungs‑ und Datenregeln zerlegt, da das Pivot‑Modell Beschriftungs‑ und Datenformatierung unabhängig behandelt.
- Ein Pivot‑Bereich kann zu mehreren disjunkten `CellArea`‑Instanzen aufgelöst werden. Eine semantische Region wie eine Gesamtsummen‑Zeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke abdecken. Daher gibt `PivotArea.GetCellAreas()` ein `Vector<CellArea>` zurück, anstatt eines einzelnen Rechtecks.
Jeder über `PivotTable.Format` ausgeführte Formatierungsvorgang wird in `PivotTable.GetPivotFormats()` protokolliert. Jeder `PivotTableFormat`‑Eintrag stellt das zugehörige `PivotArea` und den angefügten `Style` dar. Die `PivotArea`‑Überladung fügt exakt einen Eintrag pro Aufruf hinzu, während ein `CellArea`, das verschiedene semantische Regionen enthält, mehrere Einträge hinzufügen kann.
Um die gespeicherten Regionen zu unterscheiden, stellt jedes `PivotArea` die Flags `GetOnlyLabel()` und `GetOnlyData()` bereit. Das nachstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte abdeckt, prüft `PivotTable.GetPivotFormats()` und gibt die `CellArea`‑Koordinaten aus, zu denen jeder gespeicherte Pivot‑Bereich seine aktuelle Position neu auflöst.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
Da die Formate als Pivot‑Bereiche und nicht als gewöhnliche Zellstile gespeichert werden, überstehen sie die Neuberechnung und das Aktualisieren. Wenn die PivotTable mit `PivotTable.RefreshData` aktualisiert, mit `CalculateData` neu berechnet oder gespeichert und erneut geladen wird, löst jeder gespeicherte Pivot‑Bereich seine aktuelle Position neu auf und sein Stil wird erneut angewendet.
{{% /alert %}}

Verwenden Sie ein mit `Select` oder `SelectField` erstelltes `PivotArea`, wenn eine Hervorhebung über Aktualisierungen hinweg an einem Feld oder einer semantischen Region verankert bleiben soll, und nutzen Sie ein `CellArea`, wenn die Formatierung eines festen Rechtecks im aktuellen PivotTable‑Layout ausreicht. Die Einzelzellen‑Überladung `Format(int32_t row, int32_t column, const Style&)` richtet sich an eine einzelne Zelle. Verwenden Sie `FormatAll`, das auf der übergeordneten Seite beschrieben wird, wenn die gesamte PivotTable auf einmal neu gestaltet werden soll.

## **Verwandte Artikel**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/cpp/apply-style-to-pivot-table/)
- [Pivot‑Tabellen‑Zeilen- und Spaltenfelder hinzufügen](/cells/de/cpp/pivot-table-add-row-and-column-fields/)
- [Wertfelder in Pivot‑Tabelle verwalten](/cells/de/cpp/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}