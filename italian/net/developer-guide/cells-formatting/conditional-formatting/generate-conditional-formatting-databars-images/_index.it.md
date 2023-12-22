---
title: Genera immagini DataBars con formattazione condizionale
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo. Supporta la generazione di barre dati e immagini formattate in modo condizionale, consentendo agli utenti di personalizzare la visualizzazione del foglio di calcolo in base al valore delle celle. Questo articolo introdurrà come utilizzare la libreria Aspose.Cells per generare barre dati e immagini con formattazione condizionale.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /it/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 A volte, è necessario generare immagini di DataBars con formattazione condizionale. Puoi usare lo Aspose.Cells[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) metodo per generare queste immagini. Questo articolo mostra come generare un'immagine DataBar utilizzando Aspose.Cells.

{{% /alert %}}

 Il seguente codice di esempio genera l'immagine DataBar della cella C1. Innanzitutto accede all'oggetto condizione di formato della cella, quindi da quell'oggetto accede a[**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) oggetto e usa il suo[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)metodo per generare l'immagine della cella. Infine, salva l'immagine su disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
