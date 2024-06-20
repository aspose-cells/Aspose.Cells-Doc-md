---
title: Insertar hipervínculos en Excel u OpenOffice
linktitle: Gestión de hipervínculos
type: docs
weight: 45
url: /es/python-net/insert-hyperlinks-to-excel/
description: Cómo insertar hipervínculos en un archivo de Excel con la biblioteca Aspose.Cells para Python via .NET sin MS Excel.
keywords: Biblioteca de Excel de Python, Insertar hipervínculos en Excel en Python, Agregar o insertar hipervínculos en Python, Agregar o insertar un enlace a una URL en Python, Agregar o insertar un enlace a una celda en Python, Agregar un enlace a un archivo externo
---

{{% alert color="primary" %}} 

Un hipervínculo se usa para crear un enlace entre dos entidades. Todos están familiarizados con el uso de hipervínculos, especialmente en sitios web.
Usando Aspose.Cells para Python via .NET, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Microsoft Excel. Este tema discute qué tipos de hipervínculos son compatibles con Aspose.Cells para Python via .NET y cómo se pueden utilizar en nuestros archivos de Excel.

{{% /alert %}} 
## **Cómo Agregar Hipervínculos**
Aspose.Cells para Python via .NET permite a los desarrolladores agregar hipervínculos a archivos de Excel ya sea utilizando la API o hojas de cálculo de diseñador (hojas de cálculo donde los hipervínculos se crean manualmente y Aspose.Cells para Python via .NET se utiliza para importarlos en otras hojas de cálculo).

Aspose.Cells para Python via .NET proporciona una clase, [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona diferentes métodos para agregar diferentes hipervínculos a archivos de Excel.

## **Cómo Agregar un Enlace a una URL**
La clase [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) contiene una colección [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). Cada elemento en la colección [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) representa un [Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink). Agregue hipervínculos a URLs llamando al método [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) de la colección [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). El método [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la URL.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

En el ejemplo anterior, se añade un hipervínculo a una URL en una celda vacía, **A1**. En tales casos, si una celda está vacía, entonces la dirección URL también se agrega a esa celda vacía como su valor. Si la celda no está vacía y se agrega un hipervínculo, el valor de la celda se ve como texto plano. Para que se vea como un hipervínculo, aplique la configuración de formato adecuada en esa celda.

{{% /alert %}} 

## **Cómo Agregar un Enlace a una Celda en el Mismo Archivo**
Es posible añadir hipervínculos a celdas en el mismo archivo de Excel llamando al método [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) de la colección [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). El método [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) funciona tanto para hipervínculos internos como externos. Una versión del método sobrecargado toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda de destino.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **Cómo Agregar un Enlace a un Archivo Externo**
Es posible agregar hipervínculos a archivos externos de Excel llamando al método [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) de la colección [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). El método [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo externo de Excel.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **Temas avanzados**
- [Agregar hipervínculos de imagen](/cells/es/python-net/add-image-hyperlinks/)
- [Detectar tipo de hipervínculo](/cells/es/python-net/detect-hyperlink-type/)
- [Editando Hipervínculos de la Hoja de Cálculo](/cells/es/python-net/editing-hyperlinks-of-worksheet/)
- [Obtener Hipervínculos en Rango](/cells/es/python-net/get-hyperlinks-in-range/)

