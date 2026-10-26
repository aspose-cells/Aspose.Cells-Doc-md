---
title: Pivottabeller
linktitle: Pivottabeller
description: Skapa och formatera pivottabeller med Aspose.Cells for Python via Java.
keywords: Skapa pivottabell, Infoga pivottabell, Formatera pivottabell.
type: docs
weight: 160
url: /sv/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Vad är en pivottabell?**
En pivottabell är en interaktiv sammanfattningsrapport: den komprimerar en stor mängd rådata, ordnad rad för rad, till en kompakt matris utan en enda formel. Du avgör vilka kolumner som ska bli radetiketter, vilka som ska bli kolumnetiketter och vilka som ska aggregeras som värden – pivottabellen sköter grupperingen och beräkningen:
- **Sammanfatta** – total försäljning per produkt, region eller kvartal i stället för långa formelkedjor.
- **Jämför** – kategorier på raderna och perioder på kolumnerna gör en platt lista till en jämförelserapport där trender framgår direkt.
- **Granska detaljer** – dubbelklicka på valfritt sammanfattningsvärde för att se källraderna bakom värdet.
- **Uppdatera** – när källdatan ändras räknas hela rapporten om med en enda uppdatering.
Typiska användningsfall är instrumentpaneler för sälj, kostnadsuppdelningar och lageranalys – i praktiken alla frågor av formen "hur bryts dessa siffror ned per kategori och tid?". Med Aspose.Cells for Python via Java kan du programmatiskt bygga samma pivottabeller, så att arbetsböcker som din applikation genererar kan innehålla färdiga rapporter i stället för endast rådata.

### **Objektmodell för pivottabeller**
Aspose.Cells tillhandahåller en uppsättning med klasser som används för att skapa och styra pivottabeller. Grundelementen är:
- `PivotField` representerar ett fält i en `PivotTable`.
- `PivotFieldCollection` representerar en samling av alla `PivotField`-objekt i `PivotTable`.
- `PivotTable` representerar en pivottabell i ett kalkylblad.
- `PivotTableCollection` representerar en samling av alla `PivotTable`-objekt i ett kalkylblad.

### **Skapa en enkel pivottabell med Aspose.Cells**
Att skapa en pivottabell innebär att skriva källdatan till kalkylbladets celler, lägga till pivottabellen på en vald destinationsposition och placera pivotfälten i rad-, kolumn- och dataområdena.
1. Lägg till data i ett kalkylblad med cellens `putValue`-metod. Denna data används som pivottabellens datakälla.
2. Lägg till en pivottabell i kalkylbladet genom att anropa `PivotTables`-samlingens `add`-metod: `add(sourceData, row, column)`. `sourceData` är källintervallet (till exempel "A1:C8"); `row` och `column` är 0-baserade koordinater för destinationscellen i pivottabellens övre vänstra hörn (cell E3 innebär rad 2, kolumn 4). Metoden returnerar det nya `PivotTable`-objektet direkt.
3. Placera pivotfälten med `PivotTable`-objektets `addFieldToArea`-metod: ett fältnamn placeras i radområdet (`PivotFieldType.ROW`), kolumnområdet (`PivotFieldType.COLUMN`) eller dataområdet (`PivotFieldType.DATA`).
4. Spara arbetsboken – pivottabellen skrivs till den sparade filen.
En pivottabell läggs till i kalkylbladet när exempelkoden har körts.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# Skapa en ny arbetsbok och hämta det första kalkylarket
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Skriv källdata: försäljning per sport och kvartal
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# Lägg till en pivottabell vid destinationscellen E3, med A1:C8 som datakälla
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# Tilldela pivotfält: Sport till Rader, Quarter till Kolumner, Sales till Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# Spara arbetsboken
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
När ett cellintervall tilldelas som datakälla måste det sträcka sig från det övre vänstra till det nedre högra hörnet. "A1:C3" är exempelvis giltigt, men "C3:A1" är inte.
{{% /alert %}}

## Relaterade artiklar
- [Lägg till filterfält i en pivottabell med Aspose.Cells for Python via Java](/cells/sv/python-java/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller med Aspose.Cells for Python via Java](/cells/sv/python-java/apply-style-to-pivot-table/)
- [Ändra layouten för sidfält i en pivottabell](/cells/sv/python-java/change-page-field-layout/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-java/filter-by-label-or-value-of-pivot-table/)
- [Hantera värdefält i pivottabeller med Aspose.Cells for Python via Java](/cells/sv/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}