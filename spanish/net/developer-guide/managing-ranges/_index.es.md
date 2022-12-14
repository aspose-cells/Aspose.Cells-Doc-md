---
title: Gestión de rangos
linktitle: Rangos
type: docs
weight: 105
url: /es/net/managing-ranges/
---
## **Introducción**

En Excel, puede seleccionar varias celdas con una selección del cuadro del mouse, el conjunto de celdas seleccionadas se denomina "Rango".

Por ejemplo, puede hacer clic con el botón izquierdo del mouse en Cell "A1" de Excel y luego arrastrarlo a la celda "C4". El área rectangular que seleccionó también se puede crear fácilmente como un objeto usando Aspose.Cells.

Aquí se explica cómo crear un rango, poner un valor, establecer un estilo y realizar más operaciones en el objeto "Rango".

## **Gestión de rangos usando Aspose.Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación.

### **Crear rango**

Cuando desee crear un área rectangular que se extienda sobre A1:C4, puede usar el siguiente código:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Poner valor en el Cells del Rango**

Digamos que tiene un rango de celdas que se extiende sobre A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales se organizan secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas del Rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Establecer estilo del Cells de la Gama**

El siguiente ejemplo muestra cómo establecer el estilo de las celdas del Rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **Obtener región actual del rango**

 CurrentRegion es una propiedad que devuelve un objeto Range que representa la región actual.

La región actual es un rango limitado por cualquier combinación de filas y columnas en blanco. Solo lectura.

En Excel, puede obtener el área CurrentRegion de la siguiente manera:
1. Seleccione un área (rango 1) con el cuadro del mouse.
2. Haga clic en "Inicio - Edición - Buscar y seleccionar - Ir a Especial - Región actual", o use "Ctrl+Shift+*", verá que Excel automáticamente lo ayuda a seleccionar un área (rango2), ahora que lo logró, rango2 es la región actual de range1.

Usando Aspose.Cells, puede usar la propiedad "Range.CurrentRegion" para realizar la misma función.

Descargue el siguiente archivo de prueba, ábralo en Excel, use el cuadro del mouse para seleccionar un área "A1: D7", luego haga clic en "Ctrl + Shift + *", verá el área "A1: C3" seleccionada.

[región_actual.xlsx](current_region.xlsx)

Ahora ejecute el siguiente ejemplo, vea cómo funciona en Aspose.Cells:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Temas avanzados**
- [Autocompletar rango de archivo de Excel](/cells/es/net/autofill-ranges/)
- [Copiar rangos de Excel](/cells/es/net/copy-ranges-of-Excel/)
- [Copiar solo datos de rango](/cells/es/net/copy-range-data-only/)
- [Copiar datos de rango con estilo](/cells/es/net/copy-range-data-with-style/)
- [Copiar solo estilo de rango](/cells/es/net/copy-range-style-only/)
- [Crear rango de unión](/cells/es/net/create-union-range/)
- [Gama Cortar y Pegar](/cells/es/net/cut-and-paste-cells/)
- [Eliminar rangos](/cells/es/net/delete-ranges-from-Excel/)
- [Obtener la dirección Cell Contar el desplazamiento de toda la columna y toda la fila del rango](/cells/es/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insertar rangos](/cells/es/net/insert-ranges-to-Excel/)
- [Fusionar o separar Rango de Cells](/cells/es/net/merge-or-unmerge-range-of-cells/)
- [Mover rango de Cells en una hoja de trabajo](/cells/es/net/move-range-of-cells-in-a-worksheet/)
- [Crear rangos con nombre de ámbito de libro y hoja de trabajo](/cells/es/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Buscar y reemplazar datos en un rango](/cells/es/net/search-and-replace-data-in-a-range/)
