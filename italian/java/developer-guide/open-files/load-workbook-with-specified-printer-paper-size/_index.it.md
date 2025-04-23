---
title: Carica il Documento di Lavoro con il Formato Carta del Stampante Specificato
type: docs
weight: 790
url: /it/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Puoi specificare la dimensione della carta della stampante di tua scelta durante il caricamento del workbook usando il metodo [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Nota che, se crei un nuovo file in MS Excel, la dimensione della carta sarà la stessa impostata sulla stampante predefinita del tuo dispositivo.

{{% /alert %}} 
## **Carica il libro di lavoro con il formato di carta della stampante specificato**
Il seguente esempio di codice illustra l'uso del metodo [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Innanzitutto crea un workbook, quindi lo salva in un stream di byte in formato XLSX. Successivamente lo carica con formato carta A5 e lo salva in formato PDF. Poi lo ricarica con formato A3 e lo salva nuovamente in PDF. Se apri i PDF di output e controlli la loro dimensione di stampa, vedrai che sono diversi. Uno è A5 e l'altro A3. Puoi scaricare i PDF di output [A5](5473435.pdf) e [A3](5473436.pdf) generati dal codice come riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
