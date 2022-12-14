---
title: Mostrar y ocultar barras de desplazamiento de libros de trabajo
type: docs
weight: 40
url: /es/java/display-and-hide-scrollbars-of-workbooks/
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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
