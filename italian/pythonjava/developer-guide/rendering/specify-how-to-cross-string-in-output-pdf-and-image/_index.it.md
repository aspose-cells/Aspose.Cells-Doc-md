---
title: Specificare come incrociare la stringa nell'output PDF e nell'immagine
type: docs
weight: 20
url: /it/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Specificare come incrociare la stringa nell'output PDF e nell'immagine**
 Quando una cella contiene testo o stringa più grande della larghezza della cella, la stringa va in overflow se la cella successiva nella colonna successiva è nulla o vuota. Quando si salva il file Excel in PDF/Image, è possibile controllare questo overflow specificando il tipo incrociato utilizzando il[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) enumerazione. Ha i seguenti valori

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Visualizza come MS Excel, dipende dalla cella successiva. Se la cella successiva è nulla, la stringa si incrocia o viene troncata.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): Visualizza la stringa simile all'esportazione MS Excel PDF/Image
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)Visualizza tutto il testo incrociando altre celle e sovrascrive il testo delle celle incrociate
- [TextCrossType.STRICT_IN_CELLULA](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): Visualizza solo la stringa all'interno della larghezza della cella.

Il codice di esempio seguente carica il file Excel di esempio e lo salva nel formato PDF/Image specificando TextCrossType diverso. Il file Excel di esempio e i file di output possono essere scaricati dai seguenti collegamenti:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
