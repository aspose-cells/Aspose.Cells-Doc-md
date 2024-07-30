---
title: Gestionar Saltos de Página
type: docs
weight: 30
url: /es/python-net/managing-page-breaks/
description: Este artículo proporciona código de muestra y explica cómo agregar saltos de página, borrar saltos de página o eliminar saltos de página específicos en hojas de cálculo de Excel programáticamente usando Aspose.Cells para Python via .NET APIs.
keywords: Biblioteca de Excel de Python, saltos de página de Python, saltos de página de Excel en Python, borrar salto de página en Python.
---

{{% alert color="primary" %}}

Según la definición, un salto de página es un lugar en un flujo de texto donde una página termina y comienza la siguiente. Microsoft Excel permite a los usuarios agregar saltos de página en cualquier celda seleccionada de una hoja de cálculo.

La ubicación de la celda donde se agrega el salto de página, la página finaliza y el resto de los datos después del salto de página se imprime en la siguiente página al imprimir. En palabras sencillas, los saltos de página dividen tu hoja de cálculo en múltiples páginas según tus especificaciones. También puedes agregar saltos de página a tus hojas de cálculo en tiempo de ejecución utilizando Aspose.Cells para Python via .NET. Aspose.Cells para Python via .NET permite a los desarrolladores agregar dos tipos de saltos de página:

- Salto de página horizontal
- Salto de página vertical

En el resto de la discusión, describiremos cómo puedes agregar saltos de página horizontales o verticales a tus hojas de cálculo utilizando Aspose.Cells para Python via .NET.

{{% /alert %}}

## **Saltos de página**

Aspose.Cells para Python via .NET proporciona una clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite el acceso a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos utilizados para gestionar una hoja de cálculo.

Para agregar los saltos de página, utiliza las propiedades [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) y [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) de la clase,.

Las propiedades [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) y [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) son colecciones que pueden contener varios saltos de página. Cada colección contiene varios métodos para gestionar saltos de página horizontales y verticales.

## **Cómo agregar saltos de página**

Para agregar un salto de página en una hoja de cálculo, inserta saltos de página verticales y horizontales en la celda especificada llamando a los métodos [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) y [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str). Cada método **add** toma el nombre de la celda donde se debe agregar el salto.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

En la vista preliminar de saltos de página o en la vista preliminar de impresión, puedes ver cómo funcionan los saltos de página.

{{% /alert %}}


## **Importante saber**

Cuando se establecen las propiedades **FitToPages** (es decir, [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) y [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) en la configuración de la página, la configuración de saltos de página se ve afectada, por lo que si imprime la hoja de cálculo, la configuración de saltos de página no se tiene en cuenta aunque esté configurada.
