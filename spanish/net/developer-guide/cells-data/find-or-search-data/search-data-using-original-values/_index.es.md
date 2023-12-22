---
title: Buscar datos utilizando valores originales
type: docs
weight: 380
url: /es/net/search-data-using-original-values/
description: Aprenda a buscar datos utilizando valores originales a través del Aspose.Cells for .NET API.
keywords: Search Data using Original Values, Find Data using Original Values, Search Data by Original Values, Find Data by Original Values
---
{{% alert color="primary" %}}

 A veces el valor de los datos está oculto porque está formateado de alguna manera. Por ejemplo, supongamos que la celda D4 tiene la fórmula =Suma(A1:A2) y su valor es 20 pero tiene el formato ---, entonces el valor 20 está oculto y no se puede encontrar usando Microsoft opciones de búsqueda de Excel. Sin embargo, puede encontrarlo usando Aspose.Cells usando[**LookInType.Valores originales**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 El siguiente código de muestra ilustra el punto anterior. Encuentra la celda D4 que no se puede encontrar usando las opciones de búsqueda de Excel Microsoft, pero Aspose.Cells puede encontrarla usando[**LookInType.Valores originales**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Lea los comentarios dentro del código para obtener más información.

##  Código C# para buscar datos usando valores originales.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Salida de consola generada por el código de muestra

Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
