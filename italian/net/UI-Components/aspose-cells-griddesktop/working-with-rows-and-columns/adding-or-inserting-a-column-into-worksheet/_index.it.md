---
title: Aggiunta o Inserimento di una Colonna nel Foglio di lavoro
type: docs
weight: 10
url: /it/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop, inserire, aggiungere, colonna, inserire colonna, inserire riga
description: Questo articolo introduce come inserire o aggiungere una colonna in GridDesktop.
---

{{% alert color="primary" %}} 

In questo argomento, descriveremo la funzionalità di base dell'aggiunta e dell'inserimento di colonne nei fogli di lavoro in fase di esecuzione utilizzando l'API di Aspose.Cells.GridDesktop. La differenza fondamentale tra l'aggiunta e l'inserimento è che nell'aggiunta, la colonna viene aggiunta alla fine della collezione di colonne del foglio di lavoro, mentre nell'inserimento, la colonna può essere aggiunta in qualsiasi posizione specificata nel foglio di lavoro.

{{% /alert %}} 
## **Aggiunta di una colonna al foglio di lavoro**
Per aggiungere una nuova colonna al foglio di lavoro, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Aggiungi una **Colonna** al **Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Inserimento di una colonna nel Foglio di lavoro**
Per inserire una nuova colonna nel foglio di lavoro in una posizione specificata, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Inserisci una **Colonna** nel **Foglio di lavoro** (in una posizione specifica specificando l'indice della colonna in cui inserirla)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
