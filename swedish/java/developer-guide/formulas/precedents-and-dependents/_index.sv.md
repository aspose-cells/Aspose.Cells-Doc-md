---
title: Prejudikat och beroende
type: docs
weight: 230
url: /sv/java/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Komplexa ekonomiska kalkylblad, särskilt sådana som utvecklats i samarbete, kan dölja de mest pinsamma felen. Att kontrollera formler för noggrannhet och hitta källan till ett fel kan vara svårt när formeln använder prejudikatceller och beroende celler.

{{% /alert %}} 
## **Introduktion**
- **Prejudikatceller** är celler som refereras till av en formel i en annan Cell. Om cell D10 till exempel innehåller formeln =B5, är cell B5 ett prejudikat till cell D10.
- **Beroende celler** innehåller formler som refererar till andra celler. Till exempel, om cell D10 innehåller formeln =B5, är cell D10 beroende av cell B5.

För att göra kalkylarket lätt att läsa, kanske du vill tydligt visa vilka celler i ett kalkylblad som används i en formel. På liknande sätt kanske du vill extrahera de beroende cellerna från andra celler.

Aspose.Cells låter dig spåra celler och ta reda på vilka som är länkade.
## **Spåra prejudikat och beroende Cells: Microsoft Excel**
Formler kan ändras baserat på ändringar gjorda av en kund. Till exempel, om cell C1 är beroende av att C3 och C4 innehåller en formel, och C1 ändras (så att formeln åsidosätts), måste C3 och C4, eller andra celler, ändras för att balansera kalkylbladet baserat på affärsregler.

På samma sätt, anta att C1 innehåller formeln "=(B1*22)/(M2*N32)". Jag vill hitta cellerna som C1 beror på, det vill säga prejudikatcellerna B1, M2 och N32.

Du kan behöva spåra beroendet av en viss cell till andra celler. Om affärsregler är inbäddade i formler vill vi ta reda på beroendet och exekvera några regler baserat på det. På samma sätt, om värdet på en viss cell ändras, vilka celler i kalkylbladet påverkas av den ändringen?

Microsoft Excel tillåter användare att spåra prejudikat och anhöriga.

1.  På**Visa verktygsfält** , Välj**Formelrevision**. Dialogrutan Formelrevision kommer att visas.
1. Spåra prejudikat:
 1. Välj cellen som innehåller formeln som du vill hitta prejudikatceller för.
 1. För att visa en spårningspil för varje cell som direkt tillhandahåller data till den aktiva cellen, klicka**Spåra prejudikat** på**Formelrevision** verktygsfältet.
1. Spåra formler som refererar till en viss cell (beroende)
 1. Välj den cell som du vill identifiera de beroende cellerna för.
1. För att visa en spårningspil för varje cell som är beroende av den aktiva cellen, klicka på Spåra beroende i verktygsfältet Formula Auditing.
## **Spårande prejudikat och beroende Cells: Aspose.Cells**
### **Spåra prejudikat**
Aspose.Cells gör det enkelt att få prejudikatceller. Det kan inte bara hämta celler som tillhandahåller data till enkla formelprejudikat utan också hitta celler som tillhandahåller data till komplexa formelprejudikat med namngivna intervall.

exemplet nedan används en excel-mall, Book1.xls. Kalkylarket har data och formler på det första kalkylbladet.

 Aspose.Cells tillhandahåller[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) klass'[GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents() ) metod som används för att spåra en cells prejudikat. Den returnerar en[ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection). Som du kan se ovan, i Book1.xls, innehåller cell B7 en formel "=SUMMA(A1:A3)". Så cellerna A1:A3 är prejudikatcellerna till cell B7. Följande exempel visar spårningsprejudikatfunktionen med hjälp av mallfilen Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Spåra beroende**
Aspose.Cells låter dig få beroende celler i kalkylblad. Aspose.Cells kan inte bara hämta celler som tillhandahåller data om en enkel formel utan också hitta celler som tillhandahåller data till komplexa formelberoende med namngivna intervall.

 Aspose.Cells tillhandahåller[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) klass'[GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean)metod som används för att spåra en cells beroende. Till exempel, i Book1.xlsx finns formler: "=A1+20" och "=A1+30" i B2- respektive C2-cellerna. Följande exempel visar hur man spårar beroenden för A1-cellen med hjälp av mallfilen Book1.xlsx.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Spåra prejudikat- och beroendeceller enligt beräkningskedja**
 Ovanför apis av spårande prejudikat och beroende är enligt formeluttrycket själv. De ger helt enkelt ett bekvämt sätt för användaren att spåra ömsesidiga beroenden för ett fåtal formler. Om det finns stora mängder formler i arbetsboken och användaren behöver spåra prejudikat och beroenden för varje cell, kommer de att ge dålig prestanda. För en sådan situation bör användaren överväga att använda[GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation() /) och[GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean) /) metoder. Dessa två metoder spårar beroenden enligt beräkningskedjan. Så för att använda dem måste du först och främst aktivera beräkningskedjan med[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain) . Då bör du utföra fullständig beräkning för arbetsboken genom[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)). Efter det kan du spåra prejudikat eller beroende för alla de celler du behöver.

För vissa formler kan de resulterande prejudikaten vara olika för GetPrecedents och GetPrecedentsInCalculation, och de resulterande beroenden kan vara olika för GetDependents och GetDependentsInCalculation. Till exempel, om cell A1:s formel är "=OM(TRUE,B2,C3)", kommer GetPrecedents att tillhandahålla B2 och C3 som A1:s prejudikat. Följaktligen har B2 och C3 båda den beroende A1 vid kontroll av GetDependents. Men för beräkningen av denna formel är det uppenbart att endast B2 kan påverka det beräknade resultatet. Så GetPrecedentsInCalculation kommer inte att tillhandahålla C3 för A1, och GetDependentsInCalculation kommer inte att tillhandahålla A1 för C3. Ibland kan användaren bara ha kravet att spåra de ömsesidiga beroenden som faktiskt påverkar det beräknade resultatet av formler baserat på aktuella data i arbetsboken, då måste de också använda GetDependentsInCalculation/GetPrecedentsInCalculation istället för GetDependents/GetPrecedents.

Följande exempel visar hur man spårar prejudikat och beroende enligt beräkningskedjan för celler:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
