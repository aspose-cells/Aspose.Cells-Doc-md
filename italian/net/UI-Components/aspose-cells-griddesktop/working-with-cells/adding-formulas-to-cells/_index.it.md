---
title: Aggiunta di formule a Cells
type: docs
weight: 30
url: /it/net/adding-formulas-to-cells/
---
{{% alert color="primary" %}} 

Una cella non può contenere solo un valore semplice come una cifra numerica o del testo, ma possiamo anche inserire una formula in una cella come suo valore. Una formula viene utilizzata in una cella quando il valore di una cella deve essere determinato dopo alcuni calcoli. In questo argomento, discuteremo di come possiamo accedere e modificare una formula applicata su una cella.

{{% /alert %}} 
## **Aggiunta di Formula a un numero Cell**
 Aggiungere una formula a una cella è come impostare il valore di una cella come abbiamo discusso nel nostro argomento precedente:[Accesso e modifica del valore di un numero Cell](/cells/it/net/accessing-and-modifying-the-value-of-a-cell/) tranne che in quel caso, abbiamo appena aggiunto valori semplici alle celle. Ora aggiungeremo le formule. Gli sviluppatori possono utilizzare la proprietà Value di una cella per accedere e modificare la formula o altro**ImpostaValoreCella** metodo della cella può essere utilizzato anche per aggiungere o modificare la formula in una cella.

**IMPORTANTE:** La differenza fondamentale tra l'utilizzo della proprietà Value o**ImpostaValoreCella** metodo di una cella è quello richiamato dalla proprietà Value**Esegui tutte le formule** metodo di Grid automaticamente per ricalcolare i valori di tutte le formule dove come nel caso di**ImpostaValoreCella** gli sviluppatori di metodi devono chiamare**Esegui tutte le formule** metodo esplicitamente dopo che le formule sono state aggiunte alle celle. In realtà, quando usiamo**ImpostaValoreCella** metodo di una cella, questo metodo imposta il valore della cella su**Tipo di formula** solo e non calcolare la formula. Inoltre, chiamando**Esegui tutte le formule**metodo ogni volta non è necessario. Se vuoi aggiungere molte formule nelle celle di un foglio di lavoro, puoi chiamare**Esegui tutte le formule** metodo solo una volta alla fine.

 Una formula viene aggiunta a una cella come valore stringa. Inoltre, la struttura della formula deve essere compatibile con la struttura della formula di MS Excel. Tutte le formule devono iniziare con an**Segno di uguale (=)**.

 Nell'esempio riportato di seguito, abbiamo aggiunto una formula per moltiplicare i valori di due celle del foglio di lavoro e memorizzare il risultato in un'altra cella.**Esegui tutte le formule** Anche il metodo viene richiamato alla fine.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Ora esegui l'applicazione. Se fai doppio clic sulla cella in cui è stata aggiunta la formula, noterai che il valore verrà sostituito dalla formula che sta effettivamente calcolando il valore sul back-end.

{{% alert color="primary" %}} 

 Aspose.Cells.GridDesktop supporta la maggior parte delle funzioni comunemente utilizzate di MS Excel. Per maggiori dettagli sull'elenco delle funzioni supportate, per favore[clicca qui.](/cells/it/net/list-of-supported-functions/)

{{% /alert %}}
