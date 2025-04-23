---
title: Gestión de rangos
linktitle: Rangos
type: docs
weight: 105
url: /es/net/managing-ranges/
---

## **Introducción**

En Excel, puedes seleccionar varias celdas con una selección de caja de ratón, el conjunto de celdas seleccionadas se llama "Rango".

Por ejemplo, puedes hacer clic en el botón izquierdo del ratón en la celda "A1" de Excel y luego arrastrar hasta la celda "C4". El área rectangular que seleccionaste también se puede crear fácilmente como un objeto usando Aspose.Cells.

Aquí tienes cómo crear un rango, poner valor, establecer estilo y realizar más operaciones en el objeto "Rango".

## **Manejo de rangos usando Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite el acceso a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

### **Crear rango**

Cuando quieras crear un área rectangular que se extienda sobre A1:C4, puedes usar el siguiente código:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Poner valor en las celdas del rango**

Digamos que tienes un rango de celdas que se extiende sobre A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales están dispuestas secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

El siguiente ejemplo muestra cómo introducir algunos valores en las celdas del rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Establecer estilo de las celdas del rango**

El siguiente ejemplo muestra cómo establecer el estilo de las celdas del rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Temas avanzados**
- [Rango de AutoFill del archivo de Excel](/cells/es/net/autofill-ranges/)
- [Copiar rangos de Excel](/cells/es/net/copy-ranges-of-Excel/)
- [Copiar solo datos de rango](/cells/es/net/copy-range-data-only/)
- [Copiar datos de rango con estilo](/cells/es/net/copy-range-data-with-style/)
- [Copiar solo estilo de rango](/cells/es/net/copy-range-style-only/)
- [Crear rango de unión](/cells/es/net/create-union-range/)
- [Cortar y pegar rango](/cells/es/net/cut-and-paste-cells/)
- [Eliminar rangos](/cells/es/net/delete-ranges-from-Excel/)
- [Obtener dirección Celda Contar Desplazamiento Toda la columna y Toda la fila del Rango](/cells/es/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insertar rangos](/cells/es/net/insert-ranges-to-Excel/)
- [Combinar o dividir rango de celdas](/cells/es/net/merge-or-unmerge-range-of-cells/)
- [Mover rango de celdas en una hoja de cálculo](/cells/es/net/move-range-of-cells-in-a-worksheet/)
- [Crear rangos con nombre con ámbito de libro de trabajo y hoja de cálculo](/cells/es/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Buscar y reemplazar datos en un rango](/cells/es/net/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="csharp" >}}
