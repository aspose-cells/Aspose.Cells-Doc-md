---
title: Convertire il testo in colonne usando Aspose.Cells
type: docs
weight: 70
url: /it/java/convert-text-to-columns-using-aspose-cells/
---

## **Possibili Scenari di Utilizzo**
Puoi convertire il testo in colonne usando Microsoft Excel. Questa funzionalità è disponibile sotto *Data Tools* nel tab *Data*. Per dividere i contenuti di una colonna in più colonne, i dati devono contenere un delimitatore specifico come una virgola (o altro carattere) in base al quale Microsoft Excel divide i contenuti di una cella in più celle. Anche Aspose.Cells fornisce questa funzionalità tramite il metodo [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-).
## **Converti testo in colonne utilizzando Aspose.Cells**
Il seguente esempio di codice illustra l'uso del metodo [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-). Il codice prima aggiunge alcuni nomi di persone nella colonna A del primo foglio di lavoro. Il nome e il cognome sono separati da uno spazio. Successivamente applica il metodo [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) sulla colonna A e lo salva come file Excel di output. Se apri il file Excel di output [il file](25395230.xlsx), vedrai che i nomi sono in colonna A e i cognomi in colonna B come mostrato in questo screenshot.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}
