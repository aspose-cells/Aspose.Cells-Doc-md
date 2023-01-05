---
title: Specificare come incrociare la stringa nell'output PDF e nell'immagine
type: docs
weight: 110
url: /it/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Possibili scenari di utilizzo**

Quando una cella contiene testo o stringa ma è più grande della larghezza della cella, la stringa va in overflow se la cella successiva nella colonna successiva è nulla o vuota. Quando si salva il file Excel in PDF/Image, è possibile controllare questo overflow specificando il tipo incrociato utilizzando il[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)enumerazione. Ha i seguenti valori

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Visualizza come MS Excel, dipende dalla cella successiva. Se la cella successiva è nulla, la stringa si incrocia o viene troncata.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Visualizza la stringa come MS Excel che esporta PDF/Image

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): Visualizza tutto il testo incrociando altre celle e sovrascrive il testo delle celle incrociate

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): Visualizza solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nell'output PDF/Image utilizzando TextCrossType**

Il seguente codice di esempio carica il file Excel di esempio e lo salva nel formato PDF/Image specificando diversi[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Il file Excel di esempio e i file di output possono essere scaricati dai seguenti collegamenti:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
