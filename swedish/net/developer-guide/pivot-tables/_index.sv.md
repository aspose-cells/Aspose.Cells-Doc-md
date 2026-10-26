---
title: Infoga pivottabell
linktitle: Infoga pivottabell
description: Skapa och formatera pivottabeller i Excel-kalkylarksfiler.
keywords: Skapa pivottabell, Infoga pivottabell, Formatera pivottabell.
type: docs
weight: 160
url: /sv/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Vad är en pivottabell?**
En pivottabell är en interaktiv sammanfattningsrapport: den komprimerar en stor mängd rådata i enskilda rader till en kompakt matris utan en enda formel. Du avgör vilka kolumner som blir radetiketter, vilka som blir kolumnetiketter och vilka som aggregeras som värden – pivottabellen sköter gruppering och beräkning:
- **Sammanfatta** – total försäljning per produkt, region eller kvartal i stället för långa formelkedjor.
- **Jämför** – kategorier på raderna och perioder i kolumnerna gör en platt lista till en korsrapport där trender syns med en blick.
- **Granska detaljer** – dubbelklicka på ett sammanfattningsvärde för att undersöka källraderna bakom det.
- **Uppdatera** – när källdata ändras räknas hela rapporten om med en uppdatering.
Typiska scenarier är säljdashboardar, kostnadsfördelningar och lageranalys. Pivottabeller kan användas för att besvara frågor av formen "hur fördelas dessa siffror per kategori och tid?". Aspose.Cells for .NET bygger samma pivottabeller programmatiskt, så att arbetsböckerna som ditt program genererar kan innehålla färdiga rapporter i stället för enbart rådata.

### **Pivottabellens objektmodell**
I namespace [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) finns en uppsättning specialiserade klasser som används för att skapa och styra pivottabeller. Med hjälp av klasserna skapar och konfigurerar du [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-objekt, som utgör byggblocken i en pivottabell. De här objekten är:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) representerar ett fält i en [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)-objekt i [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) representerar en PivotTable på ett kalkylblad.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) representerar en samling av alla [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-objekt på ett kalkylblad.

### **Skapa en enkel pivottabell med Aspose.Cells**
En pivottabell skapas i tre steg: skriv in källdata i cellerna i ett kalkylblad, lägg till pivottabellen på en destinationsposition och placera pivotfälten i rad-, kolumn- och dataområdena.
1. Lägg till data i ett kalkylblad med hjälp av metoden [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) i objektet [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Dessa data används som pivottabellens datakälla.
2. Lägg till en pivottabell på kalkylbladet genom att anropa metoden [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) i samlingen [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection): `Add(sourceData, row, column)`. `sourceData` är källintervallet (till exempel "A1:C8"); `row` och `column` är de 0-baserade koordinaterna för destinationscellen i pivottabellens övre vänstra hörn (cell E3 innebär rad 2, kolumn 4). Metoden returnerar det nya [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-objektet direkt.
3. Placera pivotfälten med metoden `AddFieldToArea` i objektet [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable): ett fältnamn placeras i radområdet (`PivotFieldType.Row`), kolumnområdet (`PivotFieldType.Column`) eller dataområdet (`PivotFieldType.Data`).
4. Spara arbetsboken – pivottabellen skrivs till den sparade filen.
En pivottabell läggs till i kalkylbladet när exempelkoden har körts.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Skapa en ny arbetsbok och hämta det första kalkylarket
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Skriv källdata: försäljning per sport och kvartal
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// Lägg till en pivottabell vid destinationscellen E3, med data från A1:C8
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// Tilldela pivotfält: Sport till Rader, Quarter till Kolumner, Sales till Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// Spara arbetsboken
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Om ett cellintervall tilldelas som datakälla måste det gå från den övre vänstra cellen till den nedre högra. "A1:C3" är till exempel ett giltigt intervall, men "C3:A1" är det inte.
{{% /alert %}}

## Relaterade artiklar
- [Lägg till filterfält i en pivottabell med Aspose.Cells for .NET](/cells/sv/net/add-page-field-in-pivot-table/)
- [Använd stilar på pivottabeller med Aspose.Cells for .NET](/cells/sv/net/apply-style-to-pivot-table/)
- [Ändra layouten för sidfält i en pivottabell](/cells/sv/net/change-page-field-layout/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/net/filter-by-label-or-value-of-pivot-table/)
- [Hantera värdefält i pivottabeller med Aspose.Cells for .NET](/cells/sv/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}