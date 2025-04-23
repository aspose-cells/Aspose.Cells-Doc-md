---
title: Copia solo lo stile dell intervallo
type: docs
weight: 350
url: /it/java/copy-range-style-only/
---

{{% alert color="primary" %}} 

[Copia solo i dati dell'intervallo](/cells/it/java/copy-range-data-only/) e [Copia dati dell'intervallo con stile](/cells/it/java/copy-range-data-with-style/) spiegano come copiare dati da un intervallo a un altro con o senza formattazione. È anche possibile copiare solo la formattazione dell'intervallo. Questo articolo mostra come.

{{% /alert %}} 
## **Copia solo lo stile dell'intervallo**
Questo esempio crea un workbook, lo popola con dati e copia solo lo stile di un intervallo.

1. Crea un intervallo.
1. Crea un oggetto di stile con attributi di formattazione specificati.
1. Applica la formattazione di stile all'intervallo.
1. Crea un secondo intervallo di celle.
1. Copia la formattazione del primo intervallo al secondo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeStyleOnly-CopyRangeStyleOnly.java" >}}
{{< app/cells/assistant language="java" >}}
