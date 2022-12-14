---
title: Converti testo in colonne usando Aspose.Cells
type: docs
weight: 70
url: /it/java/convert-text-to-columns-using-aspose-cells/
---
## **Possibili scenari di utilizzo**
Puoi convertire il tuo testo in colonne usando Microsoft Excel. Questa funzione è disponibile da*Strumenti dati* sotto il*Dati* scheda. Per suddividere il contenuto di una colonna in più colonne, i dati devono contenere un delimitatore specifico come una virgola (o qualsiasi altro carattere) in base al quale Microsoft Excel suddivide il contenuto di una cella in più celle. Aspose.Cells fornisce anche questa funzione tramite[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) metodo.
## **Converti testo in colonne usando Aspose.Cells**
Il codice di esempio seguente illustra l'utilizzo di[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) metodo. Il codice aggiunge prima alcuni nomi di persone nella colonna A del primo foglio di lavoro. Il nome e il cognome sono separati dal carattere spazio. Quindi applica il[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\) ) sulla colonna A e lo salva come file excel di output. Se apri il file[file excel di output](25395230.xlsx), vedrai, i nomi sono nella colonna A mentre i cognomi sono nella colonna B come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](convert-text-to-columns-using-aspose-cells_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
