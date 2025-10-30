---
title: Specifica come attraversare le stringhe nel PDF e nelle immagini in output con Golang tramite C++
linktitle: Specifica come incrociare la stringa in PDF ed immagine di output
type: docs
weight: 120
url: /it/go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Scopri come controllare la fuoriuscita del testo in output PDF e immagine usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Quando una cella contiene testo o stringa più lunga della larghezza della cella, la stringa traboccherà se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il file Excel in PDF o immagine, puoi controllare questo trabocco specificando il tipo di attraversamento usando l'enumerazione [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). Ha i seguenti valori:

- **TextCrossType.Default**: visualizza il testo come MS Excel, che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa attraverserà o sarà troncata.

- **TextCrossType.CrossKeep**: visualizza la stringa come MS Excel esportando in PDF/Immagine.

- **TextCrossType.CrossOverride**: visualizza tutto il testo attraversando le altre celle e sovrascrive il testo delle celle attraversate.

- **TextCrossType.StrictInCell**: Mostra solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nel PDF / Immagine di output utilizzando TextCrossType**

Il seguente esempio di codice carica il file Excel di esempio e lo salva in formato PDF/Immagine specificando vari [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). Il file Excel di esempio e i file di output possono essere scaricati dai link seguenti:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Codice di esempio

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}
