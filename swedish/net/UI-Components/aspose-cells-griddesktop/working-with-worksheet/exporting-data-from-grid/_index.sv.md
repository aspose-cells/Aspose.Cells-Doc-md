---
title: Exportera data från Grid
type: docs
weight: 60
url: /sv/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

vårt tidigare ämne har vi pratat om att importera innehållet i en DataTable till Aspose.Cells.GridDesktop-kontroll men vi nämnde inte medvetet att Aspose.Cells.GridDesktop också stöder den omvända processen. Så i det här ämnet kommer vi att diskutera om att exportera data inuti Aspose.Cells.GridDesktop-kontroll till en DataTable.

{{% /alert %}} 
## **Exportera rutinnehåll**
### **Exportera till en specifik datatabell**
 För att exportera Grid-innehållet till ett specifikt DataTable-objekt, följ stegen nedan: Lägg till Aspose.Cells.GridDesktop-kontroll till din**Form**.

- Skapa ett specifikt DataTable-objekt enligt dina behov.
-  Exportera data för en vald**Arbetsblad** till ditt angivna DataTable-objekt.

I exemplet nedan har vi skapat ett specifikt DataTable-objekt med fyra kolumner inuti. Slutligen exporterade vi kalkylbladsdata (med början från första cellen med 69 rader och 4 kolumner) till ett DataTable-objekt som redan skapats av oss.

**Exempel:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exportera till en ny datatabell**
Ibland kanske utvecklare inte är intresserade av att skapa sitt eget DataTable-objekt och kan ha ett enkelt behov av att bara exportera kalkylbladsdata till ett nytt DataTable-objekt. Det skulle vara det snabbaste sättet för utvecklarna att bara exportera kalkylbladsdata.

I exemplet nedan har vi försökt ett annat sätt att förklara användningen av ExportDataTable-metoden. Vi har tagit referensen till det kalkylblad som för närvarande är aktivt och sedan exporterade vi hela data från det aktiva kalkylbladet till ett nytt DataTable-objekt. Nu kan detta DataTable-objekt användas på vilket sätt en utvecklare vill. Bara för ett exempel kan en utvecklare binda detta DataTable-objekt till ett DataGrid för att se data.

**Exempel:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

I ovanstående fall kommer vi att använda en överbelastad version av ExportDataTable-metoden som helt enkelt returnerar ett nytt DataTable-objekt som innehåller data som exporterats från kalkylbladet.

{{% /alert %}}
