---
title: Specifica come incrociare la stringa in PDF ed immagine di output
type: docs
weight: 120
url: /it/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Scopri come incrociare le stringhe nel PDF di output e nell immagine con l API Aspose.Cells for Python via .NET.
keywords: Incrocio di stringhe in output PDF e immagine Python
---

## **Possibili Scenari di Utilizzo**

Quando una cella contiene testo o stringa ma è più grande della larghezza della cella, allora la stringa trabocca se la cella successiva nella colonna successiva è nulla o vuota. Quando si salvano i file Excel in PDF/Immagine, è possibile controllare questo overflow specificando il tipo di incrocio usando l'enumerazione [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). Ha i seguenti valori

- **TextCrossType.DEFAULT**: Mostra il testo come MS Excel che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa verrà incrociata o verrà troncata.

- **TextCrossType.CROSS_KEEP**: Mostra la stringa come MS Excel esportando PDF/Immagine

- **TextCrossType.CROSS_OVERRIDE**: Mostra tutto il testo incrociando altre celle e sovrascrivendo il testo delle celle incrociate

- **TextCrossType.STRICT_IN_CELL**: Mostra solo la stringa entro la larghezza della cella.

## **Specificare come incrociare la stringa nel PDF / Immagine di output utilizzando TextCrossType**

Il seguente codice di esempio carica il file Excel di esempio e lo salva in formato PDF / Immagine specificando diversi [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). Il file Excel di esempio e i file di output possono essere scaricati dai seguenti link:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Codice di esempio

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
