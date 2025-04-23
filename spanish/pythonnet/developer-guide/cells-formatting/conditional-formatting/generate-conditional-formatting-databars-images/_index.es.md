---
title: Generar imágenes de barras de datos de formato condicional
description: Aspose.Cells para Python via .NET es una biblioteca de Python para trabajar con archivos de hojas de cálculo. Soporta la generación de barras de datos y elementos gráficos con formato condicional, permitiendo a los usuarios personalizar la visualización de la hoja según el valor de las celdas. Este artículo explicará cómo usar Aspose.Cells para Python para generar barras de datos y gráficos con formato condicional.
keywords: Aspose.Cells para Python via .NET, Formato condicional, Barras de datos, Imágenes, Hojas de cálculo
type: docs
weight: 40
url: /es/python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A veces, necesitas generar imágenes de Barras de Datos con Formato Condicional. Puedes usar el método [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) de Aspose.Cells para crear estas imágenes. Este artículo muestra cómo generar una imagen de barra de datos usando Aspose.Cells para Python via .NET.

{{% /alert %}}

El siguiente código de ejemplo genera la imagen de la Barra de Datos de la celda C1. Primero, accede al objeto de condición de formato de la celda, y luego a partir de ese objeto, accede al [**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar) y usa su método [**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) para generar la imagen de la celda. Finalmente, guarda la imagen en disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}
