---
title: Actualización de Slicer
type: docs
weight: 50
url: /es/net/updating-slicer/
description: Este artículo muestra cómo actualizar tablas dinámicas vinculadas actualizando el filtro mediante la API Aspose.Cells for .NET.
keywords: Aspose.Cells C# Actualizar filtro, C# cómo cambiar el filtro, cómo ajustar el filtro en C#, cómo seleccionar o deseleccionar los elementos del filtro.
---

## **Escenarios de uso posibles**

Si desea actualizar el filtro en Microsoft Excel, seleccionar o deseleccionar sus elementos, entonces actualizará la tabla de filtro o tabla dinámica según corresponda. Utilice [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems) para seleccionar o deseleccionar elementos del filtro con Aspose.Cells y luego llame al método [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) para actualizar la tabla de filtro o tabla dinámica.

## **Cómo actualizar filtro**

El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un filtro existente. Desactiva los elementos 2 y 3 del filtro y actualiza el filtro. Luego guarda el libro de trabajo como [archivo Excel de salida](67338476.xlsx). La captura de pantalla siguiente muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, al actualizar el filtro con los elementos seleccionados también se ha actualizado la tabla dinámica correspondientemente.

![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
