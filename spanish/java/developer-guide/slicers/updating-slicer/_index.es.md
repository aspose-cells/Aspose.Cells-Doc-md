---
title: Actualización de Slicer
type: docs
weight: 50
url: /es/java/updating-slicer/
---

## **Escenarios de uso posibles**
Si desea actualizar el cortador en Microsoft Excel, seleccione o deseleccione sus artículos, y luego se actualizará la tabla o tabla dinámica correspondiente. Utilice [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) para seleccionar o deseleccionar elementos del cortador con Aspose.Cells y luego llame al método [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh--) para actualizar la tabla o la tabla dinámica. 
## **Actualización de rebanador**
El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](67338506.xlsx) que contiene un filtro existente. Deselecciona los elementos 2 y 3 del filtro y actualiza el filtro. Luego guarda el libro de trabajo como el [archivo de Excel de salida](67338505.xlsx). La siguiente captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo. Como se puede ver en la captura de pantalla, al actualizar el filtro con elementos seleccionados, también se ha actualizado la tabla dinámica en consecuencia.

![todo:image_alt_text](updating-slicer_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
