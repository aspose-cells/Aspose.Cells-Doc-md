---
title: Gestire i campi valore di una tabella pivot in Aspose.Cells per .NET
linktitle: Campi valore
description: Scopri come aggiungere campi di base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.function e visualizzare il campo valore sull'asse Riga o Colonna in Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, tabella pivot, campo valore, PivotField, PivotField.function, campo dati, PivotTable.values_field, Somma, Media
type: docs
weight: 230
url: /it/python-net/pivot-table-manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Aggiunta di un campo all'area dati

L'aggiunta di un campo di base all'area dati (valore) è il primo passo per definire come una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.add_field_to_area(PivotFieldType, str)`, un overload che accetta la costante `PivotFieldType.DATA` e il nome della colonna di origine. Una volta aggiunto un campo all'area dati, l'API lo espone tramite la raccolta `PivotTable.data_fields`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna di origine numerica viene riassunta con `ConsolidationFunction.SUM`, mentre una colonna non numerica utilizza `Count` come valore predefinito.

## Modifica della funzione di riepilogo

Ogni campo posizionato nell'area dati è incapsulato internamente come istanza di `PivotField` e la sua proprietà `function` restituisce un valore dall'enum `ConsolidationFunction`. Lo stesso setter `function` consente di passare tra gli aggregati disponibili, tra cui `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` e `Varp`.

{{% alert color="primary" %}}
La modifica di `function` influisce solo sull'aggregato, la colonna di origine non cambia.
{{% /alert %}}

È quindi possibile lasciare un campo dati come `Sum` mentre si aggiunge un secondo campo dati che ha come destinazione la stessa colonna di origine ma utilizza `Count` o `Average`, il tutto in un'unica tabella pivot.

## Visualizzazione dei campi valore sull'asse Riga o Colonna

Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un campo virtuale aggiuntivo chiamato `PivotTable.values_field`. Questo campo virtuale rappresenta l'aggregato di ogni campo dati presente nell'area dati. È possibile trascinarlo nell'area Riga o Colonna come campo pivot di base, utile per disporre più misure affiancate.

{{% alert color="primary" %}}
`PivotTable.values_field` non funziona se non ci sono campi valore o se ne è presente solo uno.
{{% /alert %}}

Gli scenari seguenti illustrano tre esempi end-to-end che dimostrano ciascuna delle funzionalità descritte sopra sulla stessa struttura di tabella pivot.

## Scenario 1 — Trascinamento di un campo di base nell'area Valore

Questo scenario mostra come inserire un singolo campo di base (`Amount`) nell'area dati di una tabella pivot esistente. La struttura di tabella pivot condivisa posiziona `Category` e `Item` sull'asse Riga e `Year` sull'asse Colonna. Dopo l'operazione, `Amount` appare nell'area dati e viene calcolato come `Sum` di `Amount` per impostazione predefinita.

```python
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Intestazioni in A1:D1
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

# Righe di dati A2:D9 utilizzando cicli annidati con diramazione su j
for i in range(1, 9):
    for j in range(4):
        if j == 0:
            worksheet.cells[i, j].put_value("Fruit" if i <= 4 else "Vegetable")
        elif j == 1:
            if i == 1 or i == 2:
                worksheet.cells[i, j].put_value("Apple")
            elif i == 3 or i == 4:
                worksheet.cells[i, j].put_value("Banana")
            elif i == 5 or i == 6:
                worksheet.cells[i, j].put_value("Carrot")
            else:
                worksheet.cells[i, j].put_value("Daikon")
        elif j == 2:
            worksheet.cells[i, j].put_value(2020 + ((i - 1) % 2))
        elif j == 3:
            if i == 1:
                worksheet.cells[i, j].put_value(100)
            elif i == 2:
                worksheet.cells[i, j].put_value(150)
            elif i == 3:
                worksheet.cells[i, j].put_value(80)
            elif i == 4:
                worksheet.cells[i, j].put_value(90)
            elif i == 5:
                worksheet.cells[i, j].put_value(50)
            elif i == 6:
                worksheet.cells[i, j].put_value(60)
            elif i == 7:
                worksheet.cells[i, j].put_value(40)
            else:
                worksheet.cells[i, j].put_value(45)

# Aggiungi tabella pivot in F3 con nome PivotTable1
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Layout pivot: Categoria e Articolo su Riga, Anno su Colonna, Importo come campo dati
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## Scenario 2 — Modifica della funzione di riepilogo

Questo scenario parte dalla stessa struttura di tabella pivot dello Scenario 1 ma aggiunge il campo `Amount` all'area dati due volte. Entrambi i campi dati fanno riferimento alla stessa colonna di origine, tuttavia il secondo campo viene sovrascritto utilizzando il setter `PivotField.function` in modo che diventi `Count` invece del `Sum` predefinito.

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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
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
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

count_field = pivot_table.data_fields[1]
count_field.function = ac.ConsolidationFunction.COUNT

pivot_table.calculate_data()

workbook.save("output_function.xlsx")
```

## Scenario 3 — Visualizzazione dei campi valore sull'asse Riga o Colonna

Con due campi dati in posizione, `PivotTable.values_field` diventa utilizzabile. Questo scenario trascina tale campo virtuale aggregato nell'area Colonna in modo che ogni misura nell'area dati appaia come un proprio blocco di colonna accanto a `Year`.

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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
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
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ac.ConsolidationFunction.COUNT

# Traccia i campi valore sull'asse delle colonne.
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()

workbook.save("output_plot.xlsx")
```

Insieme, questi tre scenari coprono ogni aspetto della manipolazione dei campi valore in Aspose.Cells for Python via .NET, da un singolo campo dati con il `Sum` predefinito a una tabella pivot multi-misura in cui il virtuale `ValuesField` controlla il layout sull'asse Riga o Colonna.

## Articoli correlati

- [Campi Riga e Colonna delle tabelle pivot in Aspose.Cells for Python via .NET](/cells/it/python-net/row-and-column-fields/)
- [Campi pagina nelle tabelle pivot](/cells/it/python-net/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells for Python via .NET](/cells/it/python-net/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}
