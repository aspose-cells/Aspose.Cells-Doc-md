---
title: Buscar datos utilizando valores originales
type: docs
weight: 380
url: /es/net/search-data-using-original-values/
description: Aprenda a Buscar Datos usando Valores Originales a través de la API Aspose.Cells for .NET.
keywords: Buscar Datos usando Valores Originales, Encontrar Datos usando Valores Originales, Buscar Datos por Valores Originales, Encontrar Datos por Valores Originales
---

{{% alert color="primary" %}}

A veces el valor de los datos está oculto porque está formateado de alguna manera. Por ejemplo, supongamos que la celda D4 tiene la fórmula =Sum(A1:A2) y su valor es 20 pero está formateado como ---, entonces el valor 20 está oculto y no se puede encontrar usando las opciones de búsqueda de Microsoft Excel. Sin embargo, puedes encontrarlo usando Aspose.Cells usando [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

El siguiente código de muestra ilustra el punto anterior. Encuentra la celda D4 que no se puede encontrar utilizando las opciones de búsqueda de Microsoft Excel, pero Aspose.Cells puede encontrarla usando [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Por favor, lea los comentarios dentro del código para más información.

## Código en C# para buscar datos usando valores originales

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Salida de consola generada por el código de ejemplo

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
