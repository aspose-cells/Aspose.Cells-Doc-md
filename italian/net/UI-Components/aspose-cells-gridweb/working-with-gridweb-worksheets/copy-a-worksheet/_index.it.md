---
title: Copia un foglio di lavoro
type: docs
weight: 50
url: /it/net/copy-a-worksheet/
---
{{% alert color="primary" %}} 

[Aggiungi fogli di lavoro](/cells/it/net/add-worksheets/) descrive come aggiungere nuovi fogli di lavoro a Aspose.Cells.GridWeb. È anche possibile aggiungere una copia (o replica) di un altro foglio di lavoro al controllo Aspose.Cells.GridWeb. Questa funzione può essere utile quando dati identici o simili in un foglio di lavoro sono richiesti anche in un altro foglio di lavoro. In tal caso, è più semplice copiare un foglio di lavoro esistente e aggiungerlo a Aspose.Cells.GridWeb come nuovo foglio di lavoro anziché crearlo da zero.

{{% /alert %}} 
## **Copiare un foglio di lavoro**
### **Utilizzo dell'indice del foglio**
Il codice di esempio seguente mostra come aggiungere una copia di un foglio di lavoro al controllo GridWeb specificando l'indice del foglio di lavoro nel metodo AddCopy di GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Utilizzo del nome del foglio**
Il codice di esempio seguente mostra come aggiungere una copia di un foglio di lavoro al controllo GridWeb specificando il nome del foglio di lavoro nel metodo AddCopy di GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

 Il metodo AddCopy restituisce l'indice del foglio di lavoro appena aggiunto che può essere utilizzato per accedere all'istanza del foglio di lavoro. Per maggiori dettagli su come accedere ai fogli di lavoro, leggi[Accedi ai fogli di lavoro](/cells/it/net/access-worksheets/).

{{% /alert %}}
