---
title: Unisci e separa celle
type: docs
weight: 60
url: /it/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb, unisci, separa
description: Questo articolo presenta come unire/dividere le celle in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb dispone di una pratica funzionalità che ti consente di unire le celle in una grande cella. Questo argomento descrive come unire le celle programmatticamente.

{{% /alert %}} 
## **Unione di celle**
Unisci più celle in un foglio di lavoro in una singola cella chiamando il metodo Merge della collezione Cells. Specifica l'intervallo delle celle da unire quando si chiama il metodo Merge.

{{% alert color="primary" %}} 

Se unisci più celle e ciascuna cella contiene dati, solo il contenuto della cella in alto a sinistra nell'intervallo viene mantenuto dopo la fusione. I dati nelle altre celle non vengono persi. Se separi le celle, ciascuna cella recupera i propri dati.

{{% /alert %}} 

**Quattro celle unite in una** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Separazione delle celle**
Per separare le celle, utilizza il metodo UnMerge della collezione Cells che accetta gli stessi parametri del metodo Merge e esegue la separazione delle celle.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
