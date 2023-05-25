---
title: Obtenga el ancho y el alto del papel de la configuración de página de la hoja de trabajo
type: docs
weight: 50
url: /es/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Descubrirá en este artículo cómo obtener el ancho y la altura del papel de la configuración de página de la hoja de cálculo de Excel usando el código C# mediante programación con .NET API o Biblioteca.
keywords: excel page setup paper width c#, excel page setup paper height c#
---
##  **Posibles escenarios de uso**

A veces, necesita saber el ancho y el alto del tamaño del papel tal como se configuró en la configuración de página de la hoja de trabajo. Por favor use el[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)y[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)propiedades para este fin.

##  **Obtenga el ancho y el alto del papel de la configuración de página de la hoja de trabajo**

 El siguiente código de ejemplo explica el uso de[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) y[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) propiedades. Primero cambia el tamaño del papel a*A2*y luego encuentra el ancho y la altura del papel, luego lo cambia a*A3*, *A4*, *Carta*encuentra el ancho y la altura del papel respectivamente.

###  **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

###  **Salida de consola**

Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
