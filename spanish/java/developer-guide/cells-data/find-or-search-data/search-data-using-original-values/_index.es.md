---
title: Buscar datos utilizando valores originales
type: docs
weight: 540
url: /es/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

A veces, el valor de los datos está oculto porque está formateado de alguna manera. Por ejemplo, supongamos que la celda D4 tiene la fórmula =Sum(A1:A2) y su valor es 20, pero está formateado como ---, entonces el valor 20 está oculto y no se puede encontrar utilizando las opciones de búsqueda de Microsoft Excel. Sin embargo, puedes encontrarlo usando Aspose.Cells utilizando [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **Buscar Datos usando Valores Originales**
El siguiente código de muestra ilustra el punto anterior. Encuentra la celda D4 que no se puede encontrar utilizando las opciones de búsqueda de Microsoft Excel pero Aspose.Cells puede encontrarlo usando [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Por favor, lee los comentarios dentro del código para más información.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
