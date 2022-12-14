---
title: Actualizar rebanador
type: docs
weight: 50
url: /es/net/updating-slicer/
---
## **Posibles escenarios de uso**

Si desea actualizar la segmentación en Microsoft Excel, seleccione o anule la selección de sus elementos, luego actualizará la tabla de segmentación o la tabla dinámica en consecuencia. Por favor use[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)para seleccionar o anular la selección de elementos de corte con Aspose.Cells y luego llamar[**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)método para actualizar la tabla de segmentación o la tabla dinámica.

## **Actualizar rebanador**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](67338475.xlsx) que contiene una segmentación existente. Anula la selección de los elementos segundo y tercero de la segmentación y actualiza la segmentación. A continuación, guarda el libro de trabajo como[archivo de salida de Excel](67338476.xlsx). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra. Como puede ver en la captura de pantalla, actualizar la segmentación con elementos seleccionados también ha actualizado la tabla dinámica en consecuencia.

![todo:imagen_alternativa_texto](updating-slicer_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
