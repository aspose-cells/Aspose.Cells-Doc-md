---
title: Unisci e separa Cells
type: docs
weight: 60
url: /it/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb ha una pratica funzione di utilità che ti consente di unire le celle in una cella grande. In questo argomento viene descritto come unire le celle a livello di codice.

{{% /alert %}} 
## **Fusione Cells**
Unisci più celle in un foglio di lavoro in una singola cella chiamando il metodo Merge della raccolta Cells. Specificare l'intervallo di celle da unire quando si chiama il metodo Merge.

{{% alert color="primary" %}} 

Se unisci più celle e ogni cella contiene dati, dopo l'unione viene mantenuto solo il contenuto della cella in alto a sinistra nell'intervallo. I dati nelle altre celle non vengono persi. Se dividi le celle, ogni cella recupera i propri dati.

{{% /alert %}} 

**Quattro celle unite in una** 

![cose da fare:immagine_alt_testo](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Disaggregabile Cells**
Per separare le celle, utilizzare il metodo UnMerge della raccolta Cells che accetta gli stessi parametri del metodo Merge ed esegue la separazione delle celle.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
