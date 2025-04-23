---
title: Ocultar y Mostrar Celdas
type: docs
weight: 30
url: /es/java/hide-and-unhide-cells/
---

## **Aspose.Cells - Ocultar y Mostrar Filas y Columnas**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Microsoft Excel. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase Worksheet proporciona una colección de Celdas que representa todas las celdas en la hoja de cálculo. La colección de Celdas proporciona varios métodos para administrar filas o columnas en una hoja de cálculo. 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Ocultar / Mostrar Celdas**
Para ocultar una fila o columna, Apache POI SS proporciona el método Row.setZeroHeight(boolean).

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

Para más detalles, visite [Ocultar y Mostrar Filas y Columnas](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
