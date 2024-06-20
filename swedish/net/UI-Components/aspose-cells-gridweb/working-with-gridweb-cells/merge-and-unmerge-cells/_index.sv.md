---
title: Sammanfoga och avsammanfoga celler
type: docs
weight: 60
url: /sv/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb, sammanfoga, avsammanfoga
description: Den här artikeln introducerar hur man sammanfogar/avsammanfogar celler i GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb har en praktisk funktion som låter dig sammanfoga celler till en stor cell. Den här ämnet beskriver hur man sammanfogar celler programmatiskt.

{{% /alert %}} 
## **Sammanfoga celler**
Sammanfoga flera celler i en arbetsblad till en enda cell genom att anropa Cells-samlingen Merge-metod. Ange det cellintervall som ska sammanfogas vid anrop av Merge-metoden.

{{% alert color="primary" %}} 

Om du sammanfogar flera celler och varje cell innehåller data, behålls endast innehållet i den översta vänstra cellen i intervallet efter sammanfogningen. Data i de andra cellerna går inte förlorade. Om du avsakmanfogar cellerna återfår varje cell sin data.

{{% /alert %}} 

**Fyra celler sammanfogade till en** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Avsakmanfoga celler**
För att avsakmanfoga celler, använd Cells-samlingens UnMerge-metod som tar samma parametrar som Merge-metoden och utför avsakmanfogningen av celler.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
