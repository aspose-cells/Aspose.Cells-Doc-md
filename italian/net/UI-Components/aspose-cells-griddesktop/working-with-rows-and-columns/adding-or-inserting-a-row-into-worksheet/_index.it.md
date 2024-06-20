---
title: Aggiunta o Inserimento di una Riga nel Foglio di lavoro
type: docs
weight: 30
url: /it/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: Questo articolo presenta come aggiungere o inserire una riga in GridDesktop.
---

{{% alert color="primary" %}} 

Simile a uno dei nostri argomenti precedenti, questo argomento descrive la funzionalità di aggiunta e inserimento di righe nei fogli di lavoro in fase di esecuzione utilizzando l'API di Aspose.Cells.GridDesktop. La differenza fondamentale tra l'aggiunta e l'inserimento è che nell'aggiunta, una riga viene aggiunta alla fine della collezione di righe del foglio di lavoro, mentre nell'inserimento, una riga può essere aggiunta in qualsiasi posizione specificata nel foglio di lavoro.

{{% /alert %}} 
## **Aggiunta di una Riga al Foglio di lavoro**
Per aggiungere una nuova riga al foglio di lavoro, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Aggiungi una **Riga** al **Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Inserimento di una Riga nel Foglio di lavoro**
Per inserire una nuova riga nel foglio di lavoro in una posizione specificata, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Inserisci **riga** in **foglio di lavoro** (in una posizione specifica specificando l'indice della riga in cui inserirla)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
