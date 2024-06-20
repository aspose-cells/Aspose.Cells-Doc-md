---
title: Frågor och svar
type: docs
weight: 100
url: /sv/net/faq/
---

## **Hur man åtgärdar System.StackOverFlowException på Workbook.CalculateFormula?**
Ibland stöter användare på System.StackOverFlowException på metoden Workbook.CalculateFormula. Detta undantag inträffar vanligtvis eftersom standardstackens storlek för IIS är för liten (endast 265k). Du kan åtgärda detta fel genom att skapa en annan tråd med ökad stackstorlek och sedan flytta din Workbook.CalculateFormula-relaterade kod inuti den.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Tjocklek av linjer problem vid renderande Excel till PDF**
Ibland, när Excel-filen konverteras till PDF, är tjockleken på linjerna annorlunda i den resulterande PDFen. Detta problem orsakas inte av Aspose.Cells. Det beror på **Adobe Reader** när dess inställningar **"Jämn linjekonst"** och **"Förbättra tunna linjer"** är markerade. Att avmarkera dessa alternativ kommer att visa PDFen korrekt.

Om du markerar **"Jämn linjekonst"** och **"Förbättra tunna linjer"**, är tjockleken på linjerna annorlunda. Se följande steg hur det görs:

- Gå till **Redigera**
- Välj **Preferenser**
- I **Sidvisning**-kategori, markera **"Jämn linjekonst"** och **"Förbättra tunna linjer"**

Om du avmarkerar **"Jämn linjekonst"** och **"Förbättra tunna linjer"**, är tjockleken på linjerna densamma. För att uppnå detta följ bara stegen nedan:

- Gå till **Redigera**
- Välj **Preferenser**
- I **Sidvisning**-kategori, avmarkera **"Jämn linjekonst"** och **"Förbättra tunna linjer"**
## **Hur man åtgärdar System.OutOfMemoryException vid inläsning av stora kalkylblad?**
Det finns goda chanser att Workbook-konstruktören kan kasta System.OutOfMemoryException vid inläsning av stora kalkylblad. Detta undantag tyder på att tillgängligt minne är otillräckligt för att helt ladda kalkylbladet i minnet och därför måste kalkylbladet laddas med [Minnesinställningar](/cells/sv/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) aktiverat.

Aspose.Cells APIer tillhandahåller Minnesinställningar för att optimera minnesförbrukningen vid inläsning och bearbetning av kalkylblad. Dessa alternativ är också användbara för att effektivt ladda stora kalkylblad med stora datamängder i Workbook-objektet, som demonstreras nedan.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Bestäm vilken stackstorlek som behövs för en viss Workbook**
Även om vi har förbättrat Aspose.Cells formelberäkningsmotor och i de flesta fall bör du kunna få alla formler beräknade framgångsrikt för en given mallfil utan att specificera mindre stackstorlek, ibland kan **StackOverFlowException** på metoden Workbook.CalculateFormula vara oundviklig. Vi tillhandahåller nya APIer för användarna för att spåra formelberäkningarna. Vi har lagt till en klass med namnet "AbstractCalculationMonitor" och tillhandahållit en egenskap, dvs. *CalculationOptions.CalculationMonitor* för att hantera/spåra problemet.

Användare kan spåra stackstorleken själva med hjälp av APIer. Observera, att kontrollen av stacken för varje cell säkerligen kommer att försämra prestandan i hög grad. Se kodsnutten nedan som exempel:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

Det finns inget bättre sätt att få den använda stackstorleken vid körning. Koden ovan är bara ett exempel. Prestandan kommer att försämras avsevärt, säkerligen. Så vi anser att koden kan optimeras av användare (som verkligen vill använda den) enligt deras olika scenarier och krav. Till exempel, kontrollera stacken när antalet rekursiva celler når ett visst antal, samla in den genomsnittliga ökningshastigheten för stack för en rekursiv cell och bestäm frekvensen för att kontrollera stacken, osv.

{{% /alert %}}

