---
title: Público API Cambios en Aspose.Cells 8.3.0
type: docs
weight: 110
url: /es/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.2.2 a la 8.3.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **API añadidas**
### **Propiedad WorkbookSettings.AutoRecover agregado**
El getter/setter para la propiedad AutoRecover se ha agregado a la clase WorkbookSettings para permitir a los desarrolladores obtener/establecer la opción de Auto-Recovery para las hojas de cálculo en sus aplicaciones.

{{% alert color="primary" %}} 

 Por favor revisa el artículo[Configuración de la recuperación automática de la hoja de cálculo](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) para más información.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Propiedad WorkbookSettings.CrashSave agregado**
El getter/setter para la propiedad CrashSave se ha agregado a la clase WorkbookSettings. La propiedad de tipo booleano indica si la aplicación guardó por última vez el archivo del libro de trabajo después de un bloqueo.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Propiedad WorkbookSettings.DataExtractLoad agregado**
El getter/setter para la propiedad DataExtractLoad se ha agregado a la clase WorkbookSettings para permitir que los desarrolladores obtengan/establezcan la información sobre la última recuperación. Si la propiedad DataExtractLoad devuelve verdadero, eso indica que la recuperación de datos se ha realizado en el archivo del libro de trabajo.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Propiedad WorkbookSettings.RepairLoad agregado**
El getter/setter para la propiedad RepairLoad se ha agregado a la clase WorkbookSettings. La propiedad de tipo booleano indica si la hoja de cálculo se ha reparado en la última sesión de carga con la aplicación Excel.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Propiedad TxtLoadOptions.KeepExactFormat agregado**
La propiedad KeepExactFormat se ha agregado a la clase TxtLoadOptions que indica si se debe mantener el formato exacto para el valor de la celda cuando la cadena/texto se convierte en números o DateTime. Esta propiedad se agregó para que coincida con el comportamiento de la aplicación MS Excel para cargar valores numéricos o de fecha y hora de archivos CSV. Para simular el comportamiento de MS Excel, establezca la propiedad KeepExactFormat en falso, mientras que el valor predeterminado es verdadero, por lo que el valor de la celda se formateará como la cadena en el archivo CSV.

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Propiedad Shape.Id agregado**
La versión 8.3.0 ha agregado el getter/setter para la propiedad Shape.Id para identificar de forma única cada objeto de forma en una hoja de cálculo determinada. Esta nueva propiedad también ayuda a identificar de forma única los objetos Chart en una hoja de cálculo, como se muestra a continuación.

**Java**

{{< highlight "csharp" >}}

 Libro de trabajo book = new Workbook("sample.xlsx");

Gráficos de ChartCollection = book.getWorksheets().get(0).getCharts();

 for(int índice = 0; índice<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Método PlotArea.setPositionAuto Agregado**
El método setPositionAuto se ha agregado a la clase PlotArea que ayuda a configurar el área de trazado del gráfico en modo automático.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
