---
title: Ladda HTML till Excel med StreamProvider
type: docs
weight: 80
url: /sv/net/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

När vi laddar html-filer som innehåller externa resurser möter vi följande två problem:
1. När html-strömmen laddas kan de bilder och externa resurser som html-filen refererar till inte erhållas via relativa sökvägar.
1. Externa resurssökvägar som refereras till i html-filer måste mappas

 Den här artikeln förklarar hur du implementerar[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) gränssnitt för att ställa in[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) fast egendom. Genom att implementera detta gränssnitt kommer du att kunna ladda externa resurser under laddning av HTML-strömmar eller så är dessa externa resurser relativa.

{{% /alert %}} 

 Detta är huvudkoden som visar användningen av[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)fast egendom



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
