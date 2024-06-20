---
title: Cambios en la API pública en Aspose.Cells 8.0.0
type: docs
weight: 20
url: /es/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Esta página lista los cambios en la API pública que se introdujeron en Aspose.Cells 8.0.0. Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells que pueda afectar al código existente.

{{% /alert %}} 
## **Añadido MemorySetting a LoadOptions & WorkbookSettings**
A partir de la v8.0.0 de Aspose.Cells for Java hemos proporcionado opciones de uso de memoria para consideraciones de rendimiento. La propiedad MemorySetting ahora está disponible en las clases LoadOptions & WorkbookSettings.
### **Ejemplo**
Demuestra cómo leer un archivo de Excel (de gran tamaño) en modo optimizado.

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Demuestra cómo escribir un gran conjunto de datos en una hoja de cálculo en modo optimizado.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Por favor, revisa el artículo detallado sobre [Optimizar la memoria al trabajar con archivos grandes](/cells/es/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Implementaciones de Row & Cell han cambiado**
En versiones anteriores, los objetos Row y Cell se mantenían en memoria para representar la fila y celda correspondientes en una hoja de cálculo. La misma instancia se devolvía cuando se recuperaban **RowCollection[int índice]** o **Cells[int fila, int columna]**. Por consideraciones de rendimiento de memoria, ahora en adelante solo se mantendrán en memoria las propiedades y datos de Row y Cell. Por lo tanto, el objeto Row & Cell se ha convertido en el contenedor de dichas propiedades.
### **Ejemplo**
Demuestra cómo comparar los objetos Cell y Row de ahora en adelante.

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Debido a que los objetos Row y Cell se instancian según la invocación, no se conservarán y administrarán en la memoria por el componente Cells. Por lo tanto, después de algunas operaciones de inserción y eliminación, es posible que los índices de fila y columna no se actualicen o, peor aún, estos objetos se vuelvan inválidos.
### **Ejemplo**
Por ejemplo, el siguiente fragmento de código devolverá resultados inválidos usando 8.0.0 y superior.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Con la nueva versión, el objeto Cell se volverá inválido o se referirá a A2 con algún valor no deseado. Para evitar tal situación, obtenga nuevamente los objetos Row o Cell de la colección cells para recuperar el resultado correcto.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection ya no hereda de CollectionBase porque no hay ningún objeto Row en su lista interna.

{{% /alert %}}
## **Se ha modificado el comportamiento de Cell.StringValue**
En versiones anteriores, el patrón especial _ se ignoraba al formatear los valores de las celdas, mientras que el carácter especial * siempre producía un solo carácter en el resultado formateado. A partir de esta versión, hemos cambiado la lógica para manejar los caracteres especiales _ y * para que el resultado formateado sea igual al de la aplicación Excel. Por ejemplo, el formato de celda personalizado "_(\$* #,##0.00_)" utilizado para representar el valor 123 producía el resultado "$ 123.00". Con las nuevas versiones, Cell.StringValue contendrá el resultado como "$123.00", que es el mismo comportamiento que exhibe la aplicación Excel al copiar la celda a texto o exportar a CSV.
## **Se agregó CreatedTime a PdfSaveOptions**
Ahora los usuarios pueden obtener o establecer la hora de creación del PDF al guardar la hoja de cálculo en PDF utilizando la clase PdfSaveOptions.
## **Se agregó ShowFormulas a Worksheet**
A partir de ahora, los usuarios pueden utilizar la propiedad booleana ShowFormulas ofrecida por Worksheet para cambiar la vista entre la fórmula y el valor de una hoja de cálculo dada.
## **Se agregó Ooxml a FileFormatType**
Se ha agregado una nueva constante Ooxml a la clase FileFormatType para representar el archivo XML abierto de Office encriptado, como XLSX, DOCX, PPTX y más.
## **Obsoleto FilterColumnCollection de AutoFilter**
Con Aspose.Cells for Java, el método getFilterColumnCollection ha sido marcado como obsoleto. Se sugiere utilizar el método AuotFilter.getFilterColumns en su lugar.
## **Se reemplazó SeriesCollection.SecondCatergoryData con SeriesCollection.SecondCategoryData**
Básicamente hemos corregido el error tipográfico en el nombre del método para SeriesCollection.getSecondCatergoryData. Ahora puede utilizar el método SeriesCollection.getSecondCategoryData en adelante, mientras que el método original SeriesCollection.getSecondCatergoryData se ha marcado como obsoleto.
