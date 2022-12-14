---
title: Público API Cambios en Aspose.Cells 8.6.2
type: docs
weight: 220
url: /es/java/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.6.1 a la 8.6.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Soporte para devolución de llamada con marcadores inteligentes**
Esta versión de Aspose.Cells for Java API ha expuesto el campo WorkbookDesigner.CallBack y la interfaz ISmartMarkerCallBack que juntos permiten[obtener las notificaciones sobre la referencia de celda y/o el marcador inteligente que se está procesando](/cells/es/java/getting-notifications-while-merging-data-with-smart-markers/) . El siguiente fragmento de código demuestra el uso de la interfaz ISmartMarkerCallBack para definir una nueva clase que maneja la devolución de llamada para el método WorkbookDesigner.process.

**Java**

{{< highlight "csharp" >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

El resto del proceso incluye cargar la hoja de cálculo del diseñador que contiene los marcadores inteligentes con WorkbookDesigner o crear uno desde cero y procesarlo configurando la fuente de datos. Sin embargo, para habilitar las notificaciones, es necesario configurar la propiedad WorkbookDesigner.CallBack antes de llamar al método WorkbookDesigner.process como se muestra a continuación.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[]{ "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Método Chart.toPdf agregado**
Aspose.Cells for Java 8.6.2 ha expuesto el método Chart.toPdf que se puede usar para representar directamente la forma del gráfico en formato PDF. Dicho método actualmente acepta un parámetro de tipo Cadena como ubicación de la ruta del archivo para almacenar el archivo resultante en el disco.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Método Workbook.removeUnusedStyles añadido**
 Aspose.Cells for Java 8.6.2 ha expuesto el método Workbook.removeUnusedStyles que se puede usar para[elimine todos los objetos de estilo no utilizados del grupo de estilos](/cells/es/java/remove-unused-styles-inside-the-workbook/). 

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Propiedad Cells. Estilo agregado**
La propiedad Cells.Style se puede utilizar para acceder al estilo de la hoja de trabajo que representa el estilo predeterminado.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **Eventos agregados para GridWeb**
Aspose.Cells.GridWeb for Java 8.6.2 ha expuesto los siguientes dos eventos nuevos.

1. AjaxCallFinished: se activa cuando finaliza la actualización AJAX del control. (EnableAJAX debe establecerse en verdadero).
1. CellModifiedOnAjax: se activa cuando la celda se modifica en una llamada AJAX.
