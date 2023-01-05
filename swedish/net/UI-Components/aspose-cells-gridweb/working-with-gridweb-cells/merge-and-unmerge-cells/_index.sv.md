---
title: Sammanfoga och ta bort sammanfogningen Cells
type: docs
weight: 60
url: /sv/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb har en praktisk verktygsfunktion som låter dig slå samman celler till en stor cell. Det här avsnittet beskriver hur man sammanfogar celler programmatiskt.

{{% /alert %}} 
## **Slår ihop Cells**
Slå samman flera celler i ett kalkylblad till en enda cell genom att anropa Cells-samlingens Sammanfogningsmetod. Ange intervallet av celler som ska slås samman när du anropar Sammanfogningsmetoden.

{{% alert color="primary" %}} 

Om du slår samman flera celler och varje cell innehåller data, behålls endast innehållet i den övre vänstra cellen i intervallet efter sammanfogningen. Data i de andra cellerna går inte förlorade. Om du tar bort sammanslagningen av cellerna återställer varje cell sina data.

{{% /alert %}} 

**Fyra celler slogs samman till en** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Avslutar Cells**
För att ta bort sammanslagningen av celler, använd Cells-samlingens UnMerge-metod som tar samma parametrar som för Merge-metoden och utför upphävandet av celler.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
