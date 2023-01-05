---
title: Público API Cambios en Aspose.Cells 8.3.0
type: docs
weight: 100
url: /es/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.2.2 a la 8.3.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **API añadidas**
### **Propiedad WorkbookSettings.AutoRecover agregado**
La nueva propiedad Autorrecuperación se ha agregado a la clase WorkbookSettings para permitir que los desarrolladores configuren la opción de Autorrecuperación para las hojas de cálculo en sus aplicaciones.

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Configuración de la recuperación automática de la hoja de cálculo](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) para más información.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Propiedad WorkbookSettings.CrashSave agregado**
Se ha agregado una propiedad de tipo booleano CrashSave a la clase WorkbookSettings que indica si la aplicación guardó por última vez el archivo del libro de trabajo después de un bloqueo.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Propiedad WorkbookSettings.DataExtractLoad agregado**
La propiedad DataExtractLoad se ha agregado a la clase WorkbookSettings para permitir a los desarrolladores obtener información sobre la última recuperación. Si la propiedad DataExtractLoad devuelve verdadero, eso indica que la recuperación de datos se ha realizado en la hoja de cálculo.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Propiedad WorkbookSettings.RepairLoad agregado**
La propiedad RepairLoad indica si la hoja de cálculo ha sido reparada en la última carga con la aplicación Excel.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Propiedad TxtLoadOptions.KeepExactFormat agregado**
La propiedad KeepExactFormat se ha agregado a la clase TxtLoadOptions que indica si se debe mantener el formato exacto para el valor de la celda cuando la cadena/texto se convierte en números o DateTime. Esta propiedad se agregó para que coincida con el comportamiento de la aplicación MS Excel para cargar valores numéricos o de fecha y hora de archivos CSV. Para simular el comportamiento de MS Excel, establezca la propiedad KeepExactFormat en falso, mientras que el valor predeterminado es verdadero, por lo que el valor de la celda se formateará como la cadena en el archivo CSV.

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Propiedad Shape.Id agregado**
La propiedad Id se ha agregado a la clase Shape para identificar de forma única cada objeto de forma en una hoja de cálculo determinada. Esta nueva propiedad también ayuda a identificar objetos de gráfico en una hoja de cálculo, como se muestra a continuación.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Método PlotArea.SetPositionAuto Agregado**
El método SetPositionAuto se ha agregado a la clase PlotArea que ayuda a configurar el área de trazado del gráfico en modo automático.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
