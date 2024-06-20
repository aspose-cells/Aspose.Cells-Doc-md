---
title: Conservar el Prefijo de Comilla Simple del Valor de la Celda o del Rango
type: docs
weight: 310
url: /es/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aprenda cómo Conservar el Prefijo de Comilla Simple del Valor de la Celda o del Rango a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Python Conservar el Prefijo de Comilla Simple del Valor de la Celda o del Rango, Mostrar el prefijo de comilla simple oculto en Python, Mostrar el prefijo de comilla simple en Python
---

## **Escenarios de uso posibles**

Cuando se agrega un valor dentro de la celda que tiene un apóstrofe inicial o una comilla simple, Microsoft Excel lo oculta, pero cuando se selecciona la celda, muestra el apóstrofe o comilla simple inicial en una barra de fórmulas como se muestra en la siguiente captura de pantalla.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Python via .NET también oculta el apóstrofe inicial o la comilla simple como Microsoft Excel, pero establece [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) como **verdadero** para esa celda. Si establece un estilo vacío de la celda, entonces [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) vuelve a ser **falso**. Para lidiar con este problema, Aspose.Cells for Python via .NET proporciona la propiedad [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix), cuando se establece en **falso**, entonces [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) no se actualiza en absoluto y su antiguo valor se conserva. Esto significa que si el valor antiguo de la propiedad [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) era **verdadero**, seguirá siendo **verdadero** y si el valor antiguo era **falso**, seguirá siendo **falso**.

## **Preservar el prefijo de comilla simple del valor de la celda o rango**

El siguiente código de muestra explica el uso de la propiedad [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) como se describió anteriormente. Por favor, lea los comentarios dentro del código y vea la salida en la consola del código que se muestra a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Salida de la consola**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
