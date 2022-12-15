---
title: Offentlig API Ändringar i Aspose.Cells 8.1.0
type: docs
weight: 50
url: /sv/java/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringar av Aspose.Cells API från version 8.0.2 till 8.1.0, som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet Property har lagts till**
Klassen HtmlSaveOptions har exponerat egenskapen ExportHiddenWorksheet som kan användas för att ange om dolda kalkylblad exporteras till HTML-format. Standardvärdet är sant. medan om satt till false, kommer Aspose.Cells inte att exportera dolt kalkylbladsinnehåll.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Förhindra export av dolt kalkylblad](/cells/sv/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Lade till Cell.StringValueWithoutFormat Property**
 Egenskapen StringValueWithoutFormat har lagts till i klassen Cell för att göra det lättare för utvecklarna att hämta cellvärdet utan att använda någon formatering.

Nedan medföljande kodavsnitt visar användningen av Cell.getStringValueWithoutFormat-metoden jämfört med cell.getDisplayStringValue genom att skapa ett kalkylblad från grunden och tillämpa talformatet på en av cellerna.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Utmatningen av ovanstående kod är som följer

Formaterat strängvärde: 123 456
Oformaterat strängvärde: 123456

{{% /alert %}}
## **Föråldrade byte, tecken, tecken med mellanslag, rader, styckeegenskaper**
 Många fastigheter från klassen BuiltInDocumentPropertyCollection har märkts föråldrade från Aspose.Cells for .NET 8.1.0. Dessa egenskaper inkluderar Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. Anledningen är att ovannämnda egenskaper inte är till någon nytta för att konservera Excel-kalkylblad eftersom Excel utelämnar dem. Där dessa egenskaper ursprungligen skrevs för Word-dokument och PowerPoint presentationer.
