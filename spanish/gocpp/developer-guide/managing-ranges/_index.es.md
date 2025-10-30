---
title: Gestión de Rangos con Golang vía C++
linktitle: Rangos
type: docs
weight: 105
url: /es/go-cpp/managing-ranges/
description: Aprende cómo gestionar rangos en archivos de Excel usando Aspose.Cells con Golang vía C++. Crea, modifica y da estilo a los rangos programáticamente.
---

## **Introducción**

En Excel, puedes seleccionar varias celdas con una selección de caja de ratón, el conjunto de celdas seleccionadas se llama "Rango".

Por ejemplo, puedes hacer clic en el botón izquierdo del ratón en la celda "A1" de Excel y luego arrastrar hasta la celda "C4". El área rectangular que seleccionaste también se puede crear fácilmente como un objeto usando Aspose.Cells.

Aquí tienes cómo crear un rango, poner valor, establecer estilo y realizar más operaciones en el objeto "Rango".

## **Manejo de rangos usando Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite el acceso a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Crear rango**

Cuando quieras crear un área rectangular que se extienda sobre A1:C4, puedes usar el siguiente código:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges.go" >}}
### **Poner valor en las celdas del rango**

Digamos que tienes un rango de celdas que se extiende sobre A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales están dispuestas secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

El siguiente ejemplo muestra cómo introducir algunos valores en las celdas del rango.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-1.go" >}}
### **Establecer estilo de las celdas del rango**

El siguiente ejemplo muestra cómo establecer el estilo de las celdas del rango.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-2.go" >}}
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-3.go" >}}

## **Temas avanzados**
- [Rango de AutoFill del archivo de Excel](/cells/es/cpp/autofill-ranges/)
- [Copiar rangos de Excel](/cells/es/cpp/copy-ranges-of-Excel/)
- [Copiar solo datos de rango](/cells/es/cpp/copy-range-data-only/)
- [Copiar datos de rango con estilo](/cells/es/cpp/copy-range-data-with-style/)
- [Copiar solo estilo de rango](/cells/es/cpp/copy-range-style-only/)
- [Crear rango de unión](/cells/es/cpp/create-union-range/)
- [Cortar y pegar rango](/cells/es/cpp/cut-and-paste-cells/)
- [Eliminar rangos](/cells/es/cpp/delete-ranges-from-Excel/)
- [Obtener dirección Celda Contar Desplazamiento Toda la columna y Toda la fila del Rango](/cells/es/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insertar rangos](/cells/es/cpp/insert-ranges-to-Excel/)
- [Combinar o dividir rango de celdas](/cells/es/cpp/merge-or-unmerge-range-of-cells/)
- [Mover rango de celdas en una hoja de cálculo](/cells/es/cpp/move-range-of-cells-in-a-worksheet/)
- [Crear rangos con nombre con ámbito de libro de trabajo y hoja de cálculo](/cells/es/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Buscar y reemplazar datos en un rango](/cells/es/cpp/search-and-replace-data-in-a-range/)
