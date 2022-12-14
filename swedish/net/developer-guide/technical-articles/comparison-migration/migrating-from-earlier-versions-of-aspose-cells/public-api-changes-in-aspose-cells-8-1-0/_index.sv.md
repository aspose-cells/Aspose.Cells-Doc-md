---
title: Offentliga API-ändringar i Aspose.Cells 8.1.0
type: docs
weight: 40
url: /sv/net/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringar av Aspose.Cells API från version 8.0.2 till 8.1.0, som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet Property har lagts till**
Klassen HtmlSaveOptions har exponerat egenskapen ExportHiddenWorksheet som kan användas för att ange om dolda kalkylblad exporteras till HTML-format. Standardvärdet är sant. medan om satt till false, kommer Aspose.Cells inte att exportera dolt kalkylbladsinnehåll.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Förhindra export av dolt kalkylblad](/cells/sv/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Lade till Cell.StringValueWithoutFormat Property**
Egenskapen StringValueWithoutFormat har lagts till i klassen Cell för att göra det lättare för utvecklarna att hämta cellvärdet utan att använda någon formatering.

Nedan medföljande kodavsnitt visar användningen av Cell.StringValueWithoutFormat-egenskapen jämfört med cell.DisplayStringValue genom att skapa ett kalkylblad från början och tillämpa talformatet på en av cellerna.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Utmatningen av ovanstående kod är som följer

123,456

123456

{{% /alert %}}
## **Föråldrade byte, tecken, tecken med mellanslag, rader, styckeegenskaper**
Många egenskaper från klassen BuiltInDocumentPropertyCollection har markerats som föråldrade från Aspose.Cells för .NET 8.1.0. Dessa egenskaper inkluderar Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. Anledningen är att ovannämnda egenskaper inte är till någon nytta för att konservera Excel-kalkylblad eftersom Excel utelämnar dem. Där dessa egenskaper ursprungligen skrevs för Word-dokument och PowerPoint-presentationer.
