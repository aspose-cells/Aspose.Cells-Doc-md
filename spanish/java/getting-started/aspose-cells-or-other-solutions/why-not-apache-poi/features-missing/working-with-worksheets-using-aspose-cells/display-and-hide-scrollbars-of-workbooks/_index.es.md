---
title: Mostrar y Ocultar Barras de Desplazamiento de las Hojas de Cálculo
type: docs
weight: 40
url: /es/java/display-and-hide-scrollbars-of-workbooks/
---

## **Aspose.Cells: Mostrar y ocultar las barras de desplazamiento de los libros de trabajo**
Aspose.Cells proporciona una clase, **Workbook**, que representa un archivo de Excel. La clase **Workbook** proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel. Sin embargo, para controlar la visibilidad de las barras de desplazamiento en el archivo de Excel, los desarrolladores pueden utilizar los métodos **setVScrollBarVisible** y **setHScrollBarVisible** de la clase **Workbook**.

**Java**

{{< highlight java >}}

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
## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
{{< app/cells/assistant language="java" >}}
