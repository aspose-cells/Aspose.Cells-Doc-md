---
title: Eliminar espacios redundantes después de un salto de línea al importar HTML
type: docs
weight: 20
url: /es/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

Utilice la propiedad [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) y establezca **true** para eliminar todos los espacios redundantes que vienen después de la etiqueta de salto de línea. De forma predeterminada, esta propiedad es **false** y se conservan los espacios redundantes en los archivos de Excel de salida.

{{% /alert %}}

## Efecto de establecer la propiedad HTMLLoadOptions.DeleteRedundantSpaces en falso y verdadero

La siguiente captura de pantalla muestra el efecto de establecer esta propiedad en **false** y **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminar espacios redundantes después de un salto de línea al importar HTML

### Ejemplo de Programación

El siguiente código de muestra muestra el uso de la propiedad [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces). Por favor establézcala como **true** o **false** para obtener la salida como se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
