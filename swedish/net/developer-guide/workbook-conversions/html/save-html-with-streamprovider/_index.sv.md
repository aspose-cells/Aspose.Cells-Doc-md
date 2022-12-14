---
title: Spara HTML med StreamProvider
type: docs
weight: 80
url: /sv/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

När vi konverterar Excel-filer som innehåller bilder och former till html-filer, möter vi följande två problem:
1. Var ska vi spara bilderna och formerna när vi sparar excel-fil till html-ström.
1. Ersätt standardsökvägen med undantagen sökväg.

 Den här artikeln förklarar hur du implementerar[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) gränssnitt för att ställa in[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) fast egendom. Genom att implementera detta gränssnitt kommer du att kunna spara de skapade resurserna under HTML-generering till dina specifika platser eller minnesströmmar.

{{% /alert %}} 

 Detta är huvudkoden som visar användningen av[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)fast egendom



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



 Här är koden för*ExportStreamProvider* klass som genomför[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)gränssnitt som används i ovanstående kod.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

