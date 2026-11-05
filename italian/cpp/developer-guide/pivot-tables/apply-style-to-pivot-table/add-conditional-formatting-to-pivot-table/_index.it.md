---
title: Aggiungere la formattazione condizionale a una Tabella Pivot
linktitle: Aggiungere la formattazione condizionale a una Tabella Pivot
description: Aggiungere la formattazione condizionale a una Tabella Pivot in Aspose.Cells for C++, ancorare una regola all'area dati con ApplyTo e un ambito PivotConditionFormatScopeType, oppure definire la destinazione con AddCellArea e PivotAreas, quindi collegare regole e stili tramite FormatConditions.AddCondition
keywords: Aspose.Cells for C++, Tabella Pivot, formattazione condizionale, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /it/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Gli stili descritti nella pagina principale e nella pagina fratella sono statici: un'area `PivotArea` o `CellArea` viene colorata una volta e mantiene il proprio stile indipendentemente dai valori. La formattazione condizionale è la controparte basata su regole: evidenziare ogni importo superiore a 200, sfumare il cinquanta percento centrale o segnalare gli elementi con classifica più bassa; l'evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells, la formattazione condizionale delle tabelle pivot vive nella collezione `pivotTable.GetConditionalFormats()`. Ogni voce è un `PivotConditionalFormat` che risponde a due domande in modo indipendente:
- **Dove si applica la regola?** L'area di destinazione è definita sia tramite `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, che replica il selettore di ambito dell'interfaccia utente di Excel, sia tramite `AddCellArea(CellArea)` e la collezione `GetPivotAreas()`, che nominano esplicitamente l'area.
- **Cosa verifica la regola?** Una o più condizioni vengono aggiunte tramite `GetFormatConditions()` con `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, e ogni condizione porta il proprio `Style`.

{{% alert color="primary" %}}
Non chiamare `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` né `FormatConditionCollection.AddArea(CellArea)` sull'oggetto `GetFormatConditions()` di un formato condizionale pivot. Queste due overload provengono dall'API di formattazione condizionale dei fogli di lavoro ordinari e non funzionano per le tabelle pivot: l'area della cella non viene mai convertita in un'area pivot, quindi la richiesta viene silenziosamente ignorata. Definisci sempre l'area sul `PivotConditionalFormat` stesso (`ApplyTo`, `AddCellArea` o `GetPivotAreas()`) e aggiungi la regola con una delle overload di `AddCondition`.
{{% /alert %}}

## **Applicare una regola con ambito (modo UI di Excel)**
Il primo metodo posiziona la regola nello stesso modo dell'interfaccia utente di Excel. Una cella della tabella pivot è identificata dalle sue coordinate zero‑based del foglio di lavoro, e un ambito `PivotConditionFormatScopeType` indica ad Aspose.Cells fino a dove la regola deve estendersi da quella cella:
- `PivotConditionFormatScopeType::Data` – tutte le celle valore prodotte dalla tabella pivot, inclusi i totali generali.
- `PivotConditionFormatScopeType::Field` – le celle valore appartenenti al campo identificato dalla cella, escludendo i totali generali. La cella deve essere una cella campo, ad esempio un’etichetta di riga; passare una cella valore genera un'eccezione.
- `PivotConditionFormatScopeType::Selection` – solo le celle valore all’intersezione selezionata dalla cella, tipicamente una singola cella valore.  
L’esempio seguente crea una tabella pivot di vendite di frutta con l’angolo in alto a sinistra in E3, ancora una formattazione condizionale nella cella F4 (riga 3, colonna 5) con l’ambito `Data`, e evidenzia ogni importo superiore a 200 in bianco grassetto su rosso. Con i valori Mela 220, Banana 330, Ciliegia 200 e il totale generale 750, la regola colora F4, F5 e F7 – l’area risolta è l’intera colonna dati F4:F7, e solo le celle il cui valore supera la regola si illuminano.

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

Ancora ancorando la stessa regola all’etichetta del campo di riga E4 (riga 3, colonna 4) con l’ambito `Field`, la risoluzione avviene su F4:F6 – la stessa colonna dati ma senza la riga del totale generale – perché l’ambito ora descrive il campo `Fruit` anziché l’intera area valori. L’ambito `Selection` ancorato a F4 si risolve esclusivamente su F4.

## **Definire l’area manualmente**
Il secondo metodo evita il selettore di ambito e nomina l’area direttamente sul `PivotConditionalFormat`.

### **Un rettangolo del foglio di lavoro con AddCellArea**
`AddCellArea(CellArea)` registra il rettangolo fornito come destinazione della regola. Le coordinate sono zero‑based, e l’area è esattamente il rettangolo specificato – nessuna espansione alla colonna dei dati e nessuna logica di totale generale. Usalo quando le celle di interesse formano un rettangolo fisso noto del layout pivot corrente.

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

### **Un’area pivot semantica con PivotAreas**
`GetPivotAreas()` fornisce lo stesso modello di area semantica utilizzato nella pagina fratella per gli stili statici. Crea un `PivotArea`, seleziona un campo o un’area con `Select` o `SelectField`, e aggiungilo con `GetPivotAreas().AddPivotArea(PivotArea)`. Un’area semantica resta collegata al suo campo, così la formattazione condizionale segue il campo quando la tabella pivot viene aggiornata e il layout cambia. L’overload `GetPivotAreas().Add(PivotArea)` è ancora compilabile ma è contrassegnato come obsoleto – preferisci `AddPivotArea`.

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

## **Dove sono memorizzate le regole e come sopravvivono a una riapertura**
Ogni chiamata `pivotTable.GetConditionalFormats().Add()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i loro stili vengono salvati con la cartella di lavoro – riaprire il file nell’esempio seguente mostra la stessa regola con il relativo tipo, operatori e formule intatto, e `GetCellAreas()` restituisce le stesse aree. Le voci che non hanno mai ricevuto una condizione vengono eliminate al salvataggio della cartella di lavoro, allo stesso modo in cui Excel scarta una formattazione condizionale priva di regola.

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

## **Articoli correlati**
- [Applicare stile a Tabella Pivot](/cells/it/cpp/apply-style-to-pivot-table/)
- [Formattare parte di una Tabella Pivot](/cells/it/cpp/format-part-of-pivot-table/)
- [Top 10 Mostra o Filtra in Tabella Pivot](/cells/it/cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrare Tabelle Pivot per etichetta o valore](/cells/it/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}