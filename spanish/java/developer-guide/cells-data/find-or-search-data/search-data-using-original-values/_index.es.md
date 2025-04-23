---
title: Buscar datos utilizando valores originales
type: docs
weight: 540
url: /es/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

A veces el valor de los datos está oculto porque se formatea de alguna manera. Por ejemplo, supón que la celda D4 tiene la fórmula =Sum(A1:A2) y su valor es 20 pero está formateada como ---, entonces el valor 20 está oculto y no se puede encontrar usando las opciones de búsqueda de Microsoft Excel. Sin embargo, puedes encontrarlo usando Aspose.Cells con [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)

{{% /alert %}} 
## **Buscar Datos usando Valores Originales**
El siguiente código de ejemplo ilustra el punto anterior. Encuentra la celda D4 que no puede ser encontrada usando las opciones de búsqueda de Microsoft Excel, pero Aspose.Cells puede encontrar usando [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES). Por favor, lee los comentarios dentro del código para más información.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
