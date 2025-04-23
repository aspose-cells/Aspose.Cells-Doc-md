---
title: Eliminar filtro
type: docs
weight: 30
url: /es/java/removing-slicer/
---

## **Escenarios de uso posibles**
Si desea eliminar un cortador en Microsoft Excel, solo selecciónelo y presione el botón *Eliminar*. De manera similar, si desea eliminarlo programáticamente usando la API de Aspose.Cells, utilice el método [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove-com.aspose.cells.Slicer-). Esto eliminará el cortador de la hoja de cálculo. 
## **Eliminar rebanador**
El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](67338504.xlsx) que contiene un filtro existente. Accede a los filtros y luego los elimina. Finalmente, guarda el libro de trabajo como [archivo de Excel de salida](67338502.xlsx). La siguiente captura de pantalla muestra el filtro que se eliminará después de la ejecución del código de ejemplo.

![todo:image_alt_text](removing-slicer_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
