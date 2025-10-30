---  
title: Buscar datos utilizando valores originales
type: docs  
weight: 380  
url: /es/nodejs-cpp/search-data-using-original-values/  
description: Aprender cómo buscar datos usando valores originales a través de la API Aspose.Cells for Node.js via C++.  
keywords: Buscar datos usando valores originales Node.js a través de C++, Encontrar datos usando valores originales Node.js a través de C++, Buscar datos por valores originales Node.js a través de C++, Encontrar datos por valores originales Node.js a través de C++  
---  

{{% alert color="primary" %}}  

A veces el valor de los datos está oculto porque está formateado de alguna manera. Por ejemplo, supongamos que la celda D4 tiene la fórmula =Sum(A1:A2) y su valor es 20 pero está formateado como ---, entonces el valor 20 está oculto y no se puede encontrar usando las opciones de búsqueda de Microsoft Excel. Sin embargo, puedes encontrarlo usando Aspose.Cells usando [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype)  

{{% /alert %}}  

El siguiente código de muestra ilustra el punto anterior. Encuentra la celda D4 que no se puede encontrar utilizando las opciones de búsqueda de Microsoft Excel, pero Aspose.Cells puede encontrarla usando [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype). Por favor, lea los comentarios dentro del código para más información.  

## Código Node.js para buscar datos usando valores originales  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## Salida de consola generada por el código de ejemplo  

Aquí está la salida en consola del código de muestra anterior.  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
