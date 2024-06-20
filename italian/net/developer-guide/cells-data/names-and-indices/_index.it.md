---
title: Conversione tra nome della cella e indice riga/colonna
linktitle: Nome della Cella e Conversione Indice
type: docs
weight: 10
url: /it/net/names-and-indices/
description: Scopri come ottenere la conversione tra nome della cella e indice riga/colonna tramite l API Aspose.Cells for .NET.
keywords: Ottieni il nome della cella dagli indici di riga e colonna, Ottieni gli indici di riga e colonna dal nome della cella, Crea nomi di fogli di lavoro sicuri, Aggiungi nomi di fogli di lavoro sicuri
---

## **Ottieni il Nome della Cella dagli Indici di Riga e Colonna**
È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come fare.
Aspose.Cells fornisce il metodo CellsHelper.CellIndexToName che consente ai developer di ottenere il nome di una cella se forniscono l'indice di riga e colonna.

{{% alert color="primary" %}} 

A differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente mostra come utilizzare CellsHelper.CellIndexToName per accedere al nome della cella dato un indice di riga e colonna noto. Il codice genera l'output seguente.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Ottieni Gli Indici di Riga e Colonna dal Nome della Cella**
È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.
Aspose.Cells fornisce il metodo CellsHelper.CellNameToIndex che consente ai developer di ottenere gli indici di riga e colonna dal nome della cella.

{{% alert color="primary" %}} 

A differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente mostra come utilizzare CellsHelper.CellNameToIndex per ottenere gli indici di riga e colonna dal nome della cella. Il codice genera l'output seguente.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Crea nomi di foglio sicuri**
A volte c'è bisogno di assegnare il nome del foglio a tempo di esecuzione. In questo scenario, potrebbero esserci nomi di fogli che possono contenere alcuni caratteri aggiuntivi come <>+(?”. C'è bisogno di sostituire qualsiasi tale carattere, che non è consentito come nome del foglio, con un determinato carattere preimpostato fornito dall'utente. Allo stesso modo, la lunghezza può aumentare a più di 31 caratteri che devono essere troncati. Apache POI fornisce alcune funzionalità di creazione di nomi sicuri, quindi una funzionalità simile è fornita da Aspose.Cells per gestire tutti questi problemi. Il codice di esempio seguente illustra questa funzionalità:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Output:

questo è il primo nome che viene cre

` `<> + (adj.Private _ " Privato"
