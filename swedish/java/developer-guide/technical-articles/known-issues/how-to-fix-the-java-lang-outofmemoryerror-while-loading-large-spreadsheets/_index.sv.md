---
title: Hur man åtgärdar java.lang.OutOfMemoryError vid inläsning av stora kalkylblad
type: docs
weight: 20
url: /sv/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

Det finns goda chanser att Arbetsbokskonstruktören kan kasta java.lang.OutOfMemoryError vid inläsning av stora kalkylblad. Detta undantag tyder på att det tillgängliga minnet är otillräckligt för att helt ladda kalkylbladet i minnet, därför måste kalkylbladet laddas medan [Minnespreferenser](/cells/sv/java/optimering-av-minnesanvandningen-vid-arbete-med-stora-filer-med-stora-datauppsattningar/) är aktiverade.

{{% /alert %}} 
## **Hur man åtgärdar java.lang.OutOfMemoryError vid inläsning av stora kalkylblad**
Aspose.Cells APIer tillhandahåller Minnesinställningar för att optimera minnesförbrukningen vid inläsning och bearbetning av kalkylblad. Dessa alternativ är också användbara för att effektivt ladda stora kalkylblad med stora datamängder i Workbook-objektet, som demonstreras nedan. 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
