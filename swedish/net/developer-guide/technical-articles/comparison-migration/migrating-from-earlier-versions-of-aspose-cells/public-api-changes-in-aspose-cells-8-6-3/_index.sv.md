---
title: Offentliga API-ändringar i Aspose.Cells 8.6.3
type: docs
weight: 220
url: /sv/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.6.2 till 8.6.3 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för HTML-tolkning vid import av data**
Den här versionen av Aspose.Cells för .NET API har avslöjat egenskapen ImportTableOptions.IsHtmlString som styr API:et att tolka HTML-taggarna samtidigt som data importeras till kalkylbladet och ställer in det analyserade resultatet som cellvärde. Observera att Aspose.Cells API:er redan tillhandahåller Cell.HtmlString för att utföra den här uppgiften för en enskild cell, men samtidigt som man importerar data i bulk, t.ex. från en DataTable, försöker egenskapen ImportTableOptions.IsHtmlString (när den är satt till true) att analysera alla de stödda HTML taggar och ställer in de analyserade resultaten till motsvarande celler.

Här är det enklaste användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Metod Workbook.CreateBuiltinStyle tillagd**
 Aspose.Cells för .NET 8.6.3 har exponerat metoden Workbook.CreateBuiltinStyle som kan användas för att skapa ett objekt av klassen Style som motsvarar en av[inbyggda stilar som erbjuds av Excel-applikationen](/cells/sv/net/using-built-in-styles/)Metoden Workbook.CreateBuiltinStyle accepterar en konstant från uppräkningen BuiltinStyleType. Observera att med tidigare utgåvor av API:erna Aspose.Cells kan samma uppgift utföras via metoden StyleCollection.CreateBuiltinStyle, men eftersom de senaste utgåvorna av Aspose.Cells API:er har tagit bort StyleCollection-klassen kan den nyligen exponerade Workbook.CreateBuiltinStyle-metoden betraktas som en alternativ metod. uppnå detsamma.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Metod Cells.ImportGridView tillagd**
Aspose.Cells för .NET 8.6.3 har avslöjat en överbelastad version av Cells.ImportGridView som nu kan acceptera en instans av ImportTableOptions för att ge mer kontroll över importprocessen.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Property ImportTableOptions.ConvertGridStyle tillagd**
Som referens till de ovan nämnda förbättringarna har den senaste versionen av Aspose.Cells för .NET API också avslöjat egenskapen ImportTableOptions.ConvertGridStyle. Denna egenskap av boolesk typ tillåter utvecklarna att kontrollera utseendet på den importerade datan, där inställning av egenskapen ImportTableOptions.ConvertGridStyle till true indikerar att API:et kommer att tillämpa stilen för GridView på cellerna där data har importerats.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Egenskap LoadDataOption.OnlyVisibleWorksheet har lagts till**
 Aspose.Cells för .NET 8.6.3 har avslöjat egenskapen LoadDataOption.OnlyVisibleWorksheet som vid inställning till true kommer att påverka laddningsmekanismen för Aspose.Cells för .NET API, som ett resultat kommer endast synliga kalkylblad från ett givet kalkylblad att laddas. Vänligen kontrollera[detaljerad artikel](/cells/sv/net/different-ways-to-open-files/) på det här ämnet.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Föråldrade API:er**
### **Metod Worksheet.CopyConditionalFormatting föråldrad**
Som ett alternativ till metoden Worksheet.CopyConditionalFormatting rekommenderar vi att du använder någon av metoderna Cells.CopyRows eller Range.Copy.
### **Fastighet Cells.Slut Föråldrad**
Använd egendomen Cells.LastCell som ett alternativ till egenskapen Cells.End.
