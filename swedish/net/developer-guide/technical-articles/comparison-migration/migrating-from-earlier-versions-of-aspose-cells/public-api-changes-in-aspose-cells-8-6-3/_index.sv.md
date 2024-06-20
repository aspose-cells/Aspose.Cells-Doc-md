---
title: Offentliga API ändringar i Aspose.Cells 8.6.3
type: docs
weight: 220
url: /sv/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.6.2 till 8.6.3 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för HTML-analys vid import av data**
Den här versionen av Aspose.Cells for .NET API har exponerat ImportTableOptions.IsHtmlString-egenskapen som styr att API:t ska analysera HTML-taggar vid import av data till kalkylbladet och sätta det analyserade resultatet som cellvärde. Observera, Aspose.Cells API:erna tillhandahåller redan Cell.HtmlString för att utföra denna uppgift för en enskild cell, men vid import av data i bulk såsom från en DataTable, försöker ImportTableOptions.IsHtmlString-egenskapen (när den är satt till true) att analysera alla stödda HTML-taggar och sätta de analyserade resultaten till motsvarande celler.

Här är det enklaste användningsscenario.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Tillagd Workbook.CreateBuiltinStyle-metod**
Aspose.Cells for .NET 8.6.3 har exponerat Workbook.CreateBuiltinStyle-metoden som kan användas för att skapa ett objekt av klassen Style som motsvarar en av de [inbyggda stilarna som erbjuds av Excel-applikationen](/cells/sv/net/using-built-in-styles/). Workbook.CreateBuiltinStyle-metoden accepterar en konstant från uppräkningen BuiltinStyleType. Observera, med tidigare versioner av Aspose.Cells API:erna kunde samma uppgift utföras via StyleCollection.CreateBuiltinStyle-metoden men eftersom de senaste versionerna av Aspose.Cells API:erna har tagit bort StyleCollection-klassen kan den nyexponerade Workbook.CreateBuiltinStyle-metoden betraktas som ett alternativt tillvägagångssätt för att uppnå samma resultat.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Tillagd Cells.ImportGridView-metod**
Aspose.Cells for .NET 8.6.3 har exponerat en överlagrad version av Cells.ImportGridView som nu kan acceptera en instans av ImportTableOptions för att ge mer kontroll över importprocessen.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Tillagd ImportTableOptions.ConvertGridStyle-egenskap**
I referens till ovanstående förbättringar har den senaste versionen av Aspose.Cells for .NET API också exponerat ImportTableOptions.ConvertGridStyle-egenskapen. Denna boolska egenskap låter utvecklarna kontrollera utseendet på den importerade datan, där setting ImportTableOptions.ConvertGridStyle-egenskapen till true indikerar att API:t kommer att tillämpa stilen från GridView på cellerna där data har importerats.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Egenskapen LoadDataOption.OnlyVisibleWorksheet tillagd**
Aspose.Cells for .NET 8.6.3 har exponerat LoadDataOption.OnlyVisibleWorksheet-egenskapen som, om den sätts till true, kommer att påverka laddningsmekanismen för Aspose.Cells for .NET API, som en följd av det kommer endast synliga kalkylblad från ett givet kalkylblad att laddas. Vänligen kolla [detaljerad artikel](/cells/sv/net/different-ways-to-open-files/) om detta ämne.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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
## **Obsoletterade API:er**
### **Föråldrad Worksheet.CopyConditionalFormatting-metod**
Som ett alternativ till Worksheet.CopyConditionalFormatting-metoden rekommenderas att använda antingen Cells.CopyRows eller Range.Copy-metoder.
### **Föråldrad Cells.End-egenskap**
Använd Cells.LastCell-egenskapen som ett alternativ till Cells.End-egenskapen.
