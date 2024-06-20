---
title: Specifica come incrociare la stringa in PDF ed immagine di output
type: docs
weight: 20
url: /it/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Specificare come incrociare la stringa nel PDF e nell'immagine di output**
Quando una cella contiene testo o una stringa più grande della larghezza della cella, la stringa trabocca se la cella successiva nella colonna successiva è nulla o vuota. Quando si salva il file Excel in PDF/Immagine, è possibile controllare questo overflow specificando il tipo di incrocio utilizzando l'enumerazione [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType). Ha i seguenti valori

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Visualizzazione come in MS Excel, dipende dalla cella successiva. Se la cella successiva è nulla, la stringa si incrocerà o sarà troncata.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP) : Mostra la stringa simile all'esportazione in PDF/Immagine di MS Excel
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) : Mostra tutto il testo incrociando altre celle e sovrascrivendo il testo delle celle incrociate
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) : Mostra solo la stringa entro la larghezza della cella.

Il seguente codice di esempio carica il file Excel di esempio e lo salva in formato PDF/Immagine specificando diversi TextCrossType. Il file Excel di esempio e i file di output possono essere scaricati dai seguenti link:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
