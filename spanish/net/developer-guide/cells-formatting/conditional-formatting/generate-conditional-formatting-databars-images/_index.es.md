---
title: Generar imágenes de barras de datos de formato condicional
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Soporta la generación de barras de datos con formato condicional e imágenes, lo que permite a los usuarios personalizar la visualización de la hoja de cálculo en función del valor de las celdas. Este artículo presentará cómo utilizar la biblioteca Aspose.Cells para generar barras de datos con formato condicional e imágenes.
keywords: Aspose.Cells, Formato condicional, Barras de datos, Imágenes, Hojas de cálculo
type: docs
weight: 40
url: /es/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A veces, necesita generar imágenes de barras de datos de formato condicional. Puede utilizar el método [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) de Aspose.Cells para generar estas imágenes. Este artículo muestra cómo generar una imagen de barra de datos usando Aspose.Cells.

{{% /alert %}}

El siguiente código de ejemplo genera la imagen de la Barra de Datos de la celda C1. Primero, accede al objeto de condición de formato de la celda, y luego a partir de ese objeto, accede al [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) y usa su método [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) para generar la imagen de la celda. Finalmente, guarda la imagen en disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
