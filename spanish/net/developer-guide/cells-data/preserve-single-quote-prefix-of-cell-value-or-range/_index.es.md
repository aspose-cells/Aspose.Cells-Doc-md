---
title: Conservar el Prefijo de Comilla Simple del Valor de la Celda o del Rango
type: docs
weight: 310
url: /es/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aprende cómo preservar el prefijo de comilla simple del valor de la celda o rango a través de la API Aspose.Cells for .NET
keywords: Preservar el prefijo de comilla simple del valor de la celda o rango, ocultar el apostrofe o comilla simple inicial, mostrar el apostrofe o comilla simple inicial
---

## **Escenarios de uso posibles**

Cuando se agrega un valor dentro de la celda que tiene un apóstrofe inicial o una comilla simple, Microsoft Excel lo oculta, pero cuando se selecciona la celda, muestra el apóstrofe o comilla simple inicial en una barra de fórmulas como se muestra en la siguiente captura de pantalla.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells también oculta el apostrofe o comilla simple inicial como Microsoft Excel, pero establece el [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) como **verdadero** para esa celda. Si estableces un estilo vacío de la celda, entonces [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) vuelve a ser **falso**. Para tratar con este problema, Aspose.Cells proporciona la propiedad [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix), cuando se establece en **falso**, entonces [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) no se actualiza en absoluto y su antiguo valor se conserva. Esto significa que si el antiguo valor de la propiedad [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) era **verdadero**, permanecerá **verdadero** y si el antiguo valor era **falso**, permanecerá **falso**.

## **Preservar el prefijo de comilla simple del valor de la celda o rango**

El siguiente código de muestra explica el uso de la propiedad [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) como se describió anteriormente. Por favor, lea los comentarios dentro del código y vea la salida en la consola del código que se muestra a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
