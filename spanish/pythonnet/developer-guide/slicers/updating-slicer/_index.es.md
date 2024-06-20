---
title: Actualización de Slicer
type: docs
weight: 50
url: /es/python-net/updating-slicer/
description: Aprenda a actualizar un slicer con Aspose.Cells para Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca Python de Excel, actualizar Slicer sin Excel, Actualizar Slicer usando Aspose.Cells para Python.
---

## **Escenarios de uso posibles**

Si desea actualizar un slicer en Microsoft Excel, seleccione o deseleccione sus elementos, luego actualizará la tabla de slicer o la tabla dinámica en consecuencia. Utilice [**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/) para seleccionar o deseleccionar elementos del slicer con Aspose.Cells para Python via .NET y luego llame al método [**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#) para actualizar la tabla de slicer o la tabla dinámica.

## **Cómo actualizar Slicer usando la biblioteca Excel de Aspose.Cells para Python**

El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un filtro existente. Desactiva los elementos 2 y 3 del filtro y actualiza el filtro. Luego guarda el libro de trabajo como [archivo Excel de salida](67338476.xlsx). La captura de pantalla siguiente muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, al actualizar el filtro con los elementos seleccionados también se ha actualizado la tabla dinámica correspondientemente.

![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
