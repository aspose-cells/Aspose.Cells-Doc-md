---
title: Bedingte Formatierung zu einer Pivot-Tabelle hinzufügen
description: Bedingte Formatierung zu einer Pivot-Tabelle in Aspose.Cells for C++ hinzufügen – eine Regel mit ApplyTo und einem PivotConditionFormatScopeType‑Bereich an den Datenbereich anhängen oder das Ziel mit AddCellArea und PivotAreas festlegen und anschließend Regeln und Stile über FormatConditions.AddCondition zuweisen.
linktitle: Add Conditional Formatting to a Pivot Table
keywords: Aspose.Cells for C++, Pivot-Tabelle, bedingte Formatierung, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /de/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Die auf der übergeordneten Seite und auf der Schwesterseite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmal eingefärbt und behält seinen Stil bei, unabhängig von den Werten.  
Bedingte Formatierung ist das regelbasierte Gegenstück – jedes Ergebnis über 200 hervorheben, die mittleren fünfzig Prozent schattieren oder die am schlechtesten bewerteten Elemente kennzeichnen – und die Hervorhebung folgt den Werten, sobald die Pivot‑Tabelle neu berechnet oder aktualisiert wird.  
In Aspose.Cells befindet sich die bedingte Formatierung von Pivot‑Tabellen in der Sammlung `pivotTable.GetConditionalFormats()`. Jeder Eintrag ist ein `PivotConditionalFormat`, der unabhängig zwei Fragen beantwortet:
- **Wo wird die Regel angewendet?** Der Zielbereich wird entweder über `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` definiert, was dem Bereichsauswahl‑Werkzeug der Excel‑Benutzeroberfläche entspricht, oder über `AddCellArea(CellArea)` und die Sammlung `GetPivotAreas()`, die den Bereich explizit benennen.
- **Was prüft die Regel?** Eine oder mehrere Bedingungen werden über `GetFormatConditions()` mit `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` hinzugefügt, wobei jede Bedingung ihr eigenes `Style` enthält.

{{% alert color="primary" %}}
Rufen Sie nicht `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` oder `FormatConditionCollection.AddArea(CellArea)` auf dem `GetFormatConditions()`‑Objekt eines Pivot‑Conditional‑Formats auf. Diese beiden Überladungen stammen aus der regulären Arbeitsblatt‑Bedingten‑Formatierungs‑API und funktionieren nicht für Pivot‑Tabellen – der Zellbereich wird nie in einen Pivot‑Bereich umgewandelt, sodass die Anforderung stillschweigend ignoriert wird. Definieren Sie stets den Bereich direkt auf dem `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` oder `GetPivotAreas()`) und fügen Sie die Regel mit einer der `AddCondition`‑Überladungen hinzu.
{{% /alert %}}

## **Eine Regel mit einem Bereich anwenden (wie in der Excel‑UI)**
Die erste Methode positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der Pivot‑Tabelle wird durch ihre nullbasierten Arbeitsblattkoordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich gibt Aspose.Cells an, wie weit die Regel von dieser Zelle aus reichen soll:
- `PivotConditionFormatScopeType::Data` – alle Wertezellen, die die Pivot‑Tabelle erzeugt, inklusive Gesamtsummen.
- `PivotConditionFormatScopeType::Field` – die Wertezellen, die zu dem Feld gehören, das die Zelle identifiziert, ohne Gesamtsummen. Die Zelle muss eine Feldzelle sein, beispielsweise ein Zeilenfeld‑Bezeichner; die Übergabe einer Wertezelle löst eine Ausnahme aus.
- `PivotConditionFormatScopeType::Selection` – nur die Wertezellen an der Schnittstelle, die die Zelle auswählt, typischerweise eine einzelne Wertezelle.
Das nachstehende Beispiel erstellt eine Pivot‑Tabelle für Fruchterlöse, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format in Zelle F4 (Zeile 3, Spalte 5) mit dem `Data`‑Bereich und hebt jeden Betrag über 200 fett weiß auf rotem Hintergrund hervor. Bei den Werten Apple 220, Banana 330, Cherry 200 und der Gesamtsumme 750 färbt die Regel F4, F5 und F7 – der aufgelöste Bereich ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten auf.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Verankert man dieselbe Regel beim Zeilenfeld‑Bezeichner E4 (Zeile 3, Spalte 4) mit dem `Field`‑Bereich, ergibt sich stattdessen F4:F6 – dieselbe Datenspalte ohne die Gesamtsummen‑Zeile –, weil der Bereich nun das Feld `Fruit` statt des gesamten Wertebereichs beschreibt. Der `Selection`‑Bereich, der an F4 verankert ist, löst nur F4 auf.

## **Den Bereich manuell definieren**
Die zweite Methode lässt die Bereichsauswahl weg und benennt den Bereich explizit auf dem `PivotConditionalFormat`.

### **Ein Arbeitsblatt‑Rechteck mit AddCellArea**
`AddCellArea(CellArea)` speichert das angegebene Rechteck als Ziel der Regel. Die Koordinaten sind nullbasierte Arbeitsblattkoordinaten, und der Bereich entspricht exakt dem übergebenen Rechteck – keine Erweiterung zur Datenspalte und keine Gesamtsummen‑Logik. Verwenden Sie diese Methode, wenn die interessierenden Zellen ein bekanntes festes Rechteck des aktuellen Pivot‑Layouts bilden.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Ein semantischer Pivot‑Bereich mit PivotAreas**
`GetPivotAreas()` liefert dasselbe semantische Bereichs‑Modell, das die Schwesterseite für statische Stile verwendet. Erstellen Sie ein `PivotArea`, wählen Sie ein Feld oder einen Bereich mit `Select` bzw. `SelectField` aus und fügen Sie ihn mit `GetPivotAreas().AddPivotArea(PivotArea)` hinzu. Ein semantischer Bereich bleibt seinem Feld zugeordnet, sodass das bedingte Format dem Feld folgt, wenn die Pivot‑Tabelle aktualisiert und das Layout verschoben wird. Die Überladung `GetPivotAreas().Add(PivotArea)` lässt sich zwar noch kompilieren, ist jedoch als veraltet markiert – bevorzugen Sie `AddPivotArea`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Wo die Regeln gespeichert werden und wie sie einen Neuladevorgang überstehen**
Jeder Aufruf von `pivotTable.GetConditionalFormats().Add()` fügt ein `PivotConditionalFormat` zur Pivot‑Tabelle hinzu. Die Bedingungen, ihre Formeln und ihre Stile werden mit der Arbeitsmappe gespeichert – das erneute Öffnen der Datei im nachstehenden Beispiel zeigt dieselben beiden Regeln mit ihren Typen, Operatoren und Formeln unverändert, und `GetCellAreas()` meldet dieselben Bereiche. Einträge, denen nie eine Bedingung zugewiesen wurde, werden beim Speichern der Arbeitsmappe verworfen, analog dazu, wie Excel ein bedingtes Format ohne Regel entfernt.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Verwandte Artikel**
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/cpp/apply-style-to-pivot-table/)
- [Teil einer Pivot‑Tabelle formatieren](/cells/de/cpp/format-part-of-pivot-table/)
- [Top‑10 anzeigen oder filtern in Pivot‑Tabelle](/cells/de/cpp/top-10-show-or-filter-in-pivot-table/)
- [Pivot‑Tabellen nach Bezeichner oder Wert filtern](/cells/de/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}