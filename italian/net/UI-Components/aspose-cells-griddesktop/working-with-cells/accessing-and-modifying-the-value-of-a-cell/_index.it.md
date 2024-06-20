---
title: Accesso e Modifica del Valore di una Cella
type: docs
weight: 20
url: /it/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: Questo articolo introduce come ottenere e modificare il valore di una cella in GridDesktop.
---

{{% alert color="primary" %}} 

Nel nostro argomento precedente, abbiamo discusso dell'accesso alle celle di un foglio di lavoro. In questo argomento, estenderemo semplicemente quell'argomento per mostrare agli sviluppatori come possono accedere e modificare i valori delle celle utilizzando l'API di Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Accedere e Modificare il Valore di una Cella utilizzando Aspose.Cells.GridDesktop**
Prima di accedere e modificare il valore di una cella, dovremmo sapere come accedere alle celle. Ci sono tre approcci per accedere alle celle di un foglio di lavoro. Per ulteriori dettagli su questi tre approcci, si prega di consultare [Accesso alle Celle in un Foglio di Lavoro.](/cells/it/net/accessing-cells-in-a-worksheet/)

Ogni cella ha una proprietà chiamata Valore. Quindi, una volta che una cella viene accessa, gli sviluppatori possono accedere e modificare i contenuti della proprietà Valore per accedere e modificare il valore di una cella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**IMPORTANTE:** Utilizzare la proprietà Valore di una cella per modificare il suo valore è un buon approccio per impostare il valore di una o poche celle. Se è necessario impostare i valori di molte celle, allora le prestazioni di questo approccio non sarebbero buone. Quindi, per impostare i valori di molte celle, dovresti utilizzare il metodo **SetCellValue** della cella per migliorare le prestazioni delle tue applicazioni. Una versione modificata dello snippet di codice sopra utilizzando il metodo **SetCellValue** è mostrata di seguito.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
