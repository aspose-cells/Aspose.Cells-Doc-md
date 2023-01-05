---
title: Público API Cambios en Aspose.Cells 8.0.1
type: docs
weight: 20
url: /es/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Esta página enumera los cambios públicos API que se introdujeron en Aspose.Cells 8.0.1. Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells que puede afectar el código existente. Cualquier comportamiento introducido que pueda verse como una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}} 
## **Propiedad MemorySetting agregada a la clase Cells**
La clase Cells ha expuesto la propiedad MemorySetting que se puede usar para optimizar el uso de la memoria para los datos de las celdas y, por lo tanto, disminuir el costo total de la memoria. El siguiente ejemplo muestra cómo escribir datos grandes en una hoja de trabajo en modo optimizado.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

La configuración de la memoria no funcionará para la hoja predeterminada creada automáticamente por el objeto Libro de trabajo. Para cambiar la configuración de memoria de las hojas existentes, aplique la configuración de memoria manualmente antes de realizar cualquier manipulación de datos.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Optimización de la memoria mientras se trabaja con grandes conjuntos de datos](/cells/es/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
