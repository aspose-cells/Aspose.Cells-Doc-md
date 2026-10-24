---
title: Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells per .NET
description: Scopri come aggiungere campi di base alle aree righe e colonne di una tabella pivot e controllare i subtotali dei campi pivot utilizzando PivotField.set_subtotals in Aspose.Cells for Python via .NET.
linktitle: Campi riga e colonna
keywords: Aspose.Cells, Python via .NET, tabella pivot, campo riga, campo colonna, PivotField, set_subtotals, PivotFieldSubtotalType, subtotali
type: docs
weight: 220
url: /it/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aggiungere un campo all'area righe o colonne**
Il metodo `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` sposta un campo di base dai dati di origine in una delle quattro aree della tabella pivot. L'argomento `field_type` accetta uno dei seguenti valori di `PivotFieldType`.
- `ROW` — campi posizionati verticalmente sulla sinistra
- `COLUMN` — campi posizionati orizzontalmente nella parte superiore
- `DATA` — campi i cui valori vengono aggregati
- `PAGE` — campi utilizzati come filtri del report
Dopo aver aggiunto i campi, è possibile accedervi tramite le proprietà `PivotTable.row_fields` e `PivotTable.column_fields`. Ogni proprietà restituisce un `PivotFieldCollection`. Il campo all'indice 0 di `row_fields` è il campo riga più esterno, e gli indici successivi rappresentano i campi annidati al suo interno. La stessa convenzione di indicizzazione si applica a `column_fields`.
L'ordine di annidamento dei campi è importante. Aggiungere prima `Category` all'area righe e poi `Item` produce una tabella pivot la cui raggruppamento esterno è `Category` e il cui raggruppamento interno è `Item`. Invertire l'ordine inverte la gerarchia.

## **Subtotali dei campi pivot**
Il metodo `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` controlla quali righe di subtotale vengono visualizzate per un campo pivot. Ogni chiamata attiva/disattiva un singolo tipo di subtotale indipendentemente. Passare `shown = True` visualizza il subtotale, mentre `shown = False` lo nasconde. Poiché ogni chiamata influenza un solo tipo, chiamare il metodo più volte con valori diversi di `subtotal_type` consente di costruire un sottoinsieme personalizzato di subtotali.
L'enum `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.
- `AUTOMATIC` — Aspose.Cells sceglie la selezione predefinita (tipicamente `SUM` per i campi numerici)
- `NONE` — elimina ogni riga di subtotale
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
I subtotali vengono visualizzati solo quando sono presenti due o più campi pivot nell'area righe (o nell'area colonne). Un singolo campo non ha nulla di significativo da subtotalizzare, quindi le chiamate a `set_subtotals` non hanno alcun effetto visibile in quel caso. Questo articolo, pertanto, inserisce due campi riga (`Category` esterno, `Item` interno) in ogni esempio, in modo che il confine del subtotale tra ciascun gruppo `Category` sia visibile.
{{% /alert %}}

## **Scenario 1 — Subtotali automatici (predefiniti)**
Quando non si chiama affatto `set_subtotals`, Aspose.Cells applica la selezione `AUTOMATIC` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` sul campo riga esterno `Category`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get(0, 0).put_value("Category")
worksheet.cells.get(0, 1).put_value("Item")
worksheet.cells.get(0, 2).put_value("Year")
worksheet.cells.get(0, 3).put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **Scenario 2 — Eliminazione di tutti i subtotali (None)**
Chiamare `set_subtotals(PivotFieldSubtotalType.NONE, True)` rimuove ogni riga di subtotale dalla tabella pivot, lasciando solo le righe dei campi e il totale generale in basso. Questo è utile quando si desiderano i dati raggruppati grezzi senza alcuna riga di riepilogo.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells.get(0, j).put_value(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
]
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells.get(i + 1, j).put_value(data[i][j])
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [PivotFieldSubtotalType.SUM, PivotFieldSubtotalType.COUNT, PivotFieldSubtotalType.AVERAGE, PivotFieldSubtotalType.MAX, PivotFieldSubtotalType.MIN, PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **Scenario 3 — Sottoinsieme personalizzato di subtotali (Sum + Average)**
Non si è limitati a un singolo tipo di subtotale. Ogni chiamata a `set_subtotals` opera indipendentemente su un solo tipo, quindi chiamare il metodo due volte — una volta con `SUM` e una volta con `AVERAGE` — produce un sottoinsieme personalizzato di due righe di subtotale per ciascun gruppo `Category`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get("A1").put_value("Category")
worksheet.cells.get("B1").put_value("Item")
worksheet.cells.get("C1").put_value("Year")
worksheet.cells.get("D1").put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **Riepilogo**

I tre scenari differiscono solo in un aspetto: le chiamate a `set_subtotals`. Tutto il resto — il set di dati, i campi e le aree a cui sono assegnati — è identico, il che rende direttamente confrontabili le disposizioni grafiche.
- **Posizionamento dei campi.** `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` sposta una colonna di origine in una regione. All'interno di una stessa regione, l'ordine delle chiamate determina l'ordine di visualizzazione, per cui la prima chiamata corrisponde al gruppo più esterno. Le sotto-totalizzazioni richiedono due o più campi nella stessa regione: con un singolo campo non c'è nulla tra i gruppi su cui calcolare una sotto-totalizzazione.
- **Scenaro 1 — sotto-totalizzazioni automatiche.** L’omissione di `set_subtotals` lascia la scelta a Excel, che applica la propria sotto-totalizzazione predefinita ai campi numerici. La chiamata a `set_subtotals` con `PivotFieldSubtotalType.AUTOMATIC` registra esplicitamente tale scelta, invece di lasciarla implicita.
- **Scenaro 2 — nessuna sotto-totalizzazione.** `set_subtotals` con `PivotFieldSubtotalType.NONE` disattiva la sotto-totalizzazione predefinita, così la tabella pivot conserva le righe dei campi e il totale generale, ma omette le righe di sotto-totalizzazione che Excel altrimenti inserirebbe tra di loro.
- **Scenaro 3 — un sottoinsieme selezionato.** Ogni chiamata abilita o disabilita esattamente un tipo di sotto-totalizzazione, e le chiamate si accumulano piuttosto che annullarsi reciprocamente. Chiamarla una volta con `PivotFieldSubtotalType.SUM` e una volta con `PivotFieldSubtotalType.AVERAGE` lascia quindi entrambi abilitati, e la tabella pivot visualizza una sotto-totalizzazione Somma, una sotto-totalizzazione Media e un totale generale.

{{% alert color="primary" %}}
Niente riguardo alle sotto-totalizzazioni è specifico della regione delle righe. Le stesse chiamate a `set_subtotals` su un campo ottenuto da `PivotTable.ColumnFields` producono le stesse tre disposizioni sull’asse delle colonne, poiché l’impostazione appartiene al campo pivot e non all’asse su cui è posizionato.
{{% /alert %}}
## **Articoli correlati**

- [Campi pagina nelle tabelle pivot](/cells/it/python-net/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells per Python tramite .NET](/cells/it/python-net/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python-net" >}}