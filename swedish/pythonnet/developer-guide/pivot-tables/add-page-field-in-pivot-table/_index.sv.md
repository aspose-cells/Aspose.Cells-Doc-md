---
title: Lägga till filterfält i en pivottabell i Aspose.Cells för .NET
linktitle: Lägga till filterfält
description: Lär dig hur du lägger till och konfigurerar filterfält i pivottabeller med Aspose.Cells for Python via .NET, inklusive att lägga till filterfält, enkelvalsfiltrering och flervalsfiltrering.
keywords: Aspose.Cells, Python via .NET, pivottabell, filterfält, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /sv/python-net/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder hela livscykeln för filterfält i pivottabeller. Du kan lägga till ett filterfält via ett bekvämt API på hög nivå eller via den lägre nivåns `page_fields`-samling, och du kan styra sidfiltret i enkelvalsläge, rensa det för att visa varje sidobjekt, eller växla fältet till flerval så att användare kan välja flera sidobjekt samtidigt via kryssrutegränssnittet i Excel.
{{% /alert %}}

## **Introduktion**

Ett filterfält är ett pivotfält som styr *vilken delmängd* av källdatan som pivotkroppen visar. Slutanvändare ser det som en rullgardinsmeny överst i en renderad pivot i Excel, och val av ett av de tillgängliga sidobjekten bygger om pivotkroppen så att endast posterna som tillhör det sidobjektet sammanfattas. Ett pivotfält blir ett filterfält när det registreras som `PivotFieldType.PAGE` snarare än `PivotFieldType.ROW`, `PivotFieldType.COLUMN` eller `PivotFieldType.DATA`.

Ett filterfält kan fungera i två beteenden. I standardbeteendet **enkelval** är endast ett sidobjekt synligt åt gången, så pivotkroppen sammanfattar exakt en delmängd. I beteendet **flerval** exponerar fältet en kryssrutelista, och pivotkroppen sammanfattar unionen av varje ikryssat sidobjekt. Samma källfält kan flyttas fram och tillbaka mellan dessa beteenden genom att växla en enskild egenskap.

Aspose.Cells for Python via .NET exponerar två likvärdiga sätt att registrera ett filterfält. API:et på hög nivå är `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")`, som tar källkolonnens namn och lägger till fältet i ett enda anrop. API:et på lägre nivå är `PivotTable.page_fields.add(PivotField)`, som används när du redan har en `PivotField`-referens och vill lägga till samma fältinstans i filterområdet. Båda API:erna slutar med att fylla samma `page_fields`-samling, och resten av denna artikel visar hur du väljer mellan dem och hur du styr varje filtreringsläge.

## **Lägga till ett filterfält**

Det finns två sätt att registrera ett pivotfält i filterområdet. Anropet på hög nivå tar källkolonnens namn som en sträng och är den vanligaste vägen. Anropet på lägre nivå accepterar en befintlig `PivotField`-instans och är bekvämt när samma fältobjekt måste återanvändas över flera pivotområden. Båda anropen placerar fältet i `PivotTable.page_fields`, varefter det visas som sidans rullgardinsmeny överst i den renderade pivoten.

### Lägga till ett filterfält med add_field_to_area

Följande exempel bygger ett litet Fruit / Year / Amount-dataset, placerar en pivottabell vid cell E3 med `Fruit` i radområdet, `Amount` i dataområdet och `Year` i filterområdet, uppdaterar pivoten och sparar arbetsboken.

```python
import aspose.cells as ac

# Skapa en ny arbetsbok
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Ställ in rubrikraden
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Fyll i 9 rader med exempeldata: Fruit, Year, Amount
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# Lägg till en pivottabell förankrad vid cell E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Lägg till fält i deras områden: Fruit som Rad, Amount som Data, Year som Sidfält
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# Uppdatera och beräkna pivottabellens data
pivot_table.calculate_data()

# Spara arbetsboken
workbook.save("pageFieldSample.xlsx")
```

### Lägga till ett filterfält med page_fields.add

När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `PivotTable.page_fields.add`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast den slutliga registreringen i filterområdet ersätts med API-anropet på lägre nivå.

```python
import aspose.cells as ac

# — Pivottabellen och sidfältet konstrueras exakt som i
#   Scenario 1a (Fruit/Year/Amount-data, pivot vid E3, Fruit→Rad,
#   Amount→Data). Nedan hämtar vi Year-PivotField från
#   BaseFields-samlingen och skickar det till PageFields.Add — det
#   lågnivåalternativet till AddFieldToArea. Resultatet är
#   funktionellt identiskt med Scenario 1a.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Rubriker
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# Exempeldata (9 rader)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# Lägg till pivottabell vid E3 som täcker A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Fruit -> Rad, Amount -> Data (Year kommer att gå till Sida nedan)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Lågnivåmetod: hämta den befintliga Year-PivotField från BaseFields
# och registrera den i Sid-området via PageFields.Add(PivotField).
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# Uppdatera så att det nya sidfältet återspeglas i den sparade arbetsboken
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Enkelvalsfiltrering (visa ett sidobjekt)**

I standardbeteendet enkelval renderas filterfältet som en enda rullgardinsmeny och heltalsvärdet `PivotField.current_page_item` väljer vilket sidobjekt som styr pivotkroppen. Att tilldela ett specifikt index väljer det ena objektet; att tilldela det speciella sentinelvärdet `0x7FFD` (decimalt 32765) rensar filtret så att varje sidobjekt sammanfattas på en gång. Enkelval är standard; du behöver inte aktivera det explicit.

### Visa alla objekt

Att sätta `current_page_item` till det magiska värdet `0x7FFD` är likvärdigt med att rensa sidfiltret: pivotkroppen sammanfattar varje sidobjekt som om inget filter tillämpades.

```python
import aspose.cells as ac

# Skapa en ny arbetsbok
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Fylla i Fruit/Year/Amount-data
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# Skapa pivottabell vid E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# Konfigurera pivotfält: Fruit→Rad, Amount→Data, Year→Sida
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.calculate_data()

# Rensa sidfiltret så att alla objekt i sidfältet visas.
# 0x7FFD (decimal 32765) är det speciella sentinelvärdet som betyder "alla objekt" —
# motsvarande att välja "(Alla)" i Excels sidfält-rullgardin.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### Visa ett specifikt objekt

Att sätta `current_page_item` till ett verkligt index väljer bara det ena sidobjektet. Indexet är positionen för objektet i filterfältets sorterade objektlista, så till exempel `1` väljer det andra objektet efter sortering.

```python
import aspose.cells as ac

# Skapa arbetsbok
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Lägg till exempeldata (Frukt/År/Belopp)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# Lägg till pivottabell vid E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Lägg till fält: Frukt→Rad, Belopp→Data, År→Sida
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# Sidfältsspecifika operationer
pivot_table.page_fields[0].current_page_item = 1  # 1 = andra objektet i sorterad ordning (t.ex. "2021")

# Uppdatera och beräkna pivottabell
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Flervalsfiltrering**

Flervalsfiltrering förvandlar sidans rullgardinsmeny till en kryssrutelista och låter slutanvändaren välja flera sidobjekt samtidigt. Aspose.Cells exponerar två egenskaper som fungerar tillsammans. `PivotField.is_multiple_item_selection_allowed` måste sättas till `True` innan flervalsgränssnittet överhuvudtaget aktiveras. När det är aktiverat styr `PivotItem.is_hidden` vilka objekt som visas i kryssrutelistan, så du kan antingen visa varje objekt eller vitlista endast specifika objekt.

Koden nedan aktiverar flerval på samma Year-filterfält som byggdes i Scenario 1a, och visar sedan två mönster: Del A visar varje sidobjekt genom att lämna `is_hidden` satt till `False` för varje post, medan Del B vitlistar endast de källvärden du väljer och döljer allt annat genom ett `if` / `elif`-block som testar `pivot_items[i].get_string_value()`.

```python
import aspose.cells as ac

# — Pivottabellen och sidfältet konstrueras exakt som i
#   Scenario 1a (Fruit/Year/Amount-data, pivot vid E3, Fruit→Rad,
#   Amount→Data, Year→Sida via AddFieldToArea).
#   Nedan tillämpar vi flervalsfiltrering på sidfältet.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Exempeldata: Fruit | Year | Amount
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — Aktivera flerval på sidfältet
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# Del A — välj ALLA objekt (gör alla objekt synliga)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# Del B — välj endast specifika objekt efter källvärde
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **Obs:** När du använder flervalsfiltrering via `PivotItem.is_hidden` måste **minst en `PivotItem` förbli synlig** (`is_hidden == False`). Om varje objekt är dolt kraschar antingen Excel när filen öppnas eller renderas en tom pivot. Verifiera alltid att din flervalsvitlista innehåller minst ett objekt från din källdata.

## **Vilket API och vilket läge ska jag använda?**

Tabellen nedan sammanfattar när du ska använda varje API och läge så att du kan välja rätt kombination utan att läsa varje scenario i detalj.

| Scenario / Användningsfall | Rekommenderat API | Egenskap som används | Anteckningar |
|---|---|---|---|
| Lägg till ett filterfält efter källkolonnens namn (vanligast) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | Hög nivå, en rad. Använd detta om du inte behöver en `PivotField`-referens. |
| Lägg till ett filterfält när du redan har ett `PivotField`-objekt | `PivotTable.page_fields.add(PivotField)` | n/a | Använd när fältobjektet erhölls någon annanstans eller behöver återanvändas. |
| Filtrera till ett enskilt sidobjekt (standardläge) | `PivotField.current_page_item` | sätt till ett specifikt index | Till exempel visar `1` det andra objektet i den sorterade listan. |
| Visa alla objekt / rensa sidfiltret | `PivotField.current_page_item` | sätt till `0x7FFD` | Det magiska värdet `0x7FFD` (decimalt 32765) är sentinelvärdet för "alla objekt". |
| Aktivera flervalsgränssnitt i Excel | `PivotField.is_multiple_item_selection_allowed` | sätt till `True` | Krävs innan några `is_hidden`-anrop får effekt. |
| Dölj / visa enskilda objekt i en flervalslista | `PivotItem.is_hidden` | sätt per objekt | Minst ett objekt måste förbli synligt (`is_hidden == False`). |

{{% alert color="primary" %}}
Kom alltid ihåg synlighetsbegränsningen när du konfigurerar flervalsfiltrering. Om varje `PivotItem` i ett flervalsfilterfält är dolt kraschar Excel vid öppning eller renderar en tom pivot. Bygg din vitlista mot din källdata så att minst ett objekt förblir synligt, och dina sparade arbetsböcker öppnas tillförlitligt på varje maskin.
{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}
