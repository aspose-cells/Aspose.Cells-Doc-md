---
title: Specificare come attraversare la stringa nell output HTML usando HtmlCrossType
type: docs
weight: 140
url: /it/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Possibili Scenari di Utilizzo**

Quando la cella contiene testo o stringa ma è più grande della larghezza della cella, allora la stringa va oltre se la cella successiva nella colonna successiva è vuota o nulla. Quando si salva il file Excel in HTML, è possibile controllare questo overflow specificando il tipo di incrocio usando l'enumerazione [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Ha i seguenti valori

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Visualizzazione come MS Excel che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa verrà incrociata o verrà troncata.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Visualizza la stringa come MS Excel esportando HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): Visualizza la stringa HTML incrociata, le prestazioni per la creazione di grandi file HTML saranno più di dieci volte più veloci rispetto al setting del valore a [**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) o [**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): Visualizza la stringa HTML incrociata e nasconde la stringa di destra quando i testi si sovrappongono.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): Visualizzazione solo della stringa all'interno della larghezza della cella.

## **Specifica come attraversare la stringa nell'output HTML utilizzando HtmlCrossType**

Il seguente codice di esempio carica il [file Excel di esempio](51740747.xlsx) e lo salva in formato HTML specificando diversi [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Si prega di scaricare i [file HTML di output](51740745.zip) generati con questo codice. Il file Excel di esempio contiene l'immagine bordata in rosso come mostrato in questo screenshot che mostra l'effetto del valori sul file HTML di output.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
