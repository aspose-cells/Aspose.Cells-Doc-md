---
title: Crear filtro para tabla de Excel
type: docs
weight: 15
url: /es/java/create-slicer-to-excel-table/
---

## **Escenarios de uso posibles**

Un segmentador se usa para filtrar datos rápidamente. Puede usarse para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel le permite crear un segmentador seleccionando una tabla o tabla dinámica y luego haciendo clic en *Insertar > Segmentador*. Aspose.Cells también le permite crear un segmentador usando el método [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.ListObject-com.aspose.cells.ListColumn-int-int-).

## **Crear Cortador para Tabla de Excel**

Por favor, consulte el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](sampleCreateSlicerToExcelTable.xlsx) que contiene una tabla. Luego crea el rebanador basado en la primera columna. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](outputCreateSlicerToExcelTable.xlsx).

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
{{< app/cells/assistant language="java" >}}
