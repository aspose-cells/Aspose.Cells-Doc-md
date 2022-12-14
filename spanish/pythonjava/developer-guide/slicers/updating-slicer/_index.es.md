---
title: Actualizar rebanador
type: docs
weight: 60
url: /es/python-java/updating-slicer/
---
## **Actualizar rebanador**
Aspose.Cells para Python a través de Java admite la actualización de segmentaciones. Para esto, el API proporciona la propiedad Slicer.SlicerCache.SlicerCacheItems que se usa para seleccionar o anular la selección de elementos de segmentación. El siguiente fragmento de código carga el[ejemplo de archivo de Excel](106365050.xlsx)que contiene una cortadora. Anula la selección de los elementos segundo y tercero de la segmentación y actualiza la segmentación utilizando el método Slicer.refresh(). A continuación, guarda el libro de trabajo como el[archivo de salida de Excel](106365051.xlsx). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra. Como puede ver en la captura de pantalla, actualizar la segmentación con elementos seleccionados también ha actualizado la tabla dinámica en consecuencia.

![todo:imagen_alternativa_texto](Updating-Slicer-using-Aspose.Cells.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
