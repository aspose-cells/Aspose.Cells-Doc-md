---
title: Infoga pivottabell
linktitle: Infoga pivottabell
description: Skapa och formatera pivottabeller med Aspose.Cells for Python via .NET.
keywords: Skapa pivottabell, Infoga pivottabell, Formatera pivottabell.
type: docs
weight: 160
url: /sv/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Vad är en pivottabell?**
En pivottabell är en interaktiv sammanfattningsrapport: den komprimerar en stor mängd rådata, rad för rad, till en kompakt matris utan en enda formel. Du avgör vilka kolumner som blir radetiketter, vilka som blir kolumnetiketter och vilka som aggregeras som värden – pivottabellen sköter grupperingen och beräkningen:
- **Sammanfatta** – total försäljning per produkt, region eller kvartal i stället för långa formelkedjor.
- **Jämför** – kategorier på raderna och perioder på kolumnerna omvandlar en platt lista till en korsrapport där trender syns med en blick.
- **Granska detaljer** – dubbelklicka på ett sammanfattningsvärde för att undersöka källraderna bakom det.
- **Uppdatera** – när källdatan ändras räknar en uppdatering om hela rapporten.
Vanliga scenarier är försäljningsinstrumentpaneler, kostnadsfördelningar och lageranalys – alla frågor av typen "hur bryts dessa siffror ned per kategori och tid?". Aspose.Cells for Python via .NET skapar motsvarande pivottabeller programmatiskt, så att de arbetsböcker som programmet genererar kan innehålla färdiga rapporter i stället för enbart rådata.

### **Objektmodell för pivottabell**
Aspose.Cells for Python via .NET tillhandahåller en särskild uppsättning klasser i namespace [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) som används för att skapa och styra pivottabeller. De här klasserna används för att skapa och konfigurera [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)-objekt, som utgör byggblocken i en pivottabell. Objekten är:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) representerar ett fält i en [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)-objekt i en [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) representerar en pivottabell i ett kalkylblad.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) representerar en samling av alla [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-objekt i ett kalkylblad.

### **Skapa en enkel pivottabell med Aspose.Cells**
Att skapa en pivottabell sker i tre steg: skriv källdatan till celler i ett kalkylblad, lägg till pivottabellen på en destinationsposition och placera pivotfälten i rad-, kolumn- och dataområdena.
1. Lägg till data i ett kalkylblad med hjälp av [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-objektets [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str)-metod. Dessa data används som pivottabellens datakälla.
2. Lägg till en pivottabell i kalkylbladet genom att anropa [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)-samlingens [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)-metod: `add(source_data, row, column)`. `source_data` är källintervallet (t.ex. "A1:C8"); `row` och `column` är de 0-baserade koordinaterna för destinationscellen i pivottabellens övre vänstra hörn (cell E3 innebär rad 2, kolumn 4). Metoden returnerar det nya [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-objektet direkt.
3. Placera pivotfälten med hjälp av [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-objektets `add_field_to_area`-metod: ett fältnamn placeras i radområdet (`PivotFieldType.ROW`), kolumnområdet (`PivotFieldType.COLUMN`) eller dataområdet (`PivotFieldType.DATA`).
4. Spara arbetsboken – pivottabellen skrivs till den sparade filen.
När kodexemplet har körts läggs en pivottabell till i kalkylbladet.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# Skapa en ny arbetsbok och hämta det första kalkylbladet
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Skriv källdata: försäljning per sport och kvartal
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# Lägg till en pivottabell vid destinationscellen E3, med A1:C8 som källa
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# Tilldela pivotfält: Sport till Rader, Quarter till Kolumner, Sales till Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# Spara arbetsboken
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
När ett cellintervall tilldelas som datakälla måste intervallet gå från övre vänstra till nedre högra hörnet. "A1:C3" är exempelvis giltigt, men "C3:A1" är det inte.
{{% /alert %}}

## Relaterade artiklar
- [Lägg till filterfält i en pivottabell med Aspose.Cells for Python via .NET](/cells/sv/python-net/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller med Aspose.Cells for Python via .NET](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Ändra layouten för sidfält i pivottabell](/cells/sv/python-net/change-page-field-layout/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-net/filter-by-label-or-value-of-pivot-table/)
- [Hantera värdefält i pivottabeller med Aspose.Cells for Python via .NET](/cells/sv/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}