---
title: Ladda in html till Excel med StreamProvider
type: docs
weight: 80
url: /sv/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

När du laddar html som innehåller externa resurser stöter vi ofta på följande två problem:
1. När html-strömmen laddas kan inte bilderna och externa resurser som refereras av html-filen erhållas genom relativa sökvägar.
1. Externa resurs-sökvägar som refereras i html-filer behöver kartläggas.

Den här artikeln förklarar hur man implementerar [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)gränssnitt för att ställa in [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)egenskapen. Genom att implementera detta gränssnitt kommer du att kunna ladda externa resurser vid inläsning av Html-strömmar eller dessa externa resurser är relativa.

{{% /alert %}} 

Det här är huvudkoden som visar användningen av [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
