---
title: Buscar datos usando valores originales
type: docs
weight: 540
url: /es/java/search-data-using-original-values/
---
{{% alert color="primary" %}} 

 A veces, el valor de los datos está oculto porque está formateado de alguna manera. Por ejemplo, suponga que la celda D4 tiene la fórmula = Suma (A1: A2) y su valor es 20 pero tiene el formato ---, entonces el valor 20 está oculto y no se puede encontrar usando Microsoft Opciones de búsqueda de Excel. Sin embargo, puede encontrarlo usando Aspose.Cells usando[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **Buscar datos usando valores originales**
 El siguiente código de ejemplo ilustra el punto anterior. Encuentra la celda D4 que no se puede encontrar usando Microsoft Opciones de búsqueda de Excel pero Aspose.Cells puede encontrarla usando[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Lea los comentarios dentro del código para obtener más información.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Salida de consola**
Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
