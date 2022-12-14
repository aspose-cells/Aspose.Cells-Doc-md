---
title: Paneles divididos en Apache POI y Aspose.Cells
type: docs
weight: 70
url: /es/java/split-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Paneles divididos**
Aspose.Cells proporciona una clase, Libro de trabajo que representa un archivo de Excel Microsoft. La clase Workbook proporciona una amplia gama de propiedades y métodos para administrar archivos de Excel. Para implementar vistas divididas, use el método de división de la clase Worksheet. Para eliminar paneles divididos, use el método removeSplit.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF y XSSF - Paneles divididos**
La funcionalidad de paneles divididos se puede lograr mediante el método createSplitPane mientras se usa Apache POI SS (HSSF y XSSF) API

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

 Para más detalles, visite[Paneles divididos](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
