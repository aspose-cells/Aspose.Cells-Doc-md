---
title: Insertar Línea de Tiempo con Golang vía C++
linktitle: Líneas de tiempo
type: docs
weight: 170
url: /es/go-cpp/create-timeline/
description: Aprende cómo crear una línea de tiempo con Aspose.Cells usando C++.
---

## **Escenarios de uso posibles**

En lugar de ajustar filtros para mostrar fechas, puedes usar una línea de tiempo de Tabla Dinámica —una opción de filtro dinámica que te permite filtrar fácilmente por fecha/hora y acercar el período que deseas con un control deslizante. Microsoft Excel te permite crear una línea de tiempo seleccionando una tabla dinámica y luego haciendo clic en *Insertar > Línea de tiempo*. Aspose.Cells también te permite crear una línea de tiempo usando el método [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/).

## **Crear una línea de tiempo para una Tabla Dinámica**

Por favor, consulta el siguiente código de muestra. Carga el [archivo Excel de muestra](input.xlsx) que contiene la tabla dinámica. Luego crea la línea de tiempo basada en el primer campo pivote base. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](output.xlsx). La siguiente captura de pantalla muestra la línea de tiempo creada por Aspose.Cells en el archivo Excel de salida.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}
