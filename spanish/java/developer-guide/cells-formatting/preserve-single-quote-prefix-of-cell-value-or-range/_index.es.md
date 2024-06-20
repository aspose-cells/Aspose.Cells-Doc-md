---
title: Conservar el Prefijo de Comilla Simple del Valor de la Celda o del Rango
type: docs
weight: 1900
url: /es/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **Escenarios de uso posibles**

Cuando se agrega un valor dentro de la celda que tiene un apóstrofe inicial o una comilla simple, Microsoft Excel lo oculta, pero cuando se selecciona la celda, muestra el apóstrofe o comilla simple inicial en una barra de fórmulas como se muestra en la siguiente captura de pantalla.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells también oculta el apóstrofe inicial o comilla simple como Microsoft Excel, pero establece el [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) como **true** para esa celda. Si estableces un estilo vacío en la celda, entonces [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) vuelve a ser **falso**. Para abordar este problema, Aspose.Cells proporciona una propiedad [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix), cuando se establece en **falso**, entonces no se actualiza [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) en absoluto y se conserva su valor anterior. Esto significa que si el valor anterior de la propiedad [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) era **true**, seguirá siendo verdadero y si el valor anterior era falso, seguirá siendo falso.

## **Preservar el prefijo de comilla simple del valor de la celda o rango**

El siguiente código de muestra explica el uso de la propiedad [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) como se mencionó anteriormente. Por favor, lee los comentarios dentro del código y observa la salida por consola del código que se muestra a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
