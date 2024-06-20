---
title: Unire e separare celle in GridDesktop
linktitle: Unione e separazione di celle
type: docs
weight: 90
url: /it/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop, unire, separare
description: Questo articolo introduce l unione e la separazione in GridDesktop.
---

{{% alert color="primary" %}} 

In questo argomento, discuteremo una funzione di utilità di unire e separare celle di un foglio di lavoro. Questa funzione è utile nei casi in cui è necessario estendere alcune righe o colonne per migliorare la leggibilità dei dati.

{{% /alert %}} 
## **Unisci celle**
Per unire celle in un'unica grande cella, seguire i passaggi seguenti:

- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Creare un **Intervallo di celle** da unire
- **Unire** l'intervallo di celle in una grande cella

È possibile utilizzare il metodo **Unire** di **Foglio di lavoro** per unire le celle. Tuttavia, un intervallo di celle può essere definito utilizzando l'oggetto **CellRange**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Separare celle**
Per separare una grande cella in molte celle, seguire i passaggi seguenti:

- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Accedere alla cella unita che deve essere divisa in più celle
- **Dividere** la grande cella in molte celle utilizzando la posizione della cella unita

È possibile utilizzare il metodo **Dividi** di **Foglio di lavoro** per dividere una cella utilizzando la sua posizione.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Quando si uniscono celle in una singola cella, le impostazioni di formattazione della cella in alto a sinistra (nell'intervallo di celle) vengono applicate alla cella unita, ma quando la cella viene divisa, tutte le celle divise mantengono le impostazioni di formattazione.

{{% /alert %}}
