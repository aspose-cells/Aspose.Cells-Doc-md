---
title: Ajustar automáticamente las filas para celdas fusionadas
type: docs
weight: 120
url: /es/python-net/autofit-rows-for-merged-cells/
description: Este artículo muestra cómo ajustar automáticamente las filas para celdas combinadas a través de la API Aspose.Cells para Python via .NET.
keywords: Bibilioteca de Excel de Python, Cómo usar AutoFitMergedCellsType para ajustar automáticamente filas, Ajustar Filas para Celdas Fusionadas en Python.
---

{{% alert color="primary" %}}

Microsoft Excel proporciona una función que permite ajustar automáticamente la altura de una celda según su contenido. La función se llama autofit rows. Microsoft Excel no establece operación autofit en celdas fusionadas de forma nativa. A veces la función se vuelve vital para un usuario que realmente necesita implementar autofit rows en celdas fusionadas también.

{{% /alert %}}

## **Cómo usar AutoFitMergedCellsType para ajustar las filas automáticamente**
Aspose.Cells para Python via .NET soporta esta función a través de la [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/) API. Usando esta API, es posible ajustar automáticamente las filas en una hoja de cálculo incluyendo celdas fusionadas. Aquí hay una lista de todos los tipos posibles de ajuste automático en celdas fusionadas:

- NONE
- PRIMERA_LÍNEA
- ÚLTIMA_LÍNEA
- CADA_LÍNEA

## **Autoajustar filas para celdas fusionadas**

Por favor, vea el siguiente código, crea un objeto workbook y agrega múltiples hojas de trabajo. Utiliza diferentes métodos para operaciones autofit en cada hoja de trabajo. La captura de pantalla muestra los resultados después de la ejecución del código de muestra.

<br>
<img src="result.png" width=80% />

## **Código de muestra en C#**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
