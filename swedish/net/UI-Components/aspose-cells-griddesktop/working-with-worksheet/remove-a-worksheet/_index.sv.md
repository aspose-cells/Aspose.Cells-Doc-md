---
title: Ta bort en Arbetsblad
type: docs
weight: 30
url: /sv/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop, ta bort, arbetsblad
description: Den här artikeln introducerar hur man tar bort arbetsblad i GridDesktop.
---

{{% alert color="primary" %}} 

Det här ämnet diskuterar borttagning av arbetsblad med användning av kontrollen Aspose.Cells.GridDesktop. Det finns några enkla tillvägagångssätt för att utföra denna grundläggande uppgift.

{{% /alert %}} 
## **Ta bort ett Arbetsblad**
För att ta bort ett arbetsblad med hjälp av kontrollen Aspose.Cells.GridDesktop, följ stegen nedan:

1. Lägg till kontrollen Aspose.Cells.GridDesktop på en formulär.
1. Anropa metoden Remove för samling av Arbetsblad i GridDesktop-kontrollen.
### **Användning av Arbetsbladsindex**
I detta tillvägagångssätt skickar du helt enkelt in arbetsboksindexet (i gridets arbetsbladssamling) för arbetsboken som ska tas bort.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Användning av Arbetsbladsnamn**
Om namnet på arbetsboken är känt, är det möjligt att ta bort en specifik arbetsbok genom att ange dess namn.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Ta bort är en metod. Använd den för att ta bort ett arbetsblad med hjälp av dess index (i arbetsbladssamlingen) eller använd RemoveAt-metoden för att ta bort arbetsbladet med hjälp av dess index/namn.

{{% /alert %}}
