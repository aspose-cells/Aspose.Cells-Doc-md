---
title: Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells per .NET
linktitle: Campi riga e colonna
description: Scopri come aggiungere campi base alle regioni di riga e colonna di una tabella pivot e come controllare i subtotali dei campi pivot utilizzando PivotField.SetSubtotals in Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tabella pivot, campo riga, campo colonna, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotali
type: docs
weight: 220
url: /it/cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aggiungere un campo alla regione Riga o Colonna**

Il metodo `PivotTable.AddFieldToArea(PivotFieldType fieldType, intrusive_ptr<Aspose::Cells::Systems::String> fieldName)` sposta un campo base dai dati di origine in una delle quattro regioni della pivot. L'argomento `fieldType` accetta uno dei seguenti valori di `PivotFieldType`.

- `Row` — campi posizionati verticalmente a sinistra
- `Column` — campi posizionati orizzontalmente nella parte superiore
- `Data` — campi i cui valori vengono aggregati
- `Page` — campi utilizzati come filtri del report

Dopo aver aggiunto i campi, è possibile accedervi tramite le proprietà `PivotTable.RowFields` e `PivotTable.ColumnFields`. Ogni proprietà restituisce un `PivotFieldCollection`. Il campo all'indice 0 di `RowFields` è il campo di riga più esterno, e gli indici successivi rappresentano i campi annidati al suo interno. La stessa convenzione di indicizzazione si applica a `ColumnFields`.

L'ordine di annidamento dei campi è importante. Aggiungere prima `Category` alla regione di riga e poi `Item` produce una pivot il cui raggruppamento esterno è `Category` e il cui raggruppamento interno è `Item`. Invertire l'ordine inverte la gerarchia.

## **Subtotali dei campi pivot**

Il metodo `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` controlla quali righe di subtotale vengono visualizzate per un campo pivot. Ogni chiamata attiva/disattiva un singolo tipo di subtotale in modo indipendente. Passare `shown = true` mostra il subtotale, mentre `shown = false` lo nasconde. Poiché ogni chiamata influenza un solo tipo, chiamare il metodo più volte con valori diversi di `subtotalType` crea un sottoinsieme personalizzato di subtotali.

L'enumerazione `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.

- `Automatic` — Aspose.Cells sceglie la selezione predefinita (tipicamente `Sum` per i campi numerici)
- `None` — elimina ogni riga di subtotale
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
I subtotali vengono visualizzati solo quando ci sono due o più campi pivot nella regione di riga (o nella regione di colonna). Un singolo campo non ha nulla di significativo tra cui calcolare i subtotali, quindi le chiamate a `SetSubtotals` non hanno alcun effetto visibile in questo caso. Questo articolo quindi posiziona due campi di riga (`Category` esterno, `Item` interno) in ogni esempio, in modo che il confine dei subtotali tra ogni gruppo `Category` sia visibile.
{{% /alert %}}

## **Scenario 1 — Subtotali automatici (predefiniti)**

Quando non si chiama affatto `SetSubtotals`, Aspose.Cells applica la selezione `Automatic` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` sul campo di riga esterno `Category`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Automatic, true);

    pivotTable.CalculateData();

    workbook.Save(u"output_automatic.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Scenario 2 — Eliminazione di tutti i subtotali (None)**

La chiamata `SetSubtotals(PivotFieldSubtotalType.None, true)` rimuove ogni riga di subtotale dalla pivot, lasciando solo le righe dei campi e il totale generale in fondo. Questo è utile quando si desiderano i dati raggruppati grezzi senza righe di riepilogo.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.SetName(u"Data");

    U16String headers[] = { u"Category", u"Item", u"Year", u"Amount" };
    for (int j = 0; j < 4; j++) {
        sheet.GetCells().Get(0, j).PutValue(headers[j]);
    }

    U16String categories[] = { u"Fruit", u"Fruit", u"Fruit", u"Fruit",
                               u"Vegetable", u"Vegetable", u"Vegetable", u"Vegetable" };
    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana",
                          u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[]   = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = {  100,  150,   80,   90,   50,   60,   40,   45 };

    for (int i = 0; i < 8; i++) {
        sheet.GetCells().Get(i + 1, 0).PutValue(categories[i]);
        sheet.GetCells().Get(i + 1, 1).PutValue(items[i]);
        sheet.GetCells().Get(i + 1, 2).PutValue(years[i]);
        sheet.GetCells().Get(i + 1, 3).PutValue(amounts[i]);
    }

    int pivotIndex = sheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::None, true);
    pivotTable.CalculateData();

    wb.Save(u"output_none.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Scenario 3 — Sottoinsieme di subtotali personalizzato (Sum + Average)**

Non si è limitati a un singolo tipo di subtotale. Ogni chiamata a `SetSubtotals` opera in modo indipendente su un tipo, quindi chiamare il metodo due volte — una volta con `Sum` e una volta con `Average` — produce un sottoinsieme personalizzato di due righe di subtotale per ogni gruppo `Category`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(u"A1").PutValue(u"Category");
    worksheet.GetCells().Get(u"B1").PutValue(u"Item");
    worksheet.GetCells().Get(u"C1").PutValue(u"Year");
    worksheet.GetCells().Get(u"D1").PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Average, true);

    pivotTable.CalculateData();

    workbook.Save(u"output_custom.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Riepilogo**

I tre scenari precedenti condividono lo stesso set di dati e la stessa struttura della tabella pivot. L'unica differenza tra essi è la chiamata a `SetSubtotals` applicata al campo di riga esterno `Category`. Ricorda la regola dei due campi: un singolo campo in una regione non ha nulla tra cui calcolare i subtotali, quindi posiziona sempre almeno due campi nella regione di riga o di colonna quando desideri che `SetSubtotals` abbia un effetto visibile.

## **Articoli correlati**

- [Campi pagina nelle tabelle pivot](/cells/it/cpp/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells for C++](/cells/it/cpp/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
