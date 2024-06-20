---
title: Exportera data från Rutnät
type: docs
weight: 60
url: /sv/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop, export, data, exportera data
description: Den här artikeln introducerar hur man exporterar data i GridDesktop.
---

{{% alert color="primary" %}} 

I vårt tidigare ämne har vi talat om att importera innehållet i en DataTable till Aspose.Cells.GridDesktop-kontrollen, men vi nämnde medvetet inte att Aspose.Cells.GridDesktop också stöder omvänd process. Så i det här ämnet kommer vi att diskutera att exportera data inne i Aspose.Cells.GridDesktop-kontrollen till en DataTable.

{{% /alert %}} 
## **Exportera Rutnätsinnehåll**
### **Exportera till en specifik DataTable**
För att exportera Rutnätsinnehållet till en specifik DataTable-objekt, följ stegen nedan: Lägg till Aspose.Cells.GridDesktop-kontrollen på din **Form**.

- Skapa ett specifikt DataTable-objekt enligt dina behov.
- Exportera data från ett valt **Arbetsblad** till ditt angivna DataTable-objekt.

I det givna exemplet nedan har vi skapat ett specifikt DataTable-objekt med fyra kolumner inuti. Slutligen exporterade vi arbetsbladsdata (börjar från första cellen med 69 rader och 4 kolumner) till ett DataTable-objekt som redan skapats av oss.

**Exempel:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exportera till en ny DataTable**
Ibland kanske utvecklare inte är intresserade av att skapa sitt eget DataTable-objekt och bara har ett enkelt behov av att exportera arbetsbladsdata till ett nytt DataTable-objekt. Det skulle vara det snabbaste sättet för utvecklare att bara exportera arbetsbladsdata.

I det givna exemplet nedan har vi försökt på ett annorlunda sätt att förklara användningen av ExportDataTable-metoden. Vi har tagit referensen till arbetsbladet som för närvarande är aktivt och sedan exporterade vi all data från det aktiva arbetsbladet till ett nytt DataTable-objekt. Nu kan detta DataTable-objekt användas på vilket sätt som helst en utvecklare vill. Bara som ett exempel kan en utvecklare binda detta DataTable-objekt till en DataGrid för att visa data.

**Exempel:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

I det ovanstående fallet kommer vi att använda en överlagd version av ExportDataTable-metoden som helt enkelt kommer att returnera ett nytt DataTable-objekt innehållande data som exporterats från arbetsbladet.

{{% /alert %}}
