---
title: Raggruppamento discreto degli elementi dei campi pivot
linktitle: Raggruppamento discreto
description: Scopri come raggruppare gli elementi dei campi pivot in gruppi personalizzati denominati, ad esempio frutta e verdura, utilizzando DiscreteGroupItem e PivotFieldGroupOptions.DiscreteGroupItems in Aspose.Cells for C++.
keywords: Aspose.Cells for C++, tabella pivot, raggruppamento discreto, DiscreteGroupItem, PivotFieldGroupOptions, raggruppamento di elementi pivot, gruppi personalizzati, PivotField.Group, C++, tabella pivot di Excel
type: docs
weight: 90
url: /it/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Il raggruppamento automatico organizza gli elementi in base al tipo di dati, ad esempio in mesi e trimestri per le date e in intervalli per i numeri. Il raggruppamento discreto risolve il problema opposto, raggruppando elementi specifici e non affini in gruppi personalizzati denominati, ad esempio raggruppando i prodotti in categorie come frutta e verdura, i negozi per regioni o i conti per zone. In Aspose.Cells, il raggruppamento discreto è disponibile tramite la classe `DiscreteGroupItem` e la proprietà `PivotFieldGroupOptions.DiscreteGroupItems`.
- Un oggetto `DiscreteGroupItem` è costituito da un nome di gruppo e dagli elementi che vi appartengono. Gli elementi possono essere identificati in due modi: tramite i loro nomi (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) oppure tramite le rispettive posizioni nei dati di origine, con indice a base zero (`DiscreteGroupItem("fruit", { 0, 3 })`). Entrambe le modalità producono lo stesso risultato.
- Il raggruppamento discreto viene applicato a un campo nell'area delle righe o delle colonne della tabella pivot,assegnando le opzioni a `PivotField.Group(PivotFieldGroupOptions)`.

## **Raggruppa gli elementi dei campi pivot in base ai nomi degli elementi**
L'esempio seguente crea un piccolo elenco di vendite (prodotto, data e importo), genera una tabella pivot con `product` nell'area delle righe, `date` nell'area delle colonne e `amount` nell'area dei dati, quindi definisce due gruppi personalizzati in base ai nomi degli elementi, `fruit` (`grape`, `cherry`) e `vegetables` (`carrot`, `potato`). Il risultato mostra una struttura a due livelli nell'area delle righe, con il nome del gruppo come livello esterno e gli elementi originali annidati al di sotto, in modo da consentire l'analisi delle tendenze per ogni gruppo personalizzato e ogni singolo elemento.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Dopo `CalculateData()`, l'area delle righe della tabella pivot mostra `fruit` (`grape` 50, `cherry` 80) e `vegetable` (`carrot` 60, `potato` 70), con un totale complessivo di 260, mentre le etichette delle colonne mantengono le quattro date (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Raggruppa gli elementi dei campi pivot in base agli indici degli elementi**
Quando i nomi degli elementi sono lunghi o localizzati, il secondo costruttore di `DiscreteGroupItem` identifica gli elementi tramite l'indice. Gli indici corrispondono alle posizioni degli elementi nei dati di origine, nell'ordine in cui compaiono, e non in ordine alfabetico. La numerazione parte da zero. Nei dati di esempio precedenti, `grape` è l'elemento 0, `carrot` è l'elemento 1, `potato` è l'elemento 2 e `cherry` è l'elemento 3; pertanto `fruit` è `{ 0, 3 }` e `vegetable` è `{ 1, 2 }`. Il risultato è identico a quello dell'esempio basato sui nomi.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Nota**

{{% alert color="primary" %}}
- Gli elementi non assegnati a nessun gruppo personalizzato non vengono persi. Rimangono nella tabella pivot allo stesso livello dei gruppi personalizzati, ciascuno come voce separata composta da un solo elemento. Nell'esempio precedente, la definizione del solo gruppo `fruit` lascia `carrot` e `potato` nell'area delle righe come voci autonome accanto al gruppo `fruit`.
- La proprietà `PivotFieldGroupOptions.NewPivotField` controlla la disposizione del raggruppamento discreto. Per impostazione predefinita, `NewPivotField` è `true`; questo valore aggiunge il campo raggruppato come nuovo campo esterno accanto al campo originale, producendo la disposizione a due livelli mostrata sopra (`RowFields` cresce a 2). Se viene impostata su `false`, la proprietà sostituisce il campo originale. In questo caso, l'area delle righe mostra un unico livello contenente solo i nomi dei gruppi con i relativi valori aggregati: `fruit` 130 (50 + 80) e `vegetable` 130 (60 + 70).
- I costruttori di `DiscreteGroupItem` basati sui nomi e sugli indici possono essere utilizzati insieme all'interno della stessa raccolta `DiscreteGroupItems`.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/cpp/group-pivot-fields-in-the-pivot-table/)
- [Aggiungi campi di riga e colonna alla tabella pivot](/cells/it/cpp/pivot-table-add-row-and-column-fields/)
- [Filtra le tabelle pivot in base all'etichetta o al valore](/cells/it/cpp/filter-by-label-or-value-of-pivot-table/)
- [Applica uno stile alla tabella pivot](/cells/it/cpp/apply-style-to-pivot-table/)
- [Aggiorna la tabella pivot](/cells/it/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}