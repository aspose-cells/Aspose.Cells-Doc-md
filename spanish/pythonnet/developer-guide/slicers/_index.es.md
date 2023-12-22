---
title: Insertar rebanadora
linktitle: Rebanadoras
type: docs
weight: 170
url: /es/python-net/create-slicer/
description: Administre segmentaciones de archivos de Excel con Aspose.Cells.
---
##  **Posibles escenarios de uso**

Se utiliza una segmentación de datos para filtrar datos rápidamente. Se puede utilizar para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel le permite crear una segmentación de datos seleccionando una tabla o tabla dinámica y luego haciendo clic en *Insertar > Segmentación*. Aspose.Cells for Python via .NET también le permite crear una segmentación de datos utilizando el[**Hoja de trabajo.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField)método.

##  **Crear segmentación en una tabla dinámica**

 Consulte el siguiente código de muestra. Se carga el[archivo de Excel de muestra](67338470.xlsx) que contiene la tabla dinámica. Luego crea la segmentación de datos basada en el campo de pivote de la primera base. Finalmente, guarda el libro de trabajo en[salida XLSX](67338471.xlsx) y[salida XLSB](67338472.xlsb) formato. La siguiente captura de pantalla muestra la segmentación de datos creada por Aspose.Cells en el archivo Excel de salida.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

###  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

##  **Crear tabla de segmentación en Excel**

 Consulte el siguiente código de muestra. Se carga el[archivo de Excel de muestra](sampleCreateSlicerToExcelTable.xlsx) que contiene una tabla. Luego crea la segmentación de datos basada en la primera columna. Finalmente, guarda el libro de trabajo en[salida XLSX](outputCreateSlicerToExcelTable.xlsx) formato.

###  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

##  **Temas avanzados**
- [Cambiar propiedades de segmentación](/cells/es/python-net/change-slicer-properties/)
- [Dibuje Slicer mientras renderiza Excel en PDF](/cells/es/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [Cortadora de formato](/cells/es/python-net/formatting-slicer/)
- [Quitar la rebanadora](/cells/es/python-net/removing-slicer/)
- [Rebanador de renderizado](/cells/es/python-net/rendering-slicer/)
- [Actualizando la segmentación](/cells/es/python-net/updating-slicer/)
