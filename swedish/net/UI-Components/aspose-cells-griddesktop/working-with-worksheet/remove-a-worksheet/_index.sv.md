---
title: Ta bort ett arbetsblad
type: docs
weight: 30
url: /sv/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

Det här ämnet diskuterar borttagning av kalkylblad med Aspose.Cells.GridDesktop-kontrollen. Det finns några enkla metoder för att utföra denna grundläggande uppgift.

{{% /alert %}} 
## **Ta bort ett arbetsblad**
För att ta bort ett kalkylblad med Aspose.Cells.GridDesktop-kontroll, följ stegen nedan:

1. Lägg till Aspose.Cells.GridDesktop-kontrollen i ett formulär.
1. Anropa kalkylbladssamlingens Remove-metod i GridDesktop-kontrollen.
### **Använda kalkylbladsindex**
I detta tillvägagångssätt, skicka helt enkelt kalkylbladsindexet (i kalkylbladssamlingen i rutnätet) för det kalkylblad som ska tas bort.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Använder kalkylbladsnamn**
Om namnet på kalkylbladet är känt är det möjligt att ta bort ett specifikt kalkylblad genom att ange dess namn.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Ta bort är en metod. Använd den för att ta bort ett kalkylblad med dess index (i kalkylbladssamlingen) eller använd metoden RemoveAt för att ta bort kalkylbladet med dess index/namn.

{{% /alert %}}
