---
title: Ocultar y mostrar Cells
type: docs
weight: 30
url: /es/java/hide-and-unhide-cells/
---
## **Aspose.Cells - Ocultar y mostrar filas y columnas**
Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , que representa un archivo de Excel Microsoft. La clase Workbook contiene una WorksheetCollection que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase. La clase Worksheet proporciona una colección Cells que representa todas las celdas de la hoja de trabajo. La colección Cells proporciona varios métodos para administrar filas o columnas en una hoja de cálculo.

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Ocultar/Mostrar Cells**
Para ocultar una fila o columna, Apache POI SS proporciona el método Row.setZeroHeight (booleano).

**Java**

{{< highlight "java" >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

 Para más detalles, visite[Ocultar y mostrar filas y columnas](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}
