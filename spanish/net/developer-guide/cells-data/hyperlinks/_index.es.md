---
title: Insertar hipervínculos en Excel u OpenOffice
linktitle: Administración de hipervínculos
type: docs
weight: 45
url: /es/net/insert-hyperlinks-to-excel/
description: Cómo insertar hipervínculos en un archivo de Excel con la biblioteca Aspose.Cells sin MS Excel.
---
{{% alert color="primary" %}} 

Un hipervínculo se utiliza para crear un vínculo entre dos entidades. Todo el mundo está familiarizado con el uso de hipervínculos, especialmente en sitios web.
Usando Aspose.Cells, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Excel Microsoft. Este tema analiza qué tipos de hipervínculos son compatibles con Aspose.Cells y cómo se pueden usar en nuestros archivos de Excel.

{{% /alert %}} 
## **Adición de hipervínculos**
Aspose.Cells permite a los desarrolladores agregar hipervínculos a archivos de Excel usando API o hojas de cálculo de diseñador (hojas de cálculo donde los hipervínculos se crean manualmente y Aspose.Cells se usa para importarlos a otras hojas de cálculo).

 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/net/aspose.cells/worksheet)La clase proporciona diferentes métodos para agregar diferentes hipervínculos a archivos de Excel.
## **Agregar enlace a una URL**
 los[Hoja de cálculo](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase contiene un[hipervínculos](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) recopilación. Cada artículo en el[hipervínculos](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) colección representa un[Hipervínculo](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Agregue hipervínculos a las URL llamando al[hipervínculos](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) colección[Agregar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) método. los[Agregar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)método toma los siguientes parámetros:

- Cell nombre, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo
- URL, la dirección URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

 En el ejemplo anterior, se agrega un hipervínculo a una URL en una celda vacía,**A1**. En tales casos, si una celda está vacía, la dirección URL también se agrega a esa celda vacía como su valor. Si la celda no está vacía y se agrega un hipervínculo, el valor de la celda parece texto sin formato. Para que parezca un hipervínculo, aplique la configuración de formato adecuada en esa celda.

{{% /alert %}} 
## **Agregar un enlace a un Cell en el mismo archivo**
 Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al[hipervínculos](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) colección[Agregar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) método. los[Agregar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)El método funciona tanto para hipervínculos internos como externos. Una versión del método sobrecargado toma los siguientes parámetros:

- Cell nombre, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda objetivo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Agregar un enlace a un archivo externo**
 Es posible agregar hipervínculos a archivos de Excel externos llamando al[hipervínculos](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) colección[Agregar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) método. los[Agregar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)método toma los siguientes parámetros:

- Cell nombre, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo de Excel externo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Temas avanzados**
- [Agregar hipervínculos de imágenes](/cells/es/net/add-image-hyperlinks/)
- [Detectar tipo de hipervínculo](/cells/es/net/detect-hyperlink-type/)
- [Edición de hipervínculos de la hoja de trabajo](/cells/es/net/editing-hyperlinks-of-worksheet/)
- [Obtener hipervínculos en rango](/cells/es/net/get-hyperlinks-in-range/)

