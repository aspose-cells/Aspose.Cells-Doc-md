---
title: Load Html to Excel with StreamProvider
type: docs
weight: 80
url: /net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

When loading html which contains external resources, we offen face the following two issues:
1,When the html stream is loaded, the images and external resources referenced by the html file cannot be obtained through relative paths.
2,External resource paths referenced in html files need to be mapped

This article explains how to implement [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interface for setting the [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) property. By implementing this interface, you will be able to load external resources during loading Html streams or these external resources are relative.

{{% /alert %}} 

This is the main code showing the usage of [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) property



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
