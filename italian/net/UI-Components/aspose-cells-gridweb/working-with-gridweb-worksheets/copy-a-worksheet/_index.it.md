---
title: Copia un Foglio di Lavoro
type: docs
weight: 50
url: /it/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb,copia,GridWorksheet
description: Questo articolo introduce come copiare un foglio di lavoro (GridWorksheet) in GridWeb.
---

{{% alert color="primary" %}} 

[Aggiungere fogli di lavoro](/cells/it/net/aspose-cells-gridweb/add-worksheets/) descrive come aggiungere nuovi fogli di lavoro a Aspose.Cells.GridWeb. È inoltre possibile aggiungere una copia o replica di un altro foglio di lavoro al controllo Aspose.Cells.GridWeb. Questa funzionalità può essere utile quando dati identici o simili in un foglio di lavoro sono richiesti anche in un altro foglio di lavoro. In tal caso, è più facile copiare un foglio di lavoro esistente e aggiungerlo ad Aspose.Cells.GridWeb come nuovo foglio di lavoro invece di crearlo da zero.

{{% /alert %}} 
## **Copiare un Foglio di Lavoro**
### **Utilizzo dell'indice del foglio**
Il codice di esempio qui sotto mostra come aggiungere una copia di un foglio di lavoro al controllo GridWeb specificando l'indice del foglio di lavoro nel metodo AddCopy di GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Utilizzo del nome del foglio**
Il codice di esempio qui sotto mostra come aggiungere una copia di un foglio di lavoro al controllo GridWeb specificando il nome del foglio di lavoro nel metodo AddCopy di GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

Il metodo AddCopy restituisce l'indice del nuovo foglio di lavoro aggiunto che può essere utilizzato per accedere all'istanza del foglio di lavoro. Per ulteriori dettagli su come accedere ai fogli di lavoro, leggere [Accedere ai fogli di lavoro](/cells/it/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}}
