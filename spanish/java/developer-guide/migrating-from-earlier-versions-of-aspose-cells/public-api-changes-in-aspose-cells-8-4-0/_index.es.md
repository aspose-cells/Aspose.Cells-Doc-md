---
title: Público API Cambios en Aspose.Cells 8.4.0
type: docs
weight: 140
url: /es/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.3.2 a la 8.4.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados,[Clases añadidas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-4-0/) y[clases eliminadas, etc.](/cells/es/java/public-api-changes-in-aspose-cells-8-4-0/), pero también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Mecanismo para modificar el código VBA/macro en hojas de cálculo**
 Con el fin de proporcionar la característica de[Manipulación de código VBA/macro](/cells/es/java/modifying-vba-or-macro-code-using-aspose-cells/), el Aspose.Cells for Java 8.4.0 ha expuesto una serie de nuevas clases y propiedades en el paquete com.aspose.cells.Vba. Algunos de los detalles importantes de estas nuevas clases son los siguientes.

- La clase VbaProject se puede usar para obtener el proyecto VBA de una hoja de cálculo determinada.
- La clase VbaModuleCollection representa la colección de módulos de VBA que forman parte de un VbaProject determinado.
- La clase VbaModule representa un único módulo de VbaModuleCollection.

El siguiente fragmento de código muestra cómo modificar dinámicamente los segmentos de código VBA.

**Java**

{{< highlight "csharp" >}}

 Libro de trabajo libro de trabajo = nuevo Libro de trabajo ("fuente.xlsm");

//Cambiar el código del módulo VBA

VbaModuleCollection módulos = libro de trabajo.getVbaProject().getModules();

 para(int i=0; i< modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **Capacidad para eliminar la tabla dinámica**
Aspose.Cells for Java 8.4.0 ha expuesto dos métodos para PivotTableCollection para proporcionar la función de eliminación de tabla dinámica de una hoja de cálculo determinada. Los detalles de los métodos mencionados son los siguientes.

- El método PivotTableCollection.remove acepta un objeto de PivotTable y lo elimina de la colección.
- El método PivotTableCollection.removeAt acepta un valor entero basado en índice cero y quita la tabla dinámica particular de la colección.

El siguiente fragmento de código muestra cómo eliminar la tabla dinámica utilizando los dos métodos mencionados anteriormente.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Compatibilidad con diferentes diseños de tablas dinámicas**
Aspose.Cells for Java 8.4.0 proporciona soporte para diferentes diseños predefinidos para tablas dinámicas. Para proporcionar esta función, las API Aspose.Cells han expuesto tres métodos para la clase de tabla dinámica, como se detalla a continuación.

- El método PivotTable.showInCompactForm representa la tabla dinámica en un diseño compacto.
- El método PivotTable.showInOutlineForm representa la tabla dinámica en el diseño de esquema.
- El método PivotTable.showInTabularForm representa la tabla dinámica en un diseño tabular.

{{% alert color="primary" %}} 

 Es importante llamar a PivotTable.refreshData & PivotTable.calculateData después de configurar cualquiera de los diseños mencionados anteriormente.

{{% /alert %}} 

El siguiente código de ejemplo establece diferentes diseños para una tabla dinámica y almacena el resultado en el disco.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **Clase TxtLoadStyleStrategy y propiedad TxtLoadOptions.LoadStyleStrategy agregado**
Aspose.Cells for Java 8.4.0 ha expuesto la clase TxtLoadStyleStrategy y la propiedad TxtLoadOptions.LoadStyleStrategy para especificar la estrategia para formatear los valores analizados al convertir el valor de cadena en número o fecha y hora.
### **Método DataBar.ToImage agregado**
Con el lanzamiento de v8.4.0, el Aspose.Cells API ha proporcionado el método DataBar.toImage para guardar el DataBar con formato condicional en formato de imagen. El método {DataBar.toImage}} acepta dos parámetros como se detalla a continuación.

- El primer parámetro es de tipo com.aspose.cells.Cell en el que se ha aplicado formato condicional.
- El segundo parámetro es de tipo com.aspose.cells.rendering.ImageOrPrintOptions para establecer diferentes parámetros de la imagen resultante.

El siguiente código de ejemplo demuestra el uso del método DataBar.toImage para representar el DataBar en formato de imagen.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Propiedad Border.ThemeColor agregado**
Aspose.Cells Las API permiten extraer datos relacionados con el tema de las hojas de cálculo. Con el lanzamiento de Aspose.Cells for Java 8.4.0, API ha expuesto la propiedad Border.ThemeColor que se puede usar para recuperar los atributos de color del tema de los bordes Cell.
### **Propiedad DrawObject.ImageBytes agregada**
Aspose.Cells for Java 8.4.0 ha expuesto la propiedad DrawObject.ImageBytes para obtener los datos de imagen de Chart o Shape.
### **Propiedad HtmlSaveOptions.ExportBogusRowData agregado**
 Aspose.Cells for Java 8.4.0 ha proporcionado la propiedad {HtmlSaveOptions.ExportBogusRowData}}. La propiedad de tipo booleano determina si API inyectará datos falsos en la fila inferior al exportar la hoja de cálculo al formato HTML.

{{% alert color="primary" %}} 

El valor por defecto es verdadero.

{{% /alert %}} 

El siguiente código de ejemplo ilustra el uso de dicha propiedad.

**Java**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Propiedad HtmlSaveOptions.CellCssPrefix agregado**
La propiedad recién agregada HtmlSaveOptions.CellCssPrefix permite establecer el prefijo para los archivos CSS al exportar hojas de cálculo al formato HTML.

{{% alert color="primary" %}} 

El valor predeterminado es una cadena vacía).

{{% /alert %}}
## **API obsoletas**
### **Métodos Cells.getCellByIndex & Row.getCellByIndex Obsoletos**
Utilice el método getEnumerator para iterar todas las celdas en su lugar.
### **Propiedad DrawObject.Image obsoleta**
Utilice la propiedad DrawObject.ImageBytes para obtener datos de imagen en su lugar.
