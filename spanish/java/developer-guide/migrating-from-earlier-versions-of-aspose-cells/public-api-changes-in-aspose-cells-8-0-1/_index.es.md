---
title: Cambios en la API pública en Aspose.Cells 8.0.1
type: docs
weight: 30
url: /es/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Estas páginas enumeran los cambios en la API pública que se introdujeron en Aspose.Cells 8.0.1. Incluye no solo nuevos métodos públicos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells que puede afectar al código existente. Cualquier cambio introducido que pueda considerarse una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}} 
## **Propiedad MemorySetting agregada a la clase Cells**
La clase Cells ha expuesto los métodos setMemorySetting y getMemorySetting que se pueden utilizar para optimizar el uso de memoria para los datos de las celdas y, por lo tanto, disminuir el costo total de la memoria. El siguiente ejemplo muestra cómo escribir grandes datos en una hoja de cálculo en modo optimizado.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

La configuración de memoria no funcionará automáticamente para la hoja por defecto creada por el libro. Para cambiar la configuración de memoria de las hojas existentes, aplique manualmente la configuración de memoria antes de realizar cualquier manipulación de datos. 

{{% /alert %}} {{% alert color="primary" %}} 

Por favor, consulte el artículo detallado sobre [Optimizar la memoria mientras se trabaja con grandes conjuntos de datos](/cells/es/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
