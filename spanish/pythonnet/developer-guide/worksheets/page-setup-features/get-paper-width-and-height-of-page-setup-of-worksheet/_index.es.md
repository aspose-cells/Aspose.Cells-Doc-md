---
title: Obtener el ancho y alto del papel del Diseño de página de la hoja de cálculo
type: docs
weight: 50
url: /es/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Descubrirás en este artículo cómo obtener el ancho y la altura del papel del Configuración de Página en una hoja de Excel usando código Python de forma programática con la API o Biblioteca de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel para Python, ancho del papel en la configuración de página en Python, altura del papel en la configuración de página en Python.
---

## **Escenarios de uso posibles**

A veces, es necesario conocer el ancho y alto del tamaño de papel tal como se ha establecido en la configuración de página de la hoja de cálculo. Por favor, utiliza las propiedades [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) y [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) para este propósito.

## **Obtener el ancho y alto del papel del diseño de página de la hoja de cálculo**

El siguiente código de ejemplo explica el uso de las propiedades [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) y [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). Primero cambia el tamaño del papel a *A2* y luego encuentra el ancho y la altura del papel, después lo cambia a *A3*, *A4*, *Carta* y encuentra respectivamente el ancho y la altura del papel.

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Salida de la consola**

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
