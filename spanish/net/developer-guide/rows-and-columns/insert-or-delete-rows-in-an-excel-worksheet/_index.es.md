---
title: Insertar o Eliminar Filas en una Hoja de Cálculo de Excel
type: docs
weight: 20
url: /es/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Este artículo proporciona el código de C# para insertar y eliminar filas en una hoja de cálculo de Excel.
keywords: c# insertar o eliminar filas en hoja de cálculo de excel, c# insertar o eliminar filas en excel, c# insertar filas en excel, c# eliminar filas en excel, insertar o eliminar filas en hoja de cálculo de excel con c#, insertar o eliminar filas en excel con c#, insertar filas en excel con c#, eliminar filas en excel con c#
---

{{% alert color="primary" %}}

Al crear una hoja de cálculo nueva, o trabajar con una hoja de cálculo existente, es posible que necesite agregar filas o columnas adicionales para alojar datos. En otros momentos, es posible que necesite eliminar filas o columnas de posiciones específicas en la hoja de cálculo.

{{% /alert %}}

Aspose.Cells ofrece dos métodos para insertar y eliminar filas: [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) y [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Estos métodos están optimizados para el rendimiento y hacen el trabajo muy rápidamente.

Para insertar o eliminar un número de filas, recomendamos que siempre use los métodos [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) y [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) en lugar de usar los métodos [**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) o [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) en un bucle.

Aspose.Cells funciona de la misma manera que lo hace Microsoft Excel. Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo y hacia la derecha. Cuando se eliminan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia arriba o hacia la izquierda. Cualquier referencia en otras hojas de cálculo y celdas se actualiza cuando se agregan o eliminan filas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
