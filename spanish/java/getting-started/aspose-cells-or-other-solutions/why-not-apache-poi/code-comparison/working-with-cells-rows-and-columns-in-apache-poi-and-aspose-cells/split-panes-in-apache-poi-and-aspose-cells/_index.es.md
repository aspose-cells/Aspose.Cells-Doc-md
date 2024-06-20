---
title: Dividir Paneles en Apache POI y Aspose.Cells
type: docs
weight: 70
url: /es/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Dividir paneles**
Aspose.Cells provee una clase, Workbook que representa un archivo de Microsoft Excel. La clase Workbook provee una amplia gama de propiedades y métodos para administrar archivos de Excel. Para implementar vistas divididas, utiliza el método split de la clase Worksheet. Para eliminar paneles divididos, utiliza el método removeSplit.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Dividir Paneles**
La funcionalidad de dividir paneles puede lograrse mediante el método createSplitPane al utilizar la API de Apache POI SS (HSSF & XSSF)

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

Para más detalles, visita [Dividir Paneles](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
