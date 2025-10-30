---
title: Dividir pantalla de la hoja de cálculo de Excel
linktitle: Pantalla dividida
type: docs
weight: 190
url: /es/python-net/how-to-split-screen-of-excel-worksheet
description: En este artículo, aprenderás cómo mostrar ciertas filas y/o columnas en paneles separados dividiendo la hoja en dos o cuatro partes programáticamente usando las API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Python para Excel, Congelar filas superiores en Python, Congelar primera fila en Python, Dividir hoja de cálculo verticalmente en columnas, Dividir hoja de cálculo horizontalmente en filas, Dividir hoja en cuatro partes, Cómo eliminar la división en Python.
---

## **Introducción**

En este artículo, aprenderemos cómo mostrar ciertas filas y/o columnas en paneles separados dividiendo la hoja de cálculo en dos o cuatro partes. Al trabajar con conjuntos de datos extensos, necesitamos ver algunas áreas de la misma hoja de cálculo a la vez para comparar diferentes subconjuntos de datos. La función de pantalla dividida puede satisfacer tus necesidades.

## **Cómo dividir la pantalla en Excel**
Para dividir una hoja de cálculo en dos o cuatro partes, haz lo siguiente:

1. Selecciona la fila/columna/celda antes de la cual deseas colocar la división.
2. En la pestaña de Vista, en el grupo de Ventanas, haz clic en el botón Dividir.

**![Pantalla dividida](Split-Screen.png)**

## **Cómo dividir la hoja de cálculo verticalmente en columnas**

Para separar dos áreas de la hoja de cálculo verticalmente, selecciona la columna a la derecha de la columna donde deseas que aparezca la división y haz clic en el botón Dividir en Excel.

Es fácil dividir la hoja de cálculo verticalmente en columnas mediante programación con Aspose.Cells para Python via .NET, solo necesitamos seleccionar una celda en la fila superior como celda activa, luego
dividir con el método [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **Cómo dividir la hoja de cálculo horizontalmente en filas**
Para separar tu ventana de Excel horizontalmente, selecciona la fila debajo de la fila donde deseas que ocurra la división en Excel.

Es fácil dividir la hoja de cálculo horizontalmente en filas mediante programación con Aspose.Cells para Python via .NET, solo necesitamos seleccionar una celda en la columna izquierda como celda activa, luego
dividir con el método [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **Cómo dividir la hoja de cálculo en cuatro partes**
Para ver cuatro secciones diferentes de la misma hoja de cálculo simultáneamente, divide tu pantalla tanto vertical como horizontalmente en Excel.

Es fácil dividir la hoja de cálculo verticalmente en columnas mediante programación con Aspose.Cells para Python via .NET, solo necesitamos seleccionar una celda que no esté en la primera fila y columna como celda activa, luego
dividir con el método [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **Cómo eliminar la división**
Para eliminar la división de la hoja de cálculo, simplemente haz clic en el botón Dividir nuevamente.

Aspose.Cells para Python via .NET ofrece un método [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) para eliminar la configuración de división.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
{{< app/cells/assistant language="python-net" >}}
