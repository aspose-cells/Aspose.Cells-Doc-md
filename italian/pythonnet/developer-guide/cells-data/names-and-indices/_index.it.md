---
title: Conversione tra nome della cella e indice riga/colonna
linktitle: Nome della Cella e Conversione Indice
type: docs
weight: 10
url: /it/python-net/names-and-indices/
description: Scopri come ottenere la conversione tra il nome della cella e l indice riga/colonna tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Python Ottieni il Nome della Cella da Indici Riga e Colonna, Python Ottieni Indici Riga e Colonna dal Nome della Cella, Python Crea nomi di foglio di lavoro sicuri, Python Aggiungi nomi di foglio di lavoro sicuri
---

## **Ottieni il Nome della Cella dagli Indici di Riga e Colonna**
È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come fare.
Aspose.Cells per Python via .NET fornisce il metodo [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) che consente agli sviluppatori di ottenere il nome di una cella se vengono forniti l'indice riga e colonna.

{{% alert color="primary" %}} 

A differenza di Microsoft Excel, dove gli indici di riga e colonna partono da 1, Aspose.Cells per Python via .NET inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il seguente codice di esempio illustra come utilizzare [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) per accedere al nome della cella dato un indice di riga e colonna noto. Il codice genera l'output seguente.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Ottieni Gli Indici di Riga e Colonna dal Nome della Cella**
È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.
Aspose.Cells per Python via .NET fornisce il metodo [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) che consente agli sviluppatori di ottenere un indice di riga e colonna dal nome della cella.

{{% alert color="primary" %}} 

A differenza di Microsoft Excel, dove gli indici di riga e colonna partono da 1, Aspose.Cells per Python via .NET inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il seguente codice di esempio illustra come utilizzare [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) per ottenere l'indice di riga e colonna dal nome della cella. Il codice genera l'output seguente.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Crea nomi di foglio sicuri**
A volte c'è la necessità di assegnare il nome del foglio a tempo di esecuzione. In questo scenario, possono esserci nomi di foglio che possono contenere alcuni caratteri aggiuntivi come <>+(?”. C'è bisogno di sostituire eventuali caratteri del genere, che non sono consentiti come nome del foglio, con alcuni caratteri preimpostati forniti dall'utente. Allo stesso modo la lunghezza può aumentare a più di 31 caratteri che devono essere troncati. Apache POI fornisce determinate funzionalità per la creazione di nomi sicuri, pertanto una funzione simile è fornita da Aspose.Cells per Python via .NET per gestire tutti questi problemi. Il codice di esempio seguente dimostra questa funzionalità:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Output:

questo è il primo nome che viene cre

` `<> + (adj.Private _ " Privato"
