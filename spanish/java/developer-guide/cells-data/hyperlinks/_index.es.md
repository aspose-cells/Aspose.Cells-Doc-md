---
title: Insertar hipervínculos en Excel u OpenOffice
linktitle: Administración de hipervínculos
type: docs
weight: 160
url: /es/java/insert-hyperlinks-to-excel/
---
## **Adición de hipervínculos a datos de enlaces**
{{% alert color="primary" %}} 

Un hipervínculo se utiliza para crear un vínculo entre dos entidades. Todo el mundo está familiarizado con el uso de hipervínculos, especialmente en sitios web.

Usando Aspose.Cells, los desarrolladores pueden crear diferentes tipos de hipervínculos en archivos de Excel Microsoft. Este tema analiza qué tipos de hipervínculos son compatibles con Aspose.Cells y cómo se pueden usar en nuestros archivos de Excel.

{{% /alert %}} 
## **Adición de hipervínculos**
Se pueden agregar tres tipos de hipervínculo a una celda usando Aspose.Cells:

- [Añadir un enlace a una URL](/cells/es/java/working-with-hyperlinks-to-link-data/).
- [Agregar un enlace a otra celda en el mismo archivo](/cells/es/java/working-with-hyperlinks-to-link-data/).
- [Añadir un enlace a un archivo externo](/cells/es/java/working-with-hyperlinks-to-link-data/).

 Aspose.Cells permite a los desarrolladores agregar hipervínculos a archivos de Excel ya sea usando el API o[hojas de calculo de diseñador](/cells/es/java/what-is-a-designer-spreadsheet/)(hojas de cálculo donde los hipervínculos se crean manualmente y se usa Aspose.Cells para importarlos a otras hojas de cálculo).

Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)La clase proporciona diferentes métodos para agregar diferentes hipervínculos a archivos de Excel.
## **Agregar enlace a una URL**
 los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) la clase contiene un[hipervínculos](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) recopilación. Cada artículo en el[hipervínculos](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) colección representa un[Hipervínculo](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) . Agregue hipervínculos a las URL llamando al[hipervínculos](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) colección[Agregar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )método. los[Agregar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))método toma los siguientes parámetros:

- Cell nombre, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas de este rango de hipervínculo
- URL, la dirección URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


 En el ejemplo anterior, se agrega un hipervínculo a una URL en una celda vacía,**A1**En tales casos, si una celda está vacía, la dirección URL también se agrega a esa celda vacía como su valor. Si la celda no está vacía y se agrega un hipervínculo, el valor de la celda parece texto sin formato. Para que parezca un hipervínculo, aplique la configuración de formato adecuada en esa celda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Agregar un enlace a un Cell en el mismo archivo**
 Es posible agregar hipervínculos a celdas en el mismo archivo de Excel llamando al[hipervínculos](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) colección[Agregar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )método. los[Agregar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)El método ) funciona tanto para hipervínculos internos como externos. Una versión del método sobrecargado toma los siguientes parámetros:

- Cell nombre, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección de la celda objetivo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Agregar un enlace a un archivo externo**
 Es posible agregar hipervínculos a archivos de Excel externos llamando al[hipervínculos](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) colección[Agregar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )método. los[Agregar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))método toma los siguientes parámetros:

- Cell nombre, el nombre de la celda a la que se agregará el hipervínculo.
- Número de filas, el número de filas en este rango de hipervínculo.
- Número de columnas, el número de columnas en este rango de hipervínculo.
- URL, la dirección del destino, archivo de Excel externo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Temas avanzados**
- [Agregar hipervínculos de imágenes](/cells/es/java/add-image-hyperlinks/)
- [Detectar tipo de hipervínculo](/cells/es/java/detect-hyperlink-type/)
- [Edición de hipervínculos de la hoja de trabajo](/cells/es/java/editing-hyperlinks-of-worksheet/)
- [Obtener hipervínculos en rango](/cells/es/java/get-hyperlinks-in-range/)


