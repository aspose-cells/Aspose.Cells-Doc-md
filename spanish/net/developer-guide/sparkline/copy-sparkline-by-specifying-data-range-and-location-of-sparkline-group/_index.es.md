---
title: Copiar Sparkline especificando el rango de datos y la ubicación del grupo de sparkline
type: docs
weight: 300
url: /es/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
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

Aspose.Cells proporciona el método SparklineCollection.Add(dataRange, row, column) para especificar el rango de datos y la ubicación de un grupo de miniaturas. El siguiente código de ejemplo carga el archivo de Excel fuente como se muestra en la captura de pantalla anterior, luego accede al primer grupo de miniaturas y agrega rangos de datos y ubicaciones en el grupo de miniaturas. Finalmente, escribe el archivo de Excel de salida en el disco, que también se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
