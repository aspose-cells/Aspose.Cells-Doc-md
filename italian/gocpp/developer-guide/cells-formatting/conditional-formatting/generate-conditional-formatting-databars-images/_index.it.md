---
title: Genera immagini delle barre dati di formattazione condizionale con Golang tramite C++
linktitle: Genera immagini di formattazione condizionale DataBars
description: Aspose.Cells è una libreria C++ per lavorare con i file di fogli di calcolo. Supporta la generazione di barre dati e immagini formattate condizionatamente, permettendo agli utenti di personalizzare la visualizzazione del foglio di calcolo in base al valore delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per generare barre dati e immagini formattate condizionatamente.
keywords: Aspose.Cells, Formattazione Condizionale, Barre di Dati, Immagini, Fogli di Calcolo
type: docs
weight: 40
url: /it/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A volte è necessario generare immagini delle barre di dati formattate condizionalmente. È possibile utilizzare il [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) metodo di Aspose.Cells per generare queste immagini. Questo articolo mostra come generare un'immagine di DataBar utilizzando Aspose.Cells.

{{% /alert %}}

Il seguente esempio di codice genera l'immagine DataBar della cella C1. Prima accede all'oggetto condizione di formato della cella, e da quell'oggetto, accede all'oggetto [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/) e usa il suo metodo [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) per generare l'immagine della cella. Infine, salva l'immagine sul disco.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
