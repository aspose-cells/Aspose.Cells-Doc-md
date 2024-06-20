---
title: Ladda in html till Excel med StreamProvider
type: docs
weight: 80
url: /sv/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

När du laddar html-filer som innehåller externa resurser, stöter vi ofta på följande två problem:
1. När html-strömmen laddas kan inte bilderna och externa resurser som refereras av html-filen erhållas genom relativa sökvägar.
1. Externa resursvägar som refereras i html-filer måste mappas

Denna artikel förklarar hur man implementerar [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) gränssnittet för att ange [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) egenskapen. Genom att implementera detta gränssnitt kommer du kunna ladda externa resurser under laddning av Html-strömmar eller dessa externa resurser är relativa.

{{% /alert %}} 

Detta är den huvudsakliga koden som visar användningen av [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) egenskapen



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
