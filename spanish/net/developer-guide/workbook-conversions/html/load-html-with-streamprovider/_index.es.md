---
title: Carga HTML a Excel con StreamProvider
type: docs
weight: 80
url: /es/net/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Al cargar campos html que contienen recursos externos, a menudo nos enfrentamos a los siguientes dos problemas:
1. Cuando se carga la secuencia html, las imágenes y los recursos externos a los que hace referencia el archivo html no se pueden obtener a través de rutas relativas.
1. Las rutas de recursos externos a las que se hace referencia en los archivos html deben mapearse

 Este artículo explica cómo implementar[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) interfaz para configurar el[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) propiedad. Al implementar esta interfaz, podrá cargar recursos externos durante la carga de secuencias Html o estos recursos externos son relativos.

{{% /alert %}} 

 Este es el código principal que muestra el uso de[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)propiedad



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
