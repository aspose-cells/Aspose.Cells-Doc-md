---
title: Copia solo i dati dell intervallo.
type: docs
weight: 330
url: /it/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

A volte, è necessario copiare i dati da un intervallo di celle a un altro, copiando solo i dati, non la formattazione. Aspose.Cells offre questa funzionalità tramite il metodo [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-)

{{% /alert %}} 
## **Copia solo i dati dell'intervallo.**
Questo esempio mostra come:

1. Crea un libro di lavoro.
1. Aggiungi dati alle celle nel primo foglio di lavoro.
1. Crea un intervallo.
1. Crea un oggetto di stile con attributi di formattazione specificati.
1. Applica la formattazione di stile all'intervallo.
1. Crea un altro intervallo di celle.
1. Copiare i dati del primo intervallo in questo secondo intervallo utilizzando il metodo [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
{{< app/cells/assistant language="java" >}}
