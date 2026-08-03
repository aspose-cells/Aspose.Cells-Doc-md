---
title: Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells per .NET
linktitle: Campi riga e colonna
description: Scopri come aggiungere campi di base alle aree righe e colonne di una tabella pivot e controllare i subtotali dei campi pivot utilizzando PivotField.set_subtotals in Aspose.Cells for Python via .NET.
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

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.AUTOMATIC, True)

pivot_table.calculate_data()

workbook.save("output_automatic.xlsx")
```

## **Scenario 2 — Eliminazione di tutti i subtotali (None)**

Chiamare `set_subtotals(PivotFieldSubtotalType.NONE, True)` rimuove ogni riga di subtotale dalla tabella pivot, lasciando solo le righe dei campi e il totale generale in basso. Questo è utile quando si desiderano i dati raggruppati grezzi senza alcuna riga di riepilogo.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

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
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
for st in [ac.PivotFieldSubtotalType.SUM, ac.PivotFieldSubtotalType.COUNT, ac.PivotFieldSubtotalType.AVERAGE, ac.PivotFieldSubtotalType.MAX, ac.PivotFieldSubtotalType.MIN, ac.PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()

workbook.save("output_none.xlsx")
```

## **Scenario 3 — Sottoinsieme personalizzato di subtotali (Sum + Average)**

Non si è limitati a un singolo tipo di subtotale. Ogni chiamata a `set_subtotals` opera indipendentemente su un solo tipo, quindi chiamare il metodo due volte — una volta con `SUM` e una volta con `AVERAGE` — produce un sottoinsieme personalizzato di due righe di subtotale per ciascun gruppo `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells["A1"].put_value("Category")
worksheet.cells["B1"].put_value("Item")
worksheet.cells["C1"].put_value("Year")
worksheet.cells["D1"].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(ac.PivotFieldSubtotalType.AVERAGE, True)

pivot_table.calculate_data()

workbook.save("output_custom.xlsx")
```

## **Riepilogo**

I tre scenari precedenti condividono lo stesso dataset e la stessa struttura di tabella pivot. L'unica differenza tra di essi è la chiamata a `set_subtotals` applicata al campo riga esterno `Category`. Ricorda la regola dei due campi: un singolo campo in un'area non ha nulla da subtotalizzare, quindi è sempre necessario inserire almeno due campi nell'area righe o colonne quando si desidera che `set_subtotals` abbia un effetto visibile.
{{< app/cells/assistant language="python-net" >}}
