---
title: Cómo verificar el estado congelado sin Excel.
linktitle: Estado congelado
type: docs
weight: 190
url: /es/net/how-to-check-frozen-state-of-excel-worksheet
description: En este artículo, aprenderá a verificar el estado congelado de una hoja de cálculo de Excel programáticamente utilizando la biblioteca C# con API .NET.

---

## **Introducción**

En este artículo, aprenderemos cómo verificar el estado congelado de la hoja de cálculo de Excel programáticamente. Podemos entender fácilmente si la hoja de cálculo está congelada o dividida en MS Excel. Pero ¿hay una forma de saber si está congelada o dividida con C#? Podemos hacerlo fácilmente con Aspose.Cells para .Net.

## **¿Están congelados los paneles de la ventana?**
Con Aspose.Cells para .Net, podemos verificar si la ventana está congelada y cuántas filas y columnas están bloqueadas.

Por favor, use la propiedad [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) para verificar el estado de los paneles de la ventana 
y obtenga filas y columnas bloqueadas con el método [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/).
1. Construir un libro de trabajo para abrir el archivo.
2. Verificar si la hoja de cálculo está congelada.
3. Obtiene las filas y columnas bloqueadas

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
{{< app/cells/assistant language="csharp" >}}
