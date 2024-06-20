---
title: Actualización de Slicer
type: docs
weight: 60
url: /es/python-java/updating-slicer/
---

## **Actualización de rebanador**
Aspose.Cells for Python via Java soporta la actualización de cortadores. Para ello, la API proporciona la propiedad Slicer.SlicerCache.SlicerCacheItems que se utiliza para seleccionar o deseleccionar elementos del cortador. El siguiente fragmento de código carga el [archivo de Excel de ejemplo](106365050.xlsx) que contiene un cortador. Desmarca los elementos 2 y 3 del cortador y refresca el cortador utilizando el método Slicer.refresh(). Luego guarda el libro de trabajo como [archivo de Excel de salida](106365051.xlsx). La siguiente captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo. Como puedes ver en la captura de pantalla, al refrescar el cortador con los elementos seleccionados, también se ha actualizado la tabla dinámica en consecuencia.

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
