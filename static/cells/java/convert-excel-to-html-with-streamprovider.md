##Save Html With StreamProvider
When converting excel fiels which contain images and shapes to html files, we offen face the following two issues:
1. Where should we save the images and shapes when saving excel file to html stream.
1. Replace the default path with excepted path.
This article explains how to implement [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interface for setting the [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) property. By implementing this interface, you will be able to save the created resources during HTML generation to your specific locations or memory streams.
## Sample Code
This is the main code showing the usage of [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) property
Here is the code for *ExportStreamProvider* class which implements [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interface used inside the above code.
