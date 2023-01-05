---
title: Ridimensiona righe e colonne
type: docs
weight: 30
url: /it/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

A volte i valori delle celle sono più larghi della cella in cui si trovano o si trovano su più righe. Tali valori non sono completamente visibili agli utenti a meno che non modifichino l'altezza e la larghezza di righe e colonne. Aspose.Cells.GridWeb supporta completamente l'impostazione dell'altezza delle righe e della larghezza delle colonne. Questo argomento discute queste funzionalità in dettaglio con l'aiuto di esempi.

{{% /alert %}} 
## **Lavorare con l'altezza delle righe e la larghezza delle colonne**
### **Impostazione dell'altezza della riga**
Per impostare l'altezza di una riga:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi alla raccolta Cells del foglio di lavoro.
1. Imposta l'altezza di tutte le celle in qualsiasi riga specificata.

{{% alert color="primary" %}} 

Il metodo SetRowHeight e SetColumnWidth della raccolta Cells dispone anche di varianti disponibili per impostare le misure dell'altezza della riga e della larghezza della colonna in pollici e pixel.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **Impostazione della larghezza della colonna**
Per impostare la larghezza di una colonna:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi alla raccolta Cells del foglio di lavoro.
1. Imposta la larghezza di tutte le celle in qualsiasi colonna specificata.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
