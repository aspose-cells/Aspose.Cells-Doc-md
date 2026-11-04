---
title: Formattare una parte di una Tabella Pivot
description: Formatta una parte di una tabella pivot in Aspose.Cells for C++ applicando stili alle regioni semantiche PivotArea o ai rettangoli CellArea tramite PivotTable.Format, con i formati memorizzati in PivotTable.GetPivotFormats e conservati quando la tabella pivot viene aggiornata.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, tabella pivot, formato, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /it/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
`PivotTable.FormatAll` applica uno stile unico all'intera tabella pivot ed è descritto nella pagina padre. Non distingue tra etichette, valori, totali o regioni specifiche del report.  
Nella pratica, solo una parte di una tabella pivot solitamente necessita di evidenziazione. Obiettivi comuni includono le etichette appartenenti a un campo di riga, le celle valore generate da un campo, la riga del totale generale o un rettangolo arbitrario come le prime due righe di elementi.  
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione della tabella pivot come regioni semantiche `PivotArea` anziché come normali registri di stile cella. Un formato di area pivot rimane associato a una regione come le etichette di un campo o i valori dei dati, e viene rielaborato quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente su una cella, invece, appartiene a quella posizione di cella e non è tracciato dal modello pivot.  
Aspose.Cells espone l'intera famiglia di overload di `PivotTable.Format` in modo che entrambi i tipi di formattazione siano disponibili:
- `Format(const PivotArea&, const Style&)` associa uno stile a una regione semantica costruita con `PivotArea.Select` o `PivotArea.SelectField`.
- `Format(const CellArea&, const Style&)` associa uno stile a un rettangolo del foglio di lavoro all'interno della tabella pivot.
- `Format(int32_t row, int32_t column, const Style&)` mira a una singola cella.
- `FormatAll(const Style&)` formatta l'intera tabella pivot.

## **Formattare un'area Pivot**
Il flusso di lavoro basato su area semantica è l'approccio consigliato quando un'evidenziazione deve seguire un campo o una regione del report.
1. Creare una `PivotArea` con `PivotArea pivotArea(pivotTable);`. L'oggetto descrive una regione semantica appartenente a quella specifica tabella pivot.
1. Selezionare un campo mediante la sua posizione a indice zero su un asse dato con `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType::DataAndLabel` seleziona sia le etichette sia i dati del campo.
   - `PivotTableSelectionType::LabelOnly` seleziona solo le etichette del campo.
   - `PivotTableSelectionType::DataOnly` seleziona solo le celle dati del campo.
1. Selezionare un campo per nome con `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)`. Quando un campo di riga è selezionato per nome, la regione si risolve nelle celle valore generate dagli elementi di quel campo.
1. Creare uno `Style` con `Workbook.CreateStyle()`, configurarne il carattere, il colore di primo piano e il modello di sfondo solido, e passare lo stile a `PivotTable.Format(pivotArea, style)`.
1. Ogni chiamata all'overload `PivotArea` aggiunge una voce `PivotTableFormat` a `PivotTable.GetPivotFormats()`.
1. I formati ancorati al campo vengono dipinti quando i dati pivot sono calcolati. Pertanto, chiamare `PivotTable.CalculateData()` dopo aver applicato i formati affinché gli stili diventino visibili.  
L'esempio seguente costruisce una piccola tabella pivot di vendite di frutta, formatta le etichette di riga `Fruit` con `PivotArea.Select` e `PivotTableSelectionType::LabelOnly`, formatta le celle valore prodotte dallo stesso campo di riga con `PivotArea.SelectField`, quindi ricalcola la tabella pivot così che entrambi gli stili siano visualizzati.

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

## **Formattare un'area Cell della Tabella Pivot**
Utilizzare `PivotTable.Format(const CellArea&, const Style&)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché una regione semantica pivot.  
Una `CellArea` è descritta dai campi pubblici `StartRow`, `StartColumn`, `EndRow` e `EndColumn`. I valori sono coordinate del foglio di lavoro a indice zero, e le coordinate finali identificano l'ultima riga e colonna incluse nel rettangolo, quindi l'area copre le celle dalla posizione iniziale fino a quella finale, inclusa.  
Diversamente da un formato ancorato a un campo, un formato `CellArea` viene applicato alle celle immediatamente. Non è necessario un ulteriore chiamata a `CalculateData()` affinché lo stile appaia.  
Un rettangolo `CellArea` può contenere sia celle etichetta che celle valore. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.  
L'esempio seguente formatta il rettangolo `E4:F5` della tabella pivot con uno stile corsivo di colore blu chiaro e salva la cartella di lavoro senza ulteriori ricalcoli.

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

## **Mappatura tra PivotArea e CellArea**
Excel memorizza la formattazione della tabella pivot come record `pivotArea` anziché come normali record di stile cella del foglio di lavoro. Lo stesso modello è utilizzato da Aspose.Cells, quindi una richiesta di formattazione viene tradotta in aree pivot quando viene registrata.  
La relazione tra la `CellArea` fornita dall'utente e le aree pivot memorizzate internamente è molti‑a‑molti in entrambe le direzioni.
- Una `CellArea` può generare diverse aree pivot. Se il rettangolo comprende sia celle etichetta sia celle valore, viene scomposto in regole separate per etichette e dati, poiché il modello pivot tratta indipendentemente la formattazione delle etichette e dei dati.
- Un'area pivot può risolversi in diverse istanze disgiunte di `CellArea`. Una regione semantica come una riga di totale generale, o un campo i cui elementi non sono contigui, può coprire più rettangoli. Per questo `PivotArea.GetCellAreas()` restituisce un `Vector<CellArea>` anziché un singolo rettangolo.  
Ogni operazione di formattazione eseguita tramite `PivotTable.Format` è registrata in `PivotTable.GetPivotFormats()`. Ogni voce `PivotTableFormat` espone la `PivotArea` associata e lo `Style` applicato. L'overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre una `CellArea` che contiene regioni semantiche diverse può aggiungere più voci.  
Per distinguere le regioni memorizzate, ogni `PivotArea` espone le bandiere `GetOnlyLabel()` e `GetOnlyData()`. L'esempio qui sotto formatta un unico rettangolo che copre sia etichette sia valori, ispeziona `PivotTable.GetPivotFormats()` e stampa le coordinate `CellArea` a cui ciascuna area pivot memorizzata si risolve.

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
Poiché i formati sono memorizzati come aree pivot anziché come normali stili cella, sopravvivono a ricalcoli e aggiornamenti. Quando la tabella pivot viene aggiornata con `PivotTable.RefreshData`, ricalcolata con `CalculateData`, o salvata e ricaricata, ogni area pivot memorizzata si risolve nuovamente nella posizione corrente della sua regione e lo stile viene riapplicato.
{{% /alert %}}

Utilizzare una `PivotArea` costruita con `Select` o `SelectField` quando un'evidenziazione deve rimanere collegata a un campo o a una regione semantica attraverso gli aggiornamenti, e utilizzare una `CellArea` quando la formattazione di un rettangolo fisso nel layout corrente della tabella pivot è sufficiente. L'overload a cella singola `Format(int32_t row, int32_t column, const Style&)` mira a una singola cella. Utilizzare `FormatAll`, descritto nella pagina padre, quando l'intera tabella pivot deve essere riformattata in un'unica operazione.

## **Articoli correlati**
- [Applicare uno stile alla Tabella Pivot](/cells/it/cpp/apply-style-to-pivot-table/)
- [Aggiungere campi di riga e colonna alla Tabella Pivot](/cells/it/cpp/pivot-table-add-row-and-column-fields/)
- [Gestire i campi di valore nella Tabella Pivot](/cells/it/cpp/manage-value-fields/)
- [Aggiornare la Tabella Pivot](/cells/it/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}