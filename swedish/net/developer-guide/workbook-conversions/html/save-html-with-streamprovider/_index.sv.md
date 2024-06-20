---
title: Spara HTML med StreamProvider
type: docs
weight: 80
url: /sv/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

När du konverterar excelfiler som innehåller bilder och former till html-filer stöter vi ofta på följande två problem:
1. Var ska vi spara bilderna och formerna när vi sparar excelfilen till HTML-ström.
1. Ersätt standardvägen med förväntad väg.

I den här artikeln förklaras hur man implementerar gränssnittet [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) för att ställa in egenskapen [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider). Genom att implementera detta gränssnitt kan du spara de skapade resurserna under HTML-generering till dina specifika platser eller minnesströmmar.

{{% /alert %}} 

Detta är huvudkoden som visar användningen av egenskapen [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Här är koden för klassen *ExportStreamProvider* som implementerar gränssnittet [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) som används i ovanstående kod.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

