---
title: Carga HTML a Excel con StreamProvider
type: docs
weight: 80
url: /es/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Al cargar html que contiene recursos externos, a menudo nos enfrentamos a los siguientes dos problemas:
1. Cuando se carga la secuencia html, las imágenes y los recursos externos a los que hace referencia el archivo html no se pueden obtener a través de rutas relativas.
1. Las rutas de recursos externos a las que se hace referencia en los archivos html deben mapearse.

 Este artículo explica cómo implementar[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interfaz para configurar el[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) propiedad. Al implementar esta interfaz, podrá cargar recursos externos durante la carga de secuencias Html o estos recursos externos son relativos.

{{% /alert %}} 

Este es el código principal que muestra el uso de[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
