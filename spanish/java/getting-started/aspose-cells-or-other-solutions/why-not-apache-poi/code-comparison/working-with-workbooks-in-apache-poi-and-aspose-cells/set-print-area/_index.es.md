---
title: Establecer área de impresión
type: docs
weight: 40
url: /es/java/set-print-area/
---
## **Aspose.Cells - Establecer área de impresión**
De manera predeterminada, solo el área de impresión incorpora todas las áreas de la hoja de cálculo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de trabajo.

Para seleccionar un área de impresión específica, use el[Configuración de página](/java/pagesetup)método setPrintArea de la clase. Asigne un rango de celdas que defina el área de impresión a esta propiedad.

**Java**

{{< highlight "java" >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Establecer área de impresión**
El método Workbook.setPrintArea está disponible para establecer las propiedades de página del área de impresión.

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

 Para más detalles, visite[Configuración de las opciones de impresión](/cells/es/java/page-setup-features/#setting-print-options).

{{% /alert %}}
