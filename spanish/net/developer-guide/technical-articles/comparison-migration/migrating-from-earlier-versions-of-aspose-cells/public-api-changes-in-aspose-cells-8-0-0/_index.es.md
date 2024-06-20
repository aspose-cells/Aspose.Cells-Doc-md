---
title: Cambios en la API pública en Aspose.Cells 8.0.0
type: docs
weight: 10
url: /es/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Esta página lista los cambios en la API pública que se introdujeron en Aspose.Cells 8.0.0. Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells que pueda afectar al código existente.

{{% /alert %}} 
## **Añadido MemorySetting a LoadOptions & WorkbookSettings**
A partir de la versión 8.0.0 de Aspose.Cells for .NET, hemos proporcionado opciones de uso de memoria para consideraciones de rendimiento. La propiedad MemorySetting ahora está disponible en las clases LoadOptions y WorkbookSettings.
##### **Ejemplo**
Demuestra cómo leer un archivo de Excel (de gran tamaño) en modo optimizado.

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Demuestra cómo escribir un gran conjunto de datos en una hoja de cálculo en modo optimizado.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Por favor, consulte el artículo detallado sobre [Optimizar la memoria al trabajar con archivos grandes](/cells/es/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Implementaciones de Row & Cell han cambiado**
En versiones anteriores, los objetos Row y Cell se mantenían en memoria para representar la fila y celda correspondientes en una hoja de cálculo. La misma instancia se devolvía cuando se recuperaban **RowCollection[int índice]** o **Cells[int fila, int columna]**. Por consideraciones de rendimiento de memoria, ahora en adelante solo se mantendrán en memoria las propiedades y datos de Row y Cell. Por lo tanto, el objeto Row & Cell se ha convertido en el contenedor de dichas propiedades.
### **Ejemplo**
Demuestra cómo comparar los objetos Cell y Row de ahora en adelante.

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Debido a que los objetos Row y Cell se instancian según la invocación, no se conservarán y administrarán en la memoria por el componente Cells. Por lo tanto, después de algunas operaciones de inserción y eliminación, es posible que los índices de fila y columna no se actualicen o, peor aún, estos objetos se vuelvan inválidos.
### **Ejemplo**
Por ejemplo, el siguiente fragmento de código devolverá resultados inválidos usando 8.0.0 y superior.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Con la nueva versión, el objeto Cell se volverá inválido o se referirá a A2 con algún valor no deseado. Para evitar tal situación, obtenga nuevamente los objetos Row o Cell de la colección cells para recuperar el resultado correcto.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection ya no hereda de CollectionBase porque no hay ningún objeto Row en su lista interna.

{{% /alert %}}
## **Se ha modificado el comportamiento de Cell.StringValue**
En versiones anteriores, el patrón especial _ se ignoraba al formatear los valores de las celdas, mientras que el carácter especial * siempre producía un carácter en el resultado formateado. A partir de esta versión, hemos cambiado la lógica para manejar los caracteres especiales _ y * con el fin de hacer que el resultado formateado sea el mismo que el de la aplicación Excel. Por ejemplo, el formato de celda personalizado "_(\$* #,##0.00_)" usado para representar el valor 123 producía el resultado "$ 123.00". Con las nuevas versiones, Cell.StringValue contendrá el resultado como "$123.00", que es el mismo comportamiento que exhibe la aplicación Excel al copiar la celda a texto o exportar a CSV.
## **Se agregó CreatedTime a PdfSaveOptions**
Ahora los usuarios pueden obtener o establecer la hora de creación del PDF al guardar la hoja de cálculo en PDF utilizando la clase PdfSaveOptions.
## **Se agregó ShowFormulas a Worksheet**
De ahora en adelante, los usuarios pueden utilizar la propiedad Booleana ShowFormulas ofrecida por la Hoja de trabajo para cambiar la vista de fórmulas a valor de una hoja de trabajo dada.
## **Se agregó Ooxml a FileFormatType**
Se ha agregado una nueva constante Ooxml a la clase FileFormatType para representar el archivo XML abierto de Office encriptado, como XLSX, DOCX, PPTX y más.
## **Obsoleto FilterColumnCollection de AutoFilter**
Con Aspose.Cells for Java, la propiedad FilterColumnCollection se ha marcado como obsoleta. Se recomienda usar la propiedad AuotFilter.FilterColumns en su lugar.
## **Se reemplazó SeriesCollection.SecondCatergoryData con SeriesCollection.SecondCategoryData**
Básicamente corregimos el error tipográfico en el nombre de propiedad para SeriesCollection.SecondCatergoryData. A partir de ahora, puede usar la propiedad SeriesCollection.SecondCategoryData, mientras que la propiedad original SeriesCollection.SecondCatergoryData se ha marcado como obsoleta.
