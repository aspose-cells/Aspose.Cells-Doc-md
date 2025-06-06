---
title: Specifica come incrociare la stringa in PDF ed immagine di output
type: docs
weight: 120
url: /it/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Possibili Scenari di Utilizzo**

Quando una cella contiene testo o stringa ma è più grande della larghezza della cella, allora la stringa trabocca se la cella successiva nella colonna successiva è nulla o vuota. Quando si salvano i file Excel in PDF/Immagine, è possibile controllare questo overflow specificando il tipo di incrocio usando l'enumerazione [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Ha i seguenti valori

- **TextCrossType.Default**: Visualizza il testo come in MS Excel, che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa verrà incrociata o troncata.

- **TextCrossType.CrossKeep**: Visualizza la stringa come in MS Excel esportando in PDF/Immagine

- **TextCrossType.CrossOverride**: Visualizza tutto il testo incrociando altre celle e sovrascrivendo il testo delle celle incrociate

- **TextCrossType.StrictInCell**: Mostra solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nel PDF / Immagine di output utilizzando TextCrossType**

Il seguente codice di esempio carica il file Excel di esempio e lo salva in formato PDF / Immagine specificando diversi [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Il file Excel di esempio e i file di output possono essere scaricati dai seguenti link:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Codice di esempio

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
