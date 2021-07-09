---
title: Implementing IStreamProvider for HtmlSaveOptions.StreamProvider
type: docs
weight: 80
url: /net/implementing-istreamprovider-for-htmlsaveoptions-streamprovider/
---

{{% alert color="primary" %}} 

This article explains how to implement [IStreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/istreamprovider) interface for setting the [HtmlSaveOptions.StreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/streamprovider) property. By implementing this interface, you will be able to save the created resources during HTML generation to your specific locations or memory streams.

{{% /alert %}} 

This is the main code showing the usage of [HtmlSaveOptions.StreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/streamprovider) property



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Here is the code for *ExportStreamProvider* class which implements [IStreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/istreamprovider) interface used inside the above code.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}
