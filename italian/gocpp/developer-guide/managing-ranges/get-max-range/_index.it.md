---
title: Ottieni l intervallo massimo in un foglio di lavoro con Golang tramite C++
linktitle: Ottieni Max Range In Un Foglio di Lavoro
type: docs
weight: 360
url: /it/go-cpp/get-max-range-in-a-worksheet/
description: Questo articolo descrive come ottenere il range massimo, il massimo intervallo di dati, il massimo intervallo di visualizzazione dei file Excel con la libreria Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Quando si leggono i dati dal foglio di lavoro, è necessario conoscere l'area massima.

Quando si copiano tutti i dati da un foglio di lavoro, è necessario conoscere l'area massima.

Quando esportiamo un'area specificata in HTML e PDF, dobbiamo conoscere l'area massima.

Aspose.Cells for C++ contiene diversi modi per trovare il range massimo in un foglio di lavoro. 

{{% /alert %}} 

## **Ottenere l'intervallo massimo**
In Aspose.Cells, se gli oggetti [**Row**](https://reference.aspose.com/cells/go-cpp/row/) e [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) sono inizializzati, queste righe e colonne verranno conteggiate per l'area massima, anche se non ci sono dati nelle righe o colonne vuote.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange.go" >}}
## **Ottieni il massimo intervallo di dati**
Nella maggior parte dei casi, abbiamo solo bisogno di ottenere tutti i range contenenti tutti i dati, anche se le celle vuote al di fuori del range sono formattate.
E le impostazioni su forme, tabelle e tabelle pivot verranno ignorate.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-1.go" >}}
## **Ottieni l'intervallo massimo di visualizzazione**
Quando esportiamo tutti i dati dal foglio di lavoro in HTML, PDF o immagini, dobbiamo ottenere un'area che contenga tutti gli oggetti visibili, inclusi dati, stili, grafici, tabelle e tabelle pivot.
I seguenti codici mostrano come rendere l'intervallo di visualizzazione massimo in HTML:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-2.go" >}}
Ecco il [file excel di origine](Book1.xlsx).
