---
title: Actualizar segmentación con Golang vía C++
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/go-cpp/updating-slicer/
description: Este artículo muestra cómo actualizar tablas dinámicas vinculadas actualizando el segmentador usando la API Aspose.Cells for C++.
keywords: Aspose.Cells C++ Actualizar segmentador, C++ cómo cambiar el segmentador, cómo ajustar el segmentador en C++, cómo seleccionar o deseleccionar los elementos del segmentador.
---

## **Escenarios de uso posibles**

Si desea actualizar un segmentador en Microsoft Excel, selecciónelo o deseleccione sus elementos, y luego actualizará la tabla del segmentador o la tabla dinámica en consecuencia. Utilice [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/) para seleccionar o deseleccionar elementos del segmentador con Aspose.Cells y luego llame al método [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) para actualizar la tabla del segmentador o la tabla dinámica.

## **Cómo actualizar filtro**

El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un filtro existente. Desactiva los elementos 2 y 3 del filtro y actualiza el filtro. Luego guarda el libro de trabajo como [archivo Excel de salida](67338476.xlsx). La captura de pantalla siguiente muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, al actualizar el filtro con los elementos seleccionados también se ha actualizado la tabla dinámica correspondientemente.

![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}
