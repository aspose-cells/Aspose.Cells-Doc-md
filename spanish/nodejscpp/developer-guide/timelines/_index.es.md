---
title: Insertar línea de tiempo
linktitle: Líneas de tiempo
type: docs
weight: 170
url: /es/nodejs-cpp/create-timeline/
description: Aprende cómo crear una línea de tiempo con Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

En lugar de ajustar filtros para mostrar fechas, puedes usar una Línea de Tiempo de Tabla Dinámica, una opción de filtro dinámica que permite filtrar fácilmente por fecha/hora y acercarse al período deseado con un control deslizante. Microsoft Excel permite crear una línea de tiempo seleccionando una tabla dinámica y luego haciendo clic en *Insertar > Línea de Tiempo*. Aspose.Cells for Node.js via C++ también permite crear una línea de tiempo usando el método [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **Crear una línea de tiempo para una Tabla Dinámica**

Por favor, vea el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](input.xlsx) que contiene la tabla dinámica. Luego crea la línea de tiempo basada en el primer campo pivote base. Finalmente, guarda el libro en formato [XLSX de salida](output.xlsx). La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells for Node.js via C++ en el archivo de Excel de salida.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

