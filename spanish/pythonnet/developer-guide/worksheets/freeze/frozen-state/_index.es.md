---
title: Cómo verificar el estado congelado sin Excel.
linktitle: Estado congelado
type: docs
weight: 190
url: /es/python-net/how-to-check-frozen-state-of-excel-worksheet
description: En este artículo, aprenderás cómo verificar programáticamente el estado congelado de una hoja de cálculo de Excel usando las API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Python para Excel, Cómo verificar el estado congelado sin Excel, Verificar estado congelado sin Excel en Python.
---

## **Introducción**

En este artículo, aprenderemos cómo verificar el estado congelado de una hoja de cálculo de Excel programáticamente. Podemos simplemente determinar si la hoja está congelada o dividida en MS Excel. Pero, ¿hay alguna forma de saber si está congelada o dividida con C#. Podemos hacerlo fácilmente con Aspose.Cells para Python via .NET.

## **Cómo verificar el estado congelado**
Con Aspose.Cells para Python via .NET, podemos verificar si la ventana está congelada y cuántas filas y columnas están bloqueadas.

Por favor, use la propiedad [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) para verificar el estado de los paneles de la ventana 
y obtenga filas y columnas bloqueadas con el método [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any).
1. Construir un libro de trabajo para abrir el archivo.
2. Verificar si la hoja de cálculo está congelada.
3. Obtiene las filas y columnas bloqueadas

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
