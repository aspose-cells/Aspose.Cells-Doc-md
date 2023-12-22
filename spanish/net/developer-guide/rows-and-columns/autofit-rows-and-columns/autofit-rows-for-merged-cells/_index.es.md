---
title: AutoFit filas para fusionado Cells
type: docs
weight: 120
url: /es/net/autofit-rows-for-merged-cells/
---
{{% alert color="primary" %}}

Microsoft Excel proporciona una función que le permite ajustar automáticamente el tamaño de la altura de una celda según su contenido. La característica se llama filas de ajuste automático. Microsoft Excel no establece la operación de ajuste automático en celdas combinadas de forma nativa. A veces, la función se vuelve vital para un usuario que también necesita implementar filas de ajuste automático en celdas fusionadas.

{{% /alert %}}

##  **Cómo utilizar AutoFitMergedCellsType para ajustar automáticamente filas**
 Aspose.Cells admite esta función a través del[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API. Con este API, es posible ajustar automáticamente filas en una hoja de trabajo, incluidas celdas combinadas. Aquí hay una lista de todos los tipos posibles de celdas fusionadas de ajuste automático:

- Ninguno
- Primera linea
- Última línea
- Cada línea

##  **Filas de ajuste automático para Cells fusionado**

Consulte el siguiente código, crea un objeto de libro de trabajo y agrega varias hojas de trabajo. Utilice diferentes métodos para operaciones de ajuste automático en cada hoja de trabajo. La captura de pantalla muestra los resultados después de la ejecución del código de muestra.

<br>
<img src="result.png" width=80% />

##  **C# Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
