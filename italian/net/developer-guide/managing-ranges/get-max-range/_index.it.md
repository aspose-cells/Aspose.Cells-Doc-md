---
title: Ottieni l'intervallo massimo in un foglio di lavoro
type: docs
weight: 360
url: /it/net/get-max-range-in-a-worksheet/
description: Questo articolo descrive come ottenere l'intervallo massimo, l'intervallo massimo di dati, l'intervallo massimo di visualizzazione dei file Excel con Aspose.Cells per la libreria .Net.
---
{{% alert color="primary" %}} 

Quando leggiamo i dati dal foglio di lavoro, dobbiamo conoscere l'area massima.

Quando copiamo tutti i dati da un foglio di lavoro, dobbiamo conoscere l'area massima.

Quando esportiamo un'area specifica in HTML e PDF, dobbiamo conoscere l'area massima.

 Aspose.Cells per .Net contiene diversi modi per trovare l'intervallo massimo in un foglio di lavoro.


{{% /alert %}} 



##  **Ottenere la portata massima**
 Allo Aspose.Cells, se il[**riga**](https://reference.aspose.com/cells/net/aspose.cells/row) E[**colonna**](https://reference.aspose.com/cells/net/aspose.cells/column) vengono inizializzati gli oggetti, queste righe e colonne verranno conteggiate fino all'area massima, anche se non sono presenti dati nelle righe o colonne vuote.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

##  **Ottenere l'intervallo massimo di dati**
Nella maggior parte dei casi, dobbiamo solo ottenere tutti gli intervalli contenenti tutti i dati, anche se sono formattate le celle vuote all'esterno dell'intervallo.
E le impostazioni relative a forme, tabelle e tabelle pivot verranno ignorate.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

##  **Ottenere il raggio di visualizzazione massimo**
Quando esportiamo tutti i dati dal foglio di lavoro a HTML, PDF o immagini, dobbiamo ottenere un'area contenente tutti gli oggetti visibili, inclusi dati, stili, grafica, tabelle e tabelle pivot.
I seguenti codici mostrano come eseguire il rendering dell'intervallo di visualizzazione massimo in html:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

 Qui è[file Excel di origine](Book1.xlsx).
