---
title: Mostrar y ocultar pestañas del libro de trabajo usando Aspose.Cells
type: docs
weight: 50
url: /es/java/display-and-hide-tabs-of-workbook-using-aspose-cells/
---
## **Aspose.Cells - Mostrar y ocultar pestañas del libro de trabajo**
Aspose.Cells proporciona una clase, Workbook, que representa un archivo de Excel Microsoft. La clase Workbook proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para controlar la visibilidad de las pestañas en un archivo de Excel, los desarrolladores pueden usar el método setShowTabs de la clase Workbook.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file

workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

