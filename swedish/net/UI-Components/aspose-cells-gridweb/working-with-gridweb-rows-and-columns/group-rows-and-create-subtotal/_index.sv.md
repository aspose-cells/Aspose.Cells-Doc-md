---
title: Gruppera rader och skapa delsumma
type: docs
weight: 70
url: /sv/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: Denna artikel introducerar hur man grupperar/ogrupperar rader/kolumner och hur man arbetar med delsummor i GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb kan skapa en översikt för dina data. Detta låter dig visa och dölja detaljnivåer genom att klicka på översiktsymbolerna "+" och "-" för att endast visa de rader som ger sammanfattningar eller rubriker för avsnitt i en arbetsbok. Du kan använda symbolerna för att se detaljer under en individuell sammanfattning eller rubrik.

Vid gruppering av rader är det viktigt att bara välja detaljrader som utgör gruppen. Inkludera inte relaterad sammanfattningsrad. Till exempel, om rad 6 innehåller totala data i rad 3 till 5, välj endast rad 3 till 5 för att definiera gruppen. Aspose.Cells.GridWeb-reglaget visar **visa detaljer** (+) och **dölj detaljer** (-) symboler bredvid radrubrikerna som anger grupperna i arbetsboken.

Aspose.Cells.GridWeb tillåter också att du skapar delsummer baserat på vilket som helst datafält. En delsumma är inte nödvändigtvis en summa: det kan vara en genomsnitt, räkning, minimum, maximum eller annan statistisk beräkning.

Detta ämne diskuterar gruppering av rader och skapande av delsummor med Aspose.Cells.GridWeb API. Utvecklare kan gruppera rader med vilken nivå av inbäddning som helst och skapa delsummor enkelt.

{{% /alert %}} 
## **Gruppering av rader**
För att gruppera ett visst antal rader:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i en webbformulär.
2. Hämta ett arbetsblad.
3. Välj det önskade antalet celler i rader.
4. Gruppera raderna.

När raderna är grupperade, visas en expandera/kollapsa-knapp i toppen av radernas sammanfattningsrad. Du kan ändra riktninginställningen. Egenskapen WebWorksheet.IsSummaryRowBelow är en Boolean-egenskap. Ställ in den på falskt (standard) så visas sammanfattningenraden ovanför detaljraderna. Ställ in den på sant så visas sammanfattningenraden nedanför detaljraderna. Klicka på expandera/kollapsa-knappen för att expandera eller kollapsa grupperade rader.

Följande exempel grupperar raderna från 2: a raden till 10: e raden.

**Gruppering av rader** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Inbäddning av grupperade rader**
Du kan skapa organisationens nivåer medan du grupperar en uppsättning rader. Du kan gruppera rader bland grupperade rader. Följande exempel visar inbäddning av grupperade rader.

**Gruppering av rader** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Intern process: Hur fungerar kontrolen?**
Varje rad i arket har ett översiktsnummer. Standardvärdet för översiktsnumret är noll. Varje gång du grupperar raderna ökar översiktsnumret med 1. Du kan hämta översiktsnumret genom att ringa GridWorksheet.Cells.GetRowOutlineLevel () -metoden.
## **Ogruppering av rader**
Aspose.Cells.GridWeb tillåter dig att koppla bort grupperade rader.

För att koppla bort ett visst antal rader:

1. Välj ett antal celler i raderna i arbetsbladet att koppla bort.
2. Koppla bort raderna.

Följande exempel kopplar bort raderna från 2: a raden till 10: e raden.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

När du ringer GridWorksheet.Cells.UngroupRows () -metoden sätts grupperade raders översiktsnummer till noll.

{{% /alert %}} 
## **Skapande av delsummer**
Kontrolens delsumma-funktion kan gruppera raderna i arket med en angiven kolumn och beräkna sammanfattningen av kolumnerna. Aspose.Cells.GridWeb kan automatiskt beräkna delsummovektor för en lista. När du genomför delsummor sammanfattar kontrolen listan så att du kan visa och dölja detaljraderna för varje delsumma. Innan du lägger till delsummer sortera på fältet du vill summera på. För att skapa delsummer, använd en version av överbelastad WebWorksheet.CreateSubtotal-metoden.



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **Parameterlista**

|**Nr.**|**Parameternamn**|**Beskrivning**|
| :- | :- | :- |
|1|columnNameRowIndex|Radens index för kolumnnamnet.|
|2|dataRows|Antalet datarader.|
|3|groupByColumnIndex|Kolumnens index som ska grupperas.|
|4|subtotalFunction|Summafunktionstypenumräkning.|
|5|subtotalColumnIndexList|Kolumnindexen för att summeras.|
### **Sammanfattningsfunktioner Lista**
Det finns flera typer av sammanfattningsfunktioner som stöds av {[SubtotalFunction}}-uppräkningen:

|**Nr.**|**Funktionsnamn**|**Beskrivning**|
| :- | :- | :- |
|1|AVERAGE|Beräknar medelvärdet av värdena.|
|2|COUNT|Räknar de numeriska värdena i cellerna.|
|3|COUNTA|Räknar de icke-numeriska datavärdena i cellerna.|
|4|MAX|Beräknar det största värdet.|
|5|MIN|Beräknar det minsta värdet.|
|6|PRODUCT|Beräknar produkten av värdena.|
|7|SUM|Beräknar summan av värdena.|
Följande exempel genererar sammanfattningarna som beräknar de icke-numeriska värdena grupperade efter den andra kolumnen i arbetsbladet.

**Sammanfattningar** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Ta bort delsumma**
För att ta bort en delsumma använder du metoden WebWorksheet.RemoveSubtotal. Följande exempel tar bort delsummeringarna.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **Om SUBTOTAL-funktionen**
GridWeb-kontrollen använder sig av formlafunktionen SUBTOTAL för att beräkna delsumman.

Syntax: SUBTOTAL(funktion_num, ref1, ref2, ...)

funktion_num är ett nummer som anger typen av funktion som används vid beräkning av delsumman.

|**1**|**MEDELVÄRDE**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1, ref2 är områden som ska summeras. Om ref1, ref2 etc. innehåller andra delsummeringsfunktioner, ignoreras de refererade cellerna för att undvika dubbelberäkning.
