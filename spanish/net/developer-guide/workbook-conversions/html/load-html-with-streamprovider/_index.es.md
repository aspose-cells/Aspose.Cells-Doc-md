---
title: Cargar Html a Excel con StreamProvider
type: docs
weight: 80
url: /es/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Al cargar archivos html que contienen recursos externos, a menudo nos enfrentamos a los siguientes dos problemas:
1. Cuando se carga el flujo de html, las imágenes y recursos externos referenciados por el archivo html no se pueden obtener a través de rutas relativas.
1. Se necesitan mapear las rutas de recursos externos referenciados en archivos html

Este artículo explica cómo implementar la interfaz [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) para establecer la propiedad [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/). Al implementar esta interfaz, podrá cargar recursos externos durante la carga de flujos de Html o estos recursos externos serán relativos.

{{% /alert %}} 

Este es el código principal que muestra el uso de la propiedad [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
