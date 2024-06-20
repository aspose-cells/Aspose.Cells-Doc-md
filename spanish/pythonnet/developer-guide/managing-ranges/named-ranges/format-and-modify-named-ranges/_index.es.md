---
title: Formatear y modificar rangos con nombre
type: docs
weight: 85
url: /es/python-net/format-and-modify-named-ranges/
description: Este artículo muestra cómo Formatear y Modificar Rangos con Nombre con Aspose.Cells for Python via .NET API.
keywords: Librería de Excel en Python, Formatear y Modificar Rangos con Nombre en Python, Establecer Color de Fondo y Atributos de Fuente a un Rango con Nombre en Python, Agregar Bordes a un Rango con Nombre, Renombrar un Rango con Nombre, Unión de Rangos en Python, Intersección de Rangos en Python, Combinar Celdas en el Rango con Nombre en Python.
---

## **Formato de rangos**

### **Cómo configurar el color de fondo y los atributos de fuente a un rango con nombre**

Para aplicar formato, define un objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) para especificar la configuración del estilo y aplícalo al objeto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) .

El siguiente ejemplo muestra cómo establecer el color de relleno sólido (color de sombreado) con la configuración de fuente a un rango.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **Cómo agregar bordes a un rango con nombre**

Es posible agregar bordes a un rango de celdas en lugar de solo una celda. El objeto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) proporciona un método [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor) que toma los siguientes parámetros para agregar un borde al rango de celdas:

- Tipo de borde, el tipo de borde, seleccionado de la enumeración [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).
- Estilo de línea, el estilo de línea, seleccionado de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).
- Color, el color de la línea, seleccionado de la enumeración Color.

El siguiente ejemplo muestra cómo establecer un borde de contorno en un rango.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **Cómo cambiar el nombre a un rango con nombre**

Aspose.Cells te permite renombrar un rango con nombre según tus necesidades. Puedes obtener el rango con nombre y renombrarlo usando el atributo [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text). El siguiente ejemplo muestra cómo renombrar un rango con nombre.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **Cómo realizar la unión de rangos**

Aspose.Cells proporciona el método [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range) para realizar la unión de rangos. El siguiente ejemplo muestra cómo realizar la unión de rangos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **Cómo intersectar los rangos**

Aspose.Cells proporciona el método [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) para intersectar dos rangos. El método devuelve un objeto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Para comprobar si un rango se interseca con otro, usa el método [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) que devuelve un valor booleano. El siguiente ejemplo muestra cómo intersectar los rangos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **Cómo combinar celdas en el rango con nombre**

Aspose.Cells proporciona el método [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) para combinar las celdas en el rango. El siguiente ejemplo muestra cómo combinar las celdas individuales de un rango con nombre.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
