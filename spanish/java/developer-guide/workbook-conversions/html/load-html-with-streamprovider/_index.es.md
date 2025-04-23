---
title: Cargar Html a Excel con StreamProvider
type: docs
weight: 80
url: /es/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Cuando se carga HTML que contiene recursos externos, a menudo nos enfrentamos a los siguientes dos problemas:
1. Cuando se carga el flujo de html, las imágenes y recursos externos referenciados por el archivo html no se pueden obtener a través de rutas relativas.
1. Las rutas de recursos externos referenciadas en archivos HTML deben ser mapeadas.

Este artículo explica cómo implementar la interfaz [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) para establecer la propiedad [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider). Al implementar esta interfaz, podrá cargar recursos externos durante la carga de flujos de HTML o estos recursos externos son relativos.

{{% /alert %}} 

Este es el código principal que muestra el uso de [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
{{< app/cells/assistant language="java" >}}
