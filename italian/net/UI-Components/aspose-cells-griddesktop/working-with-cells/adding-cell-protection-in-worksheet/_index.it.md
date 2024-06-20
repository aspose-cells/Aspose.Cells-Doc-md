---
title: Aggiungi Protezione nel Foglio di lavoro
type: docs
weight: 130
url: /it/net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: GridDesktop,proteggi
description: Questo articolo illustra come proteggere le celle nel Foglio di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells per GridDesktop ti consente di proteggere le celle in un foglio di lavoro. Prima è necessario proteggere il foglio di lavoro, poi è possibile proteggere le celle desiderate nel foglio di lavoro. Per proteggere il foglio di lavoro, impostare la proprietà **Worksheet.Protected** su true, quindi utilizzare il metodo **Worksheet.SetProtected()** per proteggere il intervallo di celle.

{{% /alert %}} 
## **Proteggi la cella utilizzando Aspose.Cells.GridDesktop**
Il seguente codice di esempio protegge tutte le celle nell'intervallo **A1:B1** del foglio di lavoro attivo di GridDesktop. Quando si fa doppio clic su qualsiasi cella in questo intervallo, non sarà possibile modificarla. Queste celle diventeranno di sola lettura.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
