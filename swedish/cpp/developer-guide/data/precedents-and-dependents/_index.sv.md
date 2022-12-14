---
title: Prejudikat och beroende
type: docs
weight: 100
url: /sv/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Komplexa ekonomiska kalkylblad, särskilt sådana som utvecklats i samarbete, kan dölja de mest pinsamma felen. Att kontrollera formler för noggrannhet och hitta källan till ett fel kan vara svårt när formeln använder prejudikatceller och beroende celler.

{{% /alert %}} 
## **Introduktion**
- **Prejudikatceller** är celler som refereras till av en formel i en annan cell. Till exempel, om cell D10 innehåller formeln =B5, är cell B5 ett prejudikat till cell D10.
- **Beroende celler** innehåller formler som refererar till andra celler. Till exempel, om cell D10 innehåller formeln =B5, är cell D10 beroende av cell B5.

För att göra kalkylarket lätt att läsa, kanske du vill tydligt visa vilka celler i ett kalkylblad som används i en formel. På liknande sätt kanske du vill extrahera de beroende cellerna från andra celler.

Aspose.Cells låter dig spåra celler och ta reda på vilka som är länkade.
## **Spåra prejudikat och beroende Cells: Microsoft Excel**
Formler kan ändras baserat på ändringar gjorda av en kund. Till exempel, om cell C1 är beroende av att C3 och C4 innehåller en formel, och C1 ändras (så att formeln åsidosätts), måste C3 och C4, eller andra celler, ändras för att balansera kalkylbladet baserat på affärsregler.

På samma sätt, anta att C1 innehåller formeln "=(B1*22)/(M2*N32)". Jag vill hitta cellerna som C1 beror på, det vill säga prejudikatcellerna B1, M2 och N32.

Du kan behöva spåra beroendet av en viss cell till andra celler. Om affärsregler är inbäddade i formler vill vi ta reda på beroendet och exekvera några regler baserat på det. På samma sätt, om värdet på en viss cell ändras, vilka celler i kalkylbladet påverkas av den ändringen?

Microsoft Excel tillåter användare att spåra prejudikat och anhöriga.

1.  På**Visa verktygsfält** , Välj**Formelrevision**
1. Spåra prejudikat:
 1. Välj cellen som innehåller formeln som du vill hitta prejudikatceller för.
 1. För att visa en spårningspil för varje cell som direkt tillhandahåller data till den aktiva cellen, klicka**Spåra prejudikat** på**Formelrevision** verktygsfältet.
1. Spåra formler som refererar till en viss cell (beroende)
 1. Välj den cell som du vill identifiera de beroende cellerna för.
1. För att visa en spårningspil för varje cell som är beroende av den aktiva cellen, klicka på Spåra beroende i verktygsfältet Formula Auditing.
## **Spårande prejudikat och beroende Cells: Aspose.Cells**
### **Spåra prejudikat**
Aspose.Cells gör det enkelt att få prejudikatceller. Det kan inte bara hämta celler som tillhandahåller data till enkla formelprejudikat utan också hitta celler som tillhandahåller data till komplexa formelprejudikat med namngivna intervall.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents.cpp" >}}
### **Spåra beroende**
Aspose.Cells låter dig få beroende celler i kalkylblad. Aspose.Cells kan inte bara hämta celler som tillhandahåller data om en enkel formel utan också hitta celler som tillhandahåller data till komplexa formelberoende med namngivna intervall.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents.cpp" >}}
