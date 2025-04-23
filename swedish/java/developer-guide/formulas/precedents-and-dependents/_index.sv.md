---
title: Precedenser och beroende
type: docs
weight: 230
url: /sv/java/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Komplexa finansiella arbetsblad, särskilt de som utvecklats i samarbete, kan dölja de mest pinsamma felen. Att kontrollera formler för noggrannhet och hitta felets källa kan vara svårt när formeln använder precedens- och beroendeceller.

{{% /alert %}} 
## **Introduktion**
- **Precedensceller** är celler som hänvisas till av en formel i en annan cell. Till exempel, om cell D10 innehåller formeln =B5, är cell B5 en precedens till cell D10.
- **Beroendeceller** innehåller formler som hänvisar till andra celler. Till exempel, om cell D10 innehåller formeln =B5, är cell D10 beroende av cell B5.

För att göra kalkylarket lättläst vill du kanske tydligt visa vilka celler på ett kalkylblad som används i en formel. På liknande sätt kan du vilja extrahera de beroende cellerna för andra celler.

Aspose.Cells låter dig spåra celler och ta reda på vilka som är länkade.
## **Spåra precedens- och beroendeceller: Microsoft Excel**
Formler kan ändras baserat på ändringar som görs av en klient. Till exempel, om cell C1 är beroende av C3 och C4 som innehåller en formel, och C1 ändras (så formeln åsidosätts), måste C3 och C4, eller andra celler, ändras för att balansera kalkylarket baserat på affärsregler.

På liknande sätt, anta att C1 innehåller formeln "=(B1*22)/(M2*N32)". Jag vill hitta de celler som C1 är beroende av, dvs. precedenscellerna B1, M2 och N32.

Du kan behöva spåra beroendet för en specifik cell till andra celler. Om affärsregler är inbäddade i formler vill vi ta reda på beroendet och utföra några regler baserat på det. På liknande sätt, om värdet på en specifik cell ändras, vilka celler i arbetsbladet påverkas av den ändringen?

Microsoft Excel tillåter användare att spåra precedenser och beroenden.

1. På **Visa verktygsfältet**, välj **Formelgranskning**. Dialogrutan för formelgranskning visas.
1. Spåra Precedenser:
   1. Välj den cell som innehåller formeln för vilken du vill hitta precedensceller.
   1. För att visa en spårpil till varje cell som direkt tillhandahåller data till den aktiva cellen, klicka på **Spåra Precedenser** på verktygsfältet för formelgranskning.
1. Spåra formler som refererar till en specifik cell (beroenden)
   1. Välj den cell för vilken du vill identifiera de beroende cellerna.
   1. För att visa en spårpil till varje cell som är beroende av den aktiva cellen, klicka på Spåra Beroenden på verktygsfältet för formelgranskning.
## **Spårar föregående och beroende celler: Aspose.Cells**
### **Spårar föregående**
Aspose.Cells gör det enkelt att få föregående celler. Den kan inte bara hämta celler som ger data till enkla formelföregångare utan också hitta celler som ger data till komplexa formelföregångare med namngivna områden.

I exemplet nedan används en template excelfil, Book1.xls. Kalkylarket har data och formler på den första arbetsbladet.

Aspose.Cells tillhandahåller [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)-klassens [GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents--)metod som används för att spåra en cells föregångare. Den returnerar en [ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection). Som du kan se ovan, i Book1.xls innehåller cell B7 en formel "=SUM(A1:A3)". Så celler A1:A3 är de föregående cellerna till cell B7. Följande exempel visar spårningsfunktionen föregående med hjälp av template-filen Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Spårar beroende**
Aspose.Cells låter dig få beroende celler i kalkylblad. Aspose.Cells kan inte bara hämta celler som ger data om en enkel formel utan också hitta celler som ger data till komplexa formelberopare med namngivna områden.

Aspose.Cells erbjuder metoden [GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents-boolean-) för Cell-klassen, som kan användas för att spåra ett cells beroenden. Till exempel finns det formler: "=A1+20" och "=A1+30" i cellerna B2 och C2 respektive. Följande exempel demonstrerar hur man spårar beroenden för cellen A1 med hjälp av mallfilen Book1.xlsx.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Spårning av föregående och beroende celler enligt beräkningskedjan**
Ovan nämnda API:er för spårning av förfäder och beroenden är baserade på själva formeluttrycket. De ger en enkel metod för att spåra vissa formelberoenden. Om det finns ett stort antal formler i arbetsboken och användaren behöver spåra förfäder och beroenden för varje cell, kommer prestandan att bli dålig. I sådana fall bör användaren använda metoderna [GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation--) och [GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation-). Dessa metoder spårar beroenden enligt beräkningskedjan. För att använda dem, måste du först aktivera beräkningskedjan via [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain). Sedan måste du utföra fullständig beräkning för arbetsboken med [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions-). Då kan du spåra förfäder eller beroenden för alla de celler du behöver.

För vissa formler kan de resulterande föregångarna vara olika för GetPrecedents och GetPrecedentsInCalculation, och de resulterande beroparna kan vara olika för GetDependents och GetDependentsInCalculation. Till exempel, om cell A1:s formel är "=IF(TRUE,B2,C3)", kommer GetPrecedents att tillhandahålla B2 och C3 som A1:s föregående. På samma sätt har både B2 och C3 beropande A1 vid kontroll med GetDependents. Men för beräkningen av denna formel är det uppenbart att endast B2 kan påverka det beräknade resultatet. Så GetPrecedentsInCalculation kommer inte att visa C3 för A1, och GetDependentsInCalculation kommer inte att visa A1 för C3. Ibland kan användaren ha kravet att bara spåra de ömsesidiga beroenden som faktiskt påverkar det beräknade resultatet av formler baserat på aktuella data i arbetsboken, då behöver de också använda GetDependentsInCalculation/GetPrecedentsInCalculation istället för GetDependents/GetPrecedents.

Följande exempel visar hur man spårar föregående- och beroende enligt beräkningskedjan för celler:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
{{< app/cells/assistant language="java" >}}
