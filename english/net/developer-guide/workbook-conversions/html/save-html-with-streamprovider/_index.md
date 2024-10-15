---
title: Save Html With StreamProvider
type: docs
weight: 80
url: /net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

When converting excel fiels which contain iamges and shapes to html files, we offen face the following two issues:
1. Where should we save the images and shapes when saving excel file to html stream.
1. Replace the default path with excepted path.

This article explains how to implement [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interface for setting the [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) property. By implementing this interface, you will be able to save the created resources during HTML generation to your specific locations or memory streams.

{{% /alert %}} 

This is the main code showing the usage of [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) property



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Here is the code for *ExportStreamProvider* class which implements [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interface used inside the above code.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

{{< app/cells/assistant language="csharp" >}}