---
title: Spara HTML med StreamProvider
type: docs
weight: 120
url: /sv/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

När vi konverterar Excel-filer som innehåller bilder och former till html-filer, stöter vi på följande två problem:
1. Var ska vi spara bilderna och formerna när vi sparar excel-fil till html-ström.
1. Ersätt standardsökvägen med undantagen sökväg.

 Den här artikeln förklarar hur du implementerar[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) gränssnitt för att ställa in[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) fast egendom. Genom att implementera detta gränssnitt kommer du att kunna spara de skapade resurserna under HTML-genereringen till dina specifika platser eller minnesströmmar.

{{% /alert %}}

## Exempelkod

 Detta är huvudkoden som visar användningen av[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)fast egendom

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

 Här är koden för*ExportStreamProvider* klass som genomför[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)gränssnitt som används i ovanstående kod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

