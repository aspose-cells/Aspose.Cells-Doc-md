---
title: Copie Sparkline especificando el rango de datos y la ubicación del grupo Sparkline
type: docs
weight: 300
url: /es/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft Excel le permite copiar un minigráfico especificando el rango de datos y la ubicación de un grupo de minigráficos. Aspose.Cells admite esta función.

{{% /alert %}}

Para copiar un minigráfico a otras celdas en Microsoft Excel:

1. Seleccione la celda que contiene el minigráfico.
1.  Seleccione**Editar datos** desde el**Minigráfico** sección de la**Diseño** pestaña.
1.  Seleccione**Editar ubicación y datos del grupo**.
1. Especifique el rango de datos y la ubicación.
1.  Hacer clic**OK**.

Aspose.Cells proporciona el método SparklineCollection.Add(dataRange, fila, columna) para especificar el rango de datos y la ubicación de un grupo de minigráficos. El siguiente código de ejemplo carga el archivo de origen de Excel como se muestra en la captura de pantalla anterior, luego accede al primer grupo de minigráficos y agrega rangos de datos y ubicaciones en el grupo de minigráficos. Finalmente, escribe el archivo de salida de Excel en el disco que también se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
