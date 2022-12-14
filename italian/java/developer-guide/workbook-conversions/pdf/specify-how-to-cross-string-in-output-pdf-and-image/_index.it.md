---
title: Specificare come incrociare la stringa nel PDF di output e nell'immagine
type: docs
weight: 110
url: /it/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Possibili scenari di utilizzo**

Quando una cella contiene testo o stringa ma è più grande della larghezza della cella, la stringa va in overflow se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in PDF/immagine, puoi controllare questo overflow specificando il tipo incrociato utilizzando il[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)enumerazione. Ha i seguenti valori

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Visualizza come MS Excel, dipende dalla cella successiva. Se la cella successiva è nulla, la stringa si incrocia o viene troncata.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Visualizza la stringa come MS Excel che esporta PDF/Immagine

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): Visualizza tutto il testo incrociando altre celle e sovrascrive il testo delle celle incrociate

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): Visualizza solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nel PDF/immagine di output utilizzando TextCrossType**

Il codice di esempio seguente carica il file Excel di esempio e lo salva in formato PDF/immagine specificando different[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)Il file Excel di esempio e i file di output possono essere scaricati dai seguenti collegamenti:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
