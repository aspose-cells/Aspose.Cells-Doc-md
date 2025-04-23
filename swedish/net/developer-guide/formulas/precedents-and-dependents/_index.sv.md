---
title: Precedenser och beroende
type: docs
weight: 230
url: /sv/net/precedents-and-dependents/
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

Aspose.Cells tillhandahåller [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) klassens [GetPrecedents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents) metod som används för att spåra cellens beroenden. Den returnerar en [ReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection). Som du kan se ovan, i Book1.xls, innehåller cellen B7 en formel "=SUM(A1:A3)". Så cellerna A1:A3 är de beroende celler till cell B7. Följande exempel visar spåra beroenden-funktionen med hjälp av mallfilen Book1.xls.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **Spårar beroende**
Aspose.Cells låter dig få beroende celler i kalkylblad. Aspose.Cells kan inte bara hämta celler som ger data om en enkel formel utan också hitta celler som ger data till komplexa formelberopare med namngivna områden.

Aspose.Cells tillhandahåller [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) klassens [GetDependents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents) metod som används för att spåra cellens efterföljare. Till exempel, i Book1.xlsx finns det formler: "=A1+20" och "=A1+30" i cellerna B2 och C2. Följande exempel visar hur man spårar efterföljare för cellen A1 med hjälp av mallfilen Book1.xlsx.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **Spårning av föregående och beroende celler enligt beräkningskedjan**
Ovanstående API:er för att spåra beroenden och efterföljare är enligt formeluttrycket självt. De ger helt enkelt ett bekvämt sätt för användaren att spåra ömsesidigberoende för några formler. Om det finns ett stort antal formler i arbetsboken och användaren behöver spåra beroenden och efterföljare för varje cell, kommer de att ge dålig prestanda. För en sådan situation bör användaren överväga att använda [GetPrecedentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/) och [GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/) metoderna. Dessa två metoder spårar beroenden enligt beräkningskedjan. Så, för att använda dem, måste du först aktivera beräkningskedjan med [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/). Sedan bör du utföra fullständig beräkning för Arbetsboken med [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1). Efter det kan du spåra beroenden eller efterföljare för alla de celler du behöver.

För vissa formler kan de resulterande föregångarna vara olika för GetPrecedents och GetPrecedentsInCalculation, och de resulterande beroparna kan vara olika för GetDependents och GetDependentsInCalculation. Till exempel, om cell A1:s formel är "=IF(TRUE,B2,C3)", kommer GetPrecedents att tillhandahålla B2 och C3 som A1:s föregående. På samma sätt har både B2 och C3 beropande A1 vid kontroll med GetDependents. Men för beräkningen av denna formel är det uppenbart att endast B2 kan påverka det beräknade resultatet. Så GetPrecedentsInCalculation kommer inte att visa C3 för A1, och GetDependentsInCalculation kommer inte att visa A1 för C3. Ibland kan användaren ha kravet att bara spåra de ömsesidiga beroenden som faktiskt påverkar det beräknade resultatet av formler baserat på aktuella data i arbetsboken, då behöver de också använda GetDependentsInCalculation/GetPrecedentsInCalculation istället för GetDependents/GetPrecedents.

Följande exempel visar hur man spårar föregående- och beroende enligt beräkningskedjan för celler:


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
{{< app/cells/assistant language="csharp" >}}
