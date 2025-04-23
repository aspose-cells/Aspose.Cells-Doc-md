---
title: Obtener el ancho y alto del papel del Diseño de página de la hoja de cálculo
type: docs
weight: 50
url: /es/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Descubrirás en este artículo cómo obtener el Ancho de papel y la Altura de papel del Diseño de página de la hoja de cálculo de Excel utilizando código C# de forma programática con la API o biblioteca .NET.
keywords: ancho de papel de la configuración de página de excel c#, altura de papel de la configuración de página de excel c#
---

## **Escenarios de uso posibles**

A veces, es necesario conocer el ancho y alto del tamaño de papel tal como se ha establecido en la configuración de página de la hoja de cálculo. Por favor, utiliza las propiedades [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) y [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) para este propósito.

## **Obtener el ancho y alto del papel del diseño de página de la hoja de cálculo**

El siguiente código de muestra explica el uso de las propiedades [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) y [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight). Primero cambia el tamaño de papel a *A2* y luego encuentra el ancho y alto del papel, luego lo cambia a *A3*, *A4*, *Carta* y encuentra respectivamente el ancho y alto del papel.

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **Salida de la consola**

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
