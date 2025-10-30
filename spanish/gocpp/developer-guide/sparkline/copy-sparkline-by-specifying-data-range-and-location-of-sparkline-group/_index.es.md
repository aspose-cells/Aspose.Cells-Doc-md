---
title: Copiar Sparkline especificando rango de datos y ubicación del grupo de Sparkline con Golang vía C++
linktitle: Copiar Sparkline especificando el rango de datos y la ubicación
type: docs
weight: 300
url: /es/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Aprenda cómo copiar sparklines especificando el rango de datos y la ubicación usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel le permite copiar una sparkline especificando el rango de datos y la ubicación de un grupo de sparkline. Aspose.Cells soporta esta funcionalidad.

{{% /alert %}}

Para copiar una minigráfica en otras celdas en Microsoft Excel:

1. Seleccione la celda que contiene la miniatura.
1. Seleccione **Editar datos** en la sección de **Miniatura** de la pestaña **Diseño**.
1. Seleccione **Editar ubicación y datos de grupo**.
1. Especifique el rango de datos y la ubicación.
1. Haz clic en **Aceptar**.

Aspose.Cells proporciona el método `SparklineCollection.Add(rangoDeDatos, fila, columna)` para especificar un rango de datos y una ubicación en un grupo de sparklines. El siguiente código de ejemplo carga el archivo de Excel de origen como se muestra en la captura de pantalla anterior, luego accede al primer grupo de sparklines y añade rangos de datos y ubicaciones en el grupo. Finalmente, escribe el archivo de Excel de salida en el disco, que también se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
