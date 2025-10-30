---
title: Copiar Sparkline especificando el rango de datos y la ubicación del grupo de sparkline
type: docs
weight: 300
url: /es/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel permite copiar un mini gráfico especificando el rango de datos y la ubicación de un grupo de mini gráficos. Aspose.Cells para Python via .NET soporta esta característica.

{{% /alert %}}

Para copiar una minigráfica en otras celdas en Microsoft Excel:

1. Seleccione la celda que contiene la miniatura.
1. Seleccione **Editar datos** en la sección de **Miniatura** de la pestaña **Diseño**.
1. Seleccione **Editar ubicación y datos de grupo**.
1. Especifique el rango de datos y la ubicación.
1. Haz clic en **Aceptar**.

Aspose.Cells para Python via .NET proporciona el método SparklineCollection.Add(rangoDeDatos, fila, columna) para especificar el rango de datos y la ubicación de un grupo de mini gráficos. El siguiente código de ejemplo carga el archivo Excel fuente como se muestra en la captura de pantalla anterior, luego accede al primer grupo de mini gráficos y agrega rangos de datos y ubicaciones en el grupo. Finalmente, escribe el archivo Excel de salida en el disco, que también se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
