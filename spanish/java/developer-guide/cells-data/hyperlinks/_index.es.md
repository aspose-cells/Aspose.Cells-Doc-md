---
title: Insertar hipervínculos en Excel u OpenOffice
linktitle: Gestión de hipervínculos
type: docs
weight: 160
url: /es/java/insert-hyperlinks-to-excel/
---

## **Agregar hipervínculos para vincular datos**
{{% alert color="primary" %}} 

Un hipervínculo se usa para crear un enlace entre dos entidades. Todos están familiarizados con el uso de hipervínculos, especialmente en sitios web.

Utilizando Aspose.Cells, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Microsoft Excel. Este tema discute qué tipos de hipervínculos son compatibles con Aspose.Cells y cómo se pueden usar en nuestros archivos de Excel.

{{% /alert %}} 
## **Añadiendo hipervínculos**
Se pueden agregar tres tipos de hipervínculos a una celda utilizando Aspose.Cells:

- [Agregar un enlace a una URL](/cells/es/java/working-with-hyperlinks-to-link-data/).
- [Agregar un enlace a otra celda en el mismo archivo](/cells/es/java/working-with-hyperlinks-to-link-data/).
- [Agregar un enlace a un archivo externo](/cells/es/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells permite a los desarrolladores agregar hipervínculos a archivos de Excel ya sea usando la API o [hojas de cálculo de diseñador](/cells/es/java/what-is-a-designer-spreadsheet/) (hojas de cálculo donde los hipervínculos se crean manualmente y Aspose.Cells se utiliza para importarlos a otras hojas de cálculo).

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona diferentes métodos para agregar diferentes hipervínculos a archivos de Excel.
## **Añadir un enlace a una URL**
La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) contiene una colección [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). Cada elemento en la colección [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) representa un [Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink). Agrega hipervínculos a URLs llamando al método [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) de la colección [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). El método [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) acepta los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas de este rango de hipervínculo.
- URL, la dirección de la URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


En el ejemplo anterior, se agrega un hipervínculo a una URL en una celda vacía, **A1**. En tales casos, si una celda está vacía, entonces la dirección URL también se agrega a esa celda vacía como su valor. Si la celda no está vacía y se agrega un hipervínculo, el valor de la celda se ve como texto plano. Para que parezca un hipervínculo, aplique la configuración de formato adecuada en esa celda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Añadir un enlace a una celda en el mismo archivo**
Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al método [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) de la colección [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). El método [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) funciona tanto para hipervínculos internos como externos. Una versión del método sobrecargado acepta los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda de destino.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Agregar un enlace a un archivo externo**
Es posible agregar hipervínculos a archivos externos de Excel llamando al método [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) de la colección [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). El método [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) acepta los siguientes parámetros:

- Nombre de la celda, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo externo de Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Temas avanzados**
- [Agregar hipervínculos de imagen](/cells/es/java/add-image-hyperlinks/)
- [Detectar tipo de hipervínculo](/cells/es/java/detect-hyperlink-type/)
- [Editando Hipervínculos de la Hoja de Cálculo](/cells/es/java/editing-hyperlinks-of-worksheet/)
- [Obtener Hipervínculos en Rango](/cells/es/java/get-hyperlinks-in-range/)


{{< app/cells/assistant language="java" >}}
