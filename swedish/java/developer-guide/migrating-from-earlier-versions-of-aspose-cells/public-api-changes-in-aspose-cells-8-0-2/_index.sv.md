---
title: Offentliga API ändringar i Aspose.Cells 8.0.2
type: docs
weight: 40
url: /sv/java/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringar i Aspose.Cells API från version 8.0.1 till 8.0.2, som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **TextDirection-egenskap tillagd till Shape-klassen**
Shape-klassen har exponerat TextDirection-egenskapen som kan användas för att hämta eller sätta riktningen för textflödet i Shape-objektet. TextDirection-egenskapen kan också användas för att ange önskad textriktning för kommentarer i en kalkylblad enligt nedan.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = sheet.getComments().add("F5");

Comment comment = sheet.getComments().get(commentIndex);

//Set its vertical alignment setting            

comment.getCommentShape().setTextVerticalAlignment(TextAlignmentType.CENTER);

//Set its horizontal alignment setting

comment.getCommentShape().setTextHorizontalAlignment(TextAlignmentType.RIGHT);

//Set the Text Direction - Right-to-Left

comment.getCommentShape().setTextDirection(TextDirectionType.RIGHT_TO_LEFT);

//Set the Comment note

comment.setNote("This is my Comment Text. This is test");

//Save the Excel file

book.save(myDir + "output.xlsx");

{{< /highlight >}}
## **ConvertFormulasData-egenskap tillagd till HTMLLoadOptions-klassen**
ConvertFormulasData-egenskapen har lagts till HTMLLoadOptions-klassen, för att underlätta för utvecklare att ladda Excel-formler från HTML-filer. Den booleska ConvertFormulasData-egenskapen indikerar om strängen ska konverteras till en formel när strängvärdet börjar med tecknet '=' eller inte.

**Java**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

Standardvärdet för ConvertFormulasData-egenskapen är falskt.

{{% /alert %}}
## **ImageOptions-egenskap tillagd till HtmlSaveOptions-klassen**
ImageOptions-egenskapen har lagts till HtmlSaveOptions-klassen. Genom att exponera ImageOptions-egenskapen har utvecklare möjlighet att ange inställningarna för bilderna som bäddas in i HTML vid export av kalkylblad. 
## **Obsoletade HtmlSaveOptions.ExportChartImageFormat-egenskapen**
HtmlSaveOptions.ExportChartImageFormat har markerats som föråldrad från och med Aspose.Cells for .NET 8.0.2. Det rekommenderas att istället använda HtmlSaveOptions.ImageOptions för inställningar för bildformat vid export av kalkylblad till HTML-format.
{{< app/cells/assistant language="java" >}}
