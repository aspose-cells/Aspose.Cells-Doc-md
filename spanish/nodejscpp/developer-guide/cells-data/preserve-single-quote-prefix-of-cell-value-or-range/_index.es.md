---
title: Conservar el Prefijo de Comilla Simple del Valor de la Celda o del Rango
type: docs
weight: 310
url: /es/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aprende a Preservar el Prefijo de Comillas Simples de Valor de Celda o Rango a través de la API Aspose.Cells for Node.js via C++.
keywords: Preservar Prefijo de Comillas Simples de Valor de Celda o Rango en Node.js vía C++, Ocultar apóstrofe inicial o marca de cita simple en Node.js vía C++, Mostrar apóstrofe inicial o marca de cita simple en Node.js vía C++
---

## **Escenarios de uso posibles**

Cuando se agrega un valor dentro de la celda que tiene un apóstrofe inicial o una comilla simple, Microsoft Excel lo oculta, pero cuando se selecciona la celda, muestra el apóstrofe o comilla simple inicial en una barra de fórmulas como se muestra en la siguiente captura de pantalla.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++ también oculta el apóstrofe inicial o comilla simple como Microsoft Excel, pero establece [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) como **verdadero** para esa celda. Si estableces un estilo vacío en la celda, entonces [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) vuelve a ser **falso**. Para gestionar este problema, Aspose.Cells for Node.js via C++ proporciona el método [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-), cuando se configura como **falso**, entonces [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) no se actualiza en absoluto y su valor anterior se conserva. Esto significa que si el valor anterior de [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) era **verdadero**, seguirá siendo **verdadero**, y si era **falso**, seguirá siendo **falso**.

## **Preservar el prefijo de comilla simple del valor de la celda o rango**

El siguiente código de ejemplo explica el uso del método [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) como se describió anteriormente. Por favor, lee los comentarios dentro del código y consulta la salida de consola del código a continuación para mayor ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **Salida de la consola**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
