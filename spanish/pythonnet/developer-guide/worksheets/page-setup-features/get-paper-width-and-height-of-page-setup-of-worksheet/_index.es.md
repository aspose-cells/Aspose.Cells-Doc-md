---
title: Obtener el ancho y alto del papel del Diseño de página de la hoja de cálculo
type: docs
weight: 50
url: /es/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Descubrirás en este artículo cómo obtener el Ancho de Papel y la Altura de Papel de la Configuración de Página de la Hoja de Excel utilizando código Python de forma programática con la API o Biblioteca de Aspsoe.Cells for Python via .NET.
keywords: Biblioteca de Excel de Python, ancho de papel de configuración de página de excel en Python, altura de papel de configuración de página de excel en Python.
---

## **Escenarios de uso posibles**

A veces, es necesario conocer el ancho y alto del tamaño de papel tal como se ha establecido en la configuración de página de la hoja de cálculo. Por favor, utiliza las propiedades [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) y [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) para este propósito.

## **Obtener el ancho y alto del papel del diseño de página de la hoja de cálculo**

El siguiente código de muestra explica el uso de las propiedades [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) y [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). Primero cambia el tamaño de papel a *A2* y luego encuentra el ancho y la altura del papel, luego lo cambia a *A3*, *A4*, *Letter* y encuentra respectivamente el ancho y la altura del papel.

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
