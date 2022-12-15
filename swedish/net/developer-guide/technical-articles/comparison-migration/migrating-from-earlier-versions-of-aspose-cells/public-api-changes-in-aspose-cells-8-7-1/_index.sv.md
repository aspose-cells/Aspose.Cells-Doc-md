---
title: Offentlig API Ändringar i Aspose.Cells 8.7.1
type: docs
weight: 240
url: /sv/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.7.0 till 8.7.1 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Lade till LookInType.OriginalValues-egenskap**
 Aspose.Cells API:er stöder redan[Hitta eller sök data](/cells/sv/net/find-or-search-data/)funktion för kalkylblad för att hitta ett visst innehåll i cellvärde och formel. Den här funktionen saknade dock aspekten av formatering som applicerades på cellen som kan ändra utseendet såväl som värdet på innehållet, vilket gör texten osökbar med det ursprungliga värdet. Med denna utgåva av Aspose.Cells API:er har en annan konstant vid namn LookInType.OriginalValues exponerats för allmänheten API vilket gör det möjligt att övervinna situationen som diskuterats ovan.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Sök efter data med hjälp av ursprungliga värden](/cells/sv/net/search-data-using-original-values/)

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

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


### **Lade till OnBeforeColumnFilter Event för GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.1 har avslöjat händelsen OnBeforeColumnFilter som fungerar som återuppringning till filtreringsmekanismen som görs via GridWeb UI. Som namnet antyder utlöses händelsen innan kolumnfiltreringen tillämpas och kan användas för att få filtreringsinformation som kolumnindex och värde på vilket filter måste tillämpas.

Enkelt användningsscenario ser ut som följer.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Glöm inte att registrera evenemanget till GridWeb control<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
