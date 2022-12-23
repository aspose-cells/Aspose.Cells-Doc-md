---
title: Specificare come incrociare la stringa nell'output PDF e nell'immagine
type: docs
weight: 120
url: /it/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Possibili scenari di utilizzo**

Quando una cella contiene testo o stringa ma è più grande della larghezza della cella, la stringa va in overflow se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in PDF/Image, puoi controllare questo overflow specificando il tipo incrociato usando il[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)enumerazione. Ha i seguenti valori

- **TextCrossType.Default**: Visualizza testo come MS Excel che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa si incrocia o viene troncata.

- **TextCrossType.CrossKeep**: Visualizza la stringa come MS Excel che esporta PDF/Image

- **TextCrossType.CrossOverride**: Visualizza tutto il testo incrociando altre celle e sovrascrive il testo delle celle incrociate

- **TextCrossType.StrictInCell**: visualizza solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nell'output PDF/Image utilizzando TextCrossType**

Il seguente codice di esempio carica il file Excel di esempio e lo salva nel formato PDF/Image specificando diversi[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Il file Excel di esempio e i file di output possono essere scaricati dai seguenti collegamenti:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Codice d'esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
