---
title: Público API Cambios en Aspose.Cells 8.6.2
type: docs
weight: 210
url: /es/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.6.1 a la 8.6.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Soporte para devolución de llamada con marcadores inteligentes**
 Esta versión de Aspose.Cells for .NET API ha expuesto la propiedad WorkbookDesigner.CallBack y la interfaz ISmartMarkerCallBack que juntas permiten[obtener las notificaciones sobre la referencia de celda y/o el marcador inteligente que se está procesando](/cells/es/net/getting-notifications-while-merging-data-with-smart-markers/). El siguiente fragmento de código demuestra el uso de la interfaz ISmartMarkerCallBack para definir una nueva clase que maneja la devolución de llamada para el método WorkbookDesigner.Process.

**C#**

{{< highlight "csharp" >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



El resto del proceso incluye cargar la hoja de cálculo del diseñador que contiene los marcadores inteligentes con WorkbookDesigner y procesarla configurando la fuente de datos. Sin embargo, para habilitar las notificaciones, es necesario establecer la propiedad WorkbookDesigner.CallBack antes de llamar al método WorkbookDesigner.Process como se muestra a continuación.

**C#**

{{< highlight "csharp" >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **Método Chart.ToPdf agregado**
 Aspose.Cells for .NET 8.6.2 ha expuesto el método Chart.ToPdf que se puede utilizar para[renderice directamente la forma del gráfico al formato PDF](/cells/es/net/convert-an-excel-chart-to-image/). Dicho método actualmente acepta un parámetro de tipo cadena como ubicación de la ruta del archivo para almacenar el archivo resultante en el disco.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Método Workbook.RemoveUnusedStyles añadido**
 Aspose.Cells for .NET 8.6.2 ha expuesto el método Workbook.RemoveUnusedStyles que se puede usar para[elimine todos los objetos de estilo no utilizados del grupo de estilos](/cells/es/net/remove-unused-styles-inside-the-workbook/).

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Propiedad Cells. Estilo agregado**
La propiedad Cells.Style se puede utilizar para acceder al estilo de la hoja de trabajo que representa el estilo predeterminado.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Eventos agregados para GridWeb**
Aspose.Cells.GridWeb for .NET 8.6.2 ha expuesto los siguientes dos eventos nuevos.

1. AjaxCallFinished: se activa cuando finaliza la actualización AJAX del control. (EnableAJAX se establecerá en verdadero).
1. CellModifiedOnAjax: se activa cuando la celda se modifica en una llamada AJAX.
