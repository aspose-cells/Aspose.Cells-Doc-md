---
title: Actualizando la segmentación
type: docs
weight: 50
url: /es/python-net/updating-slicer/
---
##  **Posibles escenarios de uso**

Si desea actualizar la segmentación de datos en Microsoft Excel, seleccione o anule la selección de sus elementos, luego actualizará la tabla de segmentación o la tabla dinámica en consecuencia. Por favor use[**Cortadora.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/)para seleccionar o deseleccionar elementos de la cortadora con Aspose.Cells for Python via .NET y luego llamar[**Cortadora.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#)Método para actualizar la tabla de segmentación o la tabla dinámica.

##  **Actualizando la segmentación**

 El siguiente código de muestra carga el[archivo de Excel de muestra](67338475.xlsx) que contiene una segmentación de datos existente. Anula la selección del segundo y tercer elemento de la segmentación y la actualiza. Luego guarda el libro de trabajo como[archivo de salida de Excel](67338476.xlsx)La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra. Como puede ver en la captura de pantalla, al actualizar la segmentación de datos con elementos seleccionados también se actualizó la tabla dinámica en consecuencia.

![todo:image_alt_text](updating-slicer_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
