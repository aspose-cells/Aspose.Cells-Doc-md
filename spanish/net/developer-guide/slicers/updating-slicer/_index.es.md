---
title: Actualizando la segmentación
type: docs
weight: 50
url: /es/net/updating-slicer/
description: Este artículo muestra cómo actualizar tablas dinámicas vinculadas actualizando la segmentación de datos mediante Aspose.Cells for .NET API.
keywords: Aspose.Cells C# Update slicer, C# how to change the slicer, how to adjust the slicer in C#, how to select or unselect he slicer items.
---
##  **Posibles escenarios de uso**

Si desea actualizar la segmentación de datos en Microsoft Excel, seleccione o anule la selección de sus elementos, luego actualizará la tabla de segmentación o la tabla dinámica en consecuencia. Por favor use[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)para seleccionar o deseleccionar elementos de segmentación con Aspose.Cells y luego llamar[**Cortadora.Actualizar()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)Método para actualizar la tabla de segmentación o la tabla dinámica.

##  **Cómo actualizar la segmentación de datos**

 El siguiente código de muestra carga el[archivo de Excel de muestra](67338475.xlsx) que contiene una segmentación de datos existente. Anula la selección del segundo y tercer elemento de la segmentación y la actualiza. Luego guarda el libro de trabajo como[archivo de salida de Excel](67338476.xlsx)La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra. Como puede ver en la captura de pantalla, al actualizar la segmentación de datos con elementos seleccionados también se actualizó la tabla dinámica en consecuencia.

![todo:image_alt_text](updating-slicer_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
