---
title: Ottieni Max Range In Un Foglio di Lavoro
type: docs
weight: 360
url: /it/net/get-max-range-in-a-worksheet/
description: Questo articolo descrive come ottenere l intervallo massimo, l intervallo massimo dei dati, l intervallo massimo di visualizzazione dei file Excel con Aspose.Cells per la libreria .Net.
---

{{% alert color="primary" %}} 

Quando si leggono i dati dal foglio di lavoro, è necessario conoscere l'area massima.

Quando si copiano tutti i dati da un foglio di lavoro, è necessario conoscere l'area massima.

Quando si esporta un'area specificata in html e pdf, è necessario conoscere l'area massima.

Aspose.Cells per .Net contiene diversi modi per trovare l'intervallo massimo in un foglio di lavoro. 


{{% /alert %}} 



## **Ottenere l'intervallo massimo**
In Aspose.Cells, se gli oggetti [**row**](https://reference.aspose.com/cells/net/aspose.cells/row) e [**column**](https://reference.aspose.com/cells/net/aspose.cells/column) sono inizializzati, queste righe e colonne verranno conteggiate fino all'area massima, anche se non ci sono dati nelle righe o colonne vuote.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **Ottieni il massimo intervallo di dati**
Nella maggior parte dei casi, abbiamo solo bisogno di ottenere tutti i range contenenti tutti i dati, anche se le celle vuote al di fuori del range sono formattate.
E le impostazioni riguardanti forme, tabelle e tabelle pivot saranno ignorate.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **Ottieni l'intervallo massimo di visualizzazione**
Quando esportiamo tutti i dati dal foglio di lavoro in HTML, PDF o immagini, dobbiamo ottenere un'area che contenga tutti gli oggetti visibili, inclusi dati, stili, grafici, tabelle e tabelle pivot.
I seguenti codici mostrano come renderizzare il range di visualizzazione massimo in html:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

Ecco il [file excel di origine](Book1.xlsx).
{{< app/cells/assistant language="csharp" >}}
