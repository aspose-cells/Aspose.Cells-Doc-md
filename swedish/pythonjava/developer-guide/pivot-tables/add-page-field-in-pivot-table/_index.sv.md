---
title: Lägga till filterfält i en pivottabell i Aspose.Cells för .NET
linktitle: Lägga till filterfält
description: Lär dig hur du lägger till och konfigurerar filterfält i pivottabeller med Aspose.Cells for Python via Java, inklusive att lägga till filterfält, enkelvalfiltrering och flervalsfiltrering.
keywords: Aspose.Cells, Python, Java, pivottabell, filterfält, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /sv/python-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder hela livscykeln för filterfält i pivottabeller. Du kan lägga till ett filterfält via ett högnivå-API eller via den underliggande `page_fields`-samlingen, och du kan driva sidfiltret i enkelvalsläge, rensa det för att visa alla sidobjekt, eller växla fältet till flerval så att användare kan välja flera sidobjekt samtidigt via kryssrutegränssnittet i Excel.
{{% /alert %}}

## **Introduktion**

Ett filterfält är ett pivotfält som styr *vilken delmängd* av källdatan som pivotkroppen visar. Slutanvändare ser det som en rullgardinsmeny överst i en renderad pivot i Excel, och val av ett av de tillgängliga sidobjekten bygger om pivotkroppen så att endast posterna som tillhör det sidobjektet sammanfattas. Ett pivotfält blir ett filterfält när det registreras som `PivotFieldType.PAGE` snarare än `PivotFieldType.ROW`, `PivotFieldType.COLUMN` eller `PivotFieldType.DATA`.

Ett filterfält kan fungera i två beteenden. I standardbeteendet **enkelval** är endast ett sidobjekt synligt åt gången, så pivotkroppen sammanfattar exakt en delmängd. I beteendet **flerval** exponerar fältet en kryssrutelista, och pivotkroppen sammanfattar unionen av varje ikryssat sidobjekt. Samma källfält kan flyttas fram och tillbaka mellan dessa beteenden genom att växla en enskild egenskap.

Aspose.Cells for Python via Java exponerar två likvärdiga sätt att registrera ett filterfält. Det högnivå-API:et är `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")`, som tar källkolonnens namn och lägger till fältet i ett enda anrop. Det underliggande API:et är `PivotTable.page_fields.add(PivotField)`, som används när du redan har en `PivotField`-referens och vill lägga till samma fältinstans i filterområdet. Båda API:erna fyller slutligen samma `page_fields`-samling, och resten av denna artikel visar hur du väljer mellan dem och hur du driver varje filtreringsläge.

## **Lägga till ett filterfält**

Det finns två sätt att registrera ett pivotfält i filterområdet. Det högnivåanropet tar källkolonnens namn som en sträng och är den vanligaste vägen. Det underliggande anropet accepterar en befintlig `PivotField`-instans och är bekvämt när samma fältobjekt måste återanvändas i flera pivotområden. Båda anropen placerar fältet i `PivotTable.page_fields`, varefter det visas som sidans rullgardinsmeny överst i den renderade pivoten.

### Lägga till ett filterfält med add_field_to_area

Följande exempel bygger en liten Fruit / Year / Amount-dataset, placerar en pivottabell i cell E3 med `Fruit` i radområdet, `Amount` i dataområdet och `Year` i filterområdet, uppdaterar pivoten och sparar arbetsboken.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Skapa en ny arbetsbok
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Ställ in rubrikraden
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Fyll i 9 rader med exempeldata: Frukt, År, Belopp
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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# Lägg till en pivottabell förankrad vid cell E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Lägg till fält i deras områden: Frukt som Rad, Belopp som Data, År som Sidfält
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Uppdatera och beräkna pivottabellens data
pivotTable.calculateData()

# Spara arbetsboken
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### Lägga till ett filterfält med page_fields.add

När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `PivotTable.page_fields.add`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast den slutliga registreringen i filterområdet ersätts med det underliggande API-anropet.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — Pivottabellen och sidfältet konstrueras exakt som i
#   Scenario 1a (Fruit/Year/Amount-data, pivot vid E3, Fruit→Row,
#   Amount→Data). Nedan hämtar vi Year PivotField från
#   BaseFields-samlingen och skickar det till PageFields.Add — det
#   lågnivå-alternativet till AddFieldToArea. Resultatet är
#   funktionellt identiskt med Scenario 1a.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Rubriker
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# Exempeldata (9 rader)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# Lägg till pivottabell vid E3 som täcker A1:C10
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Fruit -> Row, Amount -> Data (Year kommer att gå till Page nedan)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Lågnivå-metod: hämta det befintliga Year PivotField från BaseFields
# och registrera det i Page-området via PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# Uppdatera så att det nya sidfältet återspeglas i den sparade arbetsboken
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Enkelvalsfiltrering (Visa ett sidobjekt)**

I standardbeteendet för enkelval renderas filterfältet som en enda rullgardinsmeny och heltalet `PivotField.current_page_item` väljer vilket sidobjekt som driver pivotkroppen. Att tilldela ett specifikt index väljer det ena objektet; att tilldela det speciella sentinelvärdet `0x7FFD` (decimalt 32765) rensar filtret så att alla sidobjekt sammanfattas på en gång. Enkelval är standard; du behöver inte aktivera det explicit.

### Visa alla objekt

Att sätta `current_page_item` till magiska värdet `0x7FFD` är likvärdigt med att rensa sidfiltret: pivotkroppen sammanfattar varje sidobjekt som om inget filter tillämpades.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Skapa en ny arbetsbok
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Fyll i Fruit/Year/Amount-data
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

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
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# Skapa pivottabell vid E3
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# Konfigurera pivotfält: Fruit→Rad, Amount→Data, Year→Sida
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.calculateData()

# Rensa sidfiltret så att alla objekt i sidfältet syns.
# 0x7FFD (decimal 32765) är det speciella sentinelvärdet som betyder "alla objekt" —
# motsvarar att välja "(Alla)" i Excel:s sidfält-rullmeny.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Visa ett specifikt objekt

Att sätta `current_page_item` till ett verkligt index väljer bara det ena sidobjektet. Indexet är positionen för objektet i filterfältets sorterade objektlista, så till exempel `1` väljer det andra objektet efter sortering.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Skapa arbetsbok
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Lägg till exempeldata (Frukt/År/Belopp)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# Lägg till pivottabell vid E3
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Lägg till fält: Frukt→Rad, Belopp→Data, År→Sida
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Sidfältsspecifika operationer
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = andra objektet i sorterad ordning (t.ex. "2021")

# Uppdatera och beräkna pivottabell
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Flervalsfiltrering**

Flervalsfiltrering förvandlar sidans rullgardinsmeny till en kryssrutelista och låter slutanvändaren välja flera sidobjekt samtidigt. Aspose.Cells exponerar två egenskaper som fungerar tillsammans. `PivotField.is_multiple_item_selection_allowed` måste sättas till `True` innan flervalsgränssnittet överhuvudtaget får effekt. När det är aktiverat styr `PivotItem.is_hidden` vilka objekt som visas i kryssrutelistan, så du kan antingen visa varje objekt eller vitlista endast specifika objekt.

Koden nedan aktiverar flerval på samma Year-filterfält som byggdes i Scenario 1a, och visar sedan två mönster: Del A visar varje sidobjekt genom att lämna `is_hidden` satt till `False` för varje post, medan Del B vitlistar endast de källvärden du väljer och döljer allt annat via ett `switch (pivot_items[i].get_string_value())`-block.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — Pivottabellen och sidfältet konstrueras exakt som i
#   Scenario 1a (Frukt/År/Belopp-data, pivot vid E3, Frukt→Rad,
#   Belopp→Data, År→Sida via AddFieldToArea).
#   Nedan tillämpar vi flervalsfiltrering på sidfältet.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Exempeldata: Frukt | År | Belopp
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

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
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Aktivera flerval på sidfältet
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Del A — välj ALLA objekt (gör varje objekt synligt)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Del B — välj endast specifika objekt efter källvärde
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **Obs:** När du använder flervalsfiltrering via `PivotItem.is_hidden` måste **minst en `PivotItem` förbli synlig** (`is_hidden == False`). Om varje objekt är dolt kraschar antingen Excel när filen öppnas eller renderas en tom pivot. Verifiera alltid att din flervalsvitlista inkluderar minst ett objekt från din källdata.

## **Vilket API och vilket läge ska jag använda?**

Tabellen nedan sammanfattar när du ska använda varje API och läge så att du kan välja rätt kombination utan att läsa varje scenario i detalj.

| Scenario / Användningsfall | Rekommenderat API | Egenskap som används | Anteckningar |
|---|---|---|---|
| Lägg till ett filterfält efter källkolonnnamn (vanligast) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/a | Högnivå, en rad. Använd detta om du inte behöver en `PivotField`-referens. |
| Lägg till ett filterfält när du redan har ett `PivotField`-objekt | `PivotTable.page_fields.add(PivotField)` | n/a | Använd när fältobjektet erhölls annorstädes eller behöver återanvändas. |
| Filtrera till ett enskilt sidobjekt (standardläge) | `PivotField.current_page_item` | sätt till ett specifikt index | Till exempel visar `1` det andra objektet i den sorterade listan. |
| Visa alla objekt / rensa sidfiltret | `PivotField.current_page_item` | sätt till `0x7FFD` | Det magiska värdet `0x7FFD` (decimalt 32765) är sentinelvärdet för "alla objekt". |
| Aktivera flervalsgränssnitt i Excel | `PivotField.is_multiple_item_selection_allowed` | sätt till `True` | Krävs innan några `is_hidden`-anrop får effekt. |
| Dölj / visa enskilda objekt i en flervalslista | `PivotItem.is_hidden` | sätt per objekt | Minst ett objekt måste förbli synligt (`is_hidden == False`). |

{{% alert color="primary" %}}
Kom alltid ihåg synlighetsbegränsningen när du konfigurerar flervalsfiltrering. Om varje `PivotItem` i ett flervalsfilterfält är dolt kraschar Excel vid öppning eller renderar en tom pivot. Bygg din vitlista mot din källdata så att minst ett objekt förblir synligt, och dina sparade arbetsböcker kommer att öppnas tillförlitligt på varje maskin.
{{% /alert %}}



{{< app/cells/assistant language="python" >}}
