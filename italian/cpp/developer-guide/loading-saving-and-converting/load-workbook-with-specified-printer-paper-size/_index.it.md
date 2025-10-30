---
title: Carica il Documento di Lavoro con il Formato Carta del Stampante Specificato
type: docs
weight: 430
url: /it/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

È possibile specificare la dimensione della carta della stampante desiderata durante il caricamento del libro di lavoro utilizzando il metodo [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Si noti che se si crea un nuovo file in MS Excel, si noterà che la dimensione della carta è la stessa dell'impostazione della stampante predefinita nel computer.

{{% /alert %}}

Il seguente esempio di codice illustra l'uso del metodo [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Prima crea un workbook, quindi lo salva in memoria in formato XLSX. Successivamente lo carica con dimensione A5 e lo salva in formato PDF. Poi lo ricarica con dimensione A3 e lo salva ancora in PDF. Se apri i PDF di output e controlli le dimensioni della carta, vedrai che sono diverse. Uno è A5 e l'altro A3. Scarica i PDF di output [A5](PrinterSize-a5_out.pdf) e [A3](PrinterSize-a3_out.pdf) generati dal codice per riferimento.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
