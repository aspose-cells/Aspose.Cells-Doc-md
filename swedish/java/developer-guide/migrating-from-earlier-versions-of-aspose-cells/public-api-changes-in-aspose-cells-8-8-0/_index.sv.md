---
title: Offentliga API ändringar i Aspose.Cells 8.8.0
type: docs
weight: 270
url: /sv/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.7.2 till 8.8.0 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Hämta Cellreferenser för extern anslutning**
Aspose.Cells for Java 8.8.0 har exponerat följande nya egenskaper som är användbara för att hämta mål- och utdatacellreferenser för externa anslutningar som lagras i kalkylarket. 

1. QueryTable.ConnectionId: Hämtar anslutnings-ID för frågetabellen.
1. ExternalConnection.Id: Hämtar ID för den externa anslutningen.
1. ListObject.QueryTable: Hämtar länkad frågetabell.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Hitta Frågetabeller och Listobjekt relaterade till externa dataanslutningar](/cells/sv/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Tillagt HTMLLoadOptions.KeepPrecision Egenskap**
Aspose.Cells for Java 8.8.0 har lagt till HTMLLoadOptions.KeepPrecision egenskapen för att kontrollera konverteringen av långa numeriska värden till exponentiell notation vid import av HTML-filer. Som standard konverteras alla värden längre än 15 siffror till exponentiell notation om datan importeras från HTML-sträng eller fil. Nu kan användarna dock kontrollera detta beteende med hjälp av HTMLLoadOptions.KeepPrecision egenskapen. Om den aktuella egenskapen är satt till true kommer värdena att importeras som de är från källan.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Undvik Konvertering av Stora Numeriska Värden till Exponentiell Notation](/cells/sv/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Tillagt HTMLLoadOptions.DeleteRedundantSpaces Egenskap**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Radera Överflödiga Mellanrum från HTML](/cells/sv/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Enkelt användningsscenarie ser ut som följande. 

**Java**

{{< highlight csharp >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Tillagt Style.QuotePrefix Egenskap**
Aspose.Cells for Java 8.8.0 har exponerat Style.QuotePrefix egenskapen för att upptäcka om en cellvärde börjar med ett enkelt citattecken. 

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Upptäcka Enkelt Citattecken i Början av Cellvärde](/cells/sv/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Enkelt användningsscenarie ser ut som följande. 

**Java**

{{< highlight csharp >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **Obsoletterade API:er**
### **Föråldrad LoadOptions.ConvertNumericData Egenskap**
Aspose.Cells 8.8.0 har markerat LoadOptions.ConvertNumericData egenskapen som föråldrad. Vänligen använd motsvarande egenskap från klasserna HTMLLoadOptions eller TxtLoadOptions.
{{< app/cells/assistant language="java" >}}
