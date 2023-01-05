---
title: Mostrar y ocultar barras de desplazamiento de libros de trabajo en xlsx4j
type: docs
weight: 30
url: /es/java/display-and-hide-scrollbars-of-workbooks-in-xlsx4j/
---
## **Aspose.Cells - Mostrar y ocultar barras de desplazamiento de libros de trabajo**
 Aspose.Cells proporciona una clase,**Libro de trabajo** que representa un archivo de Excel.**Libro de trabajo** La clase proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel. Pero, para controlar la visibilidad de las barras de desplazamiento en el archivo de Excel, los desarrolladores pueden usar**establecerVScrollBarVisible** & **setHScrollBarVisible** métodos de la**Libro de trabajo** clase.

**Java**

{{< highlight "java" >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidescrollbars/AsposeDisplayAndHideScrollbars.java)
