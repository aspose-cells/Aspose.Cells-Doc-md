---
title: Stampa pagina vuota quando non c'è niente da stampare
type: docs
weight: 80
url: /it/java/output-blank-page-when-there-is-nothing-to-print/
---
##  **Possibili scenari di utilizzo**

Se il foglio è vuoto, Aspose.Cells non stamperà nulla quando si esporta il foglio di lavoro nell'immagine. È possibile modificare questo comportamento utilizzando[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)proprietà. Quando lo imposterai su *true**, stamperà la pagina vuota.

##  **Stampa pagina vuota quando non c'è niente da stampare**

Il seguente codice di esempio crea la cartella di lavoro vuota che ha un foglio di lavoro vuoto ed esegue il rendering del foglio di lavoro vuoto in un'immagine dopo aver impostato il[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)proprietà come *true**. Di conseguenza, genera la pagina vuota in quanto non c'è nulla da stampare che puoi vedere come sotto.

![cose da fare:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
