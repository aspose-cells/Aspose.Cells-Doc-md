---
title: Spara HTML med StreamProvider
type: docs
weight: 120
url: /sv/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

När du konverterar excelfiler som innehåller bilder och former till HTML-filer stöter vi ofta på följande två problem:
1. Var ska vi spara bilderna och formerna när vi sparar excelfilen till HTML-ström.
1. Ersätt standardvägen med förväntad väg.

Den här artikeln förklarar hur man implementerar [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) gränssnittet för att ställa in [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)-egenskapen. Genom att implementera detta gränssnitt kommer du att kunna spara de skapade resurserna under HTML-genereringen till specifika platser eller minnesströmmar.

{{% /alert %}}

## Exempelkod

Det här är huvudkoden som visar användningen av [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)-egenskapen

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

Här är koden för *ExportStreamProvider*-klassen som implementerar [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)-gränssnittet som används i koden ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

