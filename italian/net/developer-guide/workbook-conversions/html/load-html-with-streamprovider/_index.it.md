---
title: Carica HTML in Excel con StreamProvider
type: docs
weight: 80
url: /it/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Quando si caricano file html che contengono risorse esterne, ci imbattiamo spesso nei seguenti due problemi:
1. Quando lo stream html viene caricato, le immagini e le risorse esterne referenziate dal file html non possono essere ottenute tramite percorsi relativi.
1. I percorsi delle risorse esterne referenziate nei file html devono essere mappati

Questo articolo spiega come implementare l'interfaccia [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) per impostare la proprietà [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/). Implementando questa interfaccia, sarà possibile caricare le risorse esterne durante il caricamento degli stream Html o queste risorse esterne sono relative.

{{% /alert %}} 

Questo è il codice principale che mostra l'uso della proprietà [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
