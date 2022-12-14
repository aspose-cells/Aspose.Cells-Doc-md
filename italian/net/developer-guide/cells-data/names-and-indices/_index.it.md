---
title: Conversione tra nome cella e indice riga/colonna
linktitle: Cell Conversione Nome e Indice
type: docs
weight: 10
url: /it/net/names-and-indices/
---
## **Ottieni il nome Cell dagli indici di riga e colonna**
È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come.
Aspose.Cells fornisce il metodo CellsHelper.CellIndexToName che consente agli sviluppatori di ottenere il nome di una cella se forniscono l'indice di riga e colonna.

{{% alert color="primary" %}} 

differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente illustra come utilizzare CellsHelper.CellIndexToName per accedere al nome della cella in base a un indice di riga e colonna noto. Il codice genera il seguente output.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Ottieni gli indici di riga e colonna dal nome Cell**
È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.
Aspose.Cells fornisce il metodo CellsHelper.CellNameToIndex che consente agli sviluppatori di ottenere un indice di riga e colonna dal nome della cella.

{{% alert color="primary" %}} 

differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente illustra come utilizzare CellsHelper.CellNameToIndex per ottenere l'indice di riga e colonna dal nome della cella. Il codice genera il seguente output.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Crea nomi di fogli sicuri**
 A volte è necessario assegnare il nome del foglio in fase di esecuzione. In questo scenario, potrebbero esserci nomi di fogli che potrebbero contenere alcuni caratteri aggiuntivi come<>+(?". È necessario sostituire qualsiasi carattere di questo tipo, che non è consentito come nome di un foglio, con un carattere preimpostato fornito dall'utente. Allo stesso modo, la lunghezza può aumentare fino a superare i 31 caratteri che devono essere troncati. Apache POI fornisce alcune funzionalità di creazione di nomi sicuri, quindi funzionalità simili sono fornite da Aspose.Cells per gestire tutti questi problemi.Il seguente codice di esempio dimostra questa funzionalità:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Produzione:

questo è il nome che è cre

` `<> + (agg.Privato _ "Privato"
