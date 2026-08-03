---
title: Lägga till rad- och kolumnfält i en pivottabell i Aspose.Cells för .NET
linktitle: Rad- och kolumnfält
description: Lär dig hur du lägger till basfält i rad- och kolumnområdena i en pivottabell och styr pivotfältets delsummor med PivotField.set_subtotals i Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, pivottabell, radfält, kolumnfält, PivotField, set_subtotals, PivotFieldSubtotalType, delsummor
type: docs
weight: 220
url: /sv/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Lägga till ett fält i rad- eller kolumnområdet**

Metoden `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` flyttar ett basfält från källdata till ett av de fyra pivotområdena. Argumentet `field_type` accepterar ett av följande `PivotFieldType`-värden.

- `ROW` — fält placerade vertikalt till vänster
- `COLUMN` — fält placerade horisontellt överst
- `DATA` — fält vars värden aggregeras
- `PAGE` — fält som används som rapportfilter

När fälten har lagts till kan du komma åt dem via egenskaperna `PivotTable.row_fields` och `PivotTable.column_fields`. Varje egenskap returnerar en `PivotFieldCollection`. Fältet vid index 0 i `row_fields` är det yttersta radfältet, och efterföljande index representerar fält som är nästlade inuti det. Samma indexeringskonvention gäller för `column_fields`.

Ordningen på fältnästningen är viktig. Att lägga till `Category` i radområdet först och sedan `Item` skapar en pivot vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Om ordningen vänds så vänds också hierarkin.

## **Delsummor för pivotfält**

Metoden `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` styr vilka delsummarader som visas för ett pivotfält. Varje anrop växlar en enskild delsummatyp oberoende av de andra. Att skicka `shown = True` visar delsummaraden, medan `shown = False` döljer den. Eftersom varje anrop endast påverkar en typ kan du bygga en anpassad delmängd av delsummor genom att anropa metoden flera gånger med olika `subtotal_type`-värden.

Uppräkningen `PivotFieldSubtotalType` definierar de tillgängliga typerna av delsummor.

- `AUTOMATIC` — Aspose.Cells väljer standardvalet (vanligtvis `SUM` för numeriska fält)
- `NONE` — undertrycker alla delsummarader
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
Delsummor visas endast när det finns två eller flera pivotfält i radområdet (eller i kolumnområdet). Ett enskilt fält saknar meningsfull grund för delsummor, så anrop till `set_subtotals` har ingen synlig effekt i det fallet. Denna artikel placerar därför två radfält (`Category` ytterst, `Item` innerst) i varje exempel så att delsummogränsen mellan varje `Category`-grupp blir synlig.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) delsummor**

När du inte anropar `set_subtotals` alls tillämpar Aspose.Cells valet `AUTOMATIC` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` på det yttre `Category`-radfältet.

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

## **Scenario 2 — Undertrycka alla delsummor (None)**

Att anropa `set_subtotals(PivotFieldSubtotalType.NONE, True)` tar bort alla delsummarader från pivottabellen och lämnar endast fältraderna och totalsumman längst ner. Detta är användbart när du vill ha den råa grupperade datan utan några sammanfattningsrader.

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

## **Scenario 3 — Anpassad delmängd av delsummor (Sum + Average)**

Du är inte begränsad till en enskild delsummatyp. Varje anrop till `set_subtotals` verkar oberoende på en typ, så att anropa metoden två gånger — en gång med `SUM` och en gång med `AVERAGE` — skapar en anpassad delmängd av två delsummarader för varje `Category`-grupp.

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

## **Sammanfattning**

De tre scenarierna ovan delar samma dataset och pivottabellstruktur. Den enda skillnaden mellan dem är anropet till `set_subtotals` som tillämpas på det yttre `Category`-radfältet. Kom ihåg regeln om två fält: ett enskilt fält i ett område saknar meningsfull grund för delsummor, så placera alltid minst två fält i rad- eller kolumnområdet när du vill att `set_subtotals` ska ha en synlig effekt.
{{< app/cells/assistant language="python-net" >}}
