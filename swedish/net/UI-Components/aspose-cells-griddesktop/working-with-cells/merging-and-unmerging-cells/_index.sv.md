---
title: Sammanfoga och ta bort Cells i GridDesktop
linktitle: Sammanfogning och upphävande Cells
type: docs
weight: 90
url: /sv/net/merging-and-unmerging-cells-griddesktop/
---
{{% alert color="primary" %}} 

I det här ämnet kommer vi att diskutera en hjälpfunktion för att slå samman och ta bort celler i ett kalkylblad. Den här funktionen är användbar i de fall vi behöver spänna över några rader eller kolumner för att förbättra läsbarheten för data.

{{% /alert %}} 
## **Slår ihop Cells**
För att slå samman celler till en enda stor cell, följ stegen nedan:

-  Få åtkomst till alla önskade**Arbetsblad**
-  Skapa en**Räckvidd Cells** ska slås samman
- **Sammanfoga** intervallet av celler till en stor cell

 Du kan använda**Sammanfoga** metod av**Arbetsblad** för att slå samman celler. Däremot kan ett cellintervall definieras med hjälp av**CellRange** objekt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Avslutar Cells**
För att ta bort en stor cell till många celler, följ stegen nedan:

-  Få åtkomst till alla önskade**Arbetsblad**
- Åtkomst till den sammanslagna cellen som måste tas bort
- **Avsluta** den stora cellen in i många celler med platsen för den sammanslagna cellen

 Du kan använda**Avsluta** metod av**Arbetsblad** för att ta bort en cell med hjälp av dess plats.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

När du slår samman celler till en enskild cell tillämpas formateringsinställningarna för den övre vänstra cellen (i cellintervallet) på den sammanslagna cellen, men när cellen inte är sammanfogad behåller alla ej sammanslagna celler sina formateringsinställningar.

{{% /alert %}}
