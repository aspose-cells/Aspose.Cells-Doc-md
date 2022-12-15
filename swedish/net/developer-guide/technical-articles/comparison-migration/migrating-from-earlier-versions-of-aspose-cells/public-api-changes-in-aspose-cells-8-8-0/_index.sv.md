---
title: Offentlig API Ändringar i Aspose.Cells 8.8.0
type: docs
weight: 260
url: /sv/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.7.2 till 8.8.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Få Cell referenser för extern anslutning**
Aspose.Cells for .NET 8.8.0 har avslöjat följande nya egenskaper som är användbara för att hämta mål- och utdatacellreferenser för externa anslutningar lagrade i kalkylarket.

1. QueryTable.ConnectionId: Hämtar anslutnings-ID för frågetabellen.
1. ExternalConnection.Id: Hämtar ID för den externa anslutningen.
1. ListObject.QueryTable: Hämtar den länkade frågetabellen.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Hitta frågetabeller och listobjekt relaterade till externa dataanslutningar](/cells/sv/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Tillagd HTMLLoadOptions.KeepPrecision-egenskap**
Aspose.Cells for .NET 8.8.0 har lagt till egenskapen HTMLLoadOptions.KeepPrecision för att kontrollera konverteringen av långa numeriska värden till exponentiell notation vid import av HTML-filer. Som standard konverteras alla värden som är längre än 15 siffror till exponentiell notation om data importeras från HTML-sträng eller -fil. Men nu kan användarna kontrollera detta beteende med hjälp av HTMLLoadOptions.KeepPrecision-egenskapen. Om egenskapen är satt till true kommer värdena att importeras som de är i källan.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[ Undvik konvertering av stora numeriska värden till exponentiell notation](/cells/sv/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Tillagd HTMLLoadOptions.DeleteRedundantSpaces-egenskap**
Aspose.Cells for .NET 8.8.0 har avslöjat egenskapen HTMLLoadOptions.DeleteRedundantSpaces för att behålla eller ta bort de extra mellanslagen efter radbrytningstaggen (<br>Tag) medan du importerar data från HTML-strängen eller filen. Egenskapen HTMLLoadOptions.DeleteRedundantSpaces har standardvärdet som false, vilket betyder att alla extra mellanslag kommer att bevaras och importeras till Workbook-objektet, men när den är satt till true, kommer API att ta bort alla redundanta mellanslag som kommer efter radbrytningstaggen.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Ta bort redundanta mellanslag från HTML](/cells/sv/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Enkelt användningsscenario ser ut som följer.

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Tillagd Style.QuotePrefix-egenskap**
Aspose.Cells for .NET 8.8.0 har exponerat egenskapen Style.QuotePrefix för att upptäcka om ett cellvärde börjar med ett enda citattecken.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Upptäck enstaka offert i början av Cell-värde](/cells/sv/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Enkelt användningsscenario ser ut som följer.

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **Föråldrade API:er**
### **Föråldrad LoadOptions.ConvertNumericData Property**
Aspose.Cells 8.8.0 har markerat egenskapen LoadOptions.ConvertNumericData som föråldrad. Använd motsvarande egenskap från klasserna HTMLLoadOptions eller TxtLoadOptions.
