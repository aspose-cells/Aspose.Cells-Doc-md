---
title: Cambios en la API pública en Aspose.Cells 8.0.1
type: docs
weight: 20
url: /es/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Estas páginas enumeran los cambios en la API pública que se introdujeron en Aspose.Cells 8.0.1. Incluye no solo nuevos métodos públicos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells que puede afectar al código existente. Cualquier cambio introducido que pueda considerarse una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}} 
## **Agregada la propiedad MemorySetting a la clase Cells**
La clase Cells ha expuesto la propiedad MemorySetting que puede utilizarse para optimizar el uso de memoria para los datos de las celdas, y por lo tanto disminuir el costo total de memoria. El siguiente ejemplo muestra cómo escribir datos extensos en una hoja de cálculo en modo optimizado.

**C#**

{{< highlight csharp >}}

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

La configuración de memoria no funcionará automáticamente para la hoja predeterminada creada por el objeto Workbook. Para cambiar la configuración de memoria de las hojas existentes, aplique la configuración de memoria manualmente antes de realizar cualquier manipulación de datos.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Optimizar la memoria al trabajar con grandes conjuntos de datos](/cells/es/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
