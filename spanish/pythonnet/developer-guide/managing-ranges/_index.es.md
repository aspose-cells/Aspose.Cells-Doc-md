---
title: Gestión de rangos
linktitle: Rangos
type: docs
weight: 105
url: /es/python-net/managing-ranges/
description: Este artículo muestra cómo gestionar rangos mediante la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, gestionar rangos en Python, crear rango en Python, poner valor en las células del rango en Python, establecer estilo de las células del rango en Python, obtener Región actual del rango en Python.
---

## **Introducción**

En Excel, puedes seleccionar varias celdas con una selección de caja de ratón, el conjunto de celdas seleccionadas se llama "Rango".

Por ejemplo, puedes hacer clic con el botón izquierdo del ratón en la Celda "A1" de Excel y luego arrastrar hasta la celda "C4". El área rectangular seleccionada también se puede crear fácilmente como un objeto utilizando Aspose.Cells para Python via .NET.

Aquí tienes cómo crear un rango, poner valor, establecer estilo y realizar más operaciones en el objeto "Rango".

## **Gestión de rangos utilizando la biblioteca de Excel de Python Aspose.Cells**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

## **Cómo crear un rango**

Cuando quieras crear un área rectangular que se extienda sobre A1:C4, puedes usar el siguiente código:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **Cómo poner valor en las celdas del rango**

Supongamos que tienes un rango de celdas que se extiende sobre A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas individuales del rango se disponen de forma secuencial.

El siguiente ejemplo muestra cómo introducir algunos valores en las celdas del rango.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **Cómo establecer el estilo de las celdas del rango**

El siguiente ejemplo muestra cómo establecer el estilo de las celdas del rango.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **Cómo obtener la Región actual del rango**

CurrentRegion es una propiedad que devuelve un objeto Range que representa la región actual. 

La región actual es un rango delimitado por cualquier combinación de filas y columnas en blanco. Solo lectura.

En Excel, puedes obtener el área CurrentRegion mediante:
1. Selecciona un área (rango1) con el cuadro del ratón.
2. Haz clic en "Inicio - Edición - Buscar y seleccionar - Ir a especial - Región actual", o usa "Ctrl+Mayús+*", verás que Excel automáticamente te ayuda a seleccionar un área (rango2), ahora lo hiciste, rango2 es el CurrentRegion de rango1.

Usando Aspose.Cells for Python via .NET, puedes usar la propiedad "Range.current_region" para realizar la misma función.

Por favor, descarga el siguiente archivo de prueba, ábrelo en Excel, usa el cuadro del ratón para seleccionar un área "A1:D7", luego haz clic en "Ctrl+Mayús+*", verás que el área "A1:C3" está seleccionada.

[current_region.xlsx](current_region.xlsx)

Ahora por favor ejecuta el siguiente ejemplo, mira cómo funciona en Aspose.Cells for Python via .NET:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **Temas avanzados**
- [Rango de AutoFill del archivo de Excel](/cells/es/python-net/autofill-ranges/)
- [Copiar rangos de Excel](/cells/es/python-net/copy-ranges-of-excel/)
- [Copiar solo datos de rango](/cells/es/python-net/copy-range-data-only/)
- [Copiar datos de rango con estilo](/cells/es/python-net/copy-range-data-with-style/)
- [Copiar solo estilo de rango](/cells/es/python-net/copy-range-style-only/)
- [Crear rango de unión](/cells/es/python-net/create-union-range/)
- [Cortar y pegar rango](/cells/es/python-net/cut-and-paste-cells/)
- [Eliminar rangos](/cells/es/python-net/delete-ranges-from-excel/)
- [Obtener dirección Celda Contar Desplazamiento Toda la columna y Toda la fila del Rango](/cells/es/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insertar rangos](/cells/es/python-net/insert-ranges-to-excel/)
- [Combinar o dividir rango de celdas](/cells/es/python-net/merge-or-unmerge-range-of-cells/)
- [Mover rango de celdas en una hoja de cálculo](/cells/es/python-net/move-range-of-cells-in-a-worksheet/)
- [Crear rangos con nombre con ámbito de libro de trabajo y hoja de cálculo](/cells/es/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Buscar y reemplazar datos en un rango](/cells/es/python-net/search-and-replace-data-in-a-range/)

