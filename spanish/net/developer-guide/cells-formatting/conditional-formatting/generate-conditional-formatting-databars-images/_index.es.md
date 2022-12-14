---
title: Generar imágenes de barras de datos de formato condicional
type: docs
weight: 40
url: /es/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 A veces, necesita generar imágenes de barras de datos de formato condicional. Puedes usar Aspose.Cells[**Barra de datos.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) método para generar estas imágenes. Este artículo muestra cómo generar una imagen DataBar usando Aspose.Cells.

{{% /alert %}}

El siguiente código de ejemplo genera la imagen DataBar de la celda C1. Primero, accede al objeto de condición de formato de la celda, y luego desde ese objeto, accede al[**barra de datos**](https://reference.aspose.com/cells/net/aspose.cells/databar) objeto y utiliza su[**A la imagen()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)método para generar la imagen de la celda. Finalmente, guarda la imagen en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
