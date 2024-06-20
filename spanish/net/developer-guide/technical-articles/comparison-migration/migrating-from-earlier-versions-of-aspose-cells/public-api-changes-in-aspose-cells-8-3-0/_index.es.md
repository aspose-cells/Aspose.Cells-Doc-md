---
title: Cambios en la API pública en Aspose.Cells 8.3.0
type: docs
weight: 100
url: /es/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.2.2 hasta la 8.3.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **APIs Añadidas**
### **Se agregó la propiedad WorkbookSettings.AutoRecover.**
La nueva propiedad AutoRecover se ha agregado a la clase WorkbookSettings para permitir a los desarrolladores establecer la opción de autorecuperación para las hojas de cálculo en sus aplicaciones.

{{% alert color="primary" %}} 

Por favor, consulte el artículo [Configuración de la autorecuperación de hojas de cálculo](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) para obtener más información.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Se agregó la propiedad WorkbookSettings.CrashSave.**
Se ha agregado una propiedad de tipo booleano, CrashSave, a la clase WorkbookSettings que indica si la aplicación guardó por última vez el archivo de la hoja de cálculo después de un bloqueo.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Se agregó la propiedad WorkbookSettings.DataExtractLoad.**
Se ha agregado la propiedad DataExtractLoad a la clase WorkbookSettings para permitir a los desarrolladores obtener información sobre la última recuperación. Si la propiedad DataExtractLoad devuelve true, indica que se ha realizado la recuperación de datos en la hoja de cálculo.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Se ha añadido la propiedad RepairLoad de WorkbookSettings.**
La propiedad RepairLoad indica si la hoja de cálculo ha sido reparada en la última carga con la aplicación Excel.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Se ha añadido la propiedad KeepExactFormat a TxtLoadOptions.**
La propiedad KeepExactFormat se ha agregado a la clase TxtLoadOptions que indica si se debe mantener el formato exacto para el valor de celda cuando una cadena/texto se convierte a números o fecha y hora. Esta propiedad se ha añadido para que coincida con el comportamiento de la aplicación MS Excel al cargar valores de fecha y hora o numéricos desde archivos CSV. Para simular el comportamiento de MS Excel, establezca la propiedad KeepExactFormat en false, mientras que el valor predeterminado es true, por lo que el valor de celda se formateará como la cadena en el archivo CSV.

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Se ha añadido la propiedad Shape.Id.**
Se ha agregado la propiedad Id a la clase Shape para identificar de forma única cada objeto de forma en una hoja de cálculo dada. Esta nueva propiedad también ayuda a identificar objetos de gráficos en una hoja de cálculo como se muestra a continuación.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Se ha agregado el método SetPositionAuto a la clase PlotArea**
El método SetPositionAuto se ha agregado a la clase PlotArea para ayudar a establecer el área de trazado del gráfico en modo automático.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
