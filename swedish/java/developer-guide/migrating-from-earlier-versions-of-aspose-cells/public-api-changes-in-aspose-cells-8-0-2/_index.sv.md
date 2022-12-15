---
title: Offentlig API Ändringar i Aspose.Cells 8.0.2
type: docs
weight: 40
url: /sv/java/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringar av Aspose.Cells API från version 8.0.1 till 8.0.2, som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **TextDirection-egenskapen har lagts till i Shape Class**
Shape-klassen har exponerat egenskapen TextDirection som kan användas för att hämta eller ställa in textflödets riktning för Shape-objektet. Egenskapen TextDirection kan också användas för att ställa in önskad textriktning för kommentarerna i ett kalkylblad som visas nedan.

**Java**

{{< highlight "csharp" >}}

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
## **Lade till ConvertFormulasData Property till HTMLLoadOptions Class**
Egenskapen ConvertFormulasData har lagts till i HTMLLoadOptions-klassen för att göra det lättare för utvecklarna att ladda Excel-formler från HTML-filer. Den booleska egenskapen ConvertFormulasData anger om strängen ska konverteras till en formel eller inte när strängvärdet börjar med tecknet '='.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

Standardvärdet för egenskapen ConvertFormulasData är falskt.

{{% /alert %}}
## **Lade till ImageOptions-egenskapen i HtmlSaveOptions-klassen**
 ImageOptions-egenskapen har lagts till i klassen HtmlSaveOptions. Att exponera egenskapen ImageOptions har gjort det möjligt för utvecklarna att ställa in inställningarna för bilderna som är inbäddade i HTML-koden medan de exporterar kalkylblad.
## **Föråldrad HtmlSaveOptions.ExportChartImageFormat Property**
HtmlSaveOptions.ExportChartImageFormat har markerats som föråldrat från Aspose.Cells for .NET 8.0.2. Det rekommenderas att använda HtmlSaveOptions.ImageOptions istället för bildformatinställningar när du exporterar kalkylblad till HTML-format.
