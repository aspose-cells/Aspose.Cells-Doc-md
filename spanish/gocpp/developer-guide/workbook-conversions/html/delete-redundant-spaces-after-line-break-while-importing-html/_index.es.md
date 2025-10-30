---
title: Eliminar espacios redundantes después del salto de línea al importar HTML con Golang vía C++
linktitle: Eliminar espacios redundantes después de un salto de línea al importar HTML
type: docs
weight: 20
url: /es/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aprende cómo eliminar espacios redundantes después de saltos de línea al importar HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Por favor, usa la propiedad [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) y establece su valor en **true** para eliminar todos los espacios redundantes que vienen después de la etiqueta de salto de línea. Por defecto, esta propiedad está en **false** y los espacios redundantes se conservan en los archivos Excel de salida.

{{% /alert %}}

## Efecto de establecer la propiedad HTMLLoadOptions.DeleteRedundantSpaces en falso y verdadero

La siguiente captura de pantalla muestra el efecto de establecer esta propiedad en **false** y **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminar espacios redundantes después de un salto de línea al importar HTML

### Ejemplo de Programación

El siguiente código de muestra muestra el uso de la propiedad [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/). Por favor establézcala como **true** o **false** para obtener la salida como se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
