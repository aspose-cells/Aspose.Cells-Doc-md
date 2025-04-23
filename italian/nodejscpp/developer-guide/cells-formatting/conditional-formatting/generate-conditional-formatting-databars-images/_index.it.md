---
title: Genera immagini di formattazione condizionale DataBars
linktitle: Genera immagini di formattazione condizionale DataBars
description: Aspose.Cells è una libreria Node.js per lavorare con i file di fogli di calcolo. Supporta la generazione di barre di dati e immagini formattate condizionatamente, consentendo agli utenti di personalizzare la visualizzazione del foglio di calcolo in base al valore delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per generare barre di dati e immagini condizionalmente formattate.
keywords: Aspose.Cells, Formattazione condizionale, Barre di dati, Immagini, Fogli di calcolo, Node.js tramite C++
type: docs
weight: 40
url: /it/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A volte è necessario generare immagini delle barre di dati formattate condizionalmente. È possibile utilizzare il [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) metodo di Aspose.Cells per generare queste immagini. Questo articolo mostra come generare un'immagine di DataBar utilizzando Aspose.Cells.

{{% /alert %}}

Il seguente esempio di codice genera l'immagine DataBar della cella C1. Prima accede all'oggetto condizione di formato della cella, e da quell'oggetto, accede all'oggetto [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar) e usa il suo metodo [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) per generare l'immagine della cella. Infine, salva l'immagine sul disco.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

