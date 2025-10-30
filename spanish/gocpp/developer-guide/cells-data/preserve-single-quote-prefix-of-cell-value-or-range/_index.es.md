---
title: Preservar el prefijo de comilla simple del valor o rango de celda con Golang vía C++
linktitle: Conservar el Prefijo de Comilla Simple del Valor de la Celda o del Rango
type: docs
weight: 310
url: /es/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aprende cómo preservar el prefijo de comillas simples del valor de la celda o rango a través de la API Aspose.Cells for C++.
keywords: Preservar el prefijo de comilla simple del valor de la celda o rango, ocultar el apostrofe o comilla simple inicial, mostrar el apostrofe o comilla simple inicial
---

## **Escenarios de uso posibles**

Cuando colocas un valor dentro de una celda que tiene un apóstrofe o comilla simple al principio, Microsoft Excel lo oculta, pero cuando seleccionas la celda, muestra el apóstrofe o comilla simple en la barra de fórmulas como se muestra en la siguiente captura de pantalla.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells también oculta el apóstrofe o comilla simple como Microsoft Excel, pero configura [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) como **true** para esa celda. Si estableces un estilo vacío en la celda, entonces [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) vuelve a ser **false**. Para resolver este problema, Aspose.Cells proporciona la propiedad [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/), que cuando se establece en **false**, no actualiza [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) y conserva su valor antiguo. Esto significa que si el valor anterior de la propiedad [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) era **true**, seguirá siendo **true**, y si era **false**, seguirá siendo **false**.

## **Preservar el prefijo de comilla simple del valor de la celda o rango**

El siguiente código de ejemplo explica el uso de la propiedad [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/) como se describió anteriormente. Por favor, lee los comentarios dentro del código y mira la salida de la consola del código dado abajo para mayor ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **Salida de la consola**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
