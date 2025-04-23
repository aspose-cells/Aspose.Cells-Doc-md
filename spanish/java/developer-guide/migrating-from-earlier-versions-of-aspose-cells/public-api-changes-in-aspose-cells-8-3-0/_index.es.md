---
title: Cambios en la API pública en Aspose.Cells 8.3.0
type: docs
weight: 110
url: /es/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.2.2 hasta la 8.3.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones.

{{% /alert %}} 
## **APIs Añadidas**
### **Se agregó la propiedad WorkbookSettings.AutoRecover.**
Se han agregado los getter/setter para la propiedad AutoRecover a la clase WorkbookSettings para permitir a los desarrolladores obtener/establecer la opción de recuperación automática para las hojas de cálculo en sus aplicaciones. 

{{% alert color="primary" %}} 

Por favor, consulte el artículo [Configurar Recuperación Automática de Hojas de Cálculo](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) para obtener más información.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Se agregó la propiedad WorkbookSettings.CrashSave.**
Se han agregado los getter/setter para la propiedad CrashSave a la clase WorkbookSettings. La propiedad de tipo Boolean indica si la aplicación guardó por última vez el archivo de la hoja de cálculo después de un cierre inesperado.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Se agregó la propiedad WorkbookSettings.DataExtractLoad.**
Se han agregado los getter/setter para la propiedad DataExtractLoad a la clase WorkbookSettings para permitir a los desarrolladores obtener/establecer la información sobre la última recuperación. Si la propiedad DataExtractLoad devuelve true, indica que se ha realizado una recuperación de datos en el archivo de la hoja de cálculo.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Se ha añadido la propiedad RepairLoad de WorkbookSettings.**
El getter/setter para la propiedad RepairLoad se ha añadido a la clase WorkbookSettings. La propiedad de tipo booleano indica si la hoja de cálculo ha sido reparada en la última sesión de carga con la aplicación Excel.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Se ha añadido la propiedad KeepExactFormat a TxtLoadOptions.**
La propiedad KeepExactFormat se ha agregado a la clase TxtLoadOptions que indica si se debe mantener el formato exacto para el valor de celda cuando una cadena/texto se convierte a números o fecha y hora. Esta propiedad se ha añadido para que coincida con el comportamiento de la aplicación MS Excel al cargar valores de fecha y hora o numéricos desde archivos CSV. Para simular el comportamiento de MS Excel, establezca la propiedad KeepExactFormat en false, mientras que el valor predeterminado es true, por lo que el valor de celda se formateará como la cadena en el archivo CSV.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Se ha añadido la propiedad Shape.Id.**
La v8.3.0 ha agregado el getter/setter para la propiedad Shape.Id para identificar de forma única cada objeto de forma en una hoja de cálculo dada. Esta nueva propiedad también ayuda a identificar de forma única objetos de gráfico en una hoja de cálculo como se muestra a continuación.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Se ha añadido el método setPositionAuto a PlotArea.**
Se ha agregado el método setPositionAuto a la clase PlotArea que ayuda a configurar el área de trazado del gráfico en modo automático.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
