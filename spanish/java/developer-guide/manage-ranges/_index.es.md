---
title: Gestión de rangos
linktitle: Rangos
type: docs
weight: 75
url: /es/java/managing-ranges/
---

## **Introducción**

En Excel, puedes seleccionar varias celdas con una selección de caja de ratón, el conjunto de celdas seleccionadas se llama "Rango".

Por ejemplo, puedes hacer clic en el botón izquierdo del ratón en la celda "A1" de Excel y luego arrastrar hasta la celda "C4". El área rectangular que seleccionaste también se puede crear fácilmente como un objeto usando Aspose.Cells.

Aquí tienes cómo crear un rango, poner valor, establecer estilo y realizar más operaciones en el objeto "Rango".

## **Manejo de rangos usando Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite el acceso a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

### **Crear rango**

Cuando quieras crear un área rectangular que se extienda sobre A1:C4, puedes usar el siguiente código:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Poner valor en las celdas del rango**

Digamos que tienes un rango de celdas que se extiende sobre A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales están dispuestas secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

El siguiente ejemplo muestra cómo introducir algunos valores en las celdas del rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Establecer estilo de las celdas del rango**

El siguiente ejemplo muestra cómo establecer el estilo de las celdas del rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

### **Obtener la región actual del rango**

CurrentRegion es una propiedad que devuelve un objeto Range que representa la región actual. 

La región actual es un rango delimitado por cualquier combinación de filas y columnas en blanco. Solo lectura.

En Excel, puedes obtener el área CurrentRegion mediante:
1. Selecciona un área (rango1) con el cuadro del ratón.
2. Haz clic en "Inicio - Edición - Buscar y seleccionar - Ir a especial - Región actual", o usa "Ctrl+Mayús+*", verás que Excel automáticamente te ayuda a seleccionar un área (rango2), ahora lo hiciste, rango2 es el CurrentRegion de rango1.

Usando Aspose.Cells, puedes utilizar la propiedad "Range.CurrentRegion" para realizar la misma función.

Por favor, descarga el siguiente archivo de prueba, ábrelo en Excel, usa el cuadro del ratón para seleccionar un área "A1:D7", luego haz clic en "Ctrl+Mayús+*", verás que el área "A1:C3" está seleccionada.

[current_region.xlsx](current_region.xlsx)

Ahora por favor ejecuta el siguiente ejemplo, mira cómo funciona en Aspose.Cells:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **Temas avanzados**
- [Rango de AutoFill del archivo de Excel](/cells/es/java/autofill-ranges/)
- [Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango](/cells/es/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Copiar rangos de Excel](/cells/es/java/copy-ranges-of-Excel/)
- [Copiar solo datos de rango](/cells/es/java/copy-range-data-only/)
- [Copiar datos de rango con estilo](/cells/es/java/copy-range-data-with-style/)
- [Copiar solo estilo de rango](/cells/es/java/copy-range-style-only/)
- [Copiar alturas de fila del rango de origen al rango de destino](/cells/es/java/copy-row-heights-of-source-range-to-destination-range/)
- [Crear rango de unión](/cells/es/java/create-union-range/)
- [Cortar y pegar rangos](/cells/es/java/cut-and-paste-cells/)
- [Eliminar rangos](/cells/es/java/delete-ranges-from-Excel/)
- [Detectar celdas combinadas en una hoja de cálculo](/cells/es/java/detect-merged-cells-in-a-worksheet/)
- [Obtener dirección Celda Contar Desplazamiento Toda la columna y Toda la fila del Rango](/cells/es/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Obtener Rango con Vínculos Externos](/cells/es/java/get-range-with-external-links/)
- [Implementación de Rangos No Secuenciales](/cells/es/java/implementing-non-sequential-ranges/)
- [Insertar rangos](/cells/es/java/insert-ranges-to-Excel/)
- [Combinar o dividir rango de celdas](/cells/es/java/merge-or-unmerge-range-of-cells/)
- [Mover rango de celdas en una hoja de cálculo](/cells/es/java/move-range-of-cells-in-a-worksheet/)
- [Rangos nombrados](/cells/es/java/named-ranges/)
- [Buscar y reemplazar datos en un rango](/cells/es/java/search-and-replace-data-in-a-range/)

