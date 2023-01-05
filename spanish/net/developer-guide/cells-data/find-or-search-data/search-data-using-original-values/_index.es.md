---
title: Buscar datos usando valores originales
type: docs
weight: 380
url: /es/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

 A veces, el valor de los datos está oculto porque está formateado de alguna manera. Por ejemplo, suponga que la celda D4 tiene la fórmula = Suma (A1: A2) y su valor es 20 pero tiene el formato ---, entonces el valor 20 está oculto y no se puede encontrar usando Microsoft Opciones de búsqueda de Excel. Sin embargo, puede encontrarlo usando Aspose.Cells usando[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 El siguiente código de ejemplo ilustra el punto anterior. Encuentra la celda D4 que no se puede encontrar usando Microsoft Opciones de búsqueda de Excel pero Aspose.Cells puede encontrarla usando[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Lea los comentarios dentro del código para obtener más información.

## C# código para buscar datos usando valores originales

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Salida de la consola generada por el código de muestra

Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
