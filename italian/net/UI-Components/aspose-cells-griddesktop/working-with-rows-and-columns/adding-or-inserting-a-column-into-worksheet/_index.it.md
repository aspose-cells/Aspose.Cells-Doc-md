---
title: Aggiunta o inserimento di una colonna nel foglio di lavoro
type: docs
weight: 10
url: /it/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

In questo argomento, descriveremo la funzionalità di base dell'aggiunta e dell'inserimento di colonne nei fogli di lavoro in fase di esecuzione utilizzando l'API di Aspose.Cells.GridDesktop. La differenza fondamentale tra addizione e inserimento è che inoltre, la colonna viene aggiunta alla fine della raccolta di colonne del foglio di lavoro dove, come nell'inserimento, la colonna può essere aggiunta a qualsiasi posizione specificata nel foglio di lavoro.

{{% /alert %}} 
## **Aggiunta di una colonna al foglio di lavoro**
Per aggiungere una nuova colonna al foglio di lavoro, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Aggiungere**Colonna** al**Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Inserimento di una colonna nel foglio di lavoro**
Per inserire una nuova colonna nel foglio di lavoro in una posizione specificata, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Inserire**Colonna** in**Foglio di lavoro** (in una posizione specifica specificando l'indice della colonna dove inserirlo)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
