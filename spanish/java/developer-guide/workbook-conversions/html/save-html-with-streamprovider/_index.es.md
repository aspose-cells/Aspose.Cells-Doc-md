---
title: Guardar HTML con StreamProvider
type: docs
weight: 120
url: /es/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

Cuando convertimos archivos de Excel que contienen imágenes y formas a archivos HTML, a menudo nos enfrentamos a los siguientes dos problemas:
1. ¿Dónde debemos guardar las imágenes y formas al guardar el archivo de Excel en un stream HTML?
1. Reemplazar la ruta predeterminada con la ruta esperada.

Este artículo explica cómo implementar la interfaz [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) para establecer la propiedad [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider). Al implementar esta interfaz, podrá guardar los recursos creados durante la generación de HTML en ubicaciones específicas o secuencias de memoria.

{{% /alert %}}

## Código de Muestra

Este es el código principal que muestra el uso de la propiedad [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

Aquí está el código para la clase *ExportStreamProvider* que implementa la interfaz [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) utilizada en el código anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

{{< app/cells/assistant language="java" >}}
