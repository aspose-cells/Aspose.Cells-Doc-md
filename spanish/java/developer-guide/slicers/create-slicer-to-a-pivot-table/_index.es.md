---
title: Crear segmentación en una tabla dinámica
type: docs
weight: 10
url: /es/java/create-slicer-to-a-pivot-table/
---
## **Posibles escenarios de uso**
La segmentación se utiliza para filtrar datos rápidamente. Se puede usar para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel le permite crear una segmentación seleccionando una tabla o tabla dinámica y luego haciendo clic en el*Insertar > Cortador*. Aspose.Cells también le permite crear una segmentación usando el[Hoja de trabajo.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) método.
## **Crear segmentación en una tabla dinámica**
Consulte el siguiente código de ejemplo. carga el[ejemplo de archivo de Excel](67338498.xlsx)que contiene la tabla dinámica. A continuación, crea la segmentación en función del primer campo pivote base. Finalmente, guarda el libro de trabajo en[salida XLSX](67338497.xlsx)y[salida XLSB](67338496.xlsb)formato. La siguiente captura de pantalla muestra la segmentación creada por Aspose.Cells en el archivo de salida de Excel.

![todo:imagen_alternativa_texto](create-slicer-to-a-pivot-table_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
