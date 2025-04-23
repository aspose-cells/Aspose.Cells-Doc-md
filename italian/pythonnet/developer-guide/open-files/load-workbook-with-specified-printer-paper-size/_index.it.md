---
title: Carica il Documento di Lavoro con il Formato Carta del Stampante Specificato
type: docs
weight: 430
url: /it/python-net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

È possibile specificare la dimensione della carta della stampante desiderata durante il caricamento del libro di lavoro utilizzando il metodo [**LoadOptions.set_paper_size()**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/set_paper_size). Si noti che se si crea un nuovo file in MS Excel, si noterà che la dimensione della carta è la stessa dell'impostazione della stampante predefinita nel computer.

{{% /alert %}}

Il seguente codice di esempio illustra l'uso del metodo [**LoadOptions.set_paper_size()**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/set_paper_size). Prima crea un libro di lavoro, quindi lo salva in memoria in formato XLSX. Poi lo carica con la dimensione della carta A5 e lo salva in formato PDF. Poi lo ricarica di nuovo con la dimensione della carta A3 e lo salva nuovamente in formato PDF. Se si apre i PDF di output e si controlla la dimensione della carta, si vedrà che sono diversi. Uno è A5 e l'altro è A3. Si prega di scaricare il [PDF di output A5](5115234.pdf) e [PDF di output A3](5115233.pdf) generato dal codice come riferimento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-LoadWorkbookWithPrinterSize-1.py" >}}

