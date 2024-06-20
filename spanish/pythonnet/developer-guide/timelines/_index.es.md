---
title: Insertar línea de tiempo
linktitle: Líneas de tiempo
type: docs
weight: 170
url: /es/python-net/create-timeline/
description: Aprenda cómo crear una línea de tiempo con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells para Excel en Python, biblioteca de Python para Excel, Python crea línea de tiempo sin Excel, Agregar línea de tiempo a través de Aspose.Cells para Python, Insertar línea de tiempo usando Aspose.Cells para Python.
---

## **Escenarios de uso posibles**

En lugar de ajustar filtros para mostrar fechas, puede usar una Línea de tiempo de tabla dinámica, una opción de filtro dinámico que le permite filtrar fácilmente por fecha/hora, y hacer zoom en el período que desee con un control deslizante. Microsoft Excel le permite crear una línea de tiempo seleccionando una tabla dinámica y luego haciendo clic en *Insertar > Línea de tiempo*. Aspose.Cells para Python via .NET también le permite crear una línea de tiempo utilizando el método [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods).

## **Cómo crear una línea de tiempo para una tabla dinámica mediante la biblioteca Aspose.Cells for Python Excel**

Por favor, consulte el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](input.xlsx) que contiene la tabla dinámica. Luego crea la línea de tiempo basada en el primer campo base de la tabla dinámica. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](output.xlsx). La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells para Python via .NET en el archivo de Excel de salida.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}

