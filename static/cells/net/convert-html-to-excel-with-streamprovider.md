##Load Html to Excel with StreamProvider
When loading html fiels which contain external resources, we offen face the following two issues:
1. When the html stream is loaded, the images and external resources referenced by the html file cannot be obtained through relative paths.
1. External resource paths referenced in html files need to be mapped
This article explains how to implement [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interface for setting the [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) property. By implementing this interface, you will be able to load external resources during loading Html streams or these external resources are relative.
This is the main code showing the usage of [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) property
