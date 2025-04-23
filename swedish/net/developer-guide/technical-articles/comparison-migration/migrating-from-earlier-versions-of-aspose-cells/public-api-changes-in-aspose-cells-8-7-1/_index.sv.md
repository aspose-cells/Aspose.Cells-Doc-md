---
title: Förändringar i offentligt API i Aspose.Cells 8.7.1
type: docs
weight: 240
url: /sv/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Det här dokumentet beskriver förändringarna i Aspose.Cells API från version 8.7.0 till 8.7.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda & borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Lagt till LookInType.OriginalValues Egenskap**
Aspose.Cells API:er stöder redan [Sök eller Sök Data](/cells/sv/net/find-or-search-data/) funktionen för kalkylblad för att hitta något speciellt innehåll i cellvärde & formel. Dock saknade denna funktion aspekten på formatering som tillämpades på cellen som kan ändra utseendet samt värdet på innehållet, följaktligen gör texten osoekbar med det ursprungliga värdet. Med denna version av Aspose.Cells API:er har en annan konstant vid namn LookInType.OriginalValues exponerats till den offentliga API: n vilket tillåter att övervinna situationen som diskuterats ovan.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Sök Data Med Ursprungliga Värden](/cells/sv/net/search-data-using-original-values/)

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **Lagt till OnBeforeColumnFilter Händelse för GridWeb**
Aspose.Cells.GridWeb för .NET 8.7.1 har exponerat OnBeforeColumnFilter händelsen som fungerar som återkoppling till filtermekanismen som utförs genom GridWeb UI. Som namnet antyder aktiveras händelsen innan kolumnfiltreringen tillämpas och kan användas för att få information om filtrering såsom kolumnindex och värde på vilket filter ska appliceras.

Enkelt användningsscenarie ser ut som följande.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
