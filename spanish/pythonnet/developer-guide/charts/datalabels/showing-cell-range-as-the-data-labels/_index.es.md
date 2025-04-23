---
title: Mostrar rango de celdas como las etiquetas de datos
description: Aprenda cómo mostrar un rango de celdas como etiquetas de datos en gráficos usando Aspose.Cells para Python via .NET. Nuestra guía demostrará cómo vincular las etiquetas a su fuente de datos y formatearlas para proporcionar información precisa y significativa en sus gráficos.
keywords: Aspose.Cells para Python via .NET, graficación, etiquetas de datos, rango de celdas, fuente de datos, formateo, precisión, información significativa.
type: docs
weight: 130
url: /es/python-net/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

En Microsoft Excel 2013, puedes mostrar un rango de celdas para las etiquetas de datos. Aspose.Cells para Python via .NET soporta esta característica.

{{% /alert %}}

## **Casilla de verificación para Mostrar rango de celdas como etiquetas de datos**

Para mostrar el rango de celdas como etiquetas de datos en Microsoft Excel:

1. Selecciona las etiquetas de datos de la serie y haz clic derecho para abrir el menú contextual.
1. Selecciona **Formato de etiquetas de datos**. Se muestran las opciones de etiquetas.
1. Selecciona o deselecciona la opción **La etiqueta contiene - Valor de las celdas**.

El código de ejemplo a continuación accede a las etiquetas de datos de una serie de gráficos y establece la propiedad [**DataLabels.show_cell_range**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/show_cell_range) como **true** para seleccionar la opción **La etiqueta contiene - Valor de las celdas**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ShowCellRangeAsDataLabels.py" >}}
