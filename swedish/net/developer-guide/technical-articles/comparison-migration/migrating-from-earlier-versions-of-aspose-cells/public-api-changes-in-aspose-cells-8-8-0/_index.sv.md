---
title: Offentliga API ändringar i Aspose.Cells 8.8.0
type: docs
weight: 260
url: /sv/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.7.2 till 8.8.0 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Hämta Cellreferenser för extern anslutning**
Aspose.Cells for .NET 8.8.0 har exponerat följande nya egenskaper som är användbara för att hämta mål- och utdatacellreferenser för externa anslutningar som lagras i kalkylarket.

1. QueryTable.ConnectionId: Hämtar anslutnings-ID för frågetabellen.
1. ExternalConnection.Id: Hämtar ID för den externa anslutningen.
1. ListObject.QueryTable: Hämtar länkad frågetabell.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Hitta frågetabeller och listobjekt relaterade till externa dataanslutningar](/cells/sv/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Tillagt HTMLLoadOptions.KeepPrecision Egenskap**
Aspose.Cells for .NET 8.8.0 har lagt till HTMLLoadOptions.KeepPrecision-egenskapen för att kontrollera omvandlingen av långa numeriska värden till exponentiellt format vid import av HTML-filer. Som standard konverteras alla värden som är längre än 15 siffror till exponentiellt format om data importeras från HTML-sträng eller fil. Nu kan användarna dock kontrollera detta beteende med hjälp av HTMLLoadOptions.KeepPrecision-egenskapen. Om sagt egenskap är inställd på true kommer värdena att importeras i sin ursprungliga form.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Undvik konvertering av stora numeriska värden till exponentiellt format](/cells/sv/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Tillagt HTMLLoadOptions.DeleteRedundantSpaces Egenskap**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Ta bort överflödiga mellanslag från HTML](/cells/sv/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Enkelt användningsscenarie ser ut som följande.

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Tillagt Style.QuotePrefix Egenskap**
Aspose.Cells for .NET 8.8.0 har exponerat Style.QuotePrefix-egenskapen för att upptäcka om en cellvärde börjar med ett enda citattecken.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Upptäck enkelt citattecken i början av cellvärdet](/cells/sv/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Enkelt användningsscenarie ser ut som följande.

**C#**

{{< highlight csharp >}}

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
## **Obsoletterade API:er**
### **Föråldrad LoadOptions.ConvertNumericData Egenskap**
Aspose.Cells 8.8.0 har markerat LoadOptions.ConvertNumericData egenskapen som föråldrad. Vänligen använd motsvarande egenskap från klasserna HTMLLoadOptions eller TxtLoadOptions.
{{< app/cells/assistant language="csharp" >}}
