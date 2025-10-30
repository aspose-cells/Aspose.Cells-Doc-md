---
title: Conversione tra nome della cella e indice riga/colonna
linktitle: Nome della Cella e Conversione Indice
type: docs
weight: 10
url: /it/nodejs-cpp/names-and-indices/
description: Impara come ottenere la Conversione tra nome della cella e indice riga/colonna tramite l API Aspose.Cells for Node.js via C++.
keywords: Node.js via C++ Ottieni il nome della cella dagli indici di riga e colonna, Ottieni indici di riga e colonna dal nome della cella, Crea nomi di fogli di lavoro sicuri, Aggiungi nomi di fogli di lavoro sicuri
---

## **Ottieni il Nome della Cella dagli Indici di Riga e Colonna**
È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come fare.
Aspose.Cells for Node.js via C++ fornisce il metodo CellsHelper.cellIndexToName che permette agli sviluppatori di ottenere il nome di una cella se forniscono l'indice di riga e colonna.

{{% alert color="primary" %}} 

Microsoft Excel inizia a contare gli indici di riga e colonna da 1. A differenza di Microsoft Excel, Aspose.Cells for Node.js via C++ inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente illustra come utilizzare CellsHelper.cellIndexToName per accedere al nome della cella dato un noto indice di riga e colonna. Il codice genera il seguente output.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **Ottieni Gli Indici di Riga e Colonna dal Nome della Cella**
È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.
Aspose.Cells for Node.js via C++ fornisce il metodo CellsHelper.cellNameToIndex che permette agli sviluppatori di ottenere un indice di riga e colonna dal nome della cella.

{{% alert color="primary" %}} 

Microsoft Excel inizia a contare gli indici di riga e colonna da 1. A differenza di Microsoft Excel, Aspose.Cells for Node.js via C++ inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente illustra come utilizzare CellsHelper.cellNameToIndex per ottenere l'indice di riga e colonna dal nome della cella. Il codice genera il seguente output.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **Crea nomi di foglio sicuri**
A volte è necessario assegnare il nome del foglio di lavoro in fase di esecuzione. In questo scenario, potrebbero esserci nomi di fogli che contengono caratteri aggiuntivi come <>+(?”. È necessario sostituire tali caratteri, non ammessi come nomi di fogli, con un carattere predefinito fornito dall'utente. Allo stesso modo, la lunghezza potrebbe superare i 31 caratteri e deve essere troncata. Apache POI offre alcune funzioni per creare nomi sicuri, e una funzionalità simile è fornita da Aspose.Cells for Node.js via C++ per gestire tutte queste questioni. Il codice di esempio seguente dimostra questa funzionalità:



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

Output:

questo è il primo nome che viene cre

` `<> + (adj.Private _ " Privato"
{{< app/cells/assistant language="nodejs-cpp" >}}
