---
title: Insertar línea de tiempo
linktitle: Líneas de tiempo
type: docs
weight: 170
url: /es/net/create-timeline/
description: Aprende a crear una línea de tiempo con Aspose.Cells
---

## **Escenarios de uso posibles**

En lugar de ajustar filtros para mostrar fechas, puedes usar una Línea de Tiempo de Tabla Dinámica: una opción de filtro dinámico que te permite filtrar fácilmente por fecha/hora y acercarte al período deseado con un control deslizante. Microsoft Excel te permite crear una línea de tiempo seleccionando una tabla dinámica y haciendo clic en *Insertar > Línea de tiempo*. Aspose.Cells también te permite crear una línea de tiempo usando el método [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index).

## **Crear una línea de tiempo para una Tabla Dinámica**

Por favor, consulta el siguiente código de muestra. Carga el [archivo Excel de muestra](input.xlsx) que contiene la tabla dinámica. Luego crea la línea de tiempo basada en el primer campo pivote base. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](output.xlsx). La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells en el archivo Excel de salida.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}

