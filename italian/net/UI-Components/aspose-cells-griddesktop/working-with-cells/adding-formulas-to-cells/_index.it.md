---
title: Aggiungi Formula alla cella
type: docs
weight: 30
url: /it/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop,formula
description: Questo articolo illustra come ottenere o impostare una formula nella cella nel Foglio di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

Una cella può contenere non solo un valore semplice come una cifra numerica o del testo, ma anche una formula come valore. Una formula viene utilizzata in una cella quando il valore della cella deve essere determinato dopo alcuni calcoli. In questo argomento, discuteremo come accedere e modificare una formula applicata a una cella.

{{% /alert %}} 
## **Aggiunta di una formula a una cella**
Aggiungere una formula a una cella è come impostare il valore di una cella come abbiamo discusso nel nostro argomento precedente: [Accesso e modifica del valore di una cella](/cells/it/net/accessing-and-modifying-the-value-of-a-cell/) tranne che in quel caso abbiamo aggiunto solo valori semplici alle celle. Ora, aggiungeremo delle formule. Gli sviluppatori possono utilizzare la proprietà Valore di una cella per accedere e modificare la formula o altrimenti il metodo **SetCellValue** della cella può essere usato anche per aggiungere o modificare la formula in una cella.

**IMPORTANTE:** La differenza di base tra l'utilizzo della proprietà Valore o del metodo **SetCellValue** di una cella è che la proprietà Valore invoca automaticamente il metodo **RunAllFormulas** di Grid per ricalcolare i valori di tutte le formule, mentre nel caso del metodo **SetCellValue** gli sviluppatori devono chiamare esplicitamente il metodo **RunAllFormulas** dopo che le formule sono state aggiunte alle celle. In realtà, quando usiamo il metodo **SetCellValue** di una cella, questo metodo imposta il valore della cella solo su **FormulaType** e non calcola la formula. Inoltre, chiamare il metodo **RunAllFormulas** ogni volta non è necessario. Se si desidera aggiungere molte formule nelle celle di un foglio di lavoro, è possibile chiamare il metodo **RunAllFormulas** solo una volta alla fine.

Una formula viene aggiunta a una cella come valore di stringa. Inoltre, la struttura della formula deve essere compatibile con la struttura della formula di MS Excel. Tutte le formule devono iniziare con un **Segno Uguale (=)**.

Nell'esempio riportato di seguito, abbiamo aggiunto una formula per moltiplicare i valori di due celle del foglio di lavoro e memorizzare il risultato in un'altra cella. Anche il metodo **RunAllFormulas** viene invocato alla fine.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Ora avvia l'applicazione. Se fai doppio clic sulla cella in cui è stata aggiunta la formula, noterai che il valore verrà sostituito dalla formula che sta effettivamente calcolando il valore sul retro.

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop supporta la maggior parte delle funzioni comunemente usate di MS Excel. Per ulteriori dettagli sulla lista delle funzioni supportate, fare clic [qui.](/cells/it/net/list-of-supported-functions/)

{{% /alert %}}
