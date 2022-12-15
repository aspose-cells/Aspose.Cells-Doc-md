---
title: Accesso e modifica del valore di un numero Cell
type: docs
weight: 20
url: /it/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

Nel nostro argomento precedente, abbiamo discusso dell'accesso alle celle di un foglio di lavoro. In questo argomento, estenderemo semplicemente tale argomento per mostrare agli sviluppatori come possono accedere e modificare i valori delle celle utilizzando l'API di Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Accedi e modifica il valore Cell utilizzando Aspose.Cells.GridDesktop**
 Prima di accedere e modificare il valore di una cella, dovremmo sapere come accedere alle celle. Esistono tre approcci per accedere alle celle di un foglio di lavoro. Per maggiori dettagli su questi tre approcci, per favore[Accesso a Cells in un foglio di lavoro.](/cells/it/net/accessing-cells-in-a-worksheet/)

Ogni cella ha una proprietà denominata Value . Pertanto, una volta effettuato l'accesso a una cella, gli sviluppatori possono accedere e modificare il contenuto della proprietà Value per accedere e modificare il valore di una cella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**IMPORTANTE:**L'utilizzo della proprietà Value di una cella per modificarne il valore è un buon approccio per impostare il valore di una o poche celle. Se è necessario impostare i valori di molte celle, le prestazioni di questo approccio non sarebbero buone. Quindi, per impostare i valori di molte celle, dovresti usare**ImpostaValoreCella** metodo della cella per migliorare le prestazioni delle vostre applicazioni. Una versione modificata del frammento di codice precedente utilizzando**ImpostaValoreCella** metodo è mostrato di seguito.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
