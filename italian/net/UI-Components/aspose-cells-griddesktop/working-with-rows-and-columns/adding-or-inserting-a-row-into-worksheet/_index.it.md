---
title: Aggiunta o inserimento di una riga nel foglio di lavoro
type: docs
weight: 30
url: /it/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

Simile a uno dei nostri argomenti precedenti, questo argomento descrive la funzionalità di aggiunta e inserimento di righe nei fogli di lavoro in fase di esecuzione utilizzando l'API di Aspose.Cells.GridDesktop. La differenza fondamentale tra addizione e inserimento è che, inoltre, viene aggiunta una riga alla fine della raccolta di righe del foglio di lavoro dove, come nell'inserimento, è possibile aggiungere una riga in qualsiasi posizione specificata nel foglio di lavoro.

{{% /alert %}} 
## **Aggiunta di una riga al foglio di lavoro**
Per aggiungere una nuova riga al foglio di lavoro, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Aggiungere**Riga** al**Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Inserimento di una riga nel foglio di lavoro**
Per inserire una nuova riga nel foglio di lavoro in una posizione specificata, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Inserire**Riga** in**Foglio di lavoro**(in una posizione specifica specificando l'indice della riga dove inserirlo)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
