---
title: Agrupar campos dinámicos en la tabla dinámica con Golang mediante C++
linktitle: Agrupar campos dinámicos en la tabla dinámica con Golang mediante C++
description: Aprenda cómo agrupar campos dinámicos en una tabla dinámica mediante Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, tabla dinámica, campo dinámico, agrupar campos dinámicos, GroupBy, PivotField, agrupación de fechas, Go
type: docs
weight: 80
url: /es/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Microsoft Excel permite agrupar campos dinámicos **en** la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo dinámico, suele ser útil agruparlos en secciones. Aspose.Cells también ofrece esta funcionalidad mediante el método [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/).

## **Agrupar campos dinámicos en la tabla dinámica**
El siguiente código de ejemplo carga el [archivo Excel de ejemplo](64716818.xlsx) y realiza la agrupación del primer campo dinámico mediante el método [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/). A continuación, actualiza la tabla dinámica, calcula sus datos y guarda el libro de trabajo como [archivo Excel de salida](64716817.xlsx). La captura de pantalla muestra el efecto del código de ejemplo en el archivo Excel de ejemplo. Como puede ver en la captura de pantalla, el primer campo dinámico ahora está agrupado por meses y trimestres.
![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de ejemplo**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}