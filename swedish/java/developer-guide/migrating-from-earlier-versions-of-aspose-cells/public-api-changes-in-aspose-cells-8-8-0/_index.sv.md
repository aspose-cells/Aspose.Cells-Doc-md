---
title: Offentlig API Ändringar i Aspose.Cells 8.8.0
type: docs
weight: 270
url: /sv/java/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.7.2 till 8.8.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Få Cell referenser för extern anslutning**
 Aspose.Cells for Java 8.8.0 har avslöjat följande nya egenskaper som är användbara för att hämta mål- och utdatacellreferenser för externa anslutningar lagrade i kalkylarket.

1. QueryTable.ConnectionId: Hämtar anslutnings-ID för frågetabellen.
1. ExternalConnection.Id: Hämtar ID för den externa anslutningen.
1. ListObject.QueryTable: Hämtar den länkade frågetabellen.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Hitta frågetabeller och listobjekt relaterade till externa dataanslutningar](/cells/sv/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Tillagd HTMLLoadOptions.KeepPrecision-egenskap**
Aspose.Cells for Java 8.8.0 har lagt till egenskapen HTMLLoadOptions.KeepPrecision för att kontrollera konverteringen av långa numeriska värden till exponentiell notation vid import av HTML-filer. Som standard konverteras alla värden som är längre än 15 siffror till exponentiell notation om data importeras från HTML sträng eller fil. Men nu kan användarna kontrollera detta beteende med hjälp av HTMLLoadOptions.KeepPrecision-egenskapen. Om egenskapen är satt till true kommer värdena att importeras som de är i källan.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[ Undvik konvertering av stora numeriska värden till exponentiell notation](/cells/sv/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

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
### **Tillagd HTMLLoadOptions.DeleteRedundantSpaces-egenskap**
Aspose.Cells for Java 8.8.0 har avslöjat egenskapen HTMLLoadOptions.DeleteRedundantSpaces för att behålla eller ta bort de extra mellanslagen efter radbrytningstaggen (<br>Tag) medan du importerar data från HTML-strängen eller filen. Egenskapen HTMLLoadOptions.DeleteRedundantSpaces har standardvärdet som false, vilket betyder att alla extra mellanslag kommer att bevaras och importeras till Workbook-objektet, men när den är satt till true, kommer API att ta bort alla redundanta mellanslag som kommer efter radbrytningstaggen.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Ta bort redundanta mellanslag från HTML](/cells/sv/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

 Enkelt användningsscenario ser ut som följer.

**Java**

{{< highlight "csharp" >}}

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

byte[]byteArray = html.getBytes();

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
### **Tillagd Style.QuotePrefix-egenskap**
 Aspose.Cells for Java 8.8.0 har exponerat egenskapen Style.QuotePrefix för att upptäcka om ett cellvärde börjar med ett enda citattecken.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Upptäck enstaka offert i början av Cell-värde](/cells/sv/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

 Enkelt användningsscenario ser ut som följer.

**Java**

{{< highlight "csharp" >}}

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
## **Föråldrade API:er**
### **Föråldrad LoadOptions.ConvertNumericData Property**
Aspose.Cells 8.8.0 har markerat egenskapen LoadOptions.ConvertNumericData som föråldrad. Använd motsvarande egenskap från klasserna HTMLLoadOptions eller TxtLoadOptions.
