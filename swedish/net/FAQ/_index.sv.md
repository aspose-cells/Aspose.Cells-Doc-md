---
title: FAQ
type: docs
weight: 100
url: /sv/net/faq/
---
## **Hur fixar jag System.StackOverFlowException på Workbook.CalculateFormula?**
Ibland möter användare System.StackOverFlowException på Workbook.CalculateFormula-metoden. Detta undantag uppstår vanligtvis eftersom standardstackstorleken för IIS är för liten (endast 265k). Du kan åtgärda det här felet genom att skapa en annan tråd med ökad stackstorlek och sedan flytta din Workbook.CalculateFormula-relaterade kod inuti den.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Problem med linjernas tjocklek när Excel renderas till PDF**
Ibland, när Excel-filen konverteras till PDF, är tjockleken på linjerna annorlunda i utdata PDF. Det här problemet orsakas inte av Aspose.Cells. Det orsakas av**Adobe läsare** när dess inställningar**"Slät linjekonst"** och**"Förbättra tunna linjer"** är kontrollerade. Om du avmarkerar dessa alternativ visas PDF fint.

 Om kontrollera**"Slät linjekonst"** och**"Förbättra tunna linjer"**, tjockleken på linjer är annorlunda. Se följande steg hur det görs:

-  Gå till**Redigera**
-  Välj**Inställningar**
-  I den**Sidvisning** Kategori Kontrollera**"Slät linjekonst"** och**"Förbättra tunna linjer"**

 Om avmarkera**"Slät linjekonst"** och**"Förbättra tunna linjer"**, tjockleken på linjer är densamma. För att uppnå detta, följ bara stegen nedan:

-  Gå till**Redigera**
-  Välj**Inställningar**
-  I den**Sidvisning** Kategori Avmarkera**"Slät linjekonst"** och**"Förbättra tunna linjer"**
## **Hur fixar man System.OutOfMemoryException när man laddar stora kalkylblad?**
Det finns rimliga chanser att Workbook-konstruktören kan kasta System.OutOfMemoryException när stora kalkylblad laddas. Detta undantag tyder på att det tillgängliga minnet är otillräckligt för att fullständigt ladda kalkylarket i minnet, därför måste kalkylarket laddas samtidigt som du aktiverar[Minnesinställningar](/cells/sv/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Aspose.Cells API:er tillhandahåller minnesinställningar för att optimera minnesförbrukningen när du laddar och bearbetar kalkylblad. Dessa alternativ är också användbara för att effektivt ladda de stora kalkylbladen som innehåller enorma datamängder i Workbook-objektet som visas nedan.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Bestäm vilken stackstorlek som behövs för en viss arbetsbok**
Även om vi har förbättrat Aspose.Cells formelberäkningsmotorn och i de flesta fall bör du kunna få alla formler beräknade framgångsrikt för en given mallfil utan att ange mindre stackstorlek. Men ändå, ibland kan StackOverFlowException på Workbook.CalculateFormula-metoden vara oundviklig. Vi tillhandahåller nya API:er för användarna att spåra formelberäkningarna. Vi har lagt till en klass som heter "AbstractCalculationMonitor" och tillhandahållit en egenskap, dvs.*CalculationOptions.CalculationMonitor*för att hantera/spåra problemet.

Användare kan spåra stackstorleken själva med hjälp av API:erna. Observera att en kontroll av stacken för varje cell säkerligen kommer att försämra prestandan i större utsträckning. Se exempelkodsegmentet för din referens:

`     `public class MyCalculationMonitor : AbstractCalculationMonitor
`     `{  ` `public override void BeforeCalculate(int sheetIndex, int rowIndex, int colIndex)  ` `{  ` `if(new StackTrace(false).FrameCount _x{000) `d 0:00:000) Stoppa formelberäkningen eftersom risken för StackOverflowException");  ` `}  ` `}  ` `} 



{{% alert color="primary" %}} 

Det finns inget bättre sätt att få stackstorleken att användas under körning. Ovanstående kod vi tillhandahållit är bara till exempel. Prestandan kommer säkert att försämras avsevärt. Så vi tror att koden kan optimeras av användare (som verkligen vill använda den) enligt deras olika scenarier och krav. Såsom att kontrollera stacken när antalet rekursiva celler når ett visst antal, samla in den genomsnittliga ökningshastigheten för stacken för en rekursiv cell och bestämma frekvensen för att kontrollera stacken, etc.

{{% /alert %}}

