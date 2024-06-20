---
title: Offentliga API ändringar i Aspose.Cells 8.6.3
type: docs
weight: 230
url: /sv/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.6.2 till 8.6.3 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för HTML-analys vid import av data**
Denna version av Aspose.Cells for Java API har exponerat attributet ImportTableOptions.setHtmlString som dirigerar API:et att analysera HTML-taggar vid import av data till kalkylbladet och sätta det analyserade resultatet som cellvärde. Observera att Aspose.Cells API:er redan tillhandahåller attributet Cell.setHtmlString för att utföra denna uppgift för en enskild cell, men vid import av data i bulk försöker attributet ImportTableOptions.setHtmlString (när det är satt till true) att analysera alla stödda HTML-taggar och sätter de analyserade resultaten till de motsvarande cellerna.

Här är det enklaste användningsscenario.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Tillagd Workbook.createBuiltinStyle-metod**
Aspose.Cells for Java 8.6.3 har exponerat Workbook.createBuiltinStyle-metoden som kan användas för att skapa ett objekt av klassen Style som motsvarar en av [inbyggda stilar som erbjuds av Excel-applikationen](/cells/sv/java/using-built-in-styles/). Workbook.createBuiltinStyle-metoden accepterar en konstant från uppräkningen BuiltinStyleType. Observera att med tidigare versioner av Aspose.Cells API:er kunde samma uppgift åstadkommas via metoden StyleCollection.createBuiltinStyle men eftersom de senaste versionerna av Aspose.Cells API:er har tagit bort klassen StyleCollection kan den nyexponerade Workbook.createBuiltinStyle-metoden betraktas som ett alternativt tillvägagångssätt för att uppnå samma sak.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Tillagd LoadDataOption.OnlyVisibleWorksheet-egenskap**
Aspose.Cells for Java 8.6.3 har exponerat LoadDataOption.OnlyVisibleWorksheet-egenskapen som vid inställning till true kommer att påverka laddningsmekanismen för Aspose.Cells for Java API, som ett resultat kommer endast synliga kalkylblad från en given kalkylblad att laddas.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Obsoletterade API:er**
### **Föråldrad Worksheet.copyConditionalFormatting-metod**
Som ett alternativ till Worksheet.copyConditionalFormatting-metoden rekommenderas att använda någon av Cells.copyRows eller Range.copy-metoderna.
### **Föråldrad Cells.End-egenskap**
Använd Cells.LastCell-egenskapen som ett alternativ till Cells.End-egenskapen.
