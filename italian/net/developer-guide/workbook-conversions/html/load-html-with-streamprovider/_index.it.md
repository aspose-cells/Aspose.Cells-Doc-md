---
title: Carica Html in Excel con StreamProvider
type: docs
weight: 80
url: /it/net/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Quando si caricano campi html che contengono risorse esterne, spesso ci troviamo di fronte ai seguenti due problemi:
1. Quando il flusso html viene caricato, le immagini e le risorse esterne a cui fa riferimento il file html non possono essere ottenute tramite percorsi relativi.
1. I percorsi delle risorse esterne a cui si fa riferimento nei file html devono essere mappati

 Questo articolo spiega come implementare[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interfaccia per l'impostazione del[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) proprietà. Implementando questa interfaccia, sarai in grado di caricare risorse esterne durante il caricamento di flussi Html o queste risorse esterne sono relative.

{{% /alert %}} 

 Questo è il codice principale che mostra l'utilizzo di[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)proprietà



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
