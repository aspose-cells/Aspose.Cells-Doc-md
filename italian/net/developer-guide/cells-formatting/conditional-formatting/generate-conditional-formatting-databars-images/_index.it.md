---
title: Genera immagini di formattazione condizionale DataBars
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli elettronici. Supporta la generazione di barre di dati e immagini formattate condizionalmente, consentendo agli utenti di personalizzare la visualizzazione del foglio elettronico in base al valore delle celle. Questo articolo introdurrà come utilizzare la libreria Aspose.Cells per generare barre di dati e immagini formattate condizionalmente.
keywords: Aspose.Cells, Formattazione Condizionale, Barre di Dati, Immagini, Fogli di Calcolo
type: docs
weight: 40
url: /it/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A volte è necessario generare immagini delle barre di dati formattate condizionalmente. È possibile utilizzare il [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) metodo di Aspose.Cells per generare queste immagini. Questo articolo mostra come generare un'immagine di DataBar utilizzando Aspose.Cells.

{{% /alert %}}

Il seguente codice di esempio genera l'immagine DataBar della cella C1. Prima, accede all'oggetto della condizione di formato della cella, e poi da quell'oggetto, accede all'oggetto [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) e utilizza il suo metodo [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) per generare l'immagine della cella. Infine, salva l'immagine sul disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
