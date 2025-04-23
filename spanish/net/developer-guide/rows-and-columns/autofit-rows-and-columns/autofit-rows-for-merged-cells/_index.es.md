---
title: Ajustar automáticamente las filas para celdas fusionadas
type: docs
weight: 120
url: /es/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel proporciona una función que permite ajustar automáticamente la altura de una celda según su contenido. La función se llama autofit rows. Microsoft Excel no establece operación autofit en celdas fusionadas de forma nativa. A veces la función se vuelve vital para un usuario que realmente necesita implementar autofit rows en celdas fusionadas también.

{{% /alert %}}

## **Cómo usar AutoFitMergedCellsType para ajustar las filas automáticamente**
Aspose.Cells admite esta función a través de la API [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/). Utilizando esta API, es posible ajustar automáticamente las filas en una hoja de cálculo, incluidas las celdas fusionadas. Aquí hay una lista de todos los posibles tipos de ajuste automático de celdas fusionadas:

- Ninguno
- Primera línea
- Última línea
- Cada línea

## **Autoajustar filas para celdas fusionadas**

Por favor, vea el siguiente código, crea un objeto workbook y agrega múltiples hojas de trabajo. Utiliza diferentes métodos para operaciones autofit en cada hoja de trabajo. La captura de pantalla muestra los resultados después de la ejecución del código de muestra.

<br>
<img src="result.png" width=80% />

## **Código de muestra en C#**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
