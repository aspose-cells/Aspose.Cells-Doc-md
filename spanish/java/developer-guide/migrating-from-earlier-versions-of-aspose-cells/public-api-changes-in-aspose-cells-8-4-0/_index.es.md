---
title: Cambios en la API pública en Aspose.Cells 8.4.0
type: docs
weight: 140
url: /es/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.3.2 hasta la 8.4.0 que pueden ser de interés para desarrolladores de módulos/aplicaciones. Incluye no solo nuevos métodos públicos actualizados, [clases añadidas, etc.](/cells/es/java/cambios-en-la-api-pública-en-aspose-cells-8-4-0/) y [clases eliminadas, etc.](/cells/es/java/cambios-en-la-api-pública-en-aspose-cells-8-4-0/), sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Mecanismo para modificar el código VBA/Macro en hojas de cálculo**
Para proporcionar la funcionalidad de [Manipulación de Código VBA/Macro](/cells/es/java/modificar-código-vba-o-macro-utilizando-aspose-cells/), la Aspose.Cells for Java 8.4.0 ha expuesto una serie de nuevas clases y propiedades en el paquete com.aspose.cells.Vba. Algunos detalles importantes de estas nuevas clases son los siguientes.

- La clase VbaProject se puede utilizar para obtener el proyecto VBA de una hoja de cálculo dada.
- La clase VbaModuleCollection representa la colección de módulos VBA que forman parte de un VbaProject dado.
- La clase VbaModule representa un único módulo de la VbaModuleCollection.

El siguiente fragmento de código muestra cómo modificar dinámicamente los segmentos de código VBA.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

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
### **Capacidad para eliminar una tabla dinámica**
Aspose.Cells for Java 8.4.0 ha expuesto dos métodos para la colección PivotTable para proporcionar la función de eliminación de una tabla dinámica de una hoja de cálculo dada. Los detalles de los mencionados métodos son los siguientes.

- El método PivotTableCollection.remove acepta un objeto de PivotTable y lo elimina de la colección.
- El método PivotTableCollection.removeAt acepta un valor entero basado en índice cero y elimina la tabla dinámica particular de la colección.

El siguiente fragmento de código muestra cómo eliminar la tabla dinámica utilizando ambos métodos mencionados anteriormente.

**Java**

{{< highlight csharp >}}

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
### **Soporte para Diferentes Diseños de Tabla Dinámica**
Aspose.Cells for Java 8.4.0 proporciona el soporte para diferentes diseños predefinidos para las Tablas Dinámicas. Para proporcionar esta función, las APIs de Aspose.Cells han expuesto tres métodos para la clase PivotTable como se detalla a continuación.

- El método PivotTable.showInCompactForm muestra la Tabla Dinámica en un diseño Compacto.
- El método PivotTable.showInOutlineForm muestra la Tabla Dinámica en un diseño de Esquema.
- El método PivotTable.showInTabularForm muestra la Tabla Dinámica en un diseño Tabular.

{{% alert color="primary" %}} 

Es importante llamar a PivotTable.refreshData y PivotTable.calculateData después de configurar cualquiera de los diseños mencionados anteriormente. 

{{% /alert %}} 

El siguiente código de muestra establece diferentes diseños para una Tabla Dinámica y guarda el resultado en disco.

**Java**

{{< highlight csharp >}}

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
### **Se agregó la Clase TxtLoadStyleStrategy y la Propiedad TxtLoadOptions.LoadStyleStrategy**
Aspose.Cells for Java 8.4.0 ha expuesto la clase TxtLoadStyleStrategy y la propiedad TxtLoadOptions.LoadStyleStrategy para especificar la estrategia para formatear los valores analizados al convertir el valor de cadena a número o fecha y hora.
### **Se agregó el método DataBar.ToImage**
Con el lanzamiento de la v8.4.0, la API de Aspose.Cells ha proporcionado el método DataBar.toImage para guardar la barra de datos formateada condicionalmente en formato de imagen. El método {DataBar.toImage}} acepta dos parámetros como se detalla a continuación.

- El primer parámetro es de tipo com.aspose.cells.Cell en el que se ha aplicado formato condicional.
- El segundo parámetro es de tipo com.aspose.cells.rendering.ImageOrPrintOptions para establecer diferentes parámetros de la imagen resultante.

El siguiente código de muestra demuestra el uso del método DataBar.toImage para representar la DataBar en formato de imagen.

**Java**

{{< highlight csharp >}}

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

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Agregada la propiedad Border.ThemeColor.**
Las APIs de Aspose.Cells permiten extraer datos relacionados con el tema de las hojas de cálculo. Con el lanzamiento de Aspose.Cells for Java 8.4.0, la API ha expuesto la propiedad Border.ThemeColor que se puede utilizar para recuperar los atributos de color del tema de los bordes de celda.
### **Agregada la propiedad DrawObject.ImageBytes.**
Aspose.Cells for Java 8.4.0 ha expuesto la propiedad DrawObject.ImageBytes para obtener los datos de la imagen de Gráfico o Forma.
### **Agregada la propiedad HtmlSaveOptions.ExportBogusRowData.**
Aspose.Cells for Java 8.4.0 ha proporcionado la propiedad {HtmlSaveOptions.ExportBogusRowData}. La propiedad de tipo Boolean determina si la API inyectará datos de fila inferior falsos al exportar la hoja de cálculo al formato HTML. 

{{% alert color="primary" %}} 

El valor predeterminado es true.

{{% /alert %}} 

El siguiente código de muestra ilustra el uso de dicha propiedad.

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Agregada la propiedad HtmlSaveOptions.CellCssPrefix.**
La propiedad recién añadida HtmlSaveOptions.CellCssPrefix permite establecer el prefijo para los archivos CSS al exportar hojas de cálculo al formato HTML.

{{% alert color="primary" %}} 

El valor predeterminado es "" (cadena vacía).

{{% /alert %}}
## **APIs obsoletas**
### **Métodos obsoletos Cells.getCellByIndex & Row.getCellByIndex**
Utilice el método getEnumerator para iterar todas las celdas en su lugar.
### **Propiedad obsoleta DrawObject.Image**
Utilice la propiedad DrawObject.ImageBytes para obtener los datos de la imagen en su lugar.
