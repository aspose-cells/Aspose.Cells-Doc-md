---
title: Carica Html in Excel con StreamProvider
type: docs
weight: 80
url: /it/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Quando si carica html che contiene risorse esterne, spesso ci troviamo di fronte ai seguenti due problemi:
1. Quando il flusso html viene caricato, le immagini e le risorse esterne a cui fa riferimento il file html non possono essere ottenute tramite percorsi relativi.
1. I percorsi delle risorse esterne a cui si fa riferimento nei file html devono essere mappati.

 Questo articolo spiega come implementare[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interfaccia per l'impostazione del[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) proprietà. Implementando questa interfaccia, sarai in grado di caricare risorse esterne durante il caricamento di flussi Html o queste risorse esterne sono relative.

{{% /alert %}} 

 Questo è il codice principale che mostra l'utilizzo di[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
