---
title: Carica il Documento di Lavoro con il Formato Carta del Stampante Specificato
type: docs
weight: 430
url: /it/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

È possibile specificare la dimensione della carta della stampante desiderata durante il caricamento del libro di lavoro utilizzando il metodo [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Si noti che se si crea un nuovo file in MS Excel, si noterà che la dimensione della carta è la stessa dell'impostazione della stampante predefinita nel computer.

{{% /alert %}}

Il codice di esempio seguente illustra l'utilizzo del metodo [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Prima crea un workbook, poi lo salva in una memory stream in formato XLSX. Successivamente lo carica con la dimensione di carta A5 e lo salva in formato PDF. Quindi lo carica nuovamente con la dimensione di carta A3 e lo salva di nuovo in formato PDF. Se apri i PDF di output e controlli le dimensioni della carta, vedrai che sono diverse. Una è A5 e l'altra è A3. Per favore scarica il [PDF di output A5](PrinterSize-a5_out.pdf) e il [PDF di output A3](PrinterSize-a3_out.pdf) generati dal codice per il tuo riferimento.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
