---
title: Carica il Documento di Lavoro con il Formato Carta del Stampante Specificato
type: docs
weight: 430
url: /it/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Puoi specificare la dimensione della carta della stampante di tua scelta durante il caricamento del tuo workbook usando il metodo [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Si noti che, se si crea un nuovo file in MS Excel, la dimensione della carta sarà uguale a quella impostata sulla stampante predefinita del tuo dispositivo.

{{% /alert %}}

Il seguente esempio di codice illustra l’uso del metodo [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Inizia creando un workbook e poi lo salva in un flusso di memoria in formato XLSX. Successivamente, lo carica con dimensione carta A5 e lo salva in formato PDF. Poi, lo ricarica con dimensione carta A3 e lo salva di nuovo in formato PDF. Se apri i PDF di output e controlli le dimensioni della carta, vedrai che sono diverse. Uno è A5 e l’altro A3. Scarica i PDF di output [A5](PrinterSize-a5_out.pdf) e [A3](PrinterSize-a3_out.pdf) generati dal codice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
