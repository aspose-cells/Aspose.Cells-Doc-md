---
title: Eliminando segmentación con Golang vía C++
linktitle: Eliminar filtro
type: docs
weight: 30
url: /es/go-cpp/removing-slicer/
description: Aprenda cómo quitar segmentadores en archivos de Excel programáticamente usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Si desea quitar un segmentador en Microsoft Excel, simplemente selecciónelo y presione el botón *Eliminar*. De manera similar, si desea quitarlo usando la API de Aspose.Cells programáticamente, utilice el método [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/go-cpp/slicercollection/remove/). Esto eliminará el segmentador de la hoja de cálculo.

## **Eliminar rebanador**

El siguiente código muestra el [archivo de Excel de muestra](67338478.xlsx) que contiene un slicer existente. Accede a los slicers y luego lo elimina. Finalmente, guarda el libro de trabajo como [archivo de Excel de salida](67338477.xlsx). La siguiente captura de pantalla muestra el slicer que se eliminará después de la ejecución del código de muestra.

![todo:image_alt_text](removing-slicer_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingSlicer.go" >}}
