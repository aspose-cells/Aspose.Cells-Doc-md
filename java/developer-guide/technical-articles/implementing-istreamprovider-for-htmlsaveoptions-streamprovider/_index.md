---
title: Implementing IStreamProvider for HtmlSaveOptions.StreamProvider
type: docs
weight: 120
url: /java/implementing-istreamprovider-for-htmlsaveoptions-streamprovider/
---

{{% alert color="primary" %}}

This article explains how to implement [**IStreamProvider**](https://apireference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interface for setting the [**HtmlSaveOptions.StreamProvider**](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) property. By implementing this interface, you will be able to save the created resources during HTML generation to your specific locations or memory streams.

{{% /alert %}}

## Sample Code

This is the main code showing the usage of [**HtmlSaveOptions.StreamProvider**](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) property

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

Here is the code for *ExportStreamProvider* class which implements [**IStreamProvider**](https://apireference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interface used inside the above code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}
