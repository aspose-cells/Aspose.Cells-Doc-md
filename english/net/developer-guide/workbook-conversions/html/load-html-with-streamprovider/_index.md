---
title: Load Html to Excel with StreamProvider
type: docs
weight: 80
url: /net/convert-html-to-excel-with-streamprovider/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

When loading **HTML** files which contain external resources, we often face the following two issues:
1. When the HTML stream is loaded, the images and external resources referenced by the HTML file cannot be obtained through relative paths.
2. External resource paths referenced in HTML files need to be mapped.

This article explains how to implement the **IStreamProvider** interface for setting the **HtmlLoadOptions.StreamProvider** property. By implementing this interface, you will be able to load external resources during loading HTML streams, even when these external resources are referenced relatively.

{{% /alert %}}

This is the main code showing the usage of the **HtmlLoadOptions.StreamProvider** property



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
