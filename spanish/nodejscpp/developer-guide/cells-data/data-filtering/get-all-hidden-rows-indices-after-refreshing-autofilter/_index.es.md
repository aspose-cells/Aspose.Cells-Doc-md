---  
title: Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro 
type: docs  
weight: 320  
url: /es/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Aprende cómo obtener todos los índices de filas ocultas después de actualizar el AutoFilter usando la API Aspose.Cells for Node.js via C++.  
keywords: Obtener todos los índices de filas ocultas después de actualizar AutoFilter en Node.js vía C++, obtener todos los índices de filas ocultas después de actualizar AutoFilter en Node.js vía C++, recuperar todos los índices de filas ocultas después de actualizar AutoFilter en Node.js vía C++  
---  

## **Escenarios de uso posibles**  

Cuando aplicas el filtro automático en las celdas de una hoja de cálculo, algunas filas se ocultan automáticamente. Pero puede ser que algunas filas ya estén ocultas manualmente por el usuario final de Excel y no por un filtro automático. Por lo tanto, es difícil saber qué filas están ocultas por el filtro automático y cuáles manualmente por el usuario. Aspose.Cells for Node.js via C++ trata este problema usando el método `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-). Este método devuelve los índices de todas las filas que están ocultas por el filtro automático y no manualmente por el usuario final de Excel.  

## **Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro**  

Por favor, vea el siguiente código de ejemplo que carga el [archivo de Excel de muestra](64716909.xlsx) que contiene algunas filas ocultas manualmente por el usuario final de Excel. El código aplica y actualiza el filtro automático usando el método `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-), que devuelve los índices de todas las filas ocultas por el filtro automático. Luego, imprime los índices de las filas ocultas en la consola junto con los nombres y valores de las celdas.  

## **Código de muestra**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


## **Salida de la consola**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
