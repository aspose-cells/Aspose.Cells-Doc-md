---
title: Público API Cambios en Aspose.Cells 8.5.2
type: docs
weight: 190
url: /es/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Este documento describe los cambios al Aspose.Cells API de la versión 8.5.1 a la 8.5.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-5-2/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Renderizar la hoja de trabajo al contexto gráfico**
Esta versión de Aspose.Cells for Java API ha expuesto otra sobrecarga del método SheetRender.toImage que ahora permite aceptar una instancia de la clase Graphics2D para[renderizar la hoja de trabajo en el contexto de gráficos](/cells/es/java/render-worksheet-to-graphic-context/). Las firmas del método recién agregado son las siguientes.

- SheetRender.toImage (índice de página int, gráfico Graphics2D)

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Create empty image and fill it with blue color

int width = 800;

int height = 800;

BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

Graphics2D g = image.createGraphics();

g.setColor(java.awt.Color.blue);

g.fillRect(0, 0, width, height);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setOnePagePerSheet(true);

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.toImage(0, g);

//Save the graphics context image in Png format

File outputfile = new File("test.png");

ImageIO.write(image, "png", outputfile);

{{< /highlight >}}
### **Método PivotTable.getCellByDisplayName agregado**
 Aspose.Cells for Java 8.5.2 ha expuesto el método PivotTable.getCellByDisplayName que se puede usar para[recuperar el objeto Cell por el nombre de PivotField](/cells/es/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Este método podría ser útil en escenarios en los que desea resaltar o formatear el encabezado PivotField.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Access cell by display name of 2nd data field of the pivot table

String displayName = pivotTable.getDataFields().get(1).getDisplayName();

Cell cell = pivotTable.getCellByDisplayName(displayName);

//Access cell style and set its fill color and font color

Style style = cell.getStyle();

style.setForegroundColor(Color.getLightBlue());

style.getFont().setColor(Color.getBlack());

//Set the style of the cell

pivotTable.format(cell.getRow(), cell.getColumn(), style);

//Save workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Propiedades SaveOptions.MergeAreas añadidas**
Aspose.Cells for Java 8.5.2 ha expuesto la propiedad SaveOptions.MergeAreas que puede aceptar valores de tipo booleano. El valor predeterminado es falso; sin embargo, si se establece en verdadero, Aspose.Cells for Java API intenta fusionar el CellArea individual antes de guardar el archivo.

{{% alert color="primary" %}} 

Si una hoja de cálculo tiene demasiadas celdas individuales con validación aplicada, existe la posibilidad de que la hoja de cálculo resultante se dañe. Una posible solución es fusionar las celdas con reglas de validación idénticas o ahora puede usar la propiedad SaveOptions.MergeAreas para indicar al API que fusione automáticamente las CellAreas antes de guardar la operación.

{{% /alert %}} 
### **Propiedad Geometry.ShapeAdjustValues Agregado**
 Con el lanzamiento de v8.5.2, el Aspose.Cells API ha expuesto el método Geometry.getShapeAdjustValues que se puede usar para[acceder y realizar cambios en los puntos de ajuste de diferentes formas](/cells/es/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

En la interfaz de Excel Microsoft, los puntos de ajuste se muestran como nodos de diamantes amarillos.

{{% /alert %}} 

 Por ejemplo,

1. Rectángulo redondeado tiene un ajuste para cambiar el arco
1. Triángulo tiene un ajuste para cambiar la ubicación del punto
1. Trapecio tiene un ajuste para cambiar el ancho de la parte superior
1. Las flechas tienen dos ajustes para cambiar la forma de la cabeza y la cola.

Este es el escenario de uso más simple.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first three shapes of the worksheet

Shape shape1 = worksheet.getShapes().get(0);

Shape shape2 = worksheet.getShapes().get(1);

Shape shape3 = worksheet.getShapes().get(2);

//Change the adjustment values of the shapes

shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8d);

shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Campo de enumeración ConsolidationFunction.DISTINCT_COUNT Agregado**
Aspose.Cells for Java 8.5.2 ha expuesto el campo ConsolidationFunction.DISTINCT_COUNT que se puede usar para aplicar la función consolidada Distinct Count en DataField de una tabla dinámica.

{{% alert color="primary" %}} 

La función de consolidación Distinct Count solo es compatible con Microsoft Excel 2013.

{{% /alert %}}
