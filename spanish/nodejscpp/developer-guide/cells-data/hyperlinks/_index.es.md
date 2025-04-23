---
title: Insertar hipervínculos en Excel u OpenOffice
linktitle: Gestión de hipervínculos
type: docs
weight: 45
url: /es/nodejs-cpp/insert-hyperlinks-to-excel/
description: Cómo insertar hipervínculos en archivos de Excel con la biblioteca Aspose.Cells sin MS Excel usando Node.js a través de C++.
keywords: Insertar Hipervínculos en Excel Node.js a través de C++, Agregar o Insertar Hipervínculos en Node.js a través de C++, Agregar o Insertar enlace a una URL en Node.js a través de C++, Añadir o Insertar un Enlace a una Celda en Node.js a través de C++, Agregar un Enlace a un Archivo Externo en Node.js a través de C++
---

{{% alert color="primary" %}} 

Un hipervínculo se usa para crear un enlace entre dos entidades. Todos están familiarizados con el uso de hipervínculos, especialmente en sitios web.
Utilizando Aspose.Cells, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Microsoft Excel. Este tema discute qué tipos de hipervínculos son compatibles con Aspose.Cells y cómo se pueden usar en nuestros archivos de Excel.

{{% /alert %}} 

## **Añadiendo hipervínculos**
Aspose.Cells permite a los desarrolladores agregar hipervínculos a archivos de Excel usando la API o hojas de cálculo de diseño (hojas donde los hipervínculos se crean manualmente y Aspose.Cells se usa para importarlos en otras hojas).

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) que permite acceder a cada hoja del archivo de Excel. Una hoja se representa por la clase [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ofrece diferentes métodos para agregar distintos hipervínculos a archivos de Excel.
## **Añadir un enlace a una URL**
La clase [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) contiene una colección [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--). Cada elemento en la colección [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) representa un [Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink). Agrega hipervínculos a URLs llamando al método [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) de la colección [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). El método [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) acepta los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la URL.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

En el ejemplo anterior, se añade un hipervínculo a una URL en una celda vacía, **A1**. En tales casos, si una celda está vacía, entonces la dirección URL también se agrega a esa celda vacía como su valor. Si la celda no está vacía y se agrega un hipervínculo, el valor de la celda se ve como texto plano. Para que se vea como un hipervínculo, aplique la configuración de formato adecuada en esa celda.

{{% /alert %}} 
## **Añadir un enlace a una celda en el mismo archivo**
Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al método [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) de la colección [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). El método [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) funciona para hipervínculos internos y externos. Una versión del método sobrecargado acepta los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda de destino.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **Agregar un enlace a un archivo externo**
Es posible agregar hipervínculos a archivos de Excel externos llamando al método [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) de la colección [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). El método [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) acepta los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo externo de Excel.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **Temas avanzados**
- [Agregar hipervínculos de imagen](/cells/es/nodejs-cpp/add-image-hyperlinks/)
- [Detectar tipo de hipervínculo](/cells/es/nodejs-cpp/detect-hyperlink-type/)
- [Editando Hipervínculos de la Hoja de Cálculo](/cells/es/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [Obtener Hipervínculos en Rango](/cells/es/nodejs-cpp/get-hyperlinks-in-range/)

