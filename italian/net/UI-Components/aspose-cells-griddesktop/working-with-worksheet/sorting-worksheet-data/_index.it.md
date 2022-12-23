---
title: Ordinamento dei dati del foglio di lavoro
type: docs
weight: 80
url: /it/net/sorting-worksheet-data/
---
{{% alert color="primary" %}} 

L'ordinamento è un'attività di routine importante che utilizziamo principalmente durante l'elaborazione dei dati. In questo argomento, discuteremo con l'aiuto di un semplice esempio di come possiamo ordinare i dati in un foglio di lavoro.

{{% /alert %}} 
## **Ordinamento dei dati del foglio di lavoro**
Per ordinare i dati in un foglio di lavoro utilizzando API di Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Prima di tutto crea un oggetto globale di**CellRange** in modo che sia possibile accedervi ovunque nell'ambito della classe
-  Crea un gestore di eventi per**SelectedCellRangeChanged** evento di**GrigliaDesktop**. **SelectedCellRangeChanged** L'evento viene attivato ogni volta che viene modificato un intervallo di celle selezionato da un utente. Ad esempio, se un utente seleziona celle (contenenti dati da ordinare), ogni volta che il suo intervallo di selezione cambia, questo evento viene attivato.
-  Il gestore dell'evento fornisce**CellRangeEventArgs** argomento che fornisce inoltre l'intervallo di aggiornamento delle celle (selezionato dall'utente) sotto forma di a**CellRange** oggetto. Quindi, in questo gestore di eventi, assegneremo this**CellRange** object (contenente l'intervallo aggiornato di celle) al global**CellRange**oggetto in modo che possa essere utilizzato anche in altre parti del codice. Per assicurarci di non perdere l'intervallo di celle, scriveremo il codice del gestore di eventi all'interno di una condizione
- Ora possiamo scrivere del codice per ordinare i dati del foglio di lavoro. Prima di tutto, accedi a un foglio di lavoro desiderato
-  Creare un**OrdinaRange** oggetto che manterrà l'intervallo di celle i cui dati devono essere ordinati. In**OrdinaRange** costruttore, possiamo specificare il foglio di lavoro, gli indici della riga e della colonna iniziali, il numero di righe e colonne da ordinare, l'orientamento dell'ordinamento (come dall'alto verso il basso o da sinistra a destra) ecc.
-  Ora possiamo chiamare**Ordinare** metodo di**OrdinaRange** oggetto per eseguire l'ordinamento dei dati. In**Ordinare** metodo, possiamo specificare l'indice della colonna o della riga da ordinare e l'ordine di ordinamento (che può essere**Ascendente** o**Discendente** in base alle vostre esigenze)
-  Finalmente possiamo chiamare**Invalidare** metodo di**GrigliaDesktop** per ridisegnare le celle.

Nell'esempio fornito di seguito, abbiamo dimostrato come ordinare i dati in una colonna.

 Crea un oggetto globale di CellRange e**SelectedCellRangeChanged**evento di GridDesktop. Ora scrivi il codice come indicato di seguito:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


 Ora scriviamo il metodo per**Ordinamento crescente** . Puoi creare un pulsante per**Ordinamento crescente** e scrivi sotto il codice all'interno del suo**Clic** Evento.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


 Infine, scriviamo del codice da raggiungere**Ordinamento decrescente** funzionalità. Creare un**Ordinamento decrescente** pulsante e scrivere sotto il codice all'interno del suo**Clic** Evento.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
