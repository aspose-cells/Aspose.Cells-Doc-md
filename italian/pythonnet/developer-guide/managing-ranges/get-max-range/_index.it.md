---
title: Ottieni Max Range In Un Foglio di Lavoro
type: docs
weight: 360
url: /it/python-net/get-max-range-in-a-worksheet/
description: Questo articolo descrive come ottenere il range massimo, il range massimo dei dati, il range di visualizzazione massimo dei file Excel con la libreria Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, ottenere il range massimo, ottenere il range massimo dei dati, ottenere il range massimo di visualizzazione.
---

{{% alert color="primary" %}} 

Quando si leggono i dati dal foglio di lavoro, è necessario conoscere l'area massima.

Quando si copiano tutti i dati da un foglio di lavoro, è necessario conoscere l'area massima.

Quando si esporta un'area specificata in html e pdf, è necessario conoscere l'area massima.

Aspose.Cells for Python via .NET contiene modi diversi per trovare il range massimo in un foglio di lavoro. 


{{% /alert %}} 



## **Come ottenere il range massimo**
In Aspose.Cells for Python via .NET, se gli oggetti [**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) e [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) sono inizializzati, queste righe e colonne verranno conteggiate fino all'area massima, anche se non ci sono dati nelle righe o colonne vuote.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}

## **Come ottenere il range massimo dei dati**
Nella maggior parte dei casi, abbiamo solo bisogno di ottenere tutti i range contenenti tutti i dati, anche se le celle vuote al di fuori del range sono formattate.
E le impostazioni riguardanti forme, tabelle e tabelle pivot saranno ignorate.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}

## **Come ottenere il range massimo di visualizzazione**
Quando esportiamo tutti i dati dal foglio di lavoro in HTML, PDF o immagini, dobbiamo ottenere un'area che contenga tutti gli oggetti visibili, inclusi dati, stili, grafici, tabelle e tabelle pivot.
I seguenti codici mostrano come renderizzare il range di visualizzazione massimo in html:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}

Ecco il [file excel di origine](Book1.xlsx).
{{< app/cells/assistant language="python-net" >}}
