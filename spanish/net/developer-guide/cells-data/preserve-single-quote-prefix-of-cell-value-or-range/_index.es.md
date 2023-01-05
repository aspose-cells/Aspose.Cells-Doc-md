---
title: Conservar el prefijo de comillas simples del valor o rango Cell
type: docs
weight: 310
url: /es/net/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Posibles escenarios de uso**

Cuando coloca algún valor dentro de la celda que tiene un apóstrofo inicial o una comilla simple, entonces Microsoft Excel lo oculta, pero cuando selecciona la celda, muestra el apóstrofe inicial o una comilla simple en una barra de fórmulas como se muestra en la siguiente captura de pantalla.

![todo:imagen_alternativa_texto](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells también oculta el apóstrofo inicial o la comilla simple como Microsoft Excel pero establece el[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) como**verdadero** para esa celda. Si establece un estilo vacío de la celda, entonces[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) se convierte**falso** de nuevo. Para hacer frente a este problema, Aspose.Cells proporciona[**Bandera de estilo.Prefijo de cotización**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) propiedad, cuando se establece**falso** , después[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)no se actualiza en absoluto y se conserva su valor anterior. Significa que si el valor antiguo de[**Estilo.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)la propiedad era**verdadero** , permanecerá**verdadero** y si el valor anterior era**falso** , permanecerá**falso**.

## **Conservar el prefijo de comillas simples del valor o rango Cell**

 El siguiente código de ejemplo explica el uso de[**Bandera de estilo.Prefijo de cotización**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)propiedad como se describió anteriormente. Lea los comentarios dentro del código y vea la salida de la consola del código que se proporciona a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
