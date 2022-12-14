---
title: Actualizar la configuración de fuentes desde el lado del cliente
type: docs
weight: 170
url: /es/net/update-font-from-client-side/
---
{{% alert color="primary" %}}

Este tema trata sobre cómo cambiar la configuración de fuentes desde el lado del cliente en el control Aspose.Cells.GridWeb.

{{% /alert %}}

Aspose.Cells GridWeb ahora admite cambiar la configuración de fuente desde el lado del cliente. Para ello, el API proporciona las siguientes funciones

- **actualizarCellFontStyle**: Parámetros - r/i/b/ib para normal/cursiva/negrita/cursiva&&negrita
- **actualizarCellFontSize**: Params - nombre de fuente, etc. 'Sistema'
- **actualizarCellFontName**: Parámetros - tamaño de fuente, etc. '12 puntos'
- **actualizarCellFontColor**: Parámetros - ninguno/u/l/ul/ para ninguno/subrayado/tachado/subrayado&&tachado
- **actualizarCellFontLine**: Params - color html como #aa22ee o nombre de color conocido como verde, rojo,...
- **actualizarCellBackGroundColor**: Params - color html como #aa22ee o nombre de color conocido como verde, rojo,...

El siguiente fragmento de código muestra cómo cambiar la configuración de fuente desde el lado del cliente en GridWeb.

## Código de muestra

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-Worksheets-UpdateFontFromClientSide.aspx" >}}
