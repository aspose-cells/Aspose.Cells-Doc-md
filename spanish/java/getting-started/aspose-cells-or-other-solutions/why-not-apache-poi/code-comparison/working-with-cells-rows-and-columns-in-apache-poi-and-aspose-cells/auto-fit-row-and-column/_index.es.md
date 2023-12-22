---
title: Ajuste automático de fila y columna
type: docs
weight: 10
url: /es/java/auto-fit-row-and-column/
description: Aprenda cómo ajustar automáticamente filas y columnas a través de Aspose.Cells for Java API.
keywords: How to Autofit Row and Column in Java, Autofit Row Data in workbook using Java, Java Autofit Column Data. 
---
##  **Cómo ajustar automáticamente filas y columnas usando Aspose.Cells for Java**
El enfoque más sencillo para ajustar automáticamente el tamaño del ancho y alto de una fila es llamar al método Worksheet.autoFitRow. El método autoFitRow toma un índice de fila (de la fila cuyo tamaño se va a cambiar) como parámetro.

**Tenga en cuenta:**Si desea ajustar automáticamente filas y columnas en hojas de cálculo de Excel usando Java, visite[Autoajustar filas y columnas](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
##  **Apache POI SS - HSSF XSSF - Ajuste automático de fila y columna**
Apache POI SS: HSSF y XSSF proporcionan Sheet.autoSizeColumn para ajustar automáticamente las columnas

**Java**

{{< highlight "java" >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet("new sheet");

sheet.autoSizeColumn(0); //adjust width of the first column

sheet.autoSizeColumn(1); //adjust width of the second column

FileOutputStream fileOut;

fileOut = new FileOutputStream("AutoFit_Apache.xls");

workbook.write(fileOut);

fileOut.close();

{{< /highlight >}}
##  **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
##  **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
