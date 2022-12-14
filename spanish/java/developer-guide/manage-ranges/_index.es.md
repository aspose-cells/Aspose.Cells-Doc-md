---
title: Gestión de rangos
linktitle: Rangos
type: docs
weight: 75
url: /es/java/managing-ranges/
---
## **Introducción**

En Excel, puede seleccionar varias celdas con una selección del cuadro del mouse, el conjunto de celdas seleccionadas se denomina "Rango".

Por ejemplo, puede hacer clic con el botón izquierdo del mouse en Cell "A1" de Excel y luego arrastrarlo a la celda "C4". El área rectangular que seleccionó también se puede crear fácilmente como un objeto usando Aspose.Cells.

Aquí se explica cómo crear un rango, poner un valor, establecer un estilo y realizar más operaciones en el objeto "Rango".

## **Gestión de rangos usando Aspose.Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación.

### **Crear rango**

Cuando desee crear un área rectangular que se extienda sobre A1:C4, puede usar el siguiente código:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Poner valor en el Cells del Rango**

Digamos que tiene un rango de celdas que se extiende sobre A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales se organizan secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas del Rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Establecer estilo del Cells de la Gama**

El siguiente ejemplo muestra cómo establecer el estilo de las celdas del Rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **Temas avanzados**
- [Autocompletar rango de archivo de Excel](/cells/es/java/autofill-ranges/)
- [Cambie la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango](/cells/es/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Copiar rangos de Excel](/cells/es/java/copy-ranges-of-Excel/)
- [Copiar solo datos de rango](/cells/es/java/copy-range-data-only/)
- [Copiar datos de rango con estilo](/cells/es/java/copy-range-data-with-style/)
- [Copiar solo estilo de rango](/cells/es/java/copy-range-style-only/)
- [Copiar alturas de fila del rango de origen al rango de destino](/cells/es/java/copy-row-heights-of-source-range-to-destination-range/)
- [Crear rango de unión](/cells/es/java/create-union-range/)
- [Cortar y pegar rangos](/cells/es/java/cut-and-paste-cells/)
- [Eliminar rangos](/cells/es/java/delete-ranges-from-Excel/)
- [Detectar fusionado Cells en una hoja de trabajo](/cells/es/java/detect-merged-cells-in-a-worksheet/)
- [Obtener la dirección Cell Contar el desplazamiento de toda la columna y toda la fila del rango](/cells/es/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Obtener rango con enlaces externos](/cells/es/java/get-range-with-external-links/)
- [Implementación de rangos no secuenciales](/cells/es/java/implementing-non-sequential-ranges/)
- [Insertar rangos](/cells/es/java/insert-ranges-to-Excel/)
- [Fusionar o separar Rango de Cells](/cells/es/java/merge-or-unmerge-range-of-cells/)
- [Mover rango de Cells en una hoja de trabajo](/cells/es/java/move-range-of-cells-in-a-worksheet/)
- [Rangos con nombre](/cells/es/java/named-ranges/)
- [Buscar y reemplazar datos en un rango](/cells/es/java/search-and-replace-data-in-a-range/)

