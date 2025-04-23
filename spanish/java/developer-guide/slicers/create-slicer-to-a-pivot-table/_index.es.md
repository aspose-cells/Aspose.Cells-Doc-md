---
title: Crear un filtro de segmentación para una tabla dinámica
type: docs
weight: 10
url: /es/java/create-slicer-to-a-pivot-table/
---

## **Escenarios de uso posibles**
El cortador se usa para filtrar datos rápidamente. Puede usarse para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel permite crear un cortador seleccionando una tabla o tabla dinámica y luego haciendo clic en *Insertar > Cortador*. Aspose.Cells también permite crear cortadores usando el método [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.PivotTable-int-int-com.aspose.cells.PivotField-)
## **Crear Cortador para una Tabla Dinámica**
Consulte el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](67338498.xlsx) que contiene la tabla dinámica. Luego crea el filtro basado en el primer campo de tabla dinámica base. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](67338497.xlsx) y [XLSB de salida](67338496.xlsb). La siguiente captura de pantalla muestra el filtro creado por Aspose.Cells en el archivo de Excel de salida.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
