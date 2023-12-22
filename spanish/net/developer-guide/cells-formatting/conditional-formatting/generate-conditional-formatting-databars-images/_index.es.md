---
title: Generar imágenes de barras de datos con formato condicional
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Admite la generación de barras de datos e imágenes con formato condicional, lo que permite a los usuarios personalizar la visualización de la hoja de cálculo en función del valor de las celdas. Este artículo presentará cómo utilizar la biblioteca Aspose.Cells para generar barras de datos e imágenes con formato condicional.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /es/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 A veces, es necesario generar imágenes de barras de datos de formato condicional. Puedes usar Aspose.Cells[**Barra de datos.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) método para generar estas imágenes. Este artículo muestra cómo generar una imagen de DataBar usando Aspose.Cells.

{{% /alert %}}

 El siguiente código de muestra genera la imagen DataBar de la celda C1. Primero accede al objeto de condición de formato de la celda, y luego desde ese objeto accede al[**Barra de datos**](https://reference.aspose.com/cells/net/aspose.cells/databar) objeto y utiliza su[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)Método para generar la imagen de la celda. Finalmente, guarda la imagen en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
