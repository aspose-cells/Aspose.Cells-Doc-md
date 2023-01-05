---
title: Guardar HTML con StreamProvider
type: docs
weight: 120
url: /es/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

Al convertir campos de Excel que contienen imágenes y formas en archivos html, a menudo nos enfrentamos a los siguientes dos problemas:
1. ¿Dónde debemos guardar las imágenes y las formas al guardar el archivo de Excel en la transmisión html?
1. Reemplace la ruta predeterminada con la ruta exceptuada.

 Este artículo explica cómo implementar[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interfaz para configurar el[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) propiedad. Al implementar esta interfaz, podrá guardar los recursos creados durante la generación HTML en sus ubicaciones o flujos de memoria específicos.

{{% /alert %}}

## Código de muestra

 Este es el código principal que muestra el uso de[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)propiedad

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

 Aquí está el código para*ExportStreamProviderExportStreamProvider* clase que implementa[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interfaz utilizada dentro del código anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

