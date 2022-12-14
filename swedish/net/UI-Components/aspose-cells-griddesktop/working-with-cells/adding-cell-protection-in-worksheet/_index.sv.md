---
title: Lägger till Cell Skydd i kalkylblad
type: docs
weight: 130
url: /sv/net/adding-cell-protection-in-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells för GridDesktop låter dig skydda dina celler i ett kalkylblad. Du måste först skydda ditt kalkylblad, sedan kan du skydda dina önskade celler i ett kalkylblad. För att skydda arbetsbladet, vänligen ställ in**Arbetsblad. Skyddad** egenskap till sant, använd sedan**Worksheet.SetProtected()** metod för att skydda cellområdet.

{{% /alert %}} 
## **Skydda Cell med Aspose.Cells.GridDesktop**
 Följande exempelkod skyddar alla celler inom området**A1:B1** av det aktiva kalkylbladet för GridDesktop. När du dubbelklickar på valfri cell i det här intervallet kommer du inte att kunna redigera. Det kommer att göra dessa celler skrivskyddade.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
