---
title: Specificare come incrociare la stringa nell'HTML di output utilizzando HtmlCrossType
type: docs
weight: 140
url: /it/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Possibili scenari di utilizzo**

Quando la cella contiene testo o stringa ma è più grande della larghezza della cella, la stringa va in overflow se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in HTML, puoi controllare questo overflow specificando il tipo incrociato usando il[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)enumerazione. Ha i seguenti valori

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Visualizza come MS Excel che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa si incrocia o viene troncata.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Visualizza la stringa come MS Excel che esporta HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : Visualizza stringa incrociata HTML, le prestazioni per la creazione di file HTML di grandi dimensioni saranno più di dieci volte più veloci rispetto all'impostazione del valore su[**PREDEFINITO**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) o[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): Mostra la stringa incrociata HTML e nasconde la stringa giusta quando i testi si sovrappongono.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): Visualizza solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nell'HTML di output utilizzando HtmlCrossType**

Il codice di esempio seguente carica il file[esempio di file Excel](51740747.xlsx)lo salva in formato HTML specificando diverso[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)Si prega di scaricare il[output HTML](51740745.zip) file generati con questo codice. Il file Excel di esempio contiene l'immagine bordata di colore rosso come mostrato in questo screenshot che mostra l'effetto del[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)valori sull'output HTML.

![cose da fare:immagine_alt_testo](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
