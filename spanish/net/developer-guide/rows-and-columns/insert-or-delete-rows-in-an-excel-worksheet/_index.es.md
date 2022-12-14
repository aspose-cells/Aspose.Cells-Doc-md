---
title: Insertar o eliminar filas en una hoja de cálculo de Excel
type: docs
weight: 20
url: /es/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Este artículo proporciona el código C# para insertar y eliminar filas en la hoja de cálculo de Excel
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

Al crear una nueva hoja de trabajo o trabajar con una hoja de trabajo existente, es posible que deba agregar filas o columnas adicionales para acomodar los datos. En otras ocasiones, es posible que deba eliminar filas o columnas de posiciones específicas en la hoja de cálculo.

{{% /alert %}}

 Aspose.Cells ofrece dos métodos para insertar y eliminar filas:[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) y[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Estos métodos están optimizados para el rendimiento y hacen el trabajo muy rápidamente.

 Para insertar o eliminar un número de filas, le recomendamos que utilice siempre el[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) y[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) métodos en lugar de usar el[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) o[**Borrar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)métodos en un bucle.

Aspose.Cells funciona de la misma manera que Microsoft Excel. Cuando se agregan filas o columnas, el contenido de la hoja de trabajo se desplaza hacia abajo y hacia la derecha. Cuando se eliminan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia arriba o hacia la izquierda. Cualquier referencia en otras hojas de trabajo y celdas se actualiza cuando se agregan o eliminan filas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
