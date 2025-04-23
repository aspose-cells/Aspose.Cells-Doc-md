---
title: Copia solo i dati dell intervallo.
type: docs
weight: 600
url: /it/net/copy-range-data-only/
---

{{% alert color="primary" %}}

A volte è necessario copiare i dati da un intervallo di celle a un altro, copiando solo i dati, non la formattazione. Aspose.Cells offre questa funzionalità.

Questo articolo fornisce un codice di esempio che utilizza Aspose.Cells per copiare un intervallo di dati.

{{% /alert %}}

Questo esempio mostra come:

1. Crea un libro di lavoro.
1. Aggiungi dati alle celle nel primo foglio di lavoro.
1. Crea un [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Crea un oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) con attributi di formattazione specificati.
1. Applica la formattazione di stile all'intervallo.
1. Crea un altro intervallo di celle.
1. Copiare i dati del primo intervallo in questo secondo intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
