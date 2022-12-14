---
title: Så här åtgärdar du java.lang.OutOfMemoryError när du laddar stora kalkylblad
type: docs
weight: 20
url: /sv/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

 Det finns rimliga chanser att Workbook-konstruktören kan kasta java.lang.OutOfMemoryError när stora kalkylblad laddas. Detta undantag tyder på att det tillgängliga minnet är otillräckligt för att fullständigt ladda kalkylarket i minnet, därför måste kalkylarket laddas samtidigt som du aktiverar[Minnesinställningar](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Så här fixar du java.lang.OutOfMemoryError när du laddar ett stort kalkylblad**
Aspose.Cells API:er tillhandahåller minnesinställningar för att optimera minnesförbrukningen när du laddar och bearbetar kalkylblad. Dessa alternativ är också användbara för att effektivt ladda de stora kalkylbladen som innehåller enorma datamängder i Workbook-objektet som visas nedan.

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
