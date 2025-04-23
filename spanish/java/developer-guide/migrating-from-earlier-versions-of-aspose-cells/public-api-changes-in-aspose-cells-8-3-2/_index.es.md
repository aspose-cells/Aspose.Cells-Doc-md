---
title: Cambios en la API Pública en Aspose.Cells 8.3.2
type: docs
weight: 130
url: /es/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.3.1 a la 8.3.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, [clases agregadas, etc.](/cells/es/java/cambios-en-la-api-publica-en-aspose-cells-8-3-2/) y [clases removidas, etc.](/cells/es/java/cambios-en-la-api-publica-en-aspose-cells-8-3-2/), sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Mecanismo para Establecer la Posición Absoluta de un Elemento de un Informe de Tabla Dinámica**
Para proporcionar la función [Posicionamiento Absoluto del Elemento de un Informe de Tabla Dinámica](/cells/es/java/especificar-la-posicion-absoluta-del-elemento-de-informe-de-tabla-dinamica/), la Aspose.Cells for Java 8.3.2 ha expuesto una serie de propiedades y un método como se enumera a continuación.

- PivotItem.setPosition se puede utilizar para establecer el índice de posición en todos los PivotItems independientemente del nodo padre.
- PivotItem.setPositionInSameParentNode se puede utilizar para establecer el índice de posición en los PivotItems ubicados bajo el mismo nodo padre.
- El método PivotItem.move(int count, bool isSameParent) se puede utilizar para mover el ítem hacia arriba o hacia abajo basándose en el valor de count, donde count es el número de posiciones para mover el PivotItem hacia arriba o hacia abajo. Si el valor de count es menor que cero, el ítem se moverá hacia arriba, y si el valor de count es mayor que cero, el PivotItem se moverá hacia abajo. El parámetro booleano isSameParent especifica si la operación de movimiento se debe realizar en el mismo nodo padre o no.

{{% alert color="primary" %}} 

Ten en cuenta que es necesario llamar a los métodos PivotTable.refreshData y PivotTable.calculateData antes de usar las propiedades PivotItem.setPosition, PivotItem.setPositionInSameParentNode y el método PivotItem.move(int count, bool isSameParent).

{{% /alert %}} 
### **Clase SignatureLine Agregada**
Aspose.Cells 8.3.2 proporciona soporte para la Línea de Firma para imitar la característica equivalente de MS Excel. Esta versión ha expuesto la clase SignatureLine y la propiedad Picture.SignatureLine para este propósito.

El siguiente código de ejemplo agrega una Línea de Firma utilizando la propiedad Picture.SignatureLine al libro de trabajo.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **Método Chart.hasAxis Agregado**
Con el lanzamiento de la v8.3.2, la API de Aspose.Cells ha proporcionado el método Chart.hasAxis(AxisType axisType, bool isPrimary) para determinar si el gráfico tiene un eje particular o no.

El siguiente código de ejemplo demuestra el uso del método Chart.hasAxis para determinar si el gráfico de ejemplo tiene ejes Primario, Secundario y de Valor.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **Método WorkbookSettings.checkWriteProtectedPassword Agregado**
El método WorkbookSettings.checkWriteProtectedPassword permite a los desarrolladores verificar si una contraseña dada para modificar la hoja de cálculo es correcta o no.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Se añadieron los métodos de sobrecarga WorkbookRender.toPrinter y SheetRender.toPrinter**
Aspose.Cells 8.3.2 ha proporcionado los métodos WorkbookRender.toPrinter y SheetRender.toPrinter para imprimir el rango de páginas de un libro y hoja de cálculo respectivamente.

El siguiente código de muestra ilustra cómo utilizar los métodos mencionados anteriormente para imprimir las páginas 2-5 del libro y hoja de cálculo.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Se agregó el método Worksheet.refreshPivotTables**
El nuevo método Worksheet.refreshPivotTables permite actualizar todas las tablas dinámicas en una hoja de cálculo en una sola llamada.

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Se agregó el método Workbook.getNamedStyle**
Aspose.Cells 8.3.2 ha expuesto el método Workbook.getNamedStyle que acepta una cadena como parámetro y recupera el objeto de estilo basado en el parámetro pasado.
### **Se agregó el método Cells.importTwoDimensionArray**
La API Aspose.Cells ha hecho posible importar matrices bidimensionales a las celdas de hojas de cálculo exponiendo el método Cells.importTwoDimensionArray.
### **Se agregaron las propiedades OnePagePerSheet, PageIndex y PageCount**
Aspose.Cells for Java 8.3.2 ha expuesto las propiedades OnePagePerSheet, PageIndex y PageCount para la clase XpsSaveOptions.
### **Se agregaron las propiedades NumberDecimalSeparator y NumberGroupSeparator**
Aspose.Cells for Java 8.3.2 ha introducido las propiedades NumberDecimalSeparator y NumberGroupSeparator que puede establecer los separadores personalizados utilizados para formatear y analizar los valores numéricos en hojas de cálculo.

El siguiente código de muestra ilustra cómo especificar los separadores personalizados utilizando la API Aspose.Cells.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Se agregó la propiedad PdfSaveOptions.setFontSubstitutionCharGranularity**
Aspose.Cells for Java 8.3.2 ha expuesto la propiedad PdfSaveOptions.setFontSubstitutionCharGranularity para superar el problema de que algunos caracteres Unicode no pueden mostrarse utilizando una fuente específica.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **APIs Eliminadas**
### **Métodos obsoletos eliminados**
Los siguientes métodos han sido eliminados de la API pública.

- Métodos Workbook.open y Workbook.save.
- Método Workbook.setOleSize.
- Método Workbook.loadData.
- Métodos WorkbookDesigner.open y WorkbookDesigner.save.
- Método WorksheetCollection.deleteName.
### **Propiedades obsoletas eliminadas**
Las siguientes propiedades han sido eliminadas de la API pública.

- Propiedad Workbook.isProtected.
- Propiedad Workbook.Language.
- Propiedad Workbook.Region.
- Propiedad WorkbookSettings.ReCalcOnOpen.
- Propiedad WorkbookSettings.Language.
- Propiedad WorkbookSettings.Encoding.
- Propiedad WorkbookSettings.ConvertNumericData.
- Propiedad WorksheetCollection.HidePivotFieldList.
- Propiedad WorksheetCollection.EnableHTTPCompression.
- Propiedad WorksheetCollection.isMinimized.
- Propiedad WorksheetCollection.isHidden.
- Propiedad WorksheetCollection.SheetTabBarWidth.
- Propiedad WorksheetCollection.WindowLeft.
- Propiedad WorksheetCollection.WindowLeftInch.
- Propiedad WorksheetCollection.WindowLeftCM.
- Propiedad WorksheetCollection.WindowTop.
- Propiedad WorksheetCollection.WindowTopInch.
- Propiedad WorksheetCollection.WindowTopCM.
- Propiedad WorksheetCollection.WindowWidth.
- Propiedad WorksheetCollection.WindowWidthInch.
- Propiedad WorksheetCollection.WindowWidthCM.
- Propiedad WorksheetCollection.WindowHeight.
- Propiedad WorksheetCollection.WindowHeightInch.
- Propiedad WorksheetCollection.WindowHeightCM.
- Propiedad Worksheet.HPageBreaks.
- Propiedad Worksheet.VPageBreaks.
- Propiedad HtmlSaveOptions.DisplayHTMLCrossString.
- Propiedad HtmlSaveOptions.ExportChartImageFormat.
- Propiedad SaveOptions.ExpCellNameToXLSX.
- Propiedad SaveOptions.DefaultFont.
- Propiedad SaveOptions.Compliance.
- Propiedad SaveOptions.PdfBookmark.
- Propiedad SaveOptions.PdfImageCompression.
- Propiedad TxtSaveOptions.AlwaysQuoted.
## **APIs obsoletas**
### **Propiedad Workbook.saveOptions obsoleta.**
Se debe pasar un objeto SaveOptions al método Workbook.Save después de configurar las propiedades adecuadas de SaveOptions. 
### **Propiedades obsoletas Workbook.Styles y Class StyleCollection.**
Se recomienda utilizar el método Workbook.createStyle para crear y manipular estilos en lugar de crear un Style con el método StyleCollection.add. Además, se puede utilizar el método Workbook.getNamedStyle(nombre) para obtener un estilo con nombre en lugar de StyleCollection.get(nombre).
### **Método obsoleto PivotItem.move(int count).**
Con el lanzamiento de Aspose.Cells 8.3.2, la API ha introducido otra sobrecarga del método PivotItem.move que acepta el parámetro entero para el conteo y un parámetro booleano para mover un PivotItem dentro del nodo padre. 
{{< app/cells/assistant language="java" >}}
