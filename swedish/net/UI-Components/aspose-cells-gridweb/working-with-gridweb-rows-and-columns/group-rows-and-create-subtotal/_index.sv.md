---
title: Gruppera rader och skapa delsumma
type: docs
weight: 70
url: /sv/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb kan skapa en disposition för dina data. Detta låter dig visa och dölja detaljnivåer genom att klicka på kontursymbolerna "+" och "-" för att endast visa de rader som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad. Du kan använda symbolerna för att se detaljer under en enskild sammanfattning eller rubrik.

När du grupperar rader är det viktigt att endast välja de detaljrader som utgör gruppen. Inkludera inte den relaterade sammanfattningsraden. Till exempel, om rad 6 innehåller summor för data i rad 3 till 5, välj endast rad 3 till 5 för att definiera gruppen. Kontrollen Aspose.Cells.GridWeb visar**visa detaljer** (+) och**dölja detaljer** (-) symboler bredvid radrubrikerna som anger grupperna i kalkylbladet.

Aspose.Cells.GridWeb låter dig också skapa delsummor baserat på vilket datafält som helst. En delsumma är inte nödvändigtvis en summa: Det kan vara ett medelvärde, antal, minimum, maximum eller annan statistisk beräkning.

Det här ämnet diskuterar gruppering av rader och skapa delsummor med hjälp av Aspose.Cells.GridWeb API. Utvecklare kan gruppera rader med valfri kapslingsnivå och enkelt skapa delsummor.

{{% /alert %}} 
## **Gruppera rader**
Så här grupperar du ett specifikt antal rader:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär.
1. Få tillgång till ett arbetsblad.
1. Välj önskat antal celler i rader.
1. Gruppera raderna.

När raderna är grupperade visas en expandera/komprimera-knapp överst på radernas sammanfattningsrad. Du kan ändra riktningsinställningen. Egenskapen WebWorksheet.IsSummaryRowBelow är en boolesk egenskap. Ställ in den på false (standard) och sammanfattningsraden kommer att vara ovanför detaljraderna. Ställ in den på sant så kommer sammanfattningsraden att vara under detaljraderna. Klicka på knappen expandera/komprimera för att expandera eller komprimera grupperade rader.

Följande exempel grupperar raderna från 2:a raden till 10:e raden.

**Gruppera rader** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Häckande grupperade rader**
Du kan skapa organisationsnivåer samtidigt som du grupperar en uppsättning rader. Du kan gruppera rader bland de grupperade raderna. Följande exempel visar kapslade grupperade rader.

**Gruppera rader** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Intern process: Hur fungerar kontrollen?**
Varje rad på arket har ett konturnummer. Standardvärdet för konturnumret är noll. Varje gång du grupperar raderna, ökas dispositionsnumret med 1. Du kan få dispositionsnumret genom att anropa metoden GridWorksheet.Cells.GetRowOutlineLevel().
## **Dela upp rader**
Aspose.Cells.GridWeb låter dig dela upp grupperade rader.

Så här avgrupperar du ett visst antal rader:

1. Välj ett antal celler i raderna i kalkylbladet för att avgruppera.
1. Dela upp raderna.

Följande exempel delar upp raderna från 2:a raden till 10:e raden.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

När du anropar metoden GridWorksheet.Cells.UngroupRows() sätts konturnummer för grupperade rader till noll.

{{% /alert %}} 
## **Skapar delsumma**
Kontrollens delsummafunktion kan gruppera raderna i arket med en specificerad kolumn och beräkna sammanfattningen av kolumnerna. Aspose.Cells.GridWeb kan automatiskt beräkna delsumma för en lista. När du implementerar delsummor, skisserar kontrollen listan så att du kan visa och dölja detaljraderna för varje delsumma. Innan du lägger till delsummor, sortera på fältet du vill lägga till delsummor på. För att skapa delsummor, använd valfri version av den överbelastade metoden WebWorksheet.CreateSubtotal.



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **Parameterlista**

|**Nej.**|**Parameternamn**|**Beskrivning**|
|:- |:- |:- |
|1|columnNameRowIndex|Radindexet för kolumnnamnsraden.|
|2|datarader|Antalet datarader.|
|3|groupByColumnIndex|Kolumnindexet för den kolumn som ska grupperas.|
|4|subtotalFunktion|Uppräkning av subtotalfunktionstyp.|
|5|subtotalColumnIndexList|Kolumnindexen som ska subtotaleras.|
### **Sammanfattningsfunktionslista**
Det finns flera typer av sammanfattningsfunktioner som stöds av {[SubtotalFunction}}-uppräkningen:

|**Nej.**|**Funktionsnamn**|**Beskrivning**|
|:- |:- |:- |
|1|MEDEL|Beräknar medelvärdet av värdena.|
|2|RÄKNA|Räknar de numeriska värdena i cellerna.|
|3|COUNTA|Räknar icke-numeriska data i cellerna.|
|4|MAX|Beräknar det största värdet.|
|5|MIN|Beräknar det minsta värdet.|
|6|PRODUKT|Beräknar produkten av värdena.|
|7|BELOPP|Beräknar summan av värdena.|
Följande exempel genererar delsummorna som beräknar de icke-numeriska värdena grupperade efter den andra kolumnen i kalkylbladet.

**Delsummor** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Tar bort delsumma**
För att ta bort en delsumma, använd metoden WebWorksheet.RemoveSubtotal. Följande exempel tar bort delsummorna.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **Om funktionen SUBTOTAL**
GridWeb-kontrollen använder formelfunktionen SUBTOTAL för att beräkna delsumman.

Syntax: SUBTOTAL(funktionsnummer, ref1, ref2, ...)

function_num är ett tal som anger typen av funktion som används vid beräkning av delsumman.

|**1**|**MEDEL**|
|:- |:- |
|2|RÄKNA|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUKT|
|7|BELOPP|
ref1, ref2, är de områden som ska subtotalas. Om ref1, ref2, ... innehåller andra subtotalfunktioner ignoreras de refererade cellerna för att undvika dubbletter av beräkningar.
