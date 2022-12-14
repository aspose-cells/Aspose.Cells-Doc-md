---
title: Carica la cartella di lavoro con il formato carta della stampante specificato
type: docs
weight: 790
url: /it/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

 È possibile specificare il formato della carta della stampante di propria scelta durante il caricamento della cartella di lavoro utilizzando il file[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) metodo. Si prega di notare che, se si crea un nuovo file in MS Excel, si noterà che il formato della carta è lo stesso dell'impostazione della stampante predefinita nella macchina.

{{% /alert %}} 
## **Carica la cartella di lavoro con il formato carta della stampante specificato**
 Il codice di esempio seguente illustra l'utilizzo di[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\) metodo. Prima crea una cartella di lavoro, quindi la salva in un flusso di array di byte in formato XLSX. Quindi lo carica con carta formato A5 e lo salva in formato PDF. Quindi lo carica di nuovo con formato carta A3 e lo salva nuovamente in formato PDF. Se apri i PDF di output e controlli il loro formato carta, vedrai che sono diversi. Uno è A5 e l'altro è A3. Si prega di scaricare il[PDF di uscita A5](5473435.pdf) e[PDF di uscita A3](5473436.pdf) generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
