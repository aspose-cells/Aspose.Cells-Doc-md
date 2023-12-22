---
title: Insertar línea de tiempo
linktitle: Líneas de tiempo
type: docs
weight: 170
url: /es/python-net/create-timeline/
description: Aprenda a crear una línea de tiempo con Aspose.Cells for Python via .NET.
---
##  **Posibles escenarios de uso**

En lugar de ajustar los filtros para mostrar fechas, puede usar una línea de tiempo de tabla dinámica, una opción de filtro dinámico que le permite filtrar fácilmente por fecha/hora y ampliar el período que desee con un control deslizante. Microsoft Excel le permite crear una línea de tiempo seleccionando una tabla dinámica y luego haciendo clic en *Insertar > Línea de tiempo*. Aspose.Cells for Python via .NET también le permite crear una línea de tiempo usando el[**Hoja de trabajo.líneas de tiempo.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods)método.

##  **Crear una línea de tiempo en una tabla dinámica**

 Consulte el siguiente código de muestra. Se carga el[archivo de Excel de muestra](input.xlsx)que contiene la tabla dinámica. Luego crea la línea de tiempo basada en el campo de pivote de la primera base. Finalmente, guarda el libro de trabajo en[salida XLSX](output.xlsx) formato. La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells for Python via .NET en el archivo Excel de salida.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

###  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}

