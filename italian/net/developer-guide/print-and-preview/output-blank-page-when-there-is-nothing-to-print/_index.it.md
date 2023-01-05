---
title: Stampa pagina vuota quando non c'è niente da stampare
type: docs
weight: 90
url: /it/net/output-blank-page-when-there-is-nothing-to-print/
---
## **Possibili scenari di utilizzo**

 Se il foglio è vuoto, Aspose.Cells non stamperà nulla quando si esporta il foglio di lavoro nell'immagine. È possibile modificare questo comportamento utilizzando[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) proprietà. Quando lo imposterai**VERO**, stamperà la pagina vuota.

## **Stampa pagina vuota quando non c'è niente da stampare**

Il seguente codice di esempio crea la cartella di lavoro vuota che ha un foglio di lavoro vuoto ed esegue il rendering del foglio di lavoro vuoto in un'immagine dopo aver impostato il[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) proprietà come**VERO**. Di conseguenza, genera la pagina vuota in quanto non c'è nulla da stampare che puoi vedere nell'immagine qui sotto.

![cose da fare:immagine_alt_testo](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
