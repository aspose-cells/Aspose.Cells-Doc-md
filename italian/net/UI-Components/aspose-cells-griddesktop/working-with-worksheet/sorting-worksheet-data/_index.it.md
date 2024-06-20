---
title: Ordinamento dei dati del foglio di lavoro
type: docs
weight: 80
url: /it/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop, ordinamento, ordinamento, ordinamento dati, ordinamento dati
description: Questo articolo introduce come ordinare i dati nel foglio di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

L'ordinamento è un'attività di routine importante che usiamo principalmente durante l'elaborazione dei dati. In questo argomento, discuteremo con l'aiuto di un semplice esempio su come possiamo ordinare i dati in un foglio di lavoro.

{{% /alert %}} 
## **Ordinamento dei dati del foglio di lavoro**
Per ordinare i dati in un foglio di lavoro utilizzando l'API di Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Prima di tutto crea un oggetto globale di **CellRange** in modo che possa essere accessibile ovunque nel contesto della tua classe
- Crea un gestore di eventi per l'evento **SelectedCellRangeChanged** di **GridDesktop**. L'evento **SelectedCellRangeChanged** viene attivato ogni volta che viene modificata la selezione di celle da parte di un utente. Ad esempio, se un utente seleziona celle (contenenti dati da ordinare) allora ogni volta che la sua selezione cambierebbe, questo evento verrebbe attivato.
- Il gestore di eventi fornisce l'argomento **CellRangeEventArgs** che fornisce ulteriori informazioni sull'intervallo di celle (selezionato dall'utente) sotto forma di un oggetto **CellRange**. Quindi, in questo gestore di eventi, assegneremo questo oggetto **CellRange** (contenente l'intervallo di celle aggiornato) all'oggetto globale **CellRange** in modo che possa essere utilizzato anche in altre parti del codice. Per assicurarci di non perdere l'intervallo di celle, scriveremo il codice del gestore eventi all'interno di una condizione
- Ora possiamo scrivere del codice per ordinare i dati del foglio di lavoro. Per prima cosa, accedi a un foglio di lavoro desiderato
- Crea un oggetto **SortRange** che conserverà l'intervallo di celle di cui ordinare i dati. Nel costruttore di **SortRange**, possiamo specificare il foglio di lavoro, gli indici della riga e della colonna di inizio, il numero di righe e colonne da ordinare, l'orientamento dell'ordinamento (come dall'alto verso il basso o da sinistra a destra) ecc.
- Ora possiamo chiamare il metodo **Sort** dell'oggetto **SortRange** per eseguire l'ordinamento dei dati. Nel metodo **Sort**, possiamo specificare l'indice della colonna o della riga da ordinare e l'ordine di ordinamento (che può essere **Crescente** o **Decrescente** secondo le tue esigenze)
- Infine, possiamo chiamare il metodo **Invalidate** di **GridDesktop** per ridisegnare le celle.

Nell'esempio qui sotto, abbiamo dimostrato come ordinare i dati in una colonna.

Crea un oggetto globale di CellRange e l'evento **SelectedCellRangeChanged** di GridDesktop. Ora scrivi il codice come indicato di seguito:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


Ora scriviamo il metodo per **Ordinamento Ascendente**. Puoi creare un pulsante per **Ordinamento Ascendente** e scrivere il codice seguente all'interno del suo evento **Click**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


Infine, scriviamo del codice per ottenere la funzionalità di **Ordinamento Decrescente**. Crea un pulsante per **Ordinamento Decrescente** e scrivi il codice indicato all'interno del suo evento **Click**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
