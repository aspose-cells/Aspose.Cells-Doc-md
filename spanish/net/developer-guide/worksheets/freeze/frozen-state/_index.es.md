---
title: Cómo comprobar el estado congelado sin Excel.
linktitle: Estado congelado
type: docs
weight: 190
url: /es/net/how-to-check-frozen-state-of-excel-worksheet
description: En este artículo, aprenderá cómo verificar el estado congelado de la hoja de cálculo de Excel mediante programación usando la biblioteca C# con .NET API.
---
{{% alert color="primary" %}}

En este artículo, aprenderemos cómo verificar el estado congelado de la hoja de cálculo de Excel mediante programación.
Simplemente podemos encontrar si la hoja de trabajo está congelada o dividida en MS Excel. Pero, ¿hay alguna manera de saber si está congelado o dividido con CSharp?
Simplemente podemos hacerlo con Aspose.Cells para .Net.
{{% /alert %}}

##  **¿Están congelados los cristales de las ventanas?**
Con Aspose.Cells para .Net, podemos comprobar si la ventana está congelada y cuántas filas y columnas están bloqueadas.

 Por favor use el[**Hoja de trabajo.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) Propiedad para comprobar el estado de los cristales de las ventanas.
 y bloquea filas y columnas con[**Hoja de trabajo.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)método.
1. Construya el libro de trabajo para abrir el archivo.
2. Compruebe si la hoja de trabajo está congelada.
3. Obtiene la fila y las columnas bloqueadas.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}