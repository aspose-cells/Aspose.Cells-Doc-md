---
title: Convertire il testo in colonne usando Aspose.Cells
type: docs
weight: 70
url: /it/java/convert-text-to-columns-using-aspose-cells/
---

## **Possibili Scenari di Utilizzo**
Puoi convertire il tuo Testo in Colonne utilizzando Microsoft Excel. Questa funzionalità è disponibile da *Strumenti Dati* nella scheda *Dati*. Per suddividere i contenuti di una colonna in più colonne, i dati devono contenere un delimitatore specifico come una virgola (o qualsiasi altro carattere) in base al quale Microsoft Excel suddivide i contenuti di una cella in colonne multiple. Anche Aspose.Cells fornisce questa funzionalità tramite il metodo [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)).
## **Converti testo in colonne utilizzando Aspose.Cells**
Il seguente codice di esempio spiega l'utilizzo del metodo [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)). Il codice aggiunge prima dei nomi di persone nella colonna A del primo foglio di lavoro. Il nome e cognome sono separati da uno spazio. Quindi applica il metodo [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) alla colonna A e lo salva come file Excel di output. Se apri il [file Excel di output](25395230.xlsx), vedrai che i nomi sono nella colonna A mentre i cognomi sono nella colonna B come mostrato in questa schermata.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
