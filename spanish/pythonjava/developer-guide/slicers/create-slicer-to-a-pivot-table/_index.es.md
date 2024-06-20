---
title: Crear un filtro de segmentación para una tabla dinámica
type: docs
weight: 10
url: /es/python-java/create-slicer-to-a-pivot-table/
---

## **Escenarios de uso posibles**
Los filtros de segmentación se utilizan para filtrar datos rápidamente. Se pueden utilizar para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel le permite crear un filtro de segmentación seleccionando una tabla o una tabla dinámica y luego haciendo clic en *Insertar > Filtro de segmentación*. Aspose.Cells para Python via Java ofrece el método Worksheet.getSlicers().add() para crear un filtro de segmentación.
## **Crear Cortador para una Tabla Dinámica**
El siguiente fragmento de código carga el [archivo de Excel de ejemplo](106364966.xlsx) que contiene la tabla dinámica. Luego crea el filtro de segmentación basado en el primer campo de la tabla dinámica. Finalmente, guarda el libro de trabajo en formato XLSX de [salida](106364967.xlsx). La siguiente captura de pantalla muestra el filtro de segmentación creado por Aspose.Cells en el archivo de Excel de salida.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
