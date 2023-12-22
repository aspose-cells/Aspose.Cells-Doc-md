---
title: Pantalla dividida de la hoja de cálculo de Excel
linktitle: Pantalla dividida
type: docs
weight: 190
url: /es/net/how-to-split-screen-of-excel-worksheet
description: En este artículo, aprenderá cómo mostrar ciertas filas y/o columnas en paneles separados dividiendo la hoja de cálculo en dos o cuatro partes mediante programación usando la Biblioteca C# con .NET API.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

En este artículo, aprenderemos cómo mostrar ciertas filas y/o columnas en paneles separados dividiendo la hoja de trabajo en dos o cuatro partes.
Cuando trabajamos con conjuntos de datos grandes, necesitamos ver algunas áreas de la misma hoja de trabajo a la vez para comparar diferentes subconjuntos de datos.
La función de pantalla dividida puede satisfacer sus necesidades.

{{% /alert %}}

##  **Cómo dividir la pantalla en Excel**
Para dividir una hoja de trabajo en dos o cuatro partes, haga lo siguiente:

1. Seleccione la fila/columna/celda delante de la cual desea realizar la división.
2. En la pestaña Ver, en el grupo Windows, haga clic en el botón Dividir.

**![Pantalla dividida](Pantalla-dividida.png)**

##  **Dividir la hoja de trabajo verticalmente en columnas**

Para separar dos áreas de la hoja de cálculo verticalmente, seleccione la columna a la derecha de la columna donde desea que aparezca la división y haga clic en el botón Dividir en Excel.

Es fácil dividir la hoja de trabajo verticalmente en columnas mediante programación con Aspose.Cells para .Net, solo necesitamos seleccionar una celda en la fila superior como celda activa, luego
dividir con[**Hoja de trabajo.Dividir**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) método.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

##  **Dividir la hoja de trabajo horizontalmente en filas**
Para separar su ventana de Excel horizontalmente, seleccione la fila debajo de la fila donde desea que se produzca la división en Excel.

Es fácil dividir la hoja de trabajo horizontalmente en filas mediante programación con Aspose.Cells para .Net, solo necesitamos seleccionar una celda en la columna de la izquierda como celda activa, luego
dividir con[**Hoja de trabajo.Dividir**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) método.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

##  **Dividir la hoja de trabajo en cuatro partes**
Para ver cuatro secciones diferentes de la misma hoja de trabajo simultáneamente, divida su pantalla vertical y horizontalmente en Excel.

Es fácil dividir la hoja de trabajo verticalmente en columnas mediante programación con Aspose.Cells para .Net, solo necesitamos seleccionar una celda que no esté en la primera fila y columna como celda activa, luego
dividir con[**Hoja de trabajo.Dividir**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) método.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

##  **Cómo eliminar la división**
Para eliminar la división de la hoja de trabajo, simplemente haga clic en el botón Dividir nuevamente.

 Aspose.Cells para .Net proporciona un[**Hoja de trabajo.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) Método para eliminar la configuración dividida.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}