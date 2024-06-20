---
title: Offentliga API ändringar i Aspose.Cells 8.1.0
type: docs
weight: 50
url: /sv/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringar i Aspose.Cells API från version 8.0.2 till 8.1.0, som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **TextDirection-egenskapen har lagts till Formklassen**
Klassen HtmlSaveOptions har exponerat ExportHiddenWorksheet-egenskapen som kan användas för att ange om dolda arbetsblad exporteras till HTML-format. Standardvärdet är sant. Om det är satt till falskt, kommer inte Aspose.Cells att exportera innehållet i dolda arbetsblad.

{{% alert color="primary" %}} 

Vänligen kontrollera den detaljerade artikeln om [Förhindra export av dolt arbetsblad](/cells/sv/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **StringValueWithoutFormat-egenskapen har lagts till Cell-klassen, för att underlätta för utvecklare att hämta cellvärdet utan formateringar.**
Nedan visas ett kodsnutt som visar användningen av Cell.StringValueWithoutFormat-egenskapen jämfört med cell.DisplayStringValue genom att skapa ett kalkylblad från grunden och tillämpa nummerformat på en av cellerna. 

Nedan medföljer kodsnutten som demonstrerar användningen av Cell.getStringValueWithoutFormat-metoden jämfört med cell.getDisplayStringValue genom att skapa en kalkyl från grunden och tillämpa nummerformatet på en av cellerna. 

**Java**

{{< highlight csharp >}}

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

Resultatet av ovanstående kod är följande

Formaterat strängvärde: 123,456
Oformaterat strängvärde: 123456

{{% /alert %}}
## **Föråldrade Bytes, Tecken, TeckenMedMellanslag, Rader, Stycken Egenskaper**
Många egenskaper från BuiltInDocumentPropertyCollection-klassen har markerats föråldrade från Aspose.Cells for .NET 8.1.0. Dessa egenskaper inkluderar Bytes, Tecken, TeckenMedMellanslag, Rader & Stycken. Anledningen är att ovanstående egenskaper inte är användbara för att bevara Excel-kalkylblad eftersom Excel exkluderar dem. Dessa egenskaper var ursprungligen skrivna för Word-dokument & PowerPoint-presentationer. 
