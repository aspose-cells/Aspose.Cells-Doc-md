---
title: Specificare come incrociare la stringa nel PDF di output e nell'immagine
type: docs
weight: 120
url: /it/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Possibili scenari di utilizzo**

Quando una cella contiene testo o stringa ma è più grande della larghezza della cella, la stringa va in overflow se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in PDF/immagine, puoi controllare questo overflow specificando il tipo incrociato utilizzando il[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)enumerazione. Ha i seguenti valori

- **TextCrossType.Default**: Visualizza testo come MS Excel che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa si incrocia o viene troncata.

- **TextCrossType.CrossKeep**: Visualizza la stringa come MS Excel che esporta PDF/Immagine

- **TextCrossType.CrossOverride**: Visualizza tutto il testo incrociando altre celle e sovrascrive il testo delle celle incrociate

- **TextCrossType.StrictInCell**: visualizza solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nel PDF/immagine di output utilizzando TextCrossType**

Il codice di esempio seguente carica il file Excel di esempio e lo salva in formato PDF/immagine specificando different[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)Il file Excel di esempio e i file di output possono essere scaricati dai seguenti collegamenti:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Codice di esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
