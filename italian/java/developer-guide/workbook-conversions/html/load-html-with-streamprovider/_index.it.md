---
title: Carica HTML in Excel con StreamProvider
type: docs
weight: 80
url: /it/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Quando si carica html che contiene risorse esterne, ci si imbatte spesso nei seguenti due problemi:
1. Quando lo stream html viene caricato, le immagini e le risorse esterne referenziate dal file html non possono essere ottenute tramite percorsi relativi.
1. I percorsi delle risorse esterne referenziati nei file html devono essere mappati.

Questo articolo spiega come implementare l'interfaccia [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) per impostare la proprietà [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider). Implementando questa interfaccia, sarà possibile caricare risorse esterne durante il caricamento di flussi Html o queste risorse esterne sono relative.

{{% /alert %}} 

Questo è il codice principale che mostra l'utilizzo di [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
{{< app/cells/assistant language="java" >}}
