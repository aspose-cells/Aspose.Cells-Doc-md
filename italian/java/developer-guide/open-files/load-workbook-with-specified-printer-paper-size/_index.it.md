---
title: Carica il Documento di Lavoro con il Formato Carta del Stampante Specificato
type: docs
weight: 790
url: /it/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

È possibile specificare il formato carta del stampante desiderato durante il caricamento del documento di lavoro utilizzando il metodo [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). Si noti che se si crea un nuovo file in MS Excel, si troverà che il formato carta è lo stesso dell'impostazione del stampante predefinito nel computer.

{{% /alert %}} 
## **Carica il libro di lavoro con il formato di carta della stampante specificato**
Il codice di esempio seguente illustra l'uso del metodo [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). Prima crea un documento di lavoro, lo salva in un flusso di byte in formato XLSX. Poi lo carica con formato carta A5 e lo salva in formato PDF. Dopo, lo carica nuovamente con formato carta A3 e lo salva ancora in formato PDF. Se apri i PDF di output e controlli il formato carta, vedrai che sono diversi. Uno è A5 e l'altro è A3. Si prega di scaricare i PDF di output [A5](5473435.pdf) e [A3](5473436.pdf) generati dal codice per il tuo riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
