---
title: Carica la cartella di lavoro con il formato carta della stampante specificato
type: docs
weight: 430
url: /it/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

 È possibile specificare il formato della carta della stampante di propria scelta durante il caricamento della cartella di lavoro utilizzando il file[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) metodo. Si prega di notare che, se si crea un nuovo file in MS Excel, si troverà che il formato della carta è lo stesso dell'impostazione della stampante predefinita nella macchina.

{{% /alert %}}

 Il codice di esempio seguente illustra l'utilizzo di[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) metodo. Prima crea una cartella di lavoro, quindi la salva nel flusso di memoria in formato XLSX. Quindi lo carica con carta formato A5 e lo salva in formato PDF. Quindi lo carica di nuovo con formato carta A3 e lo salva nuovamente in formato PDF. Se apri i PDF di output e controlli il loro formato carta, vedrai che sono diversi. Uno è A5 e l'altro è A3. Si prega di scaricare il[PDF di uscita A5](5115234.pdf) e[PDF di uscita A3](5115233.pdf) generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
