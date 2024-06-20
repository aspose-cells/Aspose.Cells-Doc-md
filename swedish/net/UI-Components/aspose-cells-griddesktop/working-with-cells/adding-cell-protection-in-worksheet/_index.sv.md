---
title: Lägg till skydd i kalkylarket
type: docs
weight: 130
url: /sv/net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: GridDesktop, skydda
description: Den här artikeln introducerar hur man skyddar celler i kalkylarket i GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells för GridDesktop låter dig skydda celler i ett kalkylark. Först måste du skydda ditt kalkylblad, sedan kan du skydda dina önskade celler i kalkylarket. För att skydda kalkylarket, ange **Worksheet.Protected**-egenskapen till true, använd sedan **Worksheet.SetProtected()**-metoden för att skydda cellområdet.

{{% /alert %}} 
## **Skydda cell med Aspose.Cells.GridDesktop**
Följande exempelkod skyddar alla celler inom området **A1:B1** i det aktiva kalkylarket i GridDesktop. När du dubbelklickar på någon cell inom detta område kommer du inte att kunna redigera. Det kommer att göra dessa celler skrivskyddade.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
