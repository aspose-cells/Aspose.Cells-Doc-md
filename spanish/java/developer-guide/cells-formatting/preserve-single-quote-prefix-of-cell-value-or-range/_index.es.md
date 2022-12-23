---
title: Conservar el prefijo de comillas simples del valor o rango Cell
type: docs
weight: 1900
url: /es/java/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Posibles escenarios de uso**

Cuando coloca algún valor dentro de la celda que tiene un apóstrofo inicial o una comilla simple, entonces Microsoft Excel lo oculta, pero cuando selecciona la celda, muestra el apóstrofe inicial o una comilla simple en una barra de fórmulas como se muestra en la siguiente captura de pantalla.

![todo:imagen_alternativa_texto](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells también oculta el apóstrofo inicial o la comilla simple como Microsoft Excel pero establece el[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) como**verdadero** para esa celda. Si establece un estilo vacío de la celda, entonces[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) se convierte**falso** de nuevo. Para hacer frente a este problema, Aspose.Cells proporciona[**Bandera de estilo.Prefijo de cotización**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) propiedad, cuando se establece**falso**, después[**Bandera de estilo.Prefijo de cotización**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)no se actualiza en absoluto y se conserva su valor anterior. Significa que si el valor antiguo de[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)la propiedad era**verdadero**, seguirá siendo verdadero y si el valor anterior era falso, seguirá siendo falso.

## **Conservar el prefijo de comillas simples del valor o rango Cell**

El siguiente código de ejemplo explica el uso de[**Bandera de estilo.Prefijo de cotización**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)propiedad como se describió anteriormente. Lea los comentarios dentro del código y vea la salida de la consola del código que se proporciona a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
