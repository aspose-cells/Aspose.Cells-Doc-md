---
title: Mostrar el rango de celdas como etiquetas de datos con Golang a través de C++
linktitle: Mostrar rango de celdas como las etiquetas de datos
description: Aprenda cómo mostrar un rango de celdas como etiquetas de datos en gráficos usando Aspose.Cells for C++. Nuestra guía demostrará cómo vincular las etiquetas a su fuente de datos y formatearlas para proporcionar información precisa y significativa en sus gráficos.
keywords: Aspose.Cells for C++, gráficos, etiquetas de datos, rango de celdas, fuente de datos, formateo, precisión, información significativa.
type: docs
weight: 130
url: /es/go-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

En Microsoft Excel 2013, puedes mostrar un rango de celdas para las etiquetas de datos. Aspose.Cells es compatible con esta función.

{{% /alert %}}

## **Casilla de verificación para Mostrar rango de celdas como etiquetas de datos**

Para mostrar el rango de celdas como etiquetas de datos en Microsoft Excel:

1. Selecciona las etiquetas de datos de la serie y haz clic derecho para abrir el menú contextual.
1. Selecciona **Formato de etiquetas de datos**. Se muestran las opciones de etiquetas.
1. Selecciona o deselecciona la opción **La etiqueta contiene - Valor de las celdas**.

El código de ejemplo a continuación accede a las etiquetas de datos de una serie de gráficos y establece la propiedad [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/go-cpp/datalabels/getshowcellrange/) como **true** para seleccionar la opción **La etiqueta contiene - Valor de las celdas**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowingCellRangeAsTheDataLabels.go" >}}
