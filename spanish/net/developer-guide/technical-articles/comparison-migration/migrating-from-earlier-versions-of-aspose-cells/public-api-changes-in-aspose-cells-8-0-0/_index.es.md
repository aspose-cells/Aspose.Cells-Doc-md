---
title: Público API Cambios en Aspose.Cells 8.0.0
type: docs
weight: 10
url: /es/net/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Esta página enumera los cambios públicos API que se introdujeron en Aspose.Cells 8.0.0. Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells que puede afectar el código existente.

{{% /alert %}} 
## **Se agregó MemorySetting a LoadOptions y WorkbookSettings**
A partir de v8.0.0 de Aspose.Cells for .NET, proporcionamos las opciones de uso de memoria para consideraciones de rendimiento. La propiedad MemorySetting ahora está disponible en las clases LoadOptions y WorkbookSettings.
##### **Ejemplo**
Demuestra cómo leer un archivo de Excel (de gran tamaño) en modo optimizado.

**C#**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Demuestra cómo escribir un conjunto de datos grande en una hoja de trabajo en modo optimizado.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Optimización de la memoria mientras se trabaja con archivos grandes](/cells/es/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Las implementaciones de Row & Cell han cambiado**
 En versiones anteriores, los objetos Row y Cell se guardaban en la memoria para representar la fila y la celda correspondientes en una hoja de trabajo. La misma instancia se devolvía cada vez que**RowCollection[índice int]** o**Cells[fila int, columna int]** fueron recuperados. Para considerar el rendimiento de la memoria, solo las propiedades y los datos de Row y Cell se mantendrán en la memoria a partir de ahora. Por lo tanto, el objeto Row & Cell se ha convertido en el envoltorio de las propiedades mencionadas.
### **Ejemplo**
Muestra cómo comparar los objetos Cell y Row a partir de ahora.

**C#**

{{< highlight "csharp" >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Debido a que los objetos Row y Cell se instancian de acuerdo con la invocación, el componente Cells no los mantendrá ni administrará en la memoria. Por lo tanto, después de algunas operaciones de inserción y eliminación, es posible que los índices de Fila y Columna no se actualicen o, lo que es peor, estos objetos dejen de ser válidos.
### **Ejemplo**
Por ejemplo, el siguiente fragmento de código devolverá resultados no válidos con 8.0.0 y superior,

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Con la nueva versión, el objeto Cell dejará de ser válido o se referirá a A2 con algún valor no deseado. Para evitar tal situación, vuelva a obtener los objetos Fila o Cell de la colección de celdas para recuperar el resultado correcto.

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection ya no hereda CollectionBase porque no hay ningún objeto Row en su lista interna.

{{% /alert %}}
## **Cell. Cambio de comportamiento de StringValue**
 En versiones anteriores, patrón especial_se ignoró al formatear los valores de las celdas, donde el carácter especial * siempre producía un carácter en el resultado formateado. A partir de esta versión, hemos cambiado la lógica para manejar caracteres especiales._ y* para que el resultado formateado sea el mismo que el de la aplicación Excel. Por ejemplo, el formato de celda personalizado "_(\$* #,##0.00_)" utilizado para representar el valor 123 produjo el resultado como "$ 123,00". Con las nuevas versiones, Cell.StringValue contendrá el resultado como "$123,00", que es el mismo comportamiento que muestra la aplicación Excel al copiar la celda para enviar mensajes de texto o exportar a CSV.
## **Se agregó CreatedTime a PdfSaveOptions**
Ahora los usuarios pueden obtener o establecer el tiempo de creación de PDF mientras guardan la hoja de cálculo en PDF mientras usan la clase PdfSaveOptions.
## **Se agregaron ShowFormulas a la hoja de trabajo**
De ahora en adelante, los usuarios pueden usar la propiedad booleana ShowFormulas que ofrece Worksheet para cambiar la vista de fórmula a valor de una hoja de cálculo determinada.
## **Se agregó Ooxml a FileFormatType**
Se agregó una nueva constante Ooxml a la clase FileFormatType para representar el archivo XML abierto de Office encriptado, como XLSX, DOCX, PPTX y más.
## **FilterColumnObsoletoColección de AutoFilter**
Con Aspose.Cells for Java, la propiedad FilterColumnCollection se ha marcado como obsoleta. Se sugiere utilizar la propiedad AuotFilter.FilterColumns en su lugar.
## **Se reemplazó SeriesCollection.SecondCatergoryData con SeriesCollection.SecondCategoryData**
Básicamente, hemos corregido el error tipográfico en el nombre de la propiedad para SeriesCollection.SecondCatergoryData. Puede usar la propiedad SeriesCollection.SecondCategoryData ahora en adelante, mientras que la propiedad original SeriesCollection.SecondCatergoryData se ha marcado como obsoleta.
