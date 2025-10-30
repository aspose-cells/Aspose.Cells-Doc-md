---
title: Insertar hipervínculos en Excel u OpenOffice con Golang vía C++
linktitle: Gestión de hipervínculos
type: docs
weight: 45
url: /es/go-cpp/insert-hyperlinks-to-excel/
description: Cómo insertar hipervínculos en archivos de Excel con la biblioteca Aspose.Cells sin usar MS Excel usando C++.
keywords: Insertar hipervínculos en Excel, Agregar o insertar hipervínculos, Agregar o insertar enlace a una URL, Agregar o insertar un enlace a una celda, Agregar un enlace a un archivo externo
---

{{% alert color="primary" %}} 

Un hipervínculo se usa para crear un enlace entre dos entidades. Todos están familiarizados con el uso de hipervínculos, especialmente en sitios web.
Utilizando Aspose.Cells, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Microsoft Excel. Este tema discute qué tipos de hipervínculos son compatibles con Aspose.Cells y cómo se pueden usar en nuestros archivos de Excel.

{{% /alert %}} 

## **Añadiendo hipervínculos**
Aspose.Cells permite a los desarrolladores agregar hipervínculos a archivos de Excel usando la API o hojas de cálculo de diseño (hojas donde los hipervínculos se crean manualmente y Aspose.Cells se usa para importarlos en otras hojas).

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja del Excel. Una hoja se representa mediante la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ofrece diferentes métodos para agregar distintos hipervínculos a archivos de Excel.

## **Añadir un enlace a una URL**
La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) contiene una colección [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/). Cada elemento en la colección representa un [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Agrega hipervínculos a URLs llamando al método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) de la colección [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). El método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la URL.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks.go" >}}
{{% alert color="primary" %}} 

En el ejemplo anterior, se añade un hipervínculo a una URL en una celda vacía, **A1**. En tales casos, si una celda está vacía, entonces la dirección URL también se agrega a esa celda vacía como su valor. Si la celda no está vacía y se agrega un hipervínculo, el valor de la celda se ve como texto plano. Para que se vea como un hipervínculo, aplique la configuración de formato adecuada en esa celda.

{{% /alert %}} 

## **Añadir un enlace a una celda en el mismo archivo**
Es posible agregar hipervínculos a celdas en el mismo archivo Excel llamando al método [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) de la colección [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/). El método [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) funciona tanto para hipervínculos internos como externos. Una versión del método sobrecargado toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda de destino.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-1.go" >}}
## **Agregar un enlace a un archivo externo**
Es posible agregar hipervínculos a archivos externos de Excel llamando al método [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) de la colección [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/). El método [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) toma los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo externo de Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-2.go" >}}
## **Temas avanzados**
- [Agregar hipervínculos de imagen](/cells/es/cpp/add-image-hyperlinks/)
- [Detectar tipo de hipervínculo](/cells/es/cpp/detect-hyperlink-type/)
- [Editando Hipervínculos de la Hoja de Cálculo](/cells/es/cpp/editing-hyperlinks-of-worksheet/)
- [Obtener Hipervínculos en Rango](/cells/es/cpp/get-hyperlinks-in-range/)
