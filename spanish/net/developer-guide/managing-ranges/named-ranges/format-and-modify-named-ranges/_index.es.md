---
title: Dar formato y modificar rangos con nombre
type: docs
weight: 85
url: /es/net/format-and-modify-named-ranges/
---
## **Rangos de formato**

### **Establecimiento de atributos de fuente y color de fondo en un rango con nombre**

 Para aplicar formato, defina un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto para especificar la configuración de estilo y aplicarlo al[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range)objeto.

El siguiente ejemplo muestra cómo establecer el color de relleno sólido (color de sombreado) con la configuración de fuente en un rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Adición de bordes a un rango con nombre**

 Es posible agregar bordes a un rango de celdas en lugar de a una sola celda. los[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto proporciona un[**EstablecerEsquemaBorde**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)método que toma los siguientes parámetros para agregar un borde al rango de celdas:

-  Tipo de borde, el tipo de borde, seleccionado de la[**Tipo de borde**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)enumeración.
-  Estilo de línea, el estilo de línea, seleccionado de la[**Tipo de borde de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumeración.
- Color, el color de la línea, seleccionado de la enumeración Color.

El siguiente ejemplo muestra cómo establecer un borde de contorno en un rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

El siguiente ejemplo muestra cómo establecer bordes alrededor de cada celda en el rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Cambiar el nombre de un rango con nombre**

 Aspose.Cells le permite cambiar el nombre de un rango con nombre según sus necesidades. Puede obtener el rango con nombre y cambiarle el nombre usando[**Nombre.Texto**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)atributo. El siguiente ejemplo muestra cómo cambiar el nombre de un rango con nombre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Unión de Rangos**

 Aspose.Cells proporciona[**Rango.Unión**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)para tomar la unión de rangos, el método devuelve un[*Lista de arreglo*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)objeto. El siguiente ejemplo muestra cómo tomar la unión de rangos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Intersección de Rangos**

 Aspose.Cells proporciona el[**Rango.Intersección**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) método para intersecar dos rangos. El método devuelve un[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto. Para verificar si un rango se cruza con otro rango, use el[**Rango.Intersección**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)método que devuelve un valor booleano. El siguiente ejemplo muestra cómo cruzar los rangos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Combinar Cells en el rango con nombre**

 Aspose.Cells proporciona[**Rango.Fusionar()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)método para fusionar las celdas en el rango. El siguiente ejemplo muestra cómo fusionar las celdas individuales de un rango con nombre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Eliminar un rango con nombre**

 Aspose.Cells proporciona el[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) método para borrar el nombre del rango. Para borrar el contenido del rango, use[**Cells.ClearRango()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)método. El siguiente ejemplo muestra cómo eliminar un rango con nombre con su contenido.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
