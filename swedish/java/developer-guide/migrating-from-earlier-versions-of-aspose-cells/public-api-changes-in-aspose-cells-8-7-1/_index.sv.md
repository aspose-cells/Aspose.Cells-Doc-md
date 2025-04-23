---
title: Förändringar i offentligt API i Aspose.Cells 8.7.1
type: docs
weight: 250
url: /sv/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Det här dokumentet beskriver förändringarna i Aspose.Cells API från version 8.7.0 till 8.7.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda & borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Tillagt LookInType.ORIGINAL_VALUES-egenskap**
Aspose.Cells API:er stöder redan [Hitta eller Sök Data](/cells/sv/java/find-or-search-data/) -funktionen för kalkylblad för att kunna hitta en specifik del av innehållet i cellvärde och formel. Dock saknades denna funktion aspekten av formatering som används på cellen som kan ändra utseendet samt värdet på innehållet och därmed göra texten omöjlig att söka med originalvärdet. Med denna version av Aspose.Cells API:er, har en annan konstant med namnet LookInType.ORIGINAL_VALUES exponerats i den offentliga API:n vilket tillåter att övervinna situationen som diskuteras ovan. 

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Sök Data Med Originalvärden](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
