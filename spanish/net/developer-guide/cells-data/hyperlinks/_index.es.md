---
title: Insertar hipervínculos en Excel u OpenOffice
linktitle: Gestión de hipervínculos
type: docs
weight: 45
url: /es/net/insert-hyperlinks-to-excel/
description: Cómo insertar hipervínculos en un archivo de Excel con la librería Aspose.Cells sin MS Excel.
keywords: Insertar hipervínculos en Excel, Agregar o insertar hipervínculos, Agregar o insertar enlace a una URL, Agregar o insertar un enlace a una celda, Agregar un enlace a un archivo externo
---

{{% alert color="primary" %}} 

Un hipervínculo se usa para crear un enlace entre dos entidades. Todos están familiarizados con el uso de hipervínculos, especialmente en sitios web.
Utilizando Aspose.Cells, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Microsoft Excel. Este tema discute qué tipos de hipervínculos son compatibles con Aspose.Cells y cómo se pueden usar en nuestros archivos de Excel.

{{% /alert %}} 
## **Añadiendo hipervínculos**
Aspose.Cells permite a los desarrolladores añadir hipervínculos a archivos de Excel ya sea utilizando la API o hojas de cálculo de diseñador (hojas de cálculo donde los hipervínculos son creados manualmente y Aspose.Cells se utiliza para importarlos en otras hojas de cálculo).

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona diferentes métodos para añadir diferentes hipervínculos a archivos de Excel.
## **Añadir un enlace a una URL**
La clase [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) contiene una colección [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Cada elemento en la colección [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) representa un [Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink). Añada hipervínculos a URLs llamando al método [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) de la colección [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). El método [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

En el ejemplo anterior, se añade un hipervínculo a una URL en una celda vacía, **A1**. En tales casos, si una celda está vacía, entonces la dirección URL también se agrega a esa celda vacía como su valor. Si la celda no está vacía y se agrega un hipervínculo, el valor de la celda se ve como texto plano. Para que se vea como un hipervínculo, aplique la configuración de formato adecuada en esa celda.

{{% /alert %}} 
## **Añadir un enlace a una celda en el mismo archivo**
Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) collection's [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) método. El método [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) funciona tanto para hipervínculos internos como externos. Una versión del metodo sobrecargado toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda de destino.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Agregar un enlace a un archivo externo**
Es posible agregar hipervínculos a archivos externos de Excel llamando al [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) collection's [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) método. El método [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo externo de Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Temas avanzados**
- [Agregar hipervínculos de imagen](/cells/es/net/add-image-hyperlinks/)
- [Detectar tipo de hipervínculo](/cells/es/net/detect-hyperlink-type/)
- [Editando Hipervínculos de la Hoja de Cálculo](/cells/es/net/editing-hyperlinks-of-worksheet/)
- [Obtener Hipervínculos en Rango](/cells/es/net/get-hyperlinks-in-range/)

