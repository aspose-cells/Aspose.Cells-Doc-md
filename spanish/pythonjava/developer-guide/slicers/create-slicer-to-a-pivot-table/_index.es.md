---
title: Crear segmentación en una tabla dinámica
type: docs
weight: 10
url: /es/python-java/create-slicer-to-a-pivot-table/
---
## **Posibles escenarios de uso**
Las segmentaciones se utilizan para filtrar datos rápidamente. Se pueden usar para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel le permite crear una segmentación seleccionando una tabla o tabla dinámica y luego haciendo clic en el*Insertar > Cortador*Aspose.Cells para Python a través de Java proporciona el método Worksheet.getSlicers().add() para crear una segmentación.
## **Crear segmentación en una tabla dinámica**
El siguiente fragmento de código carga el[ejemplo de archivo de Excel](106364966.xlsx)que contiene la tabla dinámica. A continuación, crea la segmentación en función del primer campo pivote base. Finalmente, guarda el libro de trabajo en[salida XLSX](106364967.xlsx)formato. La siguiente captura de pantalla muestra la segmentación creada por Aspose.Cells en el archivo de salida de Excel.

![todo:imagen_alternativa_texto](create-slicer-to-a-pivot-table_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
