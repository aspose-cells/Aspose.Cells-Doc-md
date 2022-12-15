---
title: Offentlig API Ändringar i Aspose.Cells 8.6.3
type: docs
weight: 230
url: /sv/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.6.2 till 8.6.3 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för HTML-tolkning vid import av data**
Den här versionen av Aspose.Cells for Java API har exponerat attributet ImportTableOptions.setHtmlString som styr API att tolka HTML-taggarna samtidigt som data importeras till kalkylbladet och ställer in det analyserade resultatet som cellvärde. Observera att API:er för Aspose.Cells redan tillhandahåller attributet Cell.setHtmlString för att utföra denna uppgift för en enskild cell, men vid massimport av data försöker attributet ImportTableOptions.setHtmlString (när det är satt till true) att analysera alla HTML-taggar och uppsättningar som stöds de analyserade resultaten till motsvarande celler.

Här är det enklaste användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Metod Workbook.createBuiltinStyle tillagd**
Aspose.Cells for Java 8.6.3 har exponerat metoden Workbook.createBuiltinStyle som kan användas för att skapa ett objekt av klassen Style som motsvarar en av[inbyggda stilar som erbjuds av Excel-applikationen](/cells/sv/java/using-built-in-styles/). Metoden Workbook.createBuiltinStyle accepterar en konstant från uppräkningen BuiltinStyleType. Observera att med tidigare utgåvor av API:erna Aspose.Cells kan samma uppgift utföras via metoden StyleCollection.createBuiltinStyle, men eftersom de senaste utgåvorna av Aspose.Cells API:er har tagit bort StyleCollection-klassen kan den nyligen exponerade metoden Workbook.createBuiltinStyle betraktas som en alternativ metod. uppnå detsamma.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Egenskap LoadDataOption.OnlyVisibleWorksheet har lagts till**
Aspose.Cells for Java 8.6.3 har avslöjat egenskapen LoadDataOption.OnlyVisibleWorksheet som vid inställning till true kommer att påverka laddningsmekanismen för Aspose.Cells for Java API, som ett resultat av detta kommer endast ett visst kalkylblad att vara synligt.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
## **Föråldrade API:er**
### **Metod Worksheet.copyConditionalFormatting föråldrad**
Som ett alternativ till metoden Worksheet.copyConditionalFormatting rekommenderar vi att du använder någon av metoderna Cells.copyRows eller Range.copy.
### **Fastighet Cells.Slut Föråldrad**
Använd egendomen Cells.LastCell som ett alternativ till egenskapen Cells.End.
