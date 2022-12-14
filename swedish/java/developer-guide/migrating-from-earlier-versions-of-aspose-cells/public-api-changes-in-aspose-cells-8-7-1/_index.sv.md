---
title: Offentliga API-ändringar i Aspose.Cells 8.7.1
type: docs
weight: 250
url: /sv/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.7.0 till 8.7.1 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Lade till LookInType.ORIGINAL_VALUES-egenskap**
 Aspose.Cells API:er stöder redan[Hitta eller sök data](/cells/sv/java/find-or-search-data/)funktion för kalkylblad för att hitta ett visst innehåll i cellvärde och formel. Den här funktionen saknade dock aspekten av formatering som applicerades på cellen som kan ändra utseendet såväl som värdet på innehållet, vilket gör texten osökbar med det ursprungliga värdet. Med denna utgåva av Aspose.Cells API:er har en annan konstant vid namn LookInType.ORIGINAL_VALUES exponerats för det offentliga API:et som gör det möjligt att övervinna situationen som diskuterats ovan.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Sök efter data med hjälp av ursprungliga värden](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
