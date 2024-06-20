---
title: Formatear y modificar rangos con nombre
type: docs
weight: 85
url: /es/net/format-and-modify-named-ranges/
---

## **Formato de rangos**

### **Establecer el color de fondo y los atributos de fuente a un rango con nombre**

Para aplicar formato, define un objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) para especificar la configuración del estilo y aplícalo al objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) .

El siguiente ejemplo muestra cómo establecer el color de relleno sólido (color de sombreado) con la configuración de fuente a un rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Agregar bordes a un rango con nombre**

Es posible agregar bordes a un rango de celdas en lugar de solo una celda. El objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) proporciona un método [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) que toma los siguientes parámetros para agregar un borde al rango de celdas:

- Tipo de borde, el tipo de borde, seleccionado de la enumeración [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).
- Estilo de línea, el estilo de línea, seleccionado de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).
- Color, el color de la línea, seleccionado de la enumeración Color.

El siguiente ejemplo muestra cómo establecer un borde de contorno en un rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

El siguiente ejemplo muestra cómo establecer bordes alrededor de cada celda en el rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Renombrar un rango con nombre**

Aspose.Cells te permite renombrar un rango con nombre según tus necesidades. Puedes obtener el rango con nombre y renombrarlo usando el atributo [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text). El siguiente ejemplo muestra cómo renombrar un rango con nombre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Unión de rangos**

Aspose.Cells proporciona el método [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) para realizar la unión de rangos, el método devuelve un objeto [*ArrayList*](https://docs.microsoft.com/es-es/dotnet/api/system.collections.arraylist?view=netframework-4.8). El siguiente ejemplo muestra cómo realizar la unión de rangos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Intersección de rangos**

Aspose.Cells proporciona el método [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) para intersectar dos rangos. El método devuelve un objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Para comprobar si un rango se interseca con otro, usa el método [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) que devuelve un valor booleano. El siguiente ejemplo muestra cómo intersectar los rangos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Combinar celdas en el rango con nombre**

Aspose.Cells proporciona el método [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) para combinar las celdas en el rango. El siguiente ejemplo muestra cómo combinar las celdas individuales de un rango con nombre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Eliminar un Rango Nombrado**

Aspose.Cells proporciona el método [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) para borrar el nombre del rango. Para borrar el contenido del rango, usa el método [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index). El siguiente ejemplo muestra cómo eliminar un rango con nombre y su contenido.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
