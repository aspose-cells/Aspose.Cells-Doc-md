---
title: Copia solo i dati dell intervallo.
type: docs
weight: 600
url: /it/python-net/copy-range-data-only/
description: Questo articolo descrive come copiare solo i dati del range con la libreria Aspose.Cells per Python via .NET.
keywords: Libreria Excel per Python, Come copiare solo i dati del range con Python, Come copiare solo i dati del range con la libreria excel python.
---

{{% alert color="primary" %}}

A volte è necessario copiare i dati da un intervallo di celle a un altro, copiando solo i dati, non la formattazione. Aspose.Cells per Python via .NET offre questa funzionalità.

Questo articolo fornisce un codice di esempio che utilizza Aspose.Cells per Python via .NET per copiare un intervallo di dati.

{{% /alert %}}

Questo esempio mostra come:

1. Crea un libro di lavoro.
1. Aggiungi dati alle celle nel primo foglio di lavoro.
1. Crea un [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Crea un oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) con attributi di formattazione specificati.
1. Applica la formattazione di stile all'intervallo.
1. Crea un altro intervallo di celle.
1. Copiare i dati del primo intervallo in questo secondo intervallo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataOnly-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
