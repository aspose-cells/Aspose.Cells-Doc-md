---
title: Specifica come incrociare la stringa in PDF ed immagine di output
type: docs
weight: 110
url: /it/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Possibili Scenari di Utilizzo**

Quando una cella contiene testo o una stringa ma è più grande della larghezza della cella, allora la stringa fuoriesce se la cella successiva nella colonna successiva è nulla o vuota. Quando si salva il file Excel in formato PDF/immagine, è possibile controllare questo overflow specificando il tipo di incrocio utilizzando l'enumerazione [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Ha i seguenti valori

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Visualizzare come in MS Excel, dipende dalla cella successiva. Se la cella successiva è nulla, la stringa verrà incrociata o verrà troncata.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP): Visualizza la stringa come in MS Excel esportando PDF/immagine

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE): Visualizza tutto il testo incrociando altre celle e sovraiscrivendo il testo delle celle incrociate

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL): Visualizzazione solo della stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nel PDF / Immagine di output utilizzando TextCrossType**

Il seguente codice di esempio carica il file Excel di esempio e lo salva in formato PDF / Immagine specificando diversi [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Il file Excel di esempio e i file di output possono essere scaricati dai seguenti link:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}
