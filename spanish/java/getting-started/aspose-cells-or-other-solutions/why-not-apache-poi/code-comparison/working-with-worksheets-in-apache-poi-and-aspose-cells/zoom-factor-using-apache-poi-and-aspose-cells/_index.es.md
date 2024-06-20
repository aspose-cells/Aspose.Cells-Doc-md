---
title: Factor de zoom utilizando Apache POI y Aspose.Cells
type: docs
weight: 70
url: /es/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Factor de Zoom**
Microsoft Excel proporciona una función que permite a los usuarios establecer un factor de zoom o escala para una hoja de cálculo. Esta función ayuda a los usuarios a ver el contenido de la hoja de cálculo en vistas más pequeñas o más grandes.

Aspose.Cells proporciona una clase, Workbook, que representa un archivo de Microsoft Excel. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una amplia gama de propiedades y métodos para administrar hojas de cálculo. Para establecer el factor de zoom de una hoja de cálculo, utilice el método setZoom de la clase Worksheet.

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Factor de zoom**
Apache POI proporciona el método Sheet.setZoom() disponible para la función de zoom.

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
