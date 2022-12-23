---
title: Ladda HTML till Excel med StreamProvider
type: docs
weight: 80
url: /sv/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

När vi laddar html som innehåller externa resurser möter vi följande två problem:
1. När html-strömmen laddas kan de bilder och externa resurser som html-filen refererar till inte erhållas via relativa sökvägar.
1. Externa resurssökvägar som refereras till i html-filer måste mappas.

 Den här artikeln förklarar hur du implementerar[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) gränssnitt för att ställa in[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) fast egendom. Genom att implementera detta gränssnitt kommer du att kunna ladda externa resurser under laddning av HTML-strömmar eller så är dessa externa resurser relativa.

{{% /alert %}} 

Detta är huvudkoden som visar användningen av[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
