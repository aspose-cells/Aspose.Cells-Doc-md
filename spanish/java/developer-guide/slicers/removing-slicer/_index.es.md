---
title: Eliminación de la cortadora
type: docs
weight: 30
url: /es/java/removing-slicer/
---
## **Posibles escenarios de uso**
Si desea eliminar el cortador en Microsoft Excel, simplemente selecciónelo y presione el botón*Borrar*botón. Del mismo modo, si desea eliminarlo usando Aspose.Cells API programáticamente, use el[Hoja de trabajo.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)) método. Eliminará la cortadora de la hoja de trabajo.
## **Eliminación de la cortadora**
El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](67338504.xlsx)que contiene una segmentación existente. Accede a las cortadoras y luego las elimina. Finalmente, guarda el libro de trabajo como[archivo de salida de Excel](67338502.xlsx). La siguiente captura de pantalla muestra la segmentación que se eliminará después de la ejecución del código de muestra.

![todo:imagen_alternativa_texto](removing-slicer_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
