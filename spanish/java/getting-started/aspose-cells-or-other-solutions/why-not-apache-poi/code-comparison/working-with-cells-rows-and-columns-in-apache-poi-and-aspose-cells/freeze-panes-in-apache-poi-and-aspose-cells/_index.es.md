---
title: Congelar paneles en Apache POI y Aspose.Cells
type: docs
weight: 80
url: /es/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Congelar paneles**
Aspose.Cells proporciona una clase, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) que representa un archivo de Microsoft Excel. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). La clase Worksheet proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para configurar paneles congelados, llama al método freezePanes de la clase Worksheet. El método FreezePanes toma los siguientes parámetros:

- **Fila**, el índice de la fila desde la cual se iniciará la congelación.
- **Columna**, el índice de la columna desde la cual se iniciará la congelación.
- **Filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo.

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Congelar paneles**
sheet.createFreezePane está disponible para lograr la funcionalidad de FreezePane al usar Apache POI SS - HSSF y XSSF

**Java**

{{< highlight java >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

Para más detalles, visita [Congelar Paneles](http://docs.aspose.com:8082/docs/display/cellsjava/Congelar+Paneles).

{{% /alert %}}
